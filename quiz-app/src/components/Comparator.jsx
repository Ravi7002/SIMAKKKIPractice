import React, { useState, useMemo } from 'react';
import { ArrowLeft, GitCompare, ChevronDown } from 'lucide-react';
import MathText from './MathText';
import QuestionChart from './QuestionChart';
import ChartDisplay from './ChartDisplay';

const Comparator = ({ allTopicsData, realQ1, generatedTryouts = [], onBack }) => {
  const [selectedTopic, setSelectedTopic] = useState('');
  const [rightSource, setRightSource] = useState('practice'); // 'practice' | 'generated'

  // Extract all unique topics present in realQ1
  const realTopics = useMemo(() => {
    const topics = new Set();
    realQ1.forEach(q => {
      if (q.topic) topics.add(q.topic);
    });
    return Array.from(topics).sort();
  }, [realQ1]);

  // Questions for the selected topic
  const realQuestions = useMemo(() => {
    if (!selectedTopic) return [];
    return realQ1.filter(q => q.topic === selectedTopic);
  }, [realQ1, selectedTopic]);

  const displayQuestions = useMemo(() => {
    if (!selectedTopic) return [];
    
    if (rightSource === 'practice') {
      const topicData = allTopicsData.find(t => t.topic === selectedTopic);
      return topicData ? (topicData.questions || []) : [];
    } else {
      const allGen = generatedTryouts.flat();
      return allGen.filter(q => q.topic === selectedTopic);
    }
  }, [allTopicsData, generatedTryouts, selectedTopic, rightSource]);

  // Option renderer helper
  const renderOptions = (options, correctAnswer) => {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem', marginTop: '1rem' }}>
        {options.map((opt, i) => (
          <div key={i} style={{ 
            display: 'flex', 
            gap: '1rem', 
            padding: '0.8rem', 
            background: opt.letter === correctAnswer ? 'rgba(16,185,129,0.1)' : 'rgba(255,255,255,0.03)',
            border: `1px solid ${opt.letter === correctAnswer ? 'var(--accent-green)' : 'rgba(255,255,255,0.1)'}`,
            borderRadius: '8px' 
          }}>
            <span style={{ fontWeight: 'bold', color: opt.letter === correctAnswer ? 'var(--accent-green)' : 'var(--text-muted)' }}>{opt.letter}.</span>
            <span><MathText text={opt.text} /></span>
          </div>
        ))}
      </div>
    );
  };

  return (
    <div style={{ width: '100%', maxWidth: '1400px', margin: '0 auto', padding: '1rem', display: 'flex', flexDirection: 'column', height: '100vh', maxHeight: '100vh', overflow: 'hidden' }}>
      {/* Header */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '1.5rem', flexShrink: 0 }}>
        <button onClick={onBack} className="btn" style={{ padding: '0.5rem 1.2rem', background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(255,255,255,0.1)' }}>
          <ArrowLeft size={18} /> Back
        </button>
        <h2 className="text-gradient" style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '0.5rem', fontSize: '2rem' }}>
          <GitCompare size={28} /> Real vs Practice
        </h2>
        
        {/* Topic Selector */}
        <div style={{ position: 'relative' }}>
          <select 
            value={selectedTopic} 
            onChange={(e) => setSelectedTopic(e.target.value)}
            style={{ 
              padding: '0.8rem 2.5rem 0.8rem 1rem', 
              background: 'rgba(255,255,255,0.05)', 
              color: 'white', 
              border: '1px solid rgba(255,255,255,0.2)', 
              borderRadius: '8px',
              fontSize: '1rem',
              appearance: 'none',
              minWidth: '250px',
              cursor: 'pointer'
            }}
          >
            <option value="" disabled>Select a topic...</option>
            {realTopics.map(t => <option key={t} value={t} style={{ color: 'black' }}>{t}</option>)}
          </select>
          <ChevronDown size={18} style={{ position: 'absolute', right: '12px', top: '50%', transform: 'translateY(-50%)', pointerEvents: 'none', color: 'var(--text-muted)' }} />
        </div>
      </div>

      {/* Split View Content */}
      <div style={{ display: 'flex', gap: '2rem', flex: 1, overflow: 'hidden' }}>
        
        {/* Left Side: Real Q1 */}
        <div className="glass-card" style={{ flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden', padding: 0 }}>
          <div style={{ padding: '1rem', background: 'rgba(239, 68, 68, 0.1)', borderBottom: '1px solid rgba(239, 68, 68, 0.2)', textAlign: 'center', flexShrink: 0 }}>
            <h3 style={{ color: 'var(--accent-red)', margin: 0 }}>Real Tryout (realQ1)</h3>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>{realQuestions.length} questions found</span>
          </div>
          <div style={{ overflowY: 'auto', padding: '1.5rem', flex: 1 }}>
            {!selectedTopic ? (
              <div style={{ textAlign: 'center', color: 'var(--text-muted)', marginTop: '4rem' }}>Please select a topic from the dropdown.</div>
            ) : realQuestions.length === 0 ? (
              <div style={{ textAlign: 'center', color: 'var(--text-muted)', marginTop: '4rem' }}>No questions found for this topic in realQ1.</div>
            ) : (
              realQuestions.map((q, idx) => (
                <div key={q.id || idx} style={{ marginBottom: '2.5rem', paddingBottom: '2.5rem', borderBottom: '1px solid rgba(255,255,255,0.1)' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem' }}>
                     <span className="text-muted" style={{ fontSize: '0.9rem', textTransform: 'uppercase', letterSpacing: '0.05em' }}>Question {idx + 1}</span>
                     <span style={{ fontSize: '0.8rem', background: 'rgba(255,255,255,0.1)', padding: '2px 8px', borderRadius: '12px' }}>{q.subject}</span>
                  </div>
                  {q.chart && <QuestionChart chart={q.chart} />}
                  <div style={{ fontSize: '1.1rem', lineHeight: '1.6', marginBottom: '1.5rem', whiteSpace: 'pre-wrap' }}>
                    <MathText text={q.question_text} />
                  </div>
                  {renderOptions(q.options, q.correct_answer)}
                </div>
              ))
            )}
          </div>
        </div>

        {/* Right Side: Compare Output */}
        <div className="glass-card" style={{ flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden', padding: 0 }}>
          <div style={{ padding: '0.8rem 1rem', background: rightSource === 'practice' ? 'rgba(59, 130, 246, 0.1)' : 'rgba(139, 92, 246, 0.1)', borderBottom: `1px solid ${rightSource === 'practice' ? 'rgba(59, 130, 246, 0.2)' : 'rgba(139, 92, 246, 0.2)'}`, display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexShrink: 0 }}>
            <div>
              <select 
                value={rightSource}
                onChange={(e) => setRightSource(e.target.value)}
                style={{ background: 'rgba(255,255,255,0.1)', border: 'none', color: 'white', padding: '0.3rem 0.6rem', borderRadius: '4px', cursor: 'pointer', fontWeight: 'bold' }}
              >
                <option value="practice" style={{color: 'black'}}>Practice Bank</option>
                <option value="generated" style={{color: 'black'}}>Generated Tryouts (Clones)</option>
              </select>
            </div>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>{displayQuestions.length} questions found</span>
          </div>
          <div style={{ overflowY: 'auto', padding: '1.5rem', flex: 1 }}>
            {!selectedTopic ? (
               <div style={{ textAlign: 'center', color: 'var(--text-muted)', marginTop: '4rem' }}>Please select a topic from the dropdown.</div>
            ) : displayQuestions.length === 0 ? (
               <div style={{ textAlign: 'center', color: 'var(--text-muted)', marginTop: '4rem' }}>No counterpart found for this topic.</div>
            ) : (
              displayQuestions.map((q, idx) => (
                <div key={q.id || idx} style={{ marginBottom: '2.5rem', paddingBottom: '2.5rem', borderBottom: '1px solid rgba(255,255,255,0.1)' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem' }}>
                     <span className="text-muted" style={{ fontSize: '0.9rem', textTransform: 'uppercase', letterSpacing: '0.05em' }}>Variant {idx + 1} {rightSource === 'generated' && `(${q.id})`}</span>
                     {q.difficulty && <span style={{ fontSize: '0.8rem', background: q.difficulty === 'easy' ? 'rgba(16,185,129,0.2)' : q.difficulty === 'medium' ? 'rgba(245,158,11,0.2)' : 'rgba(239,68,68,0.2)', color: q.difficulty === 'easy' ? 'var(--accent-green)' : q.difficulty === 'medium' ? '#f59e0b' : 'var(--accent-red)', padding: '2px 8px', borderRadius: '12px', textTransform: 'capitalize' }}>{q.difficulty}</span>}
                  </div>
                  {(q.chart_data || q.chart) && (q.chart_data ? <ChartDisplay chartData={q.chart_data} /> : <QuestionChart chart={q.chart} />)}
                  <div style={{ fontSize: '1.1rem', lineHeight: '1.6', marginBottom: '1.5rem', whiteSpace: 'pre-wrap' }}>
                    <MathText text={q.question_text} />
                  </div>
                  {renderOptions(q.options, q.correct_answer)}
                </div>
              ))
            )}
          </div>
        </div>

      </div>
    </div>
  );
};

export default Comparator;
