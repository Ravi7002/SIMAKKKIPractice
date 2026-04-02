import React, { useState, useEffect } from 'react';
import './index.css';
import Intro from './components/Intro';
import Quiz from './components/Quiz';
import TryoutQuiz from './components/TryoutQuiz';
import Results from './components/Results';

// Preload the JSONs
import practiceQ from './practiceQ.json';
import realQ1 from './realQ1.json';
import realQ2 from './realQ2.json';

function App() {
  const [phase, setPhase] = useState('intro'); // 'intro', 'practice', 'tryout', 'results'
  const [answers, setAnswers] = useState({});
  const [activeDataset, setActiveDataset] = useState(null);

  const startPractice = () => {
    setAnswers({});
    setActiveDataset(practiceQ);
    setPhase('practice');
  };

  const startTryout = (tryoutId) => {
    setAnswers({});
    if (tryoutId === 1) setActiveDataset(realQ1);
    else setActiveDataset(realQ2);
    setPhase('tryout');
  };

  const finishTest = () => {
    setPhase('results');
  };

  const restartQuiz = () => {
    setPhase('intro');
    setAnswers({});
    setActiveDataset(null);
  };

  return (
    <>
      <div style={{ position: 'absolute', top: 0, left: 0, right: 0, height: '100%', pointerEvents: 'none', background: 'radial-gradient(circle at 50% -20%, rgba(139, 92, 246, 0.15), transparent 60%)', zIndex: -1 }} />
      
      {phase === 'intro' && (
        <Intro 
          onStartPractice={startPractice} 
          onStartTryout={startTryout} 
        />
      )}
      
      {phase === 'practice' && (
        <Quiz 
          questions={activeDataset} 
          answers={answers} 
          setAnswers={setAnswers} 
          onFinish={finishTest} 
        />
      )}
      
      {phase === 'tryout' && (
        <TryoutQuiz 
          questions={activeDataset} 
          answers={answers} 
          setAnswers={setAnswers} 
          onFinish={finishTest} 
        />
      )}
      
      {phase === 'results' && (
        <Results 
          questions={activeDataset} 
          answers={answers} 
          onRestart={restartQuiz} 
        />
      )}
    </>
  );
}

export default App;
