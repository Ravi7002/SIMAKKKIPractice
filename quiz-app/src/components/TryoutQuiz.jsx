import React, { useState, useEffect, useMemo } from 'react';
import MathText from './MathText';
import QuestionChart from './QuestionChart';
import { ChevronRight, SkipForward, ArrowLeft, Clock, AlertTriangle } from 'lucide-react';

const SECTIONS = [
  { name: 'Basic Mathematics', timeSeconds: 55 * 60 },
  { name: 'English', timeSeconds: 30 * 60 },
  { name: 'Quantitative Reasoning', timeSeconds: 30 * 60 },
  { name: 'Logical Reasoning', timeSeconds: 35 * 60 }
];

const TryoutQuiz = ({ questions, answers, setAnswers, onFinish }) => {
  const [sectionIndex, setSectionIndex] = useState(0);
  const [currentIndex, setCurrentIndex] = useState(0);
  
  // Initialize timer
  const [timeLeft, setTimeLeft] = useState(SECTIONS[0].timeSeconds);
  const [timerActive, setTimerActive] = useState(true);
  
  const currentSectionInfo = SECTIONS[sectionIndex];
  
  // Filter questions for current section
  const sectionQuestions = useMemo(() => {
    return questions.filter(q => q.subject === currentSectionInfo.name);
  }, [questions, sectionIndex]);
  
  const question = sectionQuestions[currentIndex] || sectionQuestions[0];
  
  useEffect(() => {
    if (!timerActive) return;
    
    const interval = setInterval(() => {
      setTimeLeft(prev => {
        if (prev <= 1) {
          clearInterval(interval);
          handleNextSection();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
    
    return () => clearInterval(interval);
  }, [sectionIndex, timerActive]);

  const handleOptionSelect = (letter) => {
    if (question) {
      setAnswers(prev => ({ ...prev, [question.id]: letter }));
    }
  };

  const handleNextSection = () => {
    if (sectionIndex < SECTIONS.length - 1) {
      setSectionIndex(prev => prev + 1);
      setCurrentIndex(0);
      setTimeLeft(SECTIONS[sectionIndex + 1].timeSeconds);
    } else {
      onFinish();
    }
  };

  const attemptNextSection = () => {
    if (window.confirm("Are you sure you want to finish this section early? You cannot return to it later.")) {
      handleNextSection();
    }
  };

  const handleNext = () => {
    if (currentIndex < sectionQuestions.length - 1) {
      setCurrentIndex(prev => prev + 1);
    }
  };

  const handlePrev = () => {
    if (currentIndex > 0) {
      setCurrentIndex(prev => prev - 1);
    }
  };

  // Format time
  const formatTime = (seconds) => {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  if (!question) {
    return (
      <div className="fade-in w-full mx-auto text-center" style={{ maxWidth: '800px' }}>
        <h2 className="mb-4">No questions found for {currentSectionInfo.name}</h2>
        <button className="btn btn-primary" onClick={handleNextSection}>Skip Section</button>
      </div>
    );
  }

  const selectedOption = answers[question.id] || null;
  const isLastQuestion = currentIndex === sectionQuestions.length - 1;
  const isTimeCritical = timeLeft < 300; // less than 5 minutes

  return (
    <div className="fade-in w-full mx-auto" style={{ maxWidth: '800px' }}>
      
      {/* Timer Header */}
      <div className="flex-between mb-4 glass-card p-4" style={{ borderRadius: '16px', padding: '1rem 1.5rem', border: isTimeCritical ? '1px solid rgba(239, 68, 68, 0.4)' : '' }}>
        <div>
          <h3 style={{ margin: 0, fontSize: '1.2rem' }}>{currentSectionInfo.name}</h3>
          <p className="text-muted" style={{ margin: 0, fontSize: '0.9rem' }}>Section {sectionIndex + 1} of {SECTIONS.length}</p>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.8rem' }}>
          <div className="flex-column text-right">
            <span className="text-muted" style={{ fontSize: '0.8rem' }}>Time Remaining</span>
            <span style={{ fontSize: '1.5rem', fontWeight: 600, color: isTimeCritical ? 'var(--accent-red)' : 'var(--accent-green)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <Clock size={20} /> {formatTime(timeLeft)}
            </span>
          </div>
          <button onClick={attemptNextSection} className="btn btn-outline" style={{ padding: '0.5rem 1rem', fontSize: '0.9rem', borderColor: 'var(--accent-red)', color: 'white' }}>
            Submit Section
          </button>
        </div>
      </div>

      <div className="flex-between mb-4 mt-8">
        <div>
          <span className="text-muted">Question {currentIndex + 1}</span>
          <span className="text-muted" style={{ opacity: 0.5 }}> / {sectionQuestions.length}</span>
        </div>
        {question.topic !== currentSectionInfo.name && (
           <div className="badge badge-gray">
             {question.topic}
           </div>
        )}
      </div>

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
              {sectionQuestions.filter(q => q.passage_id && q.passage_id === question.passage_id).length} questions share this passage
            </span>
          </div>
          <div style={{ maxHeight: '220px', overflowY: 'auto', paddingRight: '10px', fontSize: '1rem', lineHeight: '1.75', color: 'var(--text-muted)', whiteSpace: 'pre-wrap' }}>
            <MathText text={question.passage} />
          </div>
        </div>
      )}

      <div className="glass-card mb-8">
        {question.chart && <QuestionChart chart={question.chart} />}
        <h2 className="mb-8" style={{ fontSize: '1.5rem', lineHeight: '1.6', whiteSpace: 'pre-wrap' }}>
          <MathText text={question.question_text} />
        </h2>

        <div className="options-container">
          {question.options.map((opt) => (
            <button
              key={opt.letter}
              className={`option-btn ${selectedOption === opt.letter ? 'selected' : ''}`}
              onClick={() => handleOptionSelect(opt.letter)}
            >
              <div className="option-letter">{opt.letter}</div>
              <div style={{ flex: 1, lineHeight: '1.5' }}>
                <MathText text={opt.text} />
              </div>
            </button>
          ))}
        </div>
      </div>

      <div className="flex-between">
        <button 
          onClick={handlePrev} 
          className="btn btn-outline" 
          disabled={currentIndex === 0}
          style={{ opacity: currentIndex === 0 ? 0 : 1, visibility: currentIndex === 0 ? 'hidden' : 'visible' }}
        >
          <ArrowLeft size={18} /> Previous
        </button>
        
        <div style={{ display: 'flex', gap: '1rem' }}>
          {!selectedOption && (
            <button onClick={handleNext} className="btn" disabled={isLastQuestion} style={{ background: 'rgba(255,255,255,0.05)', opacity: isLastQuestion ? 0.5 : 1 }}>
              Skip <SkipForward size={18} />
            </button>
          )}
          <button onClick={handleNext} className="btn btn-primary" disabled={isLastQuestion} style={{ minWidth: '140px', opacity: isLastQuestion ? 0.5 : 1 }}>
            Next <ChevronRight size={18} />
          </button>
        </div>
      </div>
    </div>
  );
};

export default TryoutQuiz;
