import React, { useMemo } from 'react';
import { evaluateResults } from '../utils';
import { RotateCcw, Target, AlertTriangle, CheckCircle2, XCircle } from 'lucide-react';

const Results = ({ questions, answers, onRestart }) => {
  const { totalScore, topics } = useMemo(() => evaluateResults(questions, answers), [questions, answers]);

  // Max possible score
  const maxScore = questions.length * 4;
  const percentage = Math.max(0, (totalScore / maxScore) * 100).toFixed(1);

  return (
    <div className="fade-in w-full mx-auto" style={{ maxWidth: '900px' }}>
      <div className="text-center mb-8">
        <h1 className="text-gradient mb-2" style={{ fontSize: '3.5rem' }}>Exam Completed</h1>
        <p className="text-muted text-lg">Here is your performance breakdown</p>
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

      <div className="text-center pb-8">
        <button onClick={onRestart} className="btn btn-primary" style={{ padding: '1rem 2rem' }}>
          <RotateCcw size={20} /> Try Again
        </button>
      </div>
    </div>
  );
};

export default Results;
