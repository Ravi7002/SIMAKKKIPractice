import React, { useState, useEffect } from 'react';
import MathText from './MathText';
import { ChevronRight, ArrowLeft, CheckCircle, XCircle } from 'lucide-react';

const Quiz = ({ questions, answers, setAnswers, onFinish, onQuit }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [guessedOptions, setGuessedOptions] = useState([]);
  const [showExplanation, setShowExplanation] = useState(false);
  
  const question = questions[currentIndex];
  const progress = ((currentIndex) / questions.length) * 100;

  // Reset local state when moving to a new question
  useEffect(() => {
    setGuessedOptions([]);
    // If we've already answered this in the global state, pre-fill it and show explanation
    if (answers[question.id]) {
      setGuessedOptions([answers[question.id]]);
      setShowExplanation(true);
    } else {
      setShowExplanation(false);
    }
  }, [currentIndex, question.id, answers]);

  const handleOptionSelect = (letter) => {
    if (showExplanation) return; // already got it correct
    
    if (!guessedOptions.includes(letter)) {
      const newGuesses = [...guessedOptions, letter];
      setGuessedOptions(newGuesses);
      
      if (letter === question.correct_answer) {
        setShowExplanation(true);
        // Set the answer in parent context once they find the correct one
        setAnswers(prev => ({ ...prev, [question.id]: letter }));
      }
    }
  };

  const handleNext = () => {
    if (currentIndex < questions.length - 1) {
      setCurrentIndex(prev => prev + 1);
    } else {
      onFinish();
    }
  };

  const handlePrev = () => {
    if (currentIndex > 0) {
      setCurrentIndex(prev => prev - 1);
    }
  };

  return (
    <div className="fade-in w-full mx-auto" style={{ maxWidth: '800px' }}>
      <div className="flex-between mb-4">
        <div>
          <span className="text-muted">Question {currentIndex + 1}</span>
          <span className="text-muted" style={{ opacity: 0.5 }}> / {questions.length}</span>
        </div>
        <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
          <div className="badge badge-gray">
            {question.subject} • {question.topic}
          </div>
          {onQuit && (
            <button onClick={onQuit} style={{ padding: '0.4rem 0.8rem', background: 'rgba(239, 68, 68, 0.1)', color: 'var(--accent-red)', border: 'none', borderRadius: '8px', cursor: 'pointer', fontWeight: '500' }}>
              Quit
            </button>
          )}
        </div>
      </div>

      <div className="progress-container">
        <div className="progress-fill" style={{ width: `${progress}%` }}></div>
      </div>

      <div className="glass-card mb-4">
        <h2 className="mb-8" style={{ fontSize: '1.5rem', lineHeight: '1.6' }}>
          <MathText text={question.question_text} />
        </h2>

        <div className="options-container">
          {question.options.map((opt) => {
            const isGuessed = guessedOptions.includes(opt.letter);
            const isCorrectAnswer = opt.letter === question.correct_answer;
            
            let btnClass = 'option-btn';
            if (isGuessed) {
              if (isCorrectAnswer) btnClass += ' correct';
              else btnClass += ' incorrect';
            }

            return (
              <button
                key={opt.letter}
                className={btnClass}
                onClick={() => handleOptionSelect(opt.letter)}
                disabled={isGuessed && !isCorrectAnswer}
              >
                <div className="option-letter">{opt.letter}</div>
                <div style={{ flex: 1, lineHeight: '1.5' }}>
                  <MathText text={opt.text} />
                </div>
                {isGuessed && isCorrectAnswer && <CheckCircle size={24} style={{ color: 'var(--accent-green)' }} />}
                {isGuessed && !isCorrectAnswer && <XCircle size={24} style={{ color: 'var(--accent-red)' }} />}
              </button>
            );
          })}
        </div>
      </div>

      {showExplanation && (
        <div className="glass-card fade-in mb-4" style={{ background: 'rgba(16, 185, 129, 0.1)', border: '1px solid rgba(16, 185, 129, 0.2)', padding: '1.5rem' }}>
          <h3 style={{ color: 'var(--accent-green)', marginBottom: '0.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <CheckCircle size={20} /> Correct!
          </h3>
          <p style={{ lineHeight: '1.5' }}>
            <MathText text={question.explanation || `The correct answer is ${question.correct_answer}.`} />
          </p>
        </div>
      )}

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
          {showExplanation && (
            <button onClick={handleNext} className="btn btn-primary fade-in" style={{ minWidth: '140px' }}>
              {currentIndex === questions.length - 1 ? 'Finish Exam' : 'Continue'} <ChevronRight size={18} />
            </button>
          )}
        </div>
      </div>
    </div>
  );
};

export default Quiz;
