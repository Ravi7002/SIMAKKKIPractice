import React from 'react';
import katex from 'katex';
import 'katex/dist/katex.min.css';

/**
 * Converts plain-text math notation to LaTeX:
 * - sqrt(x)   → \sqrt{x}
 * - cbrt(x)   → \sqrt[3]{x}
 * - x^2       → x^{2}
 * - ^{...}    kept as-is (already LaTeX)
 * - \sqrt{..} kept as-is
 * - log_2(x)  → \log_{2}(x)
 * - fractions like (a/b) in math context
 */
function toLatex(raw) {
  let s = raw;

  // Already-LaTeX passthrough for common patterns — leave alone
  // Normalize cbrt(x) → \sqrt[3]{x}
  s = s.replace(/cbrt\(([^)]+)\)/g, (_, inner) => `\\sqrt[3]{${inner}}`);

  // sqrt(x) → \sqrt{x}
  s = s.replace(/sqrt\(([^)]+)\)/g, (_, inner) => `\\sqrt{${inner}}`);

  // log_base(x) → \log_{base}(x)
  s = s.replace(/log_(\w+)\(([^)]+)\)/g, (_, base, arg) => `\\log_{${base}}(${arg})`);

  // plain ^ not already in {}  e.g. x^2 → x^{2}, x^10 → x^{10}
  // but leave ^{ alone (already latex)
  s = s.replace(/\^(?!\{)(-?\d+\.?\d*)/g, (_, exp) => `^{${exp}}`);

  // Inline fractions written as (a/b) in obvious math text - skip, too risky

  return s;
}

/**
 * Splits a text string into segments: regular text and $...$ or $$...$$ math blocks.
 * Also detects plain-text math patterns and wraps them in inline math.
 */
function splitIntoSegments(text) {
  if (!text) return [{ type: 'text', value: '' }];

  // First, find explicit $...$ or $$...$$ delimiters
  const segments = [];
  // Regex: $$...$$  or  $...$
  const mathRegex = /(\$\$[\s\S]+?\$\$|\$[^$\n]+?\$)/g;

  let lastIndex = 0;
  let match;
  while ((match = mathRegex.exec(text)) !== null) {
    if (match.index > lastIndex) {
      // text before this math block — check for plain-text math
      segments.push(...splitPlainMath(text.slice(lastIndex, match.index)));
    }
    const raw = match[0];
    const isDisplay = raw.startsWith('$$');
    const inner = isDisplay ? raw.slice(2, -2) : raw.slice(1, -1);
    segments.push({ type: isDisplay ? 'display' : 'inline', value: inner });
    lastIndex = match.index + match[0].length;
  }

  if (lastIndex < text.length) {
    segments.push(...splitPlainMath(text.slice(lastIndex)));
  }

  return segments;
}

/**
 * Detect plain-text math patterns like sqrt(...), x^2, \sqrt{} (LaTeX without $)
 * and wrap them as inline math segments.
 */
function splitPlainMath(text) {
  if (!text) return [];

  // Patterns that indicate math content in plain text
  const plainMathPattern = /((?:\\[a-zA-Z]+\{[^}]*\}|cbrt\([^)]+\)|sqrt\([^)]+\)|log_\w+\([^)]+\)|\w+\^(?:\{[^}]+\}|-?\d+))[^,\s\w]*)+/g;

  const segments = [];
  let lastIndex = 0;
  let match;

  while ((match = plainMathPattern.exec(text)) !== null) {
    if (match.index > lastIndex) {
      segments.push({ type: 'text', value: text.slice(lastIndex, match.index) });
    }
    segments.push({ type: 'inline', value: toLatex(match[0]) });
    lastIndex = match.index + match[0].length;
  }

  if (lastIndex < text.length) {
    segments.push({ type: 'text', value: text.slice(lastIndex) });
  }

  return segments.length > 0 ? segments : [{ type: 'text', value: text }];
}

function renderMath(latex, display) {
  try {
    return katex.renderToString(latex, {
      throwOnError: false,
      displayMode: display,
      trust: true,
    });
  } catch (e) {
    return latex;
  }
}

/**
 * MathText component — renders text with inline math expressions beautifully.
 * Supports:
 *  - $...$ and $$...$$ delimiters
 *  - Plain-text sqrt(), cbrt(), log_b(), x^2 patterns
 *  - Raw LaTeX like \sqrt{} \frac{}{}
 */
const MathText = ({ text, style, className }) => {
  if (!text) return null;

  // Remove citation brackets like [1]
  const cleaned = text.replace(/\[\d+\]/g, '').trim();

  const segments = splitIntoSegments(cleaned);

  return (
    <span style={style} className={className}>
      {segments.map((seg, i) => {
        if (seg.type === 'text') {
          // Still do a final pass: convert any remaining x^{n} patterns
          // and any \sqrt{} that slipped through as plain text
          const hasLatex = /\\[a-zA-Z]|\^{/.test(seg.value);
          if (hasLatex) {
            return (
              <span
                key={i}
                dangerouslySetInnerHTML={{ __html: renderMath(toLatex(seg.value), false) }}
              />
            );
          }
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
