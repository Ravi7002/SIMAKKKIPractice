const fs = require('fs');

const topicMap = {
  "Combinatorics and Probability": "Combinatorics and Probability",
  "Quadratic Equations": "Quadratic Equations and Functions",
  "Functions and Inverses": "Functions and Inverses",
  "Statistics": "Statistics",
  "Set Theory": "Sets and Venn Diagrams",
  "Vectors": "Vectors",
  "Algebraic Manipulation": "Quadratic Equations and Functions",
  "Exponents and Logarithms": "Exponents and Logarithms",
  "Systems of Equations": "Systems of Linear Equations",
  "Sequences and Series": "Sequences and Series",
  "Trigonometry": "Trigonometry",
  "Inequalities": "Inequalities",
  "Pattern Recognition and Puzzles": "Pattern Recognition and Puzzles",
  "Matrix Algebra": "Matrix Algebra",
  "Systems of Linear Equations": "Systems of Linear Equations",
  "Coordinate Geometry": "Geometry and Coordinates",
  "Data Interpretation and Charts": "Data Interpretation and Charts",
  "Word Problems": "Word Problems",
  "Geometry": "Geometry and Coordinates",
  "Conditional Logic": "Conditional Logic",
  "Reading Comprehension": "Reading Comprehension",
  "Grammar and Tenses": "Grammar and Tenses",
  "Paragraph Cohesion and Structure": "Paragraph Cohesion and Structure",
  "Vocabulary in Context": "Vocabulary in Context",
  "Mathematical Logic": "Mathematical Logic",
  "Deductive Logic and Syllogisms": "Syllogisms and Deductive Logic",
  "Analytical Reasoning and Sequencing": "Analytical Reasoning and Sequencing",
  "Spatial Reasoning and Arrangements": "Spatial Reasoning and Arrangements",
  "Rate, Time, and Distance": "Rate, Time, and Distance"
};

const processFile = (path) => {
  if (!fs.existsSync(path)) {
      console.log('Skipping ' + path);
      return;
  }
  const data = JSON.parse(fs.readFileSync(path));
  let modified = 0;
  for (let q of data) {
    if (topicMap[q.topic] && q.topic !== topicMap[q.topic]) {
      q.topic = topicMap[q.topic];
      modified++;
    } else if (!topicMap[q.topic]) {
      console.log('WARNING: UNMAPPED TOPIC - ' + q.topic);
    }
  }
  if (modified > 0) {
    fs.writeFileSync(path, JSON.stringify(data, null, 4));
    console.log(`Updated ${modified} questions in ${path}`);
  } else {
    console.log(`No changes needed in ${path}`);
  }
};

processFile('realQ1.json');
processFile('realQ2.json');
processFile('./quiz-app/src/realQ1.json');
processFile('./quiz-app/src/realQ2.json');
