import React from 'react';

/* ─── Stacked Bar Chart ─────────────────────────────── */
const StackedBarChart = ({ data }) => {
  const { labels, datasets, title, xLabel, yLabel } = data;
  const W = 420, H = 280;
  const PAD = { top: 30, right: 20, bottom: 50, left: 52 };
  const chartW = W - PAD.left - PAD.right;
  const chartH = H - PAD.top - PAD.bottom;

  // Calculate stacked totals
  const totals = labels.map((_, i) => datasets.reduce((sum, ds) => sum + ds.values[i], 0));
  const maxVal = Math.ceil(Math.max(...totals) / 50) * 50;
  const barW = (chartW / labels.length) * 0.6;
  const barGap = chartW / labels.length;

  const yLines = [];
  const yStep = maxVal / 4;
  for (let i = 0; i <= 4; i++) {
    const val = i * yStep;
    const y = PAD.top + chartH - (val / maxVal) * chartH;
    yLines.push({ val, y });
  }

  return (
    <svg width={W} height={H} style={{ fontFamily: 'inherit' }}>
      {/* Title */}
      <text x={W / 2} y={16} textAnchor="middle" fontSize={12} fontWeight="600" fill="#ccc">{title}</text>

      {/* Y gridlines + labels */}
      {yLines.map(({ val, y }) => (
        <g key={val}>
          <line x1={PAD.left} x2={PAD.left + chartW} y1={y} y2={y} stroke="rgba(255,255,255,0.1)" strokeWidth={1} />
          <text x={PAD.left - 6} y={y + 4} textAnchor="end" fontSize={10} fill="#999">{val}</text>
        </g>
      ))}

      {/* Y-axis label */}
      <text
        x={12} y={PAD.top + chartH / 2}
        textAnchor="middle" fontSize={10} fill="#999"
        transform={`rotate(-90, 12, ${PAD.top + chartH / 2})`}
      >{yLabel}</text>

      {/* Bars */}
      {labels.map((label, i) => {
        const cx = PAD.left + i * barGap + barGap / 2;
        let stackY = PAD.top + chartH;
        return (
          <g key={label}>
            {datasets.map((ds) => {
              const barH = (ds.values[i] / maxVal) * chartH;
              stackY -= barH;
              return (
                <rect
                  key={ds.label}
                  x={cx - barW / 2}
                  y={stackY}
                  width={barW}
                  height={barH}
                  fill={ds.color}
                  rx={2}
                />
              );
            })}
            <text x={cx} y={PAD.top + chartH + 14} textAnchor="middle" fontSize={10} fill="#ccc">{label}</text>
          </g>
        );
      })}

      {/* X-axis label */}
      <text x={PAD.left + chartW / 2} y={H - 4} textAnchor="middle" fontSize={10} fill="#999">{xLabel}</text>

      {/* Legend */}
      {datasets.map((ds, i) => (
        <g key={ds.label} transform={`translate(${PAD.left + i * 100}, ${H - 14})`}>
          <rect width={10} height={10} fill={ds.color} rx={2} />
          <text x={14} y={9} fontSize={9} fill="#ccc">{ds.label}</text>
        </g>
      ))}
    </svg>
  );
};

/* ─── Pie Chart ──────────────────────────────────────── */
const PieChart = ({ data }) => {
  const { segments, title } = data;
  const W = 300, H = 280;
  const cx = 130, cy = 150, r = 100;

  const total = segments.reduce((s, seg) => s + seg.value, 0);
  let startAngle = -Math.PI / 2;

  const slices = segments.map((seg) => {
    const angle = (seg.value / total) * 2 * Math.PI;
    const midAngle = startAngle + angle / 2;
    const x1 = cx + r * Math.cos(startAngle);
    const y1 = cy + r * Math.sin(startAngle);
    const x2 = cx + r * Math.cos(startAngle + angle);
    const y2 = cy + r * Math.sin(startAngle + angle);
    const largeArc = angle > Math.PI ? 1 : 0;
    const labelR = r * 0.65;
    const lx = cx + labelR * Math.cos(midAngle);
    const ly = cy + labelR * Math.sin(midAngle);
    // Legend label position (outside)
    const legR = r + 18;
    const legX = cx + legR * Math.cos(midAngle);
    const legY = cy + legR * Math.sin(midAngle);

    const slice = {
      path: `M ${cx} ${cy} L ${x1} ${y1} A ${r} ${r} 0 ${largeArc} 1 ${x2} ${y2} Z`,
      color: seg.color,
      label: seg.label,
      pct: seg.value + '%',
      lx, ly,
      legX, legY,
      midAngle,
    };
    startAngle += angle;
    return slice;
  });

  return (
    <svg width={W} height={H} style={{ fontFamily: 'inherit', overflow: 'visible' }}>
      <text x={W / 2} y={16} textAnchor="middle" fontSize={12} fontWeight="600" fill="#ccc">{title}</text>
      {slices.map((s, i) => (
        <g key={i}>
          <path d={s.path} fill={s.color} stroke="rgba(0,0,0,0.3)" strokeWidth={1.5} />
          {/* Percentage inside slice */}
          <text x={s.lx} y={s.ly + 4} textAnchor="middle" fontSize={11} fontWeight="bold" fill="white">{s.pct}</text>
        </g>
      ))}
      {/* Legend labels outside */}
      {slices.map((s, i) => {
        // Anchor based on which side of the pie
        const anchor = s.legX > cx ? 'start' : 'end';
        const lx = s.legX > cx ? s.legX + 4 : s.legX - 4;
        return (
          <text key={i} x={lx} y={s.legY + 4} textAnchor={anchor} fontSize={10} fill="#ccc">{s.label}</text>
        );
      })}
    </svg>
  );
};

/* ─── Main QuestionChart ─────────────────────────────── */
const QuestionChart = ({ chart }) => {
  if (!chart) return null;

  return (
    <div style={{
      display: 'flex',
      flexWrap: 'wrap',
      gap: '1rem',
      alignItems: 'center',
      justifyContent: 'center',
      background: 'rgba(255,255,255,0.03)',
      border: '1px solid rgba(255,255,255,0.08)',
      borderRadius: '12px',
      padding: '1rem',
      marginBottom: '1.5rem',
      overflowX: 'auto',
    }}>
      {chart.bar && <StackedBarChart data={chart.bar} />}
      {chart.pie && <PieChart data={chart.pie} />}
    </div>
  );
};

export default QuestionChart;
