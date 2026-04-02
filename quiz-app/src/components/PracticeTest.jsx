import React, { useState } from 'react';
import Quiz from './Quiz';
import { ArrowLeft, Book, Grid } from 'lucide-react';
import { cleanText } from '../utils';

const PracticeTest = ({ allTopicsData, onBack }) => {
  const [view, setView] = useState('subjects'); // 'subjects', 'topics', 'intro', 'quiz'
  const [selectedSubject, setSelectedSubject] = useState(null);
  const [selectedTopic, setSelectedTopic] = useState(null);

  // Derive unique subjects
  const subjects = [...new Set(allTopicsData.map(t => t.subject))];

  // Topics for selected subject
  const topicsForSubject = selectedSubject 
    ? allTopicsData.filter(t => t.subject === selectedSubject) 
    : [];

  const handleSubjectClick = (sub) => {
    setSelectedSubject(sub);
    setView('topics');
  };

  const handleTopicClick = (topicObj) => {
    setSelectedTopic(topicObj);
    setView('intro');
  };

  const startQuiz = () => {
    setView('quiz');
  };

  const goBack = () => {
    if (view === 'subjects') onBack();
    else if (view === 'topics') setView('subjects');
    else if (view === 'intro') setView('topics');
    else if (view === 'quiz') setView('topics'); // Back out of quiz without finishing
  };

  const [answers, setAnswers] = useState({});

  if (view === 'quiz') {
    return (
      <Quiz 
        questions={selectedTopic.questions} 
        answers={answers} 
        setAnswers={setAnswers} 
        onFinish={() => setView('topics')}
        onQuit={goBack}
      />
    );
  }

  return (
    <div className="glass-card fade-in" style={{ maxWidth: '800px', margin: '2rem auto' }}>
      <button onClick={goBack} className="btn" style={{ marginBottom: '2rem', padding: '0.5rem 1rem', background: 'transparent', border: '1px solid var(--text-muted)' }}>
        <ArrowLeft size={18} /> Back
      </button>

      {view === 'subjects' && (
        <div className="fade-in">
          <h2 className="text-gradient mb-6" style={{ fontSize: '2rem', textAlign: 'center' }}>
            <Book size={32} style={{ display: 'inline', verticalAlign: 'middle', marginRight: '10px' }} />
            Select a Subject
          </h2>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '1rem' }}>
            {subjects.map(sub => (
              <button key={sub} className="btn btn-outline" onClick={() => handleSubjectClick(sub)} style={{ padding: '1.5rem', fontSize: '1.2rem' }}>
                {sub}
              </button>
            ))}
          </div>
        </div>
      )}

      {view === 'topics' && (
        <div className="fade-in">
          <h2 className="text-gradient mb-6" style={{ fontSize: '2rem', textAlign: 'center' }}>
            <Grid size={32} style={{ display: 'inline', verticalAlign: 'middle', marginRight: '10px' }} />
            {selectedSubject} Topics
          </h2>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '1rem' }}>
            {topicsForSubject.map(t => (
              <button key={t.topic} className="btn btn-outline" onClick={() => handleTopicClick(t)} style={{ padding: '1.5rem', textAlign: 'left', display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
                <span style={{ fontSize: '1.2rem', fontWeight: 'bold' }}>{t.topic}</span>
                <span className="text-muted" style={{ fontSize: '0.9rem' }}>{t.questions.length} Practice Questions</span>
              </button>
            ))}
          </div>
        </div>
      )}

      {view === 'intro' && (
        <div className="fade-in text-center">
          <h2 className="text-gradient mb-4" style={{ fontSize: '2.5rem' }}>{selectedTopic.topic}</h2>
          <div className="glass-card" style={{ background: 'rgba(255, 255, 255, 0.05)', marginBottom: '2rem', textAlign: 'left' }}>
            <h3 style={{ color: 'var(--accent-blue)', marginBottom: '1rem' }}>Introduction to Topic</h3>
            <p style={{ lineHeight: '1.6', fontSize: '1.1rem', marginBottom: '2rem' }}>
              {selectedTopic.introduction || 'Learn the fundamental concepts to master these questions.'}
            </p>

            {selectedTopic.tips_and_tricks && selectedTopic.tips_and_tricks.length > 0 && (
              <>
                <h3 style={{ color: 'var(--accent-purple)', marginBottom: '1rem' }}>Tips & Tricks</h3>
                <ul style={{ listStyleType: 'disc', paddingLeft: '2rem', lineHeight: '1.6' }}>
                  {selectedTopic.tips_and_tricks.map((tip, idx) => (
                    <li key={idx} className="text-muted">{tip}</li>
                  ))}
                </ul>
              </>
            )}
          </div>

          <button onClick={startQuiz} className="btn btn-primary" style={{ fontSize: '1.2rem', padding: '1rem 3rem' }}>
            Start Practice Questions
          </button>
        </div>
      )}
    </div>
  );
};

export default PracticeTest;
