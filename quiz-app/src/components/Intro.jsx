import React, { useState } from 'react';
import { BookOpen, Sparkles, BrainCircuit, Activity, Clock, Award, ChevronRight, FlaskConical, Lock, User, Eye, EyeOff } from 'lucide-react';

const PASSWORD = 'ravigantengbgt';

/* ── Password Gate ── */
const HayyuGate = ({ onEnter, onBack }) => {
  const [pw, setPw] = useState('');
  const [showPw, setShowPw] = useState(false);
  const [error, setError] = useState('');
  const [shake, setShake] = useState(false);

  const attempt = () => {
    if (pw === PASSWORD) {
      onEnter();
    } else {
      setError('Wrong password. Try again! 🙅');
      setShake(true);
      setTimeout(() => { setShake(false); setPw(''); setError(''); }, 1200);
    }
  };

  return (
    <div className="glass-card fade-in" style={{ maxWidth: '420px', margin: '0 auto', textAlign: 'center' }}>
      <div style={{ fontSize: '3.5rem', marginBottom: '1rem' }}>🔐</div>
      <h2 className="text-gradient" style={{ fontSize: '1.8rem', marginBottom: '0.5rem' }}>Hayyu's Private Mode</h2>
      <p className="text-muted mb-6" style={{ fontSize: '0.95rem' }}>Enter the secret password to unlock Hayyu's personal features ❤️</p>

      <div style={{
        position: 'relative',
        marginBottom: '1rem',
        animation: shake ? 'shake 0.4s cubic-bezier(0.36,0.07,0.19,0.97) both' : 'none'
      }}>
        <input
          type={showPw ? 'text' : 'password'}
          value={pw}
          onChange={e => setPw(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && attempt()}
          placeholder="Enter password..."
          style={{
            width: '100%', padding: '0.9rem 3rem 0.9rem 1.2rem',
            borderRadius: '12px', border: `1px solid ${error ? 'var(--accent-red)' : 'rgba(255,255,255,0.15)'}`,
            background: 'rgba(255,255,255,0.05)', color: 'white',
            fontSize: '1rem', fontFamily: 'inherit', outline: 'none',
          }}
        />
        <button onClick={() => setShowPw(v => !v)} style={{
          position: 'absolute', right: '12px', top: '50%', transform: 'translateY(-50%)',
          background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text-muted)'
        }}>
          {showPw ? <EyeOff size={18}/> : <Eye size={18}/>}
        </button>
      </div>

      {error && <p style={{ color: 'var(--accent-red)', fontSize: '0.9rem', marginBottom: '1rem' }}>{error}</p>}

      <div style={{ display: 'flex', gap: '0.8rem', justifyContent: 'center' }}>
        <button onClick={onBack} className="btn" style={{ background: 'transparent', color: 'var(--text-muted)', border: '1px solid rgba(255,255,255,0.1)' }}>
          ← Back
        </button>
        <button onClick={attempt} className="btn btn-primary" style={{ flex: 1 }}>
          <Lock size={16}/> Unlock
        </button>
      </div>
    </div>
  );
};

/* ── Main Intro ── */
const Intro = ({ onStartPractice, onStartAbility, onStartTryout, onStartCompare, onStartPracticeTryout, isHayyu }) => {
  const [menuState, setMenuState] = useState('home'); // 'home' | 'tryout' | 'practice-tryout'

  return (
    <div className="glass-card fade-in" style={{ maxWidth: '640px', margin: '0 auto', textAlign: 'center' }}>
      <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '2rem' }}>
        <div style={{ position: 'relative' }}>
          <BrainCircuit size={80} color="var(--accent-purple)" />
          <Sparkles size={32} color="var(--accent-pink)" style={{ position: 'absolute', top: '-10px', right: '-10px', animation: 'pulse 2s infinite' }} />
        </div>
      </div>

      {isHayyu ? (
        <>
          <h1 className="text-gradient mb-4" style={{ fontSize: '2.4rem' }}>
            Hayyu's Personal SIMAK KKI UI Practice Web
          </h1>
          <p className="text-muted mb-8 text-lg">
            Master your skills with Hayyu's custom-built practice suite.
            <br/><br/>
            <i>"Happy practicing sayang, cemangats - lop ravi"</i> ❤️
          </p>
        </>
      ) : (
        <>
          <h1 className="text-gradient mb-4" style={{ fontSize: '2.4rem' }}>
            SIMAK KKI UI Practice
          </h1>
          <p className="text-muted mb-8 text-lg">
            Sharpen your skills with high-quality practice tryouts for SIMAK KKI UI.
          </p>
        </>
      )}

      {/* ── Home Menu ── */}
      {menuState === 'home' && (
        <div className="flex-column fade-in" style={{ gap: '1rem' }}>

          {isHayyu && (
            <>
              <button onClick={onStartAbility} className="btn" style={{ fontSize: '1.2rem', padding: '1rem', background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(255,255,255,0.1)' }}>
                <Activity size={24} style={{ color: 'var(--accent-blue)' }} /> Ability Test
              </button>
              <button onClick={onStartPractice} className="btn" style={{ fontSize: '1.2rem', padding: '1rem', background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(255,255,255,0.1)' }}>
                <BookOpen size={24} style={{ color: 'var(--accent-green)' }} /> Practice by Topic
              </button>
            </>
          )}

          <button
            onClick={() => setMenuState('practice-tryout')}
            className="btn btn-primary"
            style={{ fontSize: '1.2rem', padding: '1rem', background: 'linear-gradient(135deg, #7c3aed, #db2777)', boxShadow: '0 0 24px rgba(139,92,246,0.4)' }}
          >
            <FlaskConical size={24} /> Practice Tryout (80Q · No Timer · Hints · Explanation)
          </button>

          {isHayyu && (
            <>
              <button onClick={() => setMenuState('tryout')} className="btn btn-outline" style={{ fontSize: '1.2rem', padding: '1rem' }}>
                <Award size={24} /> Real Tryout (Timed)
              </button>
              <button onClick={onStartCompare} className="btn" style={{ fontSize: '1.1rem', padding: '1rem', background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(255,255,255,0.1)', marginTop: '0.5rem', color: 'var(--text-muted)' }}>
                <Activity size={20} /> Compare Questions (Real vs Practice)
              </button>
            </>
          )}
        </div>
      )}

      {/* ── Real Tryout Selector (Hayyu only) ── */}
      {menuState === 'tryout' && isHayyu && (
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
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '1rem', marginBottom: '1.5rem', maxHeight: '50vh', overflowY: 'auto', padding: '0.5rem' }}>
            {Array.from({length: 4}, (_, i) => i + 1).map(n => (
              <button
                key={n}
                onClick={() => onStartPracticeTryout(n - 1)}
                className="glass-card btn"
                style={{
                  padding: '1.8rem 1rem',
                  display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '0.6rem',
                  border: '1px solid rgba(244,63,94,0.25)',
                  cursor: 'pointer', transition: 'all 0.2s',
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

export { HayyuGate };
export default Intro;
