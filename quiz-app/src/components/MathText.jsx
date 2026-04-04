import React from 'react';
import katex from 'katex';
import 'katex/dist/katex.min.css';

/**
 * Converts plain-text math notation into LaTeX.
 */
function toLatex(s) {
  // cbrt(x) → \sqrt[3]{x}
  s = s.replace(/cbrt\(([^)]+)\)/g, (_, inner) => `\\sqrt[3]{${inner}}`);

  // sqrt(x) → \sqrt{x}
  s = s.replace(/\bsqrt\(([^)]+)\)/g, (_, inner) => `\\sqrt{${inner}}`);

  // log_base(x) → \log_{base}(x) or log_base → \log_{base}
  s = s.replace(/log_(\w+)(?:\(([^)]+)\))?/g, (_, base, arg) => arg ? `\\log_{${base}}(${arg})` : `\\log_{${base}}`);

  // x^{...} → already fine, leave
  // x^word or x^digit → x^{word}  (handles 3^x, x^2, 3^{xy})
  s = s.replace(/\^(?!\{)(-?[a-zA-Z0-9]+)/g, (_, exp) => `^{${exp}}`);

  // x_{...} → already fine, leave
  // x_word or x_digit → x_{word}  (handles a_n, x_1, S_{n-1})
  s = s.replace(/_(?!\{)(-?[a-zA-Z0-9]+)/g, (_, sub) => `_{${sub}}`);

  // * → \cdot (but not ** or */)
  s = s.replace(/(?<![*])\*(?![*/])/g, ' \\cdot ');

  // Common symbols
  s = s.replace(/\+\/?\-/g, '\\pm ');
  s = s.replace(/~=/g, '\\approx ');
  s = s.replace(/!=/g, '\\neq ');
  s = s.replace(/<=/g, '\\le ');
  s = s.replace(/>=/g, '\\ge ');
  // Logical Reasoning relations
  s = s.replace(/ (>) /g, ' \\gt ');
  s = s.replace(/ (<) /g, ' \\lt ');

  // 2x2 Matrix: [[a,b], [c,d]] -> \begin{pmatrix} a & b \\ c & d \end{pmatrix}
  s = s.replace(/\[\[(.*?)\]\s*,\s*\[(.*?)\]\]/g, (_, row1, row2) => {
    return `\\begin{pmatrix} ${row1.replace(/,/g, ' & ')} \\\\ ${row2.replace(/,/g, ' & ')} \\end{pmatrix}`;
  });

  // Vector / 1D Matrix: [a, b] or [a, b, c] -> stacked matrix. Ignore intervals with ° or similar.
  s = s.replace(/(?<!\d)\[\s*(-?[\w\d]+)\s*,\s*(-?[\w\d]+)\s*(?:,\s*(-?[\w\d]+))?\s*\](?!\s*°)/g, (match, v1, v2, v3) => {
     if (match.includes('°') || match.includes('.')) return match;
     if (v3) return `\\begin{pmatrix} ${v1} \\\\ ${v2} \\\\ ${v3} \\end{pmatrix}`;
     return `\\begin{pmatrix} ${v1} \\\\ ${v2} \\end{pmatrix}`;
  });

  return s;
}

/**
 * Render a LaTeX string with KaTeX.
 */
function renderMath(latex, display = false) {
  try {
    return katex.renderToString(latex, {
      throwOnError: false,
      displayMode: display,
      trust: true,
    });
  } catch {
    return latex;
  }
}

/**
 * A "math token" is any of:
 *  - something^something  (e.g. 3^x, x^2, x^{10})
 *  - something_something  (e.g. a_n, x_1, S_21)
 *  - sqrt(...) or cbrt(...)
 *  - \latexCommand{...}
 *  - log_b(...)
 *  - single letter followed by operator (e.g. A > B)
 */
const MATH_TOKEN = /(?:[a-zA-Z0-9.\\]+(?:\^|_)(?:\{[^}]+\}|[a-zA-Z0-9-]+)|sqrt\([^)]+\)|cbrt\([^)]+\)|\\[a-zA-Z]+(?:\{[^}]*\})*|\blog_\w+(?:\([^)]+\))?|[A-Za-z][0-9]|(?:[A-Za-z](?=\s*[<>≤≥=+*/-])))/;
/**
 * Splits a plain-text block into text/math segments.
 * Groups consecutive math tokens + operators into one math block.
 */
function splitPlainMath(text) {
  if (!text) return [];

  // Build a pattern that matches a "math run":
  // one or more math tokens connected by operators/spaces
  const MATH_TOKEN_STR = MATH_TOKEN.source;
  const OPERATOR = /\s*[*/+\-=<>≤≥^!~|±()∘]\s*|\s+/.source;
  // A math run must start with a math token, then optionally more tokens/operators, and end with a math token or a bare number/result
  const MATH_RUN = new RegExp(
    `(${MATH_TOKEN_STR}(?:(?:${OPERATOR})(?:${MATH_TOKEN_STR}|[A-Za-z]\\b|[0-9]+(?:\\.[0-9]+)?))*)`,
    'g'
  );

  const segments = [];
  let lastIndex = 0;
  let match;

  while ((match = MATH_RUN.exec(text)) !== null) {
    // Only treat as math if the match actually contains a real math token
    if (!MATH_TOKEN.test(match[0])) continue;

    if (match.index > lastIndex) {
      segments.push({ type: 'text', value: text.slice(lastIndex, match.index) });
    }
    segments.push({ type: 'inline', value: toLatex(match[0].trim()) });
    lastIndex = match.index + match[0].length;
  }

  if (lastIndex < text.length) {
    segments.push({ type: 'text', value: text.slice(lastIndex) });
  }

  return segments.length > 0 ? segments : [{ type: 'text', value: text }];
}

/**
 * Master split: handles explicit $...$ / $$...$$ delimiters first,
 * then falls back to plain-text math detection.
 */
function splitIntoSegments(text) {
  if (!text) return [{ type: 'text', value: '' }];

  // Remove citation brackets
  text = text.replace(/\[\d+\]/g, '').trim();

  const segments = [];
  const mathDelim = /(\$\$[\s\S]+?\$\$|\$[^$\n]+?\$)/g;
  let lastIndex = 0;
  let match;

  while ((match = mathDelim.exec(text)) !== null) {
    if (match.index > lastIndex) {
      segments.push(...splitPlainMath(text.slice(lastIndex, match.index)));
    }
    const raw = match[0];
    const isDisplay = raw.startsWith('$$');
    let inner = isDisplay ? raw.slice(2, -2) : raw.slice(1, -1);
    
    // Convert plain-text notations inside $...$ as well
    inner = toLatex(inner);

    segments.push({ type: isDisplay ? 'display' : 'inline', value: inner });
    lastIndex = match.index + raw.length;
  }

  if (lastIndex < text.length) {
    segments.push(...splitPlainMath(text.slice(lastIndex)));
  }

  return segments;
}

/**
 * MathText — renders text with inline math expressions.
 * Handles sqrt(), cbrt(), x^2, x^y, log_b(), LaTeX \cmd{}, $...$ delimiters.
 */
const MathText = ({ text, style, className }) => {
  if (!text) return null;

  const segments = splitIntoSegments(String(text));

  return (
    <span style={style} className={className}>
      {segments.map((seg, i) => {
        if (seg.type === 'text') {
          return <span key={i}>{seg.value}</span>;
        }
        return (
          <span
            key={i}
            dangerouslySetInnerHTML={{ __html: renderMath(seg.value, seg.type === 'display') }}
          />
        );
      })}
    </span>
  );
};

export default MathText;
