import React from 'react';

const ChartDisplay = ({ chartData }) => {
  if (!chartData) return null;
  const { type, title, x_label, y_label, labels = [], datasets = [], headers, rows } = chartData;

  const cardStyle = {
    background: 'rgba(255,255,255,0.04)',
    border: '1px solid rgba(255,255,255,0.1)',
    borderRadius: '12px',
    padding: '1.2rem',
    marginBottom: '1.2rem',
  };

  if (type === 'table') {
    return (
      <div style={cardStyle}>
        {title && <div style={{ textAlign: 'center', fontWeight: 'bold', color: '#60a5fa', marginBottom: '0.8rem', fontSize: '0.95rem' }}>{title}</div>}
        <div style={{ overflowX: 'auto' }}>
          <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '0.85rem' }}>
            <thead><tr>{(headers||[]).map((h,i) => <th key={i} style={{ padding:'0.45rem 0.7rem', background:'rgba(139,92,246,0.2)', color:'#a78bfa', textAlign:'center', border:'1px solid rgba(255,255,255,0.08)', fontWeight:600 }}>{h}</th>)}</tr></thead>
            <tbody>{(rows||[]).map((row,ri) => <tr key={ri}>{row.map((cell,ci) => <td key={ci} style={{ padding:'0.35rem 0.7rem', textAlign:'center', border:'1px solid rgba(255,255,255,0.08)', color: ci===0?'#e2e8f0':'#94a3b8' }}>{cell}</td>)}</tr>)}</tbody>
          </table>
        </div>
      </div>
    );
  }

  const COLORS = ['#8b5cf6','#06b6d4','#f59e0b','#10b981','#ef4444','#f43f5e','#a3e635'];

  if (type === 'bar') {
    const allVals = datasets.flatMap(d => d.values||[]);
    const maxVal = allVals.length ? Math.max(...allVals) : 1;
    const W=540,H=220,padL=52,padB=46,padT=28,padR=16;
    const chartW=W-padL-padR, chartH=H-padB-padT;
    const numGroups=labels.length, numSeries=datasets.length;
    const groupW=chartW/numGroups, barW=Math.min(groupW/(numSeries+1),28);
    return (
      <div style={cardStyle}>
        {title && <div style={{ textAlign:'center', fontWeight:'bold', color:'#60a5fa', marginBottom:'0.5rem', fontSize:'0.9rem' }}>{title}</div>}
        {numSeries>1 && <div style={{ display:'flex', justifyContent:'center', gap:'1rem', marginBottom:'0.4rem', flexWrap:'wrap' }}>{datasets.map((d,i)=><div key={i} style={{ display:'flex', alignItems:'center', gap:'5px', fontSize:'0.78rem', color:'#94a3b8' }}><div style={{ width:12,height:12,borderRadius:2,background:COLORS[i%COLORS.length] }}/>{d.label}</div>)}</div>}
        <div style={{ overflowX:'auto' }}>
          <svg width={W} height={H} style={{ maxWidth:'100%' }}>
            {[0,1,2,3,4,5].map(i=>{ const v=Math.round((maxVal/5)*i); const y=padT+chartH-(i/5)*chartH; return <g key={i}><line x1={padL} y1={y} x2={W-padR} y2={y} stroke="rgba(255,255,255,0.07)"/><text x={padL-5} y={y+4} textAnchor="end" fontSize="10" fill="rgba(255,255,255,0.4)">{v}</text></g>; })}
            {labels.map((label,gi)=>{ const gX=padL+gi*groupW; return <g key={gi}>{datasets.map((ds,si)=>{ const val=ds.values[gi]||0; const bH=(val/maxVal)*chartH; const x=gX+(groupW-numSeries*(barW+2))/2+si*(barW+2); const y=padT+chartH-bH; const c=COLORS[si%COLORS.length]; return <g key={si}><rect x={x} y={y} width={barW} height={bH} fill={c} rx="3" opacity="0.85"/>{bH>14&&<text x={x+barW/2} y={y+11} textAnchor="middle" fontSize="9" fill="white" opacity="0.8">{val}</text>}</g>; })}<text x={gX+groupW/2} y={H-padB+15} textAnchor="middle" fontSize="9" fill="rgba(255,255,255,0.5)">{label}</text></g>; })}
            <line x1={padL} y1={padT} x2={padL} y2={padT+chartH} stroke="rgba(255,255,255,0.3)" strokeWidth="1.5"/>
            <line x1={padL} y1={padT+chartH} x2={W-padR} y2={padT+chartH} stroke="rgba(255,255,255,0.3)" strokeWidth="1.5"/>
            {x_label&&<text x={padL+chartW/2} y={H-3} textAnchor="middle" fontSize="10" fill="rgba(255,255,255,0.35)">{x_label}</text>}
          </svg>
        </div>
      </div>
    );
  }

  if (type === 'line') {
    const allVals=datasets.flatMap(d=>d.values||[]);
    const maxVal=allVals.length?Math.max(...allVals)*1.1:1;
    const minVal=Math.min(0,...allVals)*0.9;
    const W=540,H=220,padL=52,padB=46,padT=28,padR=16;
    const chartW=W-padL-padR, chartH=H-padB-padT;
    const range=maxVal-minVal||1;
    const toX=i=>padL+(i/(labels.length-1||1))*chartW;
    const toY=v=>padT+chartH-((v-minVal)/range)*chartH;
    return (
      <div style={cardStyle}>
        {title && <div style={{ textAlign:'center', fontWeight:'bold', color:'#60a5fa', marginBottom:'0.5rem', fontSize:'0.9rem' }}>{title}</div>}
        {datasets.length>1 && <div style={{ display:'flex', justifyContent:'center', gap:'1rem', marginBottom:'0.4rem', flexWrap:'wrap' }}>{datasets.map((d,i)=><div key={i} style={{ display:'flex', alignItems:'center', gap:'5px', fontSize:'0.78rem', color:'#94a3b8' }}><div style={{ width:20,height:3,background:COLORS[i%COLORS.length],borderRadius:2 }}/>{d.label}</div>)}</div>}
        <div style={{ overflowX:'auto' }}>
          <svg width={W} height={H} style={{ maxWidth:'100%' }}>
            {[0,1,2,3,4,5].map(i=>{ const v=minVal+(range/5)*i; const y=toY(v); return <g key={i}><line x1={padL} y1={y} x2={W-padR} y2={y} stroke="rgba(255,255,255,0.07)"/><text x={padL-5} y={y+4} textAnchor="end" fontSize="10" fill="rgba(255,255,255,0.4)">{Math.round(v)}</text></g>; })}
            {labels.map((l,i)=><text key={i} x={toX(i)} y={H-padB+15} textAnchor="middle" fontSize="9" fill="rgba(255,255,255,0.5)">{l}</text>)}
            {datasets.map((ds,si)=>{ const c=COLORS[si%COLORS.length]; const pts=ds.values.map((v,i)=>`${toX(i)},${toY(v)}`).join(' '); return <g key={si}><polyline points={pts} fill="none" stroke={c} strokeWidth="2" strokeLinejoin="round"/>{ds.values.map((v,i)=><circle key={i} cx={toX(i)} cy={toY(v)} r="3.5" fill={c}/>)}</g>; })}
            <line x1={padL} y1={padT} x2={padL} y2={padT+chartH} stroke="rgba(255,255,255,0.3)" strokeWidth="1.5"/>
            <line x1={padL} y1={padT+chartH} x2={W-padR} y2={padT+chartH} stroke="rgba(255,255,255,0.3)" strokeWidth="1.5"/>
            {x_label&&<text x={padL+chartW/2} y={H-3} textAnchor="middle" fontSize="10" fill="rgba(255,255,255,0.35)">{x_label}</text>}
          </svg>
        </div>
      </div>
    );
  }

  if (type === 'pie') {
    const vals=(datasets[0]?.values||[]);
    const total=vals.reduce((s,v)=>s+v,0)||1;
    const cx=90,cy=90,r=78;
    let cum=-Math.PI/2;
    const slices=vals.map((v,i)=>{ const ang=(v/total)*2*Math.PI; const s=cum; cum+=ang; const e=cum; const x1=cx+r*Math.cos(s),y1=cy+r*Math.sin(s),x2=cx+r*Math.cos(e),y2=cy+r*Math.sin(e); const lg=ang>Math.PI?1:0; return { d:`M${cx},${cy} L${x1},${y1} A${r},${r},0,${lg},1,${x2},${y2} Z`, c:COLORS[i%COLORS.length] }; });
    return (
      <div style={cardStyle}>
        {title && <div style={{ textAlign:'center', fontWeight:'bold', color:'#60a5fa', marginBottom:'0.8rem', fontSize:'0.9rem' }}>{title}</div>}
        <div style={{ display:'flex', alignItems:'center', gap:'1.5rem', flexWrap:'wrap', justifyContent:'center' }}>
          <svg width={180} height={180} style={{ flexShrink:0 }}>{slices.map((s,i)=><path key={i} d={s.d} fill={s.c} stroke="rgba(0,0,0,0.3)" strokeWidth="1.5"/>)}</svg>
          <div style={{ display:'flex', flexDirection:'column', gap:'0.45rem' }}>{labels.map((label,i)=><div key={i} style={{ display:'flex', alignItems:'center', gap:'7px', fontSize:'0.82rem', color:'#94a3b8' }}><div style={{ width:11,height:11,borderRadius:'50%',background:COLORS[i%COLORS.length],flexShrink:0 }}/><span>{label}: <strong style={{ color:'#e2e8f0' }}>{vals[i]}%</strong></span></div>)}</div>
        </div>
      </div>
    );
  }
  return null;
};

export default ChartDisplay;
