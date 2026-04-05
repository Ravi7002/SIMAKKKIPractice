import React, { useState } from 'react';
import './index.css';
import Intro, { HayyuGate } from './components/Intro';
import TryoutQuiz from './components/TryoutQuiz';
import Results from './components/Results';
import AbilityTest from './components/AbilityTest';
import PracticeTest from './components/PracticeTest';
import Comparator from './components/Comparator';
import { BrainCircuit, Sparkles, Lock } from 'lucide-react';

// Preload the JSONs
import realQ1 from './realQ1.json';
import realQ2 from './realQ2.json';

const practiceModules = import.meta.glob('./PracticeQuestions/**/*.json', { eager: true });
export const allTopicsData = Object.values(practiceModules).map(mod => mod.default || mod);

const tryoutModules = import.meta.glob('./GeneratedTryouts/**/*.json', { eager: true });
export const generatedTryoutsData = Object.entries(tryoutModules)
  .sort(([keyA], [keyB]) => {
    const numA = parseInt((keyA.match(/tryout_(\d+)/) || [])[1] || '0', 10);
    const numB = parseInt((keyB.match(/tryout_(\d+)/) || [])[1] || '0', 10);
    return numA - numB;
  })
  .map(([, mod]) => mod.default || mod);

/* ── Landing: Ask if Hayyu ── */
const Landing = ({ onGuest, onIsHayyu }) => (
  <div className="glass-card fade-in" style={{ maxWidth: '500px', margin: '0 auto', textAlign: 'center' }}>
    <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '1.5rem' }}>
      <div style={{ position: 'relative' }}>
        <BrainCircuit size={72} color="var(--accent-purple)" />
        <Sparkles size={28} color="var(--accent-pink)" style={{ position: 'absolute', top: '-8px', right: '-8px', animation: 'pulse 2s infinite' }} />
      </div>
    </div>
    <h1 className="text-gradient mb-4" style={{ fontSize: '2rem' }}>SIMAK KKI UI Practice</h1>
    <p className="text-muted mb-8" style={{ fontSize: '1rem', lineHeight: 1.7 }}>
      Welcome! Are you Hayyu?
    </p>
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      <button onClick={onIsHayyu} className="btn btn-primary" style={{ fontSize: '1.1rem', padding: '1rem' }}>
        💖 Yes, I am Hayyu
      </button>
      <button onClick={onGuest} className="btn" style={{ fontSize: '1.1rem', padding: '1rem', background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(255,255,255,0.12)' }}>
        👤 No, I'm a guest
      </button>
    </div>
  </div>
);

function App() {
  // 'landing' | 'hayyu-gate' | 'app'
  const [authPhase, setAuthPhase] = useState('landing');
  const [isHayyu, setIsHayyu] = useState(false);

  const [phase, setPhase] = useState('intro');
  const [answers, setAnswers] = useState({});
  const [activeDataset, setActiveDataset] = useState(null);
  const [activeTryoutIndex, setActiveTryoutIndex] = useState(null);

  const startPracticeTryout = (idx) => { setActiveTryoutIndex(idx); setPhase('practice-tryout'); };
  const startPractice = () => { setActiveTryoutIndex(null); setPhase('practice'); };
  const startAbility = () => setPhase('ability');
  const startTryout = (tryoutId) => {
    setAnswers({});
    setActiveDataset(tryoutId === 1 ? realQ1 : realQ2);
    setPhase('tryout');
  };
  const startCompare = () => setPhase('compare');
  const finishTest = () => setPhase('results');
  const restartQuiz = () => { setPhase('intro'); setAnswers({}); setActiveDataset(null); setActiveTryoutIndex(null); };

  // ── Auth Flow ──
  if (authPhase === 'landing') {
    return (
      <>
        <div style={{ position: 'absolute', top: 0, left: 0, right: 0, height: '100%', pointerEvents: 'none', background: 'radial-gradient(circle at 50% -20%, rgba(139, 92, 246, 0.15), transparent 60%)', zIndex: -1 }} />
        <Landing
          onGuest={() => { setIsHayyu(false); setAuthPhase('app'); }}
          onIsHayyu={() => setAuthPhase('hayyu-gate')}
        />
      </>
    );
  }

  if (authPhase === 'hayyu-gate') {
    return (
      <>
        <div style={{ position: 'absolute', top: 0, left: 0, right: 0, height: '100%', pointerEvents: 'none', background: 'radial-gradient(circle at 50% -20%, rgba(139, 92, 246, 0.15), transparent 60%)', zIndex: -1 }} />
        <HayyuGate
          onEnter={() => { setIsHayyu(true); setAuthPhase('app'); }}
          onBack={() => setAuthPhase('landing')}
        />
      </>
    );
  }

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
          isHayyu={isHayyu}
        />
      )}

      {(phase === 'practice' || phase === 'practice-tryout') && (
        <PracticeTest
          allTopicsData={allTopicsData}
          generatedTryouts={generatedTryoutsData}
          initialTryoutIndex={phase === 'practice-tryout' ? activeTryoutIndex : null}
          onBack={() => setPhase('intro')}
          isHayyu={isHayyu}
        />
      )}

      {phase === 'ability' && (
        <AbilityTest allTopicsData={allTopicsData} onFinish={() => setPhase('intro')} />
      )}

      {phase === 'tryout' && (
        <TryoutQuiz questions={activeDataset} answers={answers} setAnswers={setAnswers} onFinish={finishTest} />
      )}

      {phase === 'results' && (
        <Results questions={activeDataset} answers={answers} onRestart={restartQuiz} />
      )}

      {phase === 'compare' && (
        <Comparator allTopicsData={allTopicsData} realQ1={realQ1} generatedTryouts={generatedTryoutsData} onBack={() => setPhase('intro')} />
      )}
    </>
  );
}

export default App;
