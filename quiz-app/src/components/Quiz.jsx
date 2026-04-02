import React, { useState } from 'react';
import { cleanText } from '../utils';
import { ChevronRight, SkipForward, ArrowLeft } from 'lucide-react';

const Quiz = ({ questions, answers, setAnswers, onFinish }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  
  const question = questions[currentIndex];
  const progress = ((currentIndex) / questions.length) * 100;

  const handleOptionSelect = (letter) => {
    setAnswers(prev => ({ ...prev, [question.id]: letter }));
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

  const selectedOption = answers[question.id] || null;

  return (
    <div className="fade-in w-full mx-auto" style={{ maxWidth: '800px' }}>
      <div className="flex-between mb-4">
        <div>
          <span className="text-muted">Question {currentIndex + 1}</span>
          <span className="text-muted" style={{ opacity: 0.5 }}> / {questions.length}</span>
        </div>
        <div className="badge badge-gray">
          {question.subject} • {question.topic}
        </div>
      </div>

      <div className="progress-container">
        <div className="progress-fill" style={{ width: `${progress}%` }}></div>
      </div>

      <div className="glass-card mb-8">
        <h2 className="mb-8" style={{ fontSize: '1.5rem', lineHeight: '1.6' }}>
          {cleanText(question.question_text)}
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
                {cleanText(opt.text)}
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
            <button onClick={handleNext} className="btn" style={{ background: 'rgba(255,255,255,0.05)' }}>
              Skip <SkipForward size={18} />
            </button>
          )}
          <button onClick={handleNext} className="btn btn-primary" style={{ minWidth: '140px' }}>
            {currentIndex === questions.length - 1 ? 'Finish Exam' : 'Continue'} <ChevronRight size={18} />
          </button>
        </div>
      </div>
    </div>
  );
};

export default Quiz;
