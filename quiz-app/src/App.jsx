import React, { useState } from 'react';
import './index.css';
import Intro from './components/Intro';
import TryoutQuiz from './components/TryoutQuiz';
import Results from './components/Results';
import AbilityTest from './components/AbilityTest';
import PracticeTest from './components/PracticeTest';
import Comparator from './components/Comparator';

// Preload the JSONs
import realQ1 from './realQ1.json';
import realQ2 from './realQ2.json';

const practiceModules = import.meta.glob('./PracticeQuestions/**/*.json', { eager: true });
export const allTopicsData = Object.values(practiceModules).map(mod => mod.default || mod);

const tryoutModules = import.meta.glob('./GeneratedTryouts/**/*.json', { eager: true });
export const generatedTryoutsData = Object.values(tryoutModules).map(mod => mod.default || mod);

function App() {
  const [phase, setPhase] = useState('intro'); // 'intro', 'practice', 'ability', 'tryout', 'practice-tryout', 'results'
  const [answers, setAnswers] = useState({});
  const [activeDataset, setActiveDataset] = useState(null);
  const [activeTryoutIndex, setActiveTryoutIndex] = useState(null);

  const startPracticeTryout = (idx) => {
    setActiveTryoutIndex(idx);
    setPhase('practice-tryout');
  };

  const startPractice = () => {
    setActiveTryoutIndex(null);
    setPhase('practice');
  };

  const startAbility = () => {
    setPhase('ability');
  };

  const startTryout = (tryoutId) => {
    setAnswers({});
    setActiveDataset(tryoutId === 1 ? realQ1 : realQ2);
    setPhase('tryout');
  };

  const startCompare = () => {
    setPhase('compare');
  };

  const finishTest = () => {
    setPhase('results');
  };

  const restartQuiz = () => {
    setPhase('intro');
    setAnswers({});
    setActiveDataset(null);
    setActiveTryoutIndex(null);
  };

  return (
    <>
      <div style={{ position: 'absolute', top: 0, left: 0, right: 0, height: '100%', pointerEvents: 'none', background: 'radial-gradient(circle at 50% -20%, rgba(139, 92, 246, 0.15), transparent 60%)', zIndex: -1 }} />
      
      {phase === 'intro' && (
        <Intro
          onStartPractice={startPractice}
          onStartAbility={startAbility}
          onStartTryout={startTryout}
          onStartCompare={startCompare}
          onStartPracticeTryout={startPracticeTryout}
        />
      )}
      
      {(phase === 'practice' || phase === 'practice-tryout') && (
        <PracticeTest
          allTopicsData={allTopicsData}
          generatedTryouts={generatedTryoutsData}
          initialTryoutIndex={phase === 'practice-tryout' ? activeTryoutIndex : null}
          onBack={() => setPhase('intro')}
        />
      )}

      {phase === 'ability' && (
        <AbilityTest 
          allTopicsData={allTopicsData} 
          onFinish={() => setPhase('intro')} 
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

      {phase === 'compare' && (
        <Comparator 
          allTopicsData={allTopicsData} 
          realQ1={realQ1} 
          generatedTryouts={generatedTryoutsData}
          onBack={() => setPhase('intro')} 
        />
      )}
    </>
  );
}

export default App;
