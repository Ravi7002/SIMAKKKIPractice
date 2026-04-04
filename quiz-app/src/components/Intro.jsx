import React, { useState } from 'react';
import { BookOpen, Sparkles, BrainCircuit, Activity, Clock, Award, ChevronRight, FlaskConical } from 'lucide-react';

const Intro = ({ onStartPractice, onStartAbility, onStartTryout, onStartCompare, onStartPracticeTryout }) => {
  const [menuState, setMenuState] = useState('home'); // 'home' | 'tryout' | 'practice-tryout'

  return (
    <div className="glass-card fade-in" style={{ maxWidth: '640px', margin: '0 auto', textAlign: 'center' }}>
      <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '2rem' }}>
        <div style={{ position: 'relative' }}>
          <BrainCircuit size={80} color="var(--accent-purple)" />
          <Sparkles
            size={32}
            color="var(--accent-pink)"
            style={{ position: 'absolute', top: '-10px', right: '-10px', animation: 'pulse 2s infinite' }}
          />
        </div>
      </div>

      <h1 className="text-gradient mb-4" style={{ fontSize: '3rem' }}>
        University Entrance Exam
      </h1>

      <p className="text-muted mb-8 text-lg">
        Master your skills with this comprehensive practice suite.
      </p>

      {/* ── Home Menu ── */}
      {menuState === 'home' && (
        <div className="flex-column fade-in" style={{ gap: '1rem' }}>
          <button onClick={onStartAbility} className="btn" style={{ fontSize: '1.2rem', padding: '1rem', background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(255,255,255,0.1)' }}>
            <Activity size={24} style={{ color: 'var(--accent-blue)' }} /> Ability Test
          </button>

          <button onClick={onStartPractice} className="btn" style={{ fontSize: '1.2rem', padding: '1rem', background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(255,255,255,0.1)' }}>
            <BookOpen size={24} style={{ color: 'var(--accent-green)' }} /> Practice by Topic
          </button>

          <button
            onClick={() => setMenuState('practice-tryout')}
            className="btn btn-primary"
            style={{ fontSize: '1.2rem', padding: '1rem', background: 'linear-gradient(135deg, #7c3aed, #db2777)', boxShadow: '0 0 24px rgba(139,92,246,0.4)' }}
          >
            <FlaskConical size={24} /> Practice Tryout (80Q, No Timer)
          </button>

          <button
            onClick={() => setMenuState('tryout')}
            className="btn btn-outline"
            style={{ fontSize: '1.2rem', padding: '1rem' }}
          >
            <Award size={24} /> Real Tryout (Timed)
          </button>

          <button onClick={onStartCompare} className="btn" style={{ fontSize: '1.1rem', padding: '1rem', background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(255,255,255,0.1)', marginTop: '0.5rem', color: 'var(--text-muted)' }}>
            <Activity size={20} /> Compare Questions (Real vs Practice)
          </button>
        </div>
      )}

      {/* ── Real Tryout Selector ── */}
      {menuState === 'tryout' && (
        <div className="fade-in">
          <h2 className="mb-2" style={{ fontSize: '1.5rem', color: 'var(--accent-purple)' }}>Select Real Tryout</h2>
          <p className="text-muted mb-6" style={{ fontSize: '0.9rem' }}>These use the original real exam question sets with a timer.</p>
          <div className="flex-column" style={{ gap: '1rem', marginBottom: '1.5rem' }}>
            <button onClick={() => onStartTryout(1)} className="btn btn-outline" style={{ fontSize: '1.2rem', padding: '1rem' }}>
              <Clock size={20} /> Tryout 1 (Real Q Set 1)
            </button>
            <button onClick={() => onStartTryout(2)} className="btn btn-outline" style={{ fontSize: '1.2rem', padding: '1rem' }}>
              <Clock size={20} /> Tryout 2 (Real Q Set 2)
            </button>
          </div>
          <button onClick={() => setMenuState('home')} className="btn" style={{ background: 'transparent', color: 'var(--text-muted)' }}>
            ← Back
          </button>
        </div>
      )}

      {/* ── Practice Tryout Selector ── */}
      {menuState === 'practice-tryout' && (
        <div className="fade-in">
          <h2 className="mb-2" style={{ fontSize: '1.5rem', color: 'var(--accent-pink)' }}>Select Practice Tryout</h2>
          <p className="text-muted mb-6" style={{ fontSize: '0.9rem' }}>80 questions, no timer. Includes hints & step-by-step explanations.</p>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '1rem', marginBottom: '1.5rem' }}>
            {[1, 2, 3, 4, 5].map(n => (
              <button
                key={n}
                onClick={() => onStartPracticeTryout(n - 1)}
                className="glass-card btn"
                style={{
                  padding: '1.8rem 1rem',
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  gap: '0.6rem',
                  border: '1px solid rgba(244,63,94,0.25)',
                  cursor: 'pointer',
                  transition: 'all 0.2s',
                }}
              >
                <span style={{ fontSize: '2rem' }}>📝</span>
                <span style={{ fontSize: '1.1rem', fontWeight: 700, color: 'var(--accent-pink)' }}>Tryout {n}</span>
                <span className="text-muted" style={{ fontSize: '0.8rem' }}>80 questions</span>
              </button>
            ))}
          </div>
          <button onClick={() => setMenuState('home')} className="btn" style={{ background: 'transparent', color: 'var(--text-muted)' }}>
            ← Back
          </button>
        </div>
      )}
    </div>
  );
};

export default Intro;
