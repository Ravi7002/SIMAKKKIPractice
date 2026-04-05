import React, { useMemo, useState } from 'react';
import { evaluateResults } from '../utils';
import { RotateCcw, Target, AlertTriangle, CheckCircle2, XCircle } from 'lucide-react';
import MathText from './MathText';
import QuestionChart from './QuestionChart';

const Results = ({ questions, answers, onRestart }) => {
  const { totalScore, topics } = useMemo(() => evaluateResults(questions, answers), [questions, answers]);

  const maxScore = questions.length * 4;
  const percentage = Math.max(0, (totalScore / maxScore) * 100).toFixed(1);

  const [showReview, setShowReview] = useState(false);

  if (showReview) {
    return (
      <div className="fade-in w-full mx-auto" style={{ maxWidth: '900px' }}>
        <div className="text-center mb-8">
          <h2 className="text-gradient mb-2" style={{ fontSize: '2.5rem' }}>Review Answers</h2>
          <button onClick={() => setShowReview(false)} className="btn btn-outline mt-4">Back to Results</button>
        </div>
        
        <div className="review-list" style={{ display: 'flex', flexDirection: 'column', gap: '2rem', textAlign: 'left' }}>
          {questions.map((q, idx) => {
            const userAnswer = answers[q.id];
            const isCorrect = userAnswer === q.correct_answer;
            return (
              <div key={q.id} className="glass-card" style={{ borderLeft: isCorrect ? '4px solid var(--accent-green)' : (userAnswer ? '4px solid var(--accent-red)' : '4px solid var(--text-muted)') }}>
                <div style={{ marginBottom: '1rem', color: 'var(--text-muted)' }}>Question {idx + 1}</div>
                {q.chart && <QuestionChart chart={q.chart} />}
                <div style={{ fontSize: '1.2rem', marginBottom: '1.5rem', whiteSpace: 'pre-wrap' }}><MathText text={q.question_text} /></div>
                
                <div style={{ display: 'flex', flexDirection: 'column', gap: '0.8rem', marginBottom: '1.5rem' }}>
                  {q.options.map(opt => {
                    const isSelected = userAnswer === opt.letter;
                    const isCorrectOpt = q.correct_answer === opt.letter;
                    let optStyle = { padding: '1rem', borderRadius: '8px', border: '1px solid rgba(255,255,255,0.1)' };
                    
                    if (isCorrectOpt) {
                      optStyle.background = 'rgba(16, 185, 129, 0.2)';
                      optStyle.borderColor = 'var(--accent-green)';
                    } else if (isSelected) {
                      optStyle.background = 'rgba(239, 68, 68, 0.2)';
                      optStyle.borderColor = 'var(--accent-red)';
                    }
                    
                    return (
                      <div key={opt.letter} style={optStyle}>
                        <span style={{ fontWeight: 'bold', marginRight: '1rem' }}>{opt.letter}.</span>
                        <MathText text={opt.text} />
                      </div>
                    )
                  })}
                </div>
                
                <div style={{ background: 'rgba(255,255,255,0.05)', padding: '1rem', borderRadius: '8px' }}>
                  <h4 style={{ color: 'var(--accent-purple)', marginBottom: '0.5rem' }}>Explanation:</h4>
                  <p style={{ lineHeight: '1.5' }}><MathText text={q.explanation || 'No explanation provided.'} /></p>
                </div>
              </div>
            );
          })}
        </div>
        <div className="text-center mt-8 pb-8">
          <button onClick={() => setShowReview(false)} className="btn btn-primary">Back to Results</button>
        </div>
      </div>
    );
  }

  return (
    <div className="fade-in w-full mx-auto" style={{ maxWidth: '900px' }}>
      <div className="text-center mb-8">
        <h1 className="text-gradient mb-2" style={{ fontSize: '3.5rem' }}>Hayyu Done!</h1>
        <p className="text-muted text-lg">Here is your personal performance breakdown</p>
      </div>

      <div className="grid-3 mb-8">
        <div className="glass-card stat-card delay-1">
          <div className="stat-value">{totalScore}</div>
          <div className="text-muted">Total Score</div>
          <div style={{ fontSize: '0.85rem', marginTop: '0.5rem', color: 'var(--accent-purple)' }}>Out of {maxScore}</div>
        </div>
        
        <div className="glass-card stat-card delay-2">
          <div className="stat-value">{percentage}%</div>
          <div className="text-muted">Accuracy Equivalent</div>
        </div>
        
        <div className="glass-card stat-card delay-3">
          <div className="stat-value">{Object.keys(answers).length}</div>
          <div className="text-muted">Questions Attempted</div>
          <div style={{ fontSize: '0.85rem', marginTop: '0.5rem', color: 'var(--accent-green)' }}>Out of {questions.length}</div>
        </div>
      </div>

      <div className="glass-card mb-8 delay-3">
        <div className="flex-between mb-6">
          <h2 style={{ fontSize: '1.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Target className="text-muted" /> Topic Analysis
          </h2>
        </div>

        <p className="text-muted mb-4" style={{ fontSize: '0.9rem' }}>
          Sorted from lowest score to highest. Focus your studies on the top areas below.
        </p>

        <div className="topic-list">
          {topics.map((t, index) => {
            const maxTopicScore = t.totalQuestions * 4;
            const needsPractice = t.score < (maxTopicScore * 0.4); // Less than 40%
            
            return (
              <div key={t.topic} className={`topic-row ${needsPractice ? 'needs-practice' : ''}`} style={{ borderLeft: needsPractice ? '4px solid var(--accent-red)' : '4px solid transparent' }}>
                <div className="topic-header">
                  <div className="topic-title">{t.topic}</div>
                  <div className="topic-score">Score: {t.score} / {maxTopicScore}</div>
                </div>
                
                <div className="flex-between w-full mt-4">
                  <div className="topic-stats">
                    <span className="badge badge-green" title="Correct"><CheckCircle2 size={14}/> {t.correct}</span>
                    <span className="badge badge-red" title="Incorrect"><XCircle size={14}/> {t.incorrect}</span>
                    <span className="badge badge-gray" title="Blank">- {t.blank}</span>
                  </div>
                  {needsPractice && (
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.3rem', color: 'var(--accent-red)', fontSize: '0.85rem', fontWeight: 500 }}>
                      <AlertTriangle size={14} /> Practice Needed
                    </div>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </div>

      <div className="text-center pb-8" style={{ display: 'flex', gap: '1rem', justifyContent: 'center' }}>
        <button onClick={() => setShowReview(true)} className="btn btn-outline" style={{ padding: '1rem 2rem' }}>
          Review Questions
        </button>
        <button onClick={onRestart} className="btn btn-primary" style={{ padding: '1rem 2rem' }}>
          <RotateCcw size={20} /> Try Again
        </button>
      </div>
    </div>
  );
};

export default Results;
