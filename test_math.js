const MATH_TOKEN = /(?:[a-zA-Z0-9.]+\^(?:\{[^}]+\}|[a-zA-Z0-9-]+)|[a-zA-Z0-9.]+_\{[^}]+\}|[a-zA-Z0-9.]+_(-?[a-zA-Z0-9]+)|sqrt\([^)]+\)|cbrt\([^)]+\)|\\[a-zA-Z]+(?:\{[^}]*\})*|\blog_\w+\([^)]+\)|[a-z][0-9])/;
const MATH_TOKEN_STR = MATH_TOKEN.source;
const OPERATOR = /\s*[*/+\-=<>≤≥^!~|±]\s*|\s+/.source;
const MATH_RUN = new RegExp(
  `(${MATH_TOKEN_STR}(?:(?:${OPERATOR})(?:${MATH_TOKEN_STR}|[0-9]+(?:\\.[0-9]+)?))*)`,
  'g'
);

function splitPlainMath(text) {
  const segments = [];
  let lastIndex = 0;
  let match;

  while ((match = MATH_RUN.exec(text)) !== null) {
      if (!MATH_TOKEN.test(match[0])) continue;
      
      console.log("MATCH:", match[0]);
      lastIndex = match.index + match[0].length;
  }
}

splitPlainMath("meaning our original roots are x_1 = 0 and x_2 = 2.");
splitPlainMath("The sum of this sequence is S_21 = (21/2) * (4 + 144) = (21/2)");
splitPlainMath("a_n = (n+1)^2 - 1");
splitPlainMath("log_2(x+6) = 2 + log_2(x)");
