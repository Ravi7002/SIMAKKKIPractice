import React, { useState, useMemo } from 'react';
import { ArrowLeft, Book, Grid, ChevronRight, ChevronDown, Lightbulb, CheckCircle, XCircle, FlaskConical } from 'lucide-react';
import MathText from './MathText';

/* ─── Chart / Table Renderer ─────────────────────────────── */
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

/* ─── Topic Quiz (no back, no timer, pick until correct, hints) ─── */
const TopicQuiz = ({ questions, onFinish }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [guessedOptions, setGuessedOptions] = useState([]);
  const [showExplanation, setShowExplanation] = useState(false);
  const [hintsRevealed, setHintsRevealed] = useState(0);

  const question = questions[currentIndex];
  const isLast = currentIndex === questions.length - 1;

  const handleOption = (letter) => {
    if (showExplanation) return;
    if (guessedOptions.includes(letter)) return;

    const newGuesses = [...guessedOptions, letter];
    setGuessedOptions(newGuesses);

    if (letter === question.correct_answer) {
      setShowExplanation(true);
    }
  };

  const handleNext = () => {
    if (isLast) {
      onFinish();
    } else {
      setCurrentIndex(i => i + 1);
      setGuessedOptions([]);
      setShowExplanation(false);
      setHintsRevealed(0);
    }
  };

  const revealHint = () => {
    if (hintsRevealed < (question.hints?.length || 0)) {
      setHintsRevealed(h => h + 1);
    }
  };

  if (!question) return null;

  return (
    <div className="fade-in" style={{ maxWidth: '800px', margin: '0 auto' }}>
      {/* Progress */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
        <div>
          <span className="text-muted">Question </span>
          <strong>{currentIndex + 1}</strong>
          <span className="text-muted"> / {questions.length}</span>
        </div>
        <div className="badge badge-gray" style={{ textTransform: 'capitalize' }}>{question.difficulty}</div>
      </div>

      <div className="progress-container" style={{ marginBottom: '1.5rem' }}>
        <div className="progress-fill" style={{ width: `${(currentIndex / questions.length) * 100}%` }} />
      </div>

      {/* Question card */}
      <div className="glass-card mb-4">
        {question.chart_data && <ChartDisplay chartData={question.chart_data} />}
        <div style={{ fontSize: '1.2rem', lineHeight: '1.7', marginBottom: '1.5rem', whiteSpace: 'pre-wrap' }}>
          <MathText text={question.question_text} />
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
          {question.options.map(opt => {
            const isGuessed = guessedOptions.includes(opt.letter);
            const isCorrect = opt.letter === question.correct_answer;

            let borderColor = 'rgba(255,255,255,0.1)';
            let bg = 'rgba(255,255,255,0.03)';
            if (isGuessed && isCorrect) { borderColor = 'var(--accent-green)'; bg = 'rgba(16,185,129,0.1)'; }
            else if (isGuessed && !isCorrect) { borderColor = 'var(--accent-red)'; bg = 'rgba(239,68,68,0.1)'; }

            return (
              <button
                key={opt.letter}
                onClick={() => handleOption(opt.letter)}
                disabled={isGuessed && !isCorrect}
                style={{
                  display: 'flex', gap: '1rem', alignItems: 'flex-start',
                  padding: '1rem', borderRadius: '10px',
                  border: `1px solid ${borderColor}`,
                  background: bg,
                  cursor: (isGuessed && !isCorrect) ? 'not-allowed' : 'pointer',
                  textAlign: 'left', transition: 'all 0.2s',
                  color: 'var(--text)',
                }}
              >
                <span style={{ fontWeight: 'bold', minWidth: '24px', color: 'var(--accent-purple)' }}>{opt.letter}.</span>
                <span style={{ flex: 1, lineHeight: '1.5' }}><MathText text={opt.text} /></span>
                {isGuessed && isCorrect && <CheckCircle size={20} style={{ color: 'var(--accent-green)', flexShrink: 0 }} />}
                {isGuessed && !isCorrect && <XCircle size={20} style={{ color: 'var(--accent-red)', flexShrink: 0 }} />}
              </button>
            );
          })}
        </div>
      </div>

      {/* Hint section */}
      {!showExplanation && question.hints && question.hints.length > 0 && (
        <div className="glass-card mb-4 fade-in" style={{ background: 'rgba(234,179,8,0.05)', border: '1px solid rgba(234,179,8,0.15)' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: '#f59e0b' }}>
              <Lightbulb size={18} />
              <strong>Hints</strong>
              <span className="text-muted" style={{ fontSize: '0.85rem' }}>({hintsRevealed}/{question.hints.length} revealed)</span>
            </div>
            {hintsRevealed < question.hints.length && (
              <button
                onClick={revealHint}
                style={{ padding: '0.4rem 1rem', borderRadius: '8px', border: '1px solid rgba(234,179,8,0.3)', background: 'rgba(234,179,8,0.1)', color: '#f59e0b', cursor: 'pointer', fontSize: '0.9rem' }}
              >
                Show Hint {hintsRevealed + 1}
              </button>
            )}
          </div>

          {hintsRevealed > 0 && (
            <div style={{ marginTop: '1rem', display: 'flex', flexDirection: 'column', gap: '0.6rem' }}>
              {question.hints.slice(0, hintsRevealed).map((hint, i) => (
                <div key={i} className="fade-in" style={{ display: 'flex', gap: '0.8rem', alignItems: 'flex-start' }}>
                  <span style={{ background: '#f59e0b', color: 'black', borderRadius: '50%', width: '22px', height: '22px', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '0.75rem', fontWeight: 'bold', flexShrink: 0 }}>{i + 1}</span>
                  <span style={{ color: '#fde68a', lineHeight: '1.5', fontSize: '0.95rem' }}><MathText text={hint} /></span>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* Explanation */}
      {showExplanation && (
        <div className="glass-card fade-in mb-4" style={{ background: 'rgba(16,185,129,0.05)', border: '1px solid rgba(16,185,129,0.2)' }}>
          <h4 style={{ color: 'var(--accent-green)', marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <CheckCircle size={18} /> Correct! Here's the full solution:
          </h4>
          <div style={{ lineHeight: '1.7', whiteSpace: 'pre-wrap', color: 'var(--text-muted)' }}>
            <MathText text={question.explanation} />
          </div>
        </div>
      )}

      {/* Next button */}
      {showExplanation && (
        <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
          <button onClick={handleNext} className="btn btn-primary fade-in" style={{ minWidth: '160px' }}>
            {isLast ? 'Finish Quiz' : 'Next Question'} <ChevronRight size={18} />
          </button>
        </div>
      )}
    </div>
  );
};

/* ─── Learn View ─────────────────────────────────────── */
const LearnView = ({ topicData, onStartQuiz }) => {
  const [openExample, setOpenExample] = useState(null);

  return (
    <div className="fade-in" style={{ maxWidth: '860px', margin: '0 auto' }}>
      {/* Header */}
      <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
        <h2 className="text-gradient" style={{ fontSize: '2.5rem', marginBottom: '0.5rem' }}>{topicData.topic}</h2>
        <p className="text-muted">{topicData.subject}</p>
      </div>

      {/* Introduction */}
      <div className="glass-card mb-4">
        <h3 style={{ color: 'var(--accent-blue)', marginBottom: '1rem' }}>📖 Introduction</h3>
        <p style={{ lineHeight: '1.7' }}>{topicData.introduction}</p>
      </div>

      {/* Key Formulas */}
      {topicData.key_formulas && topicData.key_formulas.length > 0 && (
        <div className="glass-card mb-4">
          <h3 style={{ color: 'var(--accent-purple)', marginBottom: '1.2rem' }}>📐 Key Formulas</h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
            {topicData.key_formulas.map((f, i) => (
              <div key={i} style={{ display: 'flex', alignItems: 'center', gap: '1rem', padding: '0.8rem 1.2rem', background: 'rgba(139,92,246,0.07)', borderRadius: '8px', border: '1px solid rgba(139,92,246,0.15)' }}>
                <span style={{ color: 'var(--text-muted)', fontSize: '0.9rem', minWidth: '160px' }}>{f.name}:</span>
                <span style={{ fontWeight: '600' }}><MathText text={f.formula} /></span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Tips & Tricks */}
      {topicData.tips_and_tricks && topicData.tips_and_tricks.length > 0 && (
        <div className="glass-card mb-4">
          <h3 style={{ color: 'var(--accent-green)', marginBottom: '1rem' }}>💡 Tips & Tricks</h3>
          <ul style={{ listStyle: 'none', padding: 0, display: 'flex', flexDirection: 'column', gap: '0.7rem' }}>
            {topicData.tips_and_tricks.map((tip, i) => (
              <li key={i} style={{ display: 'flex', gap: '0.8rem', alignItems: 'flex-start' }}>
                <span style={{ color: 'var(--accent-green)', marginTop: '2px' }}>✓</span>
                <span className="text-muted" style={{ lineHeight: '1.6' }}><MathText text={tip} /></span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Worked Examples */}
      {topicData.worked_examples && topicData.worked_examples.length > 0 && (
        <div className="glass-card mb-6">
          <h3 style={{ color: '#f59e0b', marginBottom: '1.2rem' }}>🎯 Worked Examples (Real Exam Style)</h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            {topicData.worked_examples.map((ex, i) => (
              <div key={i} style={{ border: '1px solid rgba(245,158,11,0.2)', borderRadius: '10px', overflow: 'hidden' }}>
                <button
                  onClick={() => setOpenExample(openExample === i ? null : i)}
                  style={{ width: '100%', padding: '1rem 1.2rem', background: 'rgba(245,158,11,0.07)', border: 'none', cursor: 'pointer', display: 'flex', justifyContent: 'space-between', alignItems: 'center', color: 'white', textAlign: 'left' }}
                >
                  <span style={{ fontWeight: '600' }}>{ex.title}</span>
                  <ChevronDown size={18} style={{ transform: openExample === i ? 'rotate(180deg)' : 'none', transition: 'transform 0.2s' }} />
                </button>

                {openExample === i && (
                  <div className="fade-in" style={{ padding: '1.2rem' }}>
                    <div style={{ background: 'rgba(255,255,255,0.04)', borderRadius: '8px', padding: '1rem', marginBottom: '1rem' }}>
                      <strong style={{ color: '#f59e0b' }}>Question:</strong>
                      <p style={{ marginTop: '0.5rem', lineHeight: '1.6' }}><MathText text={ex.question} /></p>
                    </div>
                    <div>
                      <strong style={{ color: 'var(--accent-green)' }}>Step-by-Step Solution:</strong>
                      <div style={{ marginTop: '0.8rem', display: 'flex', flexDirection: 'column', gap: '0.6rem' }}>
                        {ex.solution.map((step, j) => (
                          <div key={j} style={{ display: 'flex', gap: '0.8rem', alignItems: 'flex-start' }}>
                            <span style={{ background: 'var(--accent-green)', color: 'black', borderRadius: '50%', width: '22px', height: '22px', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '0.75rem', fontWeight: 'bold', flexShrink: 0 }}>{j + 1}</span>
                            <span className="text-muted" style={{ lineHeight: '1.6' }}><MathText text={step} /></span>
                          </div>
                        ))}
                      </div>
                    </div>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Start Quiz CTA */}
      <div style={{ textAlign: 'center', padding: '2rem 0' }}>
        <p className="text-muted mb-4">Ready to test your understanding?</p>
        <button onClick={onStartQuiz} className="btn btn-primary" style={{ fontSize: '1.2rem', padding: '1rem 3rem' }}>
          <FlaskConical size={22} /> Start Practice Quiz (3 Questions)
        </button>
      </div>
    </div>
  );
};

/* ─── Quiz Complete ──────────────────────────────────── */
const QuizComplete = ({ onRetry, onBack }) => (
  <div className="glass-card fade-in text-center" style={{ maxWidth: '500px', margin: '4rem auto', padding: '3rem' }}>
    <div style={{ fontSize: '4rem', marginBottom: '1rem' }}>🎉</div>
    <h2 className="text-gradient mb-4" style={{ fontSize: '2rem' }}>Quiz Complete!</h2>
    <p className="text-muted mb-6">Great work! You answered all 3 questions correctly.</p>
    <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center', flexWrap: 'wrap' }}>
      <button onClick={onRetry} className="btn btn-outline">Try Again</button>
      <button onClick={onBack} className="btn btn-primary">Back to Topics</button>
    </div>
  </div>
);

/* ─── Main PracticeTest Component ────────────────────── */
const PracticeTest = ({ allTopicsData, onBack }) => {
  const [view, setView] = useState('subjects'); // 'subjects', 'topics', 'learn', 'quiz', 'done'
  const [selectedSubject, setSelectedSubject] = useState(null);
  const [selectedTopic, setSelectedTopic] = useState(null);
  const [quizQuestions, setQuizQuestions] = useState([]);

  const subjects = [...new Set(allTopicsData.map(t => t.subject))];

  const topicsForSubject = selectedSubject
    ? allTopicsData.filter(t => t.subject === selectedSubject)
    : [];

  const handleSubjectClick = (sub) => {
    setSelectedSubject(sub);
    setView('topics');
  };

  const handleTopicClick = (topicObj) => {
    setSelectedTopic(topicObj);
    setView('learn');
  };

  const startQuiz = () => {
    // Randomly pick 3 questions from the topic
    const pool = [...(selectedTopic.questions || [])];
    const shuffled = pool.sort(() => Math.random() - 0.5);
    setQuizQuestions(shuffled.slice(0, 3));
    setView('quiz');
  };

  const goBack = () => {
    if (view === 'subjects') onBack();
    else if (view === 'topics') { setSelectedSubject(null); setView('subjects'); }
    else if (view === 'learn') setView('topics');
    else if (view === 'quiz') setView('learn');
    else if (view === 'done') setView('topics');
  };

  // Subject color map
  const subjectColors = {
    'Basic Mathematics': 'var(--accent-blue)',
    'English': 'var(--accent-green)',
    'Quantitative Reasoning': 'var(--accent-purple)',
    'Logical Reasoning': 'var(--accent-pink)',
  };
  const subjectIcons = {
    'Basic Mathematics': '📐',
    'English': '📝',
    'Quantitative Reasoning': '🔢',
    'Logical Reasoning': '🧠',
  };

  return (
    <div style={{ width: '100%', maxWidth: '960px', margin: '0 auto', padding: '1rem' }}>

      {/* Back button */}
      {view !== 'done' && (
        <button onClick={goBack} className="btn" style={{ marginBottom: '2rem', padding: '0.5rem 1.2rem', background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(255,255,255,0.1)' }}>
          <ArrowLeft size={18} /> Back
        </button>
      )}

      {/* Subjects */}
      {view === 'subjects' && (
        <div className="fade-in">
          <div style={{ textAlign: 'center', marginBottom: '2.5rem' }}>
            <h2 className="text-gradient" style={{ fontSize: '2.5rem' }}>
              <Book size={36} style={{ verticalAlign: 'middle', marginRight: '12px' }} /> Practice Test
            </h2>
            <p className="text-muted">Select a subject to begin learning</p>
          </div>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '1.2rem' }}>
            {subjects.map(sub => (
              <button
                key={sub}
                className="glass-card btn"
                onClick={() => handleSubjectClick(sub)}
                style={{ padding: '2rem', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '1rem', border: `1px solid ${subjectColors[sub] || 'rgba(255,255,255,0.1)'}20`, transition: 'all 0.2s' }}
              >
                <span style={{ fontSize: '2.5rem' }}>{subjectIcons[sub] || '📚'}</span>
                <span style={{ fontSize: '1.1rem', fontWeight: '600', color: subjectColors[sub] || 'white' }}>{sub}</span>
                <span className="text-muted" style={{ fontSize: '0.85rem' }}>
                  {allTopicsData.filter(t => t.subject === sub).length} topics
                </span>
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Topics */}
      {view === 'topics' && (
        <div className="fade-in">
          <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
            <h2 className="text-gradient" style={{ fontSize: '2rem' }}>
              <Grid size={28} style={{ verticalAlign: 'middle', marginRight: '10px' }} />
              {selectedSubject}
            </h2>
            <p className="text-muted">Select a topic to study</p>
          </div>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '1rem' }}>
            {topicsForSubject.map(t => (
              <button
                key={t.topic}
                className="glass-card"
                onClick={() => handleTopicClick(t)}
                style={{ padding: '1.5rem', textAlign: 'left', cursor: 'pointer', border: '1px solid rgba(255,255,255,0.08)', transition: 'all 0.2s', display: 'flex', flexDirection: 'column', gap: '0.6rem' }}
              >
                <span style={{ fontSize: '1.1rem', fontWeight: '700' }}>{t.topic}</span>
                <span className="text-muted" style={{ fontSize: '0.85rem' }}>
                  {t.questions?.length || 0} questions · {
                    [...new Set(t.questions?.map(q => q.difficulty) || [])].join(', ')
                  }
                </span>
                <div style={{ display: 'flex', gap: '0.4rem', marginTop: '0.3rem' }}>
                  {['easy','medium','hard'].map(d => {
                    const n = (t.questions || []).filter(q => q.difficulty === d).length;
                    if (!n) return null;
                    const color = d === 'easy' ? 'var(--accent-green)' : d === 'medium' ? '#f59e0b' : 'var(--accent-red)';
                    return <span key={d} style={{ fontSize: '0.75rem', padding: '2px 8px', borderRadius: '10px', border: `1px solid ${color}50`, color }}>{n} {d}</span>;
                  })}
                </div>
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Learn */}
      {view === 'learn' && selectedTopic && (
        <LearnView topicData={selectedTopic} onStartQuiz={startQuiz} />
      )}

      {/* Quiz */}
      {view === 'quiz' && quizQuestions.length > 0 && (
        <TopicQuiz questions={quizQuestions} onFinish={() => setView('done')} />
      )}

      {/* Done */}
      {view === 'done' && (
        <QuizComplete
          onRetry={startQuiz}
          onBack={() => setView('topics')}
        />
      )}
    </div>
  );
};

export default PracticeTest;
