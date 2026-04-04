import React, { useState } from 'react';
import { BookOpen, Sparkles, BrainCircuit, Activity, Clock, Award } from 'lucide-react';

const Intro = ({ onStartPractice, onStartAbility, onStartTryout, onStartCompare }) => {
  const [showTryoutOptions, setShowTryoutOptions] = useState(false);

  return (
    <div className="glass-card fade-in" style={{ maxWidth: '600px', margin: '0 auto', textAlign: 'center' }}>
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

      {!showTryoutOptions ? (
        <div className="flex-column" style={{ gap: '1rem' }}>
          <button onClick={onStartAbility} className="btn" style={{ fontSize: '1.2rem', padding: '1rem', background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(255,255,255,0.1)' }}>
            <Activity size={24} style={{ color: 'var(--accent-blue)' }} /> Ability Test
          </button>
          
          <button onClick={onStartPractice} className="btn" style={{ fontSize: '1.2rem', padding: '1rem', background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(255,255,255,0.1)' }}>
            <BookOpen size={24} style={{ color: 'var(--accent-green)' }} /> Practice Test
          </button>
          
          <button onClick={() => setShowTryoutOptions(true)} className="btn btn-primary" style={{ fontSize: '1.2rem', padding: '1rem' }}>
            <Award size={24} /> Tryouts
          </button>
          
          <button onClick={onStartCompare} className="btn" style={{ fontSize: '1.1rem', padding: '1rem', background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(255,255,255,0.1)', marginTop: '1rem', color: 'var(--text-muted)' }}>
            <Activity size={20} /> Compare Questions (Real vs Practice)
          </button>
        </div>
      ) : (
        <div className="fade-in">
          <h2 className="mb-4" style={{ fontSize: '1.5rem', color: 'var(--accent-purple)' }}>Select Tryout</h2>
          <div className="flex-column" style={{ gap: '1rem', marginBottom: '1.5rem' }}>
            <button onClick={() => onStartTryout(1)} className="btn btn-outline" style={{ fontSize: '1.2rem', padding: '1rem' }}>
              <Clock size={20} /> Tryout 1 (Timed)
            </button>
            <button onClick={() => onStartTryout(2)} className="btn btn-outline" style={{ fontSize: '1.2rem', padding: '1rem' }}>
              <Clock size={20} /> Tryout 2 (Timed)
            </button>
          </div>
          <button onClick={() => setShowTryoutOptions(false)} className="btn" style={{ background: 'transparent', color: 'var(--text-muted)' }}>
            Back
          </button>
        </div>
      )}
    </div>
  );
};

export default Intro;
