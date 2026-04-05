import React, { useState, useMemo } from 'react';
import { ArrowLeft, Book, Grid, ChevronRight, ChevronDown, Lightbulb, CheckCircle, XCircle, FlaskConical, Sparkles } from 'lucide-react';
import MathText from './MathText';

import ChartDisplay from './ChartDisplay';
import QuestionChart from './QuestionChart';

/* ─── Topic Quiz ─── */
const TopicQuiz = ({ questions, startIndex = 0, onFinish, onBackToBank }) => {
  const [currentIndex, setCurrentIndex] = useState(startIndex);
  const [guessedOptions, setGuessedOptions] = useState([]);
  const [showExplanation, setShowExplanation] = useState(false);
  const [hintsRevealed, setHintsRevealed] = useState(0);

  const question = questions[currentIndex];
  const isLast = currentIndex === questions.length - 1;

  const groupedQuestions = useMemo(() => {
    const groups = {};
    questions.forEach((q, idx) => {
      const subject = q.subject || 'Practice';
      if (!groups[subject]) groups[subject] = [];
      groups[subject].push({ q, idx });
    });
    return groups;
  }, [questions]);

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
    <div className="fade-in" style={{ display: 'flex', gap: '2rem', maxWidth: '1200px', margin: '0 auto', alignItems: 'flex-start' }}>
      
      {/* MAIN CONTENT AREA */}
      <div style={{ flex: 1, minWidth: 0 }}>
      {/* Progress & Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
        <button onClick={onBackToBank} className="btn" style={{ padding: '0.4rem 0.8rem', background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(255,255,255,0.1)', fontSize: '0.9rem' }}>
          <ArrowLeft size={16} /> Back to Bank
        </button>
        <div style={{ flex: 1, textAlign: 'center' }}>
          <span className="text-muted">Question </span>
          <strong>{currentIndex + 1}</strong>
          <span className="text-muted"> / {questions.length}</span>
        </div>
        <div className="badge badge-gray" style={{ textTransform: 'capitalize' }}>{question.difficulty}</div>
      </div>

      <div className="progress-container" style={{ marginBottom: '1.5rem' }}>
        <div className="progress-fill" style={{ width: `${(currentIndex / questions.length) * 100}%` }} />
      </div>

      {/* Passage Panel — only shown for reading-comp questions, sticks while passage_id is same */}
      {question.passage && (
        <div className="glass-card mb-4 fade-in" style={{
          background: 'rgba(139,92,246,0.04)',
          borderLeft: '4px solid var(--accent-purple)',
          borderRadius: '12px'
        }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.8rem' }}>
            <h4 style={{ color: 'var(--accent-purple)', margin: 0, fontSize: '0.85rem', textTransform: 'uppercase', letterSpacing: '0.07em' }}>
              📖 Reading Passage{question.passage_title ? ` — ${question.passage_title}` : ''}
            </h4>
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
              {questions.filter(q => q.passage_id && q.passage_id === question.passage_id).length} questions share this passage
            </span>
          </div>
          <div style={{ maxHeight: '240px', overflowY: 'auto', paddingRight: '10px', fontSize: '1rem', lineHeight: '1.75', color: 'var(--text-muted)', whiteSpace: 'pre-wrap' }}>
            <MathText text={question.passage} />
          </div>
        </div>
      )}

      {/* Question card */}
      <div className="glass-card mb-4">
        {(question.chart_data || question.chart) && (question.chart_data ? <ChartDisplay chartData={question.chart_data} /> : <QuestionChart chart={question.chart} />)}
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
            <CheckCircle size={18} /> Correct! Step-by-Step Explanation:
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
      </div> {/* END MAIN CONTENT AREA */}

      {/* SIDEBAR FOR QUESTION NAVIGATION */}
      <div className="glass-card" style={{ width: '320px', flexShrink: 0, padding: '1.2rem' }}>
        <h3 style={{ marginBottom: '1.5rem', color: 'var(--text-muted)' }}>Navigator</h3>
        {Object.entries(groupedQuestions).map(([subject, list]) => (
          <div key={subject} style={{ marginBottom: '1.5rem' }}>
            <h4 style={{ fontSize: '0.8rem', color: 'var(--accent-blue)', marginBottom: '0.8rem', textTransform: 'uppercase', letterSpacing: '0.05em' }}>{subject}</h4>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: '8px' }}>
              {list.map((item, li) => {
                 const isActive = item.idx === currentIndex;
                 const sharesPassage = item.q.passage_id && item.q.passage_id === question.passage_id;
                 const isFirstInPassage = sharesPassage && (li === 0 || list[li-1].q.passage_id !== item.q.passage_id);
                 return (
                   <button 
                     key={item.idx} 
                     onClick={() => {
                        setCurrentIndex(item.idx);
                        setGuessedOptions([]);
                        setShowExplanation(false);
                        setHintsRevealed(0);
                     }}
                     title={item.q.passage_title ? `Passage: ${item.q.passage_title}` : undefined}
                     style={{
                        padding: '0.5rem 0',
                        textAlign: 'center',
                        fontSize: '0.9rem',
                        fontWeight: 'bold',
                        borderRadius: '6px',
                        background: isActive ? 'var(--accent-purple)' : sharesPassage ? 'rgba(139,92,246,0.12)' : 'rgba(255,255,255,0.05)',
                        border: `1px solid ${isActive ? 'var(--accent-purple)' : sharesPassage ? 'rgba(139,92,246,0.4)' : 'rgba(255,255,255,0.1)'}`,
                        color: isActive ? 'white' : 'var(--text-muted)',
                        cursor: 'pointer',
                        transition: 'all 0.2s',
                        position: 'relative'
                     }}
                   >
                     {item.q.passage_id && <span style={{ position:'absolute', top:'-4px', right:'-2px', fontSize:'8px' }}>📖</span>}
                     {item.idx + 1}
                   </button>
                 );
              })}
            </div>
          </div>
        ))}
      </div>

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
                <span style={{ fontWeight: '600' }}><MathText text={f.formula.includes('$') ? f.formula : `$\\displaystyle ${f.formula}$`} /></span>
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

      {/* Question Bank Grid */}
      <div className="glass-card mb-6" style={{ background: 'rgba(59,130,246,0.03)', border: '1px solid rgba(59,130,246,0.15)' }}>
        <h3 style={{ color: '#60a5fa', marginBottom: '1.2rem', textAlign: 'center' }}>🗃️ Question Bank ({topicData.questions?.length || 0})</h3>
        <p className="text-muted mb-4" style={{ textAlign: 'center', fontSize: '0.95rem' }}>Select any question to practice at your own pace. Options are fully shuffled.</p>
        
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(60px, 1fr))', gap: '8px' }}>
          {topicData.questions?.map((q, i) => {
             const color = q.difficulty === 'easy' ? 'var(--accent-green)' : q.difficulty === 'medium' ? '#f59e0b' : 'var(--accent-red)';
             return (
               <button
                 key={q.id || i}
                 onClick={() => onStartQuiz(i)}
                 className="btn glass-card"
                 style={{ 
                   padding: '0.8rem 0', fontWeight: 'bold', fontSize: '1.1rem', 
                   border: `1px solid ${color}40`, background: `color-mix(in srgb, ${color} 10%, transparent)`,
                   transition: 'all 0.2s', display: 'flex', flexDirection: 'column', alignItems: 'center'
                 }}
               >
                 <span>{i + 1}</span>
                 <span style={{ fontSize: '0.65rem', fontWeight: 'normal', color: color, opacity: 0.8, textTransform: 'uppercase', marginTop: '2px' }}>{q.difficulty}</span>
               </button>
             );
          })}
        </div>
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
const PracticeTest = ({ allTopicsData, generatedTryouts = [], initialTryoutIndex = null, onBack }) => {
  const [view, setView] = useState('subjects'); // 'subjects', 'topics', 'learn', 'quiz', 'done'
  const [selectedSubject, setSelectedSubject] = useState(null);
  const [selectedTopic, setSelectedTopic] = useState(null);
  const [quizQuestions, setQuizQuestions] = useState([]);

  // If a specific tryout was selected from the menu, launch it immediately
  React.useEffect(() => {
    if (initialTryoutIndex !== null && generatedTryouts.length > 0) {
      const tryout = generatedTryouts[initialTryoutIndex] || generatedTryouts[0];
      // Sort by subject order
      const subjectOrder = ['Basic Mathematics', 'English', 'Quantitative Reasoning', 'Logical Reasoning'];
      const sorted = [...tryout].sort((a, b) => {
        const ai = subjectOrder.indexOf(a.subject);
        const bi = subjectOrder.indexOf(b.subject);
        return (ai === -1 ? 99 : ai) - (bi === -1 ? 99 : bi);
      });
      setQuizQuestions(sorted);
      setView('quiz');
    }
  }, [initialTryoutIndex, generatedTryouts]);

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

  const [quizStartIndex, setQuizStartIndex] = useState(0);

  const startQuiz = (startIndex = 0) => {
    setQuizStartIndex(startIndex);
    setQuizQuestions(selectedTopic.questions || []);
    setView('quiz');
  };

  const startFullMock = () => {
    // Generate an 80-question test from generated clones, maintaining 20 per section.
    const allGen = generatedTryouts.flat();
    const subjectsList = ['Basic Mathematics', 'English', 'Quantitative Reasoning', 'Logical Reasoning'];
    const mockQuestions = [];
    
    subjectsList.forEach(sub => {
       const qs = allGen.filter(q => q.subject === sub).sort(() => Math.random() - 0.5);
       if (qs.length >= 20) {
         mockQuestions.push(...qs.slice(0, 20));
       } else {
         mockQuestions.push(...qs);
       }
    });
    
    setQuizStartIndex(0);
    setQuizQuestions(mockQuestions);
    setView('quiz');
  };

  const goBack = () => {
    if (view === 'subjects') onBack();
    else if (view === 'topics') { setSelectedSubject(null); setView('subjects'); }
    else if (view === 'learn') setView('topics');
    else if (view === 'quiz') {
      // If launched from tryout selector directly, go back to intro
      if (initialTryoutIndex !== null) onBack();
      else setView(selectedTopic ? 'learn' : 'subjects');
    }
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
              <Book size={36} style={{ verticalAlign: 'middle', marginRight: '12px' }} /> Hayyu's Practice Bank
            </h2>
            <p className="text-muted">Master topics at your own pace, Hayyu!</p>
          </div>


          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '1.2rem' }}>
            {subjects.map(sub => {
              const color = subjectColors[sub] || 'var(--accent-blue)';
              return (
              <button
                key={sub}
                className="glass-card btn subject-card"
                onClick={() => handleSubjectClick(sub)}
                style={{ 
                  '--subject-color': color, 
                  padding: '2.5rem 2rem', 
                  display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '1rem',
                  borderColor: `color-mix(in srgb, ${color} 30%, transparent)` 
                }}
              >
                <div style={{ background: `color-mix(in srgb, ${color} 15%, transparent)`, padding: '1rem', borderRadius: '50%', boxShadow: `0 0 20px color-mix(in srgb, ${color} 20%, transparent)` }}>
                  <span style={{ fontSize: '2.5rem', display: 'block' }}>{subjectIcons[sub] || '📚'}</span>
                </div>
                <span style={{ fontSize: '1.2rem', fontWeight: '700', color: color, letterSpacing: '0.02em' }}>{sub}</span>
                <span className="text-muted" style={{ fontSize: '0.9rem', background: 'rgba(0,0,0,0.2)', padding: '0.3rem 0.8rem', borderRadius: '20px' }}>
                  {allTopicsData.filter(t => t.subject === sub).length} topics
                </span>
              </button>
            )})}
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
                className="glass-card topic-card"
                onClick={() => handleTopicClick(t)}
                style={{ 
                   padding: '1.5rem', textAlign: 'left', cursor: 'pointer', 
                   border: `1px solid rgba(255,255,255,0.06)`, 
                   transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)', 
                   display: 'flex', flexDirection: 'column', gap: '0.8rem' 
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
                   <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: subjectColors[selectedSubject] || 'white' }} />
                   <span style={{ fontSize: '1.1rem', fontWeight: '700', color: 'var(--text-main)' }}>{t.topic}</span>
                </div>
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

      {view === 'quiz' && quizQuestions.length > 0 && (
        <TopicQuiz
          questions={quizQuestions}
          startIndex={quizStartIndex}
          onFinish={() => setView('done')}
          onBackToBank={initialTryoutIndex !== null ? onBack : () => setView(selectedTopic ? 'learn' : 'subjects')}
        />
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
