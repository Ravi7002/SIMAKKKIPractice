export const cleanText = (text) => {
  if (!text) return text;
  return text.replace(/\[\d+\]/g, '').trim();
};

export const calculateScore = (question, selectedAnswer) => {
  if (!selectedAnswer) return 0;
  if (selectedAnswer === question.correct_answer) return 4;
  return -1;
};

export const evaluateResults = (questions, answers) => {
  let totalScore = 0;
  const topicStats = {};

  questions.forEach(q => {
    const selectedAnswer = answers[q.id] || null;
    const score = calculateScore(q, selectedAnswer);
    totalScore += score;

    if (!topicStats[q.topic]) {
      topicStats[q.topic] = {
        topic: q.topic,
        subject: q.subject,
        correct: 0,
        incorrect: 0,
        blank: 0,
        score: 0,
        totalQuestions: 0
      };
    }

    const t = topicStats[q.topic];
    t.totalQuestions++;
    t.score += score;

    if (!selectedAnswer) {
      t.blank++;
    } else if (selectedAnswer === q.correct_answer) {
      t.correct++;
    } else {
      t.incorrect++;
    }
  });

  // Convert to array and sort by score (lowest first) to highlight areas needing practice
  const topicsArray = Object.values(topicStats).sort((a, b) => a.score - b.score);

  return {
    totalScore,
    topics: topicsArray
  };
};
