import React, { useState, useEffect } from 'react';
import { Clock, ShieldAlert, CheckCircle, XCircle, ArrowRight, ArrowLeft, Activity } from 'lucide-react';
import MathText from './MathText';
import ChartDisplay from './ChartDisplay';

const AbilityTest = ({ allTopicsData, onFinish }) => {
  const [phase, setPhase] = useState('intro'); // 'intro', 'stage1', 'stage2', 'review'
  
  // Data for stages
  const [stage1Questions, setStage1Questions] = useState([]);
  const [stage2Questions, setStage2Questions] = useState([]);
  
  // State for Quizzes
  const [currentStage, setCurrentStage] = useState(1);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [answers, setAnswers] = useState({});
  const [timeLeft, setTimeLeft] = useState(0); // in seconds
  
  // Track topic mastery
  const [masteryStatus, setMasteryStatus] = useState({}); // { topicName: 'mastered' | 'partial' | 'not' }

  // Subject order for the Ability Test
  const SUBJECT_ORDER = ['Basic Mathematics', 'English', 'Quantitative Reasoning', 'Logical Reasoning'];

  const sortBySubject = (qs) => [...qs].sort((a, b) => {
    // Prefer the question's own subject, fall back to the topic-level subject
    const aSubj = a.subject ?? a._topicData?.subject ?? '';
    const bSubj = b.subject ?? b._topicData?.subject ?? '';
    const ai = SUBJECT_ORDER.indexOf(aSubj);
    const bi = SUBJECT_ORDER.indexOf(bSubj);
    return (ai === -1 ? 99 : ai) - (bi === -1 ? 99 : bi);
  });

  // Initialization
  useEffect(() => {
    // Pick 1 hard question per topic, sorted by subject order:
    // Basic Mathematics → English → Quantitative Reasoning → Logical Reasoning
    const hardQs = allTopicsData.map(topicData => {
      const q = topicData.questions.find(q => q.difficulty === 'hard') || topicData.questions[0];
      // Explicitly carry the topic-level subject onto the question object as a fallback
      return { ...q, subject: q.subject ?? topicData.subject, _topicName: topicData.topic, _topicData: topicData };
    });
    setStage1Questions(sortBySubject(hardQs));
  }, [allTopicsData]);

  const startStage1 = () => {
    setPhase('stage1');
    setCurrentStage(1);
    setCurrentIndex(0);
    setAnswers({});
    setTimeLeft(120); // 2 minutes per question
  };

  const submitStage1 = () => {
    const newMastery = {};
    const easyQs = [];

    stage1Questions.forEach(q => {
      const isCorrect = answers[q.id] === q.correct_answer;
      if (isCorrect) {
        newMastery[q._topicName] = 'mastered';
      } else {
        // Needs retest
        newMastery[q._topicName] = 'not_yet';
        const easyQ = q._topicData.questions.find(sq => sq.difficulty === 'easy') || q._topicData.questions[0];
        easyQs.push({ ...easyQ, subject: easyQ.subject ?? q._topicData.subject, _topicName: q._topicName, _topicData: q._topicData });
      }
    });

    setMasteryStatus(newMastery);
    setStage2Questions(sortBySubject(easyQs));
    
    if (easyQs.length === 0) {
      setPhase('review'); // Got everything perfect!
    } else {
      // Transition to stage 2
      setPhase('stage2_intro');
    }
  };

  const startStage2 = () => {
    setPhase('stage2');
    setCurrentStage(2);
    setCurrentIndex(0);
    // Keep stage 1 answers, but we use a new answers mapping implicitly or overwrite. Let's just track globally based on unique ID.
    // Or we keep the same answers obj.
    setTimeLeft(120); // 2 min per question
  };

  const submitStage2 = () => {
    const finalMastery = { ...masteryStatus };

    stage2Questions.forEach(q => {
      const isCorrect = answers[q.id] === q.correct_answer;
      if (isCorrect) {
        finalMastery[q._topicName] = 'partial';
      } else {
        finalMastery[q._topicName] = 'none';
      }
    });

    setMasteryStatus(finalMastery);
    setPhase('review');
  };

  useEffect(() => {
    if ((phase === 'stage1' || phase === 'stage2') && timeLeft > 0) {
      const timer = setInterval(() => setTimeLeft(t => t - 1), 1000);
      return () => clearInterval(timer);
    } else if ((phase === 'stage1' || phase === 'stage2') && timeLeft === 0) {
      const questions = phase === 'stage1' ? stage1Questions : stage2Questions;
      if (currentIndex < questions.length - 1) {
        setCurrentIndex(i => i + 1);
        setTimeLeft(120);
      } else {
        if (phase === 'stage1') submitStage1();
        else submitStage2();
      }
    }
  }, [phase, timeLeft, currentIndex, stage1Questions, stage2Questions, answers, masteryStatus]);

  // Handle generic quiz rendering
  const renderQuiz = (questions, stageLabel, onSubmit) => {
    if (!questions[currentIndex]) return null;
    const q = questions[currentIndex];
    
    return (
      <div className="glass-card fade-in" style={{ maxWidth: '800px', margin: '2rem auto' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem', borderBottom: '1px solid rgba(255,255,255,0.1)', paddingBottom: '1rem' }}>
          <div>
            <h2 className="text-gradient" style={{ margin: 0 }}>{stageLabel}</h2>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginTop: '0.5rem', flexWrap: 'wrap' }}>
              <span style={{
                background: (() => {
                  switch(q.subject) {
                    case 'Basic Mathematics': return 'rgba(139, 92, 246, 0.25)';
                    case 'English': return 'rgba(59, 130, 246, 0.25)';
                    case 'Quantitative Reasoning': return 'rgba(16, 185, 129, 0.25)';
                    case 'Logical Reasoning': return 'rgba(245, 158, 11, 0.25)';
                    default: return 'rgba(255,255,255,0.1)';
                  }
                })(),
                color: (() => {
                  switch(q.subject) {
                    case 'Basic Mathematics': return 'var(--accent-purple)';
                    case 'English': return 'var(--accent-blue)';
                    case 'Quantitative Reasoning': return 'var(--accent-green)';
                    case 'Logical Reasoning': return '#f59e0b';
                    default: return 'var(--text-muted)';
                  }
                })(),
                padding: '3px 10px', borderRadius: '20px', fontSize: '0.8rem', fontWeight: '600', letterSpacing: '0.03em'
              }}>
                {q.subject ?? 'Unknown Subject'}
              </span>
              <span className="text-muted" style={{ fontSize: '0.9rem' }}>
                {q._topicName} • Question {currentIndex + 1} of {questions.length}
              </span>
            </div>
          </div>
          
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', background: timeLeft < 60 ? 'rgba(239, 68, 68, 0.2)' : 'rgba(255,255,255,0.05)', padding: '0.5rem 1rem', borderRadius: '20px', color: timeLeft < 60 ? 'var(--accent-pink)' : 'inherit', transition: 'all 0.3s ease' }}>
            <Clock size={18} />
            <span style={{ fontWeight: 'bold', fontFamily: 'monospace', fontSize: '1.2rem' }}>
              {Math.floor(timeLeft / 60).toString().padStart(2, '0')}:{(timeLeft % 60).toString().padStart(2, '0')}
            </span>
          </div>
        </div>

        <div style={{ fontSize: '1.2rem', lineHeight: '1.6', marginBottom: '2rem' }}>
          {q.chart_data && <ChartDisplay chartData={q.chart_data} />}
          <MathText text={q.question_text} />
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem', marginBottom: '2rem' }}>
          {q.options.map((opt) => {
            const isSelected = answers[q.id] === opt.letter;
            return (
              <button 
                key={opt.letter} 
                className={`btn ${isSelected ? 'btn-primary' : 'btn-outline'}`}
                onClick={() => setAnswers({ ...answers, [q.id]: opt.letter })}
                style={{ textAlign: 'left', padding: '1rem', display: 'flex', gap: '1rem', fontSize: '1.1rem' }}
              >
                <span style={{ fontWeight: 'bold', minWidth: '24px' }}>{opt.letter}.</span>
                <span><MathText text={opt.text} /></span>
              </button>
            )
          })}
        </div>

        <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '2rem' }}>
          {currentIndex === questions.length - 1 ? (
            <button className="btn btn-primary" onClick={onSubmit} style={{ background: 'var(--accent-pink)' }}>
              Submit Stage
            </button>
          ) : (
            <button className="btn btn-primary" onClick={() => {
              setCurrentIndex(i => i + 1);
              setTimeLeft(120);
            }}>
              Next Question
            </button>
          )}
        </div>
      </div>
    );
  };

  if (phase === 'intro') {
    return (
      <div className="glass-card fade-in text-center" style={{ maxWidth: '600px', margin: '4rem auto' }}>
        <ShieldAlert size={64} className="mb-4" style={{ color: 'var(--accent-blue)', margin: '0 auto' }} />
        <h2 className="text-gradient mb-4" style={{ fontSize: '2.5rem' }}>Ability Test</h2>
        <p className="text-muted mb-6 text-lg" style={{ lineHeight: '1.6' }}>
          This adaptive test will evaluate your true mastery over all 29 exam topics.
        </p>
        <div style={{ background: 'rgba(255,255,255,0.05)', padding: '1.5rem', borderRadius: '12px', textAlign: 'left', marginBottom: '2rem' }}>
          <h4 style={{ color: 'var(--accent-purple)', marginBottom: '1rem' }}>Test Structure:</h4>
          <ul style={{ display: 'flex', flexDirection: 'column', gap: '0.8rem', color: 'var(--text-muted)' }}>
            <li><strong style={{ color: 'white' }}>Stage 1:</strong> 29 Hard questions (1 per topic). 2 minutes per question.</li>
            <li><strong style={{ color: 'white' }}>Stage 2:</strong> Retest on failed topics with Easy questions. 2 minutes per question.</li>
            <li><strong style={{ color: 'white' }}>Evaluation:</strong> Topics will be graded as Mastered, Partially Mastered, or Not Mastered At All.</li>
            <li><strong style={{ color: 'white' }}>Note:</strong> You cannot return to previous questions.</li>
          </ul>
        </div>
        <button className="btn btn-primary" onClick={startStage1} style={{ fontSize: '1.2rem', padding: '1rem 3rem' }}>
          Begin Stage 1
        </button>
        <div style={{ marginTop: '1rem' }}>
          <button className="btn btn-outline" onClick={onFinish} style={{ border: 'none' }}>Cancel</button>
        </div>
      </div>
    );
  }

  if (phase === 'stage1') return renderQuiz(stage1Questions, 'Ability Test • Stage 1 (Hard)', submitStage1);

  if (phase === 'stage2_intro') {
    return (
      <div className="glass-card fade-in text-center" style={{ maxWidth: '600px', margin: '4rem auto' }}>
        <Activity size={64} className="mb-4" style={{ color: 'var(--accent-pink)', margin: '0 auto' }} />
        <h2 className="text-gradient mb-4" style={{ fontSize: '2.5rem' }}>Stage 1 Complete</h2>
        <p className="text-muted mb-6 text-lg" style={{ lineHeight: '1.6' }}>
          You mastered {stage1Questions.length - stage2Questions.length} out of {stage1Questions.length} topics on the first try!
          <br /><br />
          We will now retest the remaining {stage2Questions.length} topics using fundamentals (Easy questions).
        </p>
        <button className="btn btn-primary" onClick={startStage2} style={{ fontSize: '1.2rem', padding: '1rem 3rem', background: 'var(--accent-pink)' }}>
          Begin Stage 2
        </button>
      </div>
    );
  }

  if (phase === 'stage2') return renderQuiz(stage2Questions, 'Ability Test • Stage 2 (Foundation Recovery)', submitStage2);

  if (phase === 'review') {
    const mastered = Object.entries(masteryStatus).filter(([k,v]) => v === 'mastered').map(e => e[0]);
    const partial = Object.entries(masteryStatus).filter(([k,v]) => v === 'partial').map(e => e[0]);
    const none = Object.entries(masteryStatus).filter(([k,v]) => v === 'none').map(e => e[0]);

    return (
      <div className="glass-card fade-in" style={{ maxWidth: '800px', margin: '2rem auto' }}>
        <h2 className="text-gradient mb-6" style={{ fontSize: '2.5rem', textAlign: 'center' }}>Final Ability Review</h2>
        
        <div style={{ display: 'grid', gap: '2rem' }}>
          
          <div style={{ background: 'rgba(34, 197, 94, 0.1)', padding: '1.5rem', borderRadius: '12px', borderLeft: '4px solid var(--accent-green)' }}>
            <h3 style={{ color: 'var(--accent-green)', display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1rem' }}>
              <CheckCircle /> Mastered ({mastered.length})
            </h3>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem' }}>
              {masteryStatus && mastered.length > 0 ? mastered.map(t => (
                <span key={t} style={{ background: 'rgba(34, 197, 94, 0.2)', padding: '5px 10px', borderRadius: '4px', fontSize: '0.9rem' }}>{t}</span>
              )) : <span className="text-muted">None</span>}
            </div>
          </div>

          <div style={{ background: 'rgba(234, 179, 8, 0.1)', padding: '1.5rem', borderRadius: '12px', borderLeft: '4px solid var(--accent-blue)' }}>
            <h3 style={{ color: 'var(--accent-blue)', display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1rem' }}>
              <ArrowRight /> Partially Mastered ({partial.length})
            </h3>
            <div className="text-muted" style={{ fontSize: '0.9rem', marginBottom: '1rem' }}>Passed foundational test but struggled with advance concepts.</div>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem' }}>
              {masteryStatus && partial.length > 0 ? partial.map(t => (
                <span key={t} style={{ background: 'rgba(59, 130, 246, 0.2)', padding: '5px 10px', borderRadius: '4px', fontSize: '0.9rem' }}>{t}</span>
              )) : <span className="text-muted">None</span>}
            </div>
          </div>

          <div style={{ background: 'rgba(239, 68, 68, 0.1)', padding: '1.5rem', borderRadius: '12px', borderLeft: '4px solid var(--accent-pink)' }}>
            <h3 style={{ color: 'var(--accent-pink)', display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1rem' }}>
              <XCircle /> Not Mastered At All ({none.length})
            </h3>
            <div className="text-muted" style={{ fontSize: '0.9rem', marginBottom: '1rem' }}>Needs urgent review of fundamentals.</div>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem' }}>
              {masteryStatus && none.length > 0 ? none.map(t => (
                <span key={t} style={{ background: 'rgba(239, 68, 68, 0.2)', padding: '5px 10px', borderRadius: '4px', fontSize: '0.9rem' }}>{t}</span>
              )) : <span className="text-muted">None</span>}
            </div>
          </div>
          
        </div>

        <div style={{ textAlign: 'center', marginTop: '3rem' }}>
          <button className="btn btn-primary" onClick={onFinish} style={{ fontSize: '1.2rem', padding: '1rem 3rem' }}>
            Back to Home
          </button>
        </div>
      </div>
    );
  }

  return null;
};

export default AbilityTest;
