function toLatex(s) {
  // cbrt(x) → \sqrt[3]{x}
  s = s.replace(/cbrt\(([^)]+)\)/g, (_, inner) => `\\sqrt[3]{${inner}}`);

  // sqrt(x) → \sqrt{x}
  s = s.replace(/\bsqrt\(([^)]+)\)/g, (_, inner) => `\\sqrt{${inner}}`);

  // log_base(x) → \log_{base}(x)
  s = s.replace(/log_(\w+)\(([^)]+)\)/g, (_, base, arg) => `\\log_{${base}}(${arg})`);

  // x^{...} → already fine, leave
  // x^word or x^digit → x^{word}  (handles 3^x, x^2, 3^{xy})
  s = s.replace(/\^(?!\{)(-?[a-zA-Z0-9]+)/g, (_, exp) => `^{${exp}}`);

  // x_{...} → already fine, leave
  // x_word or x_digit → x_{word}  (handles a_n, x_1, S_{n-1})
  s = s.replace(/_(?!\{)(-?[a-zA-Z0-9]+)/g, (_, sub) => `_{${sub}}`);

  // * → \cdot (but not ** or */)
  s = s.replace(/(?<![*])\*(?![*/])/g, ' \\cdot ');

  // Common symbols
  s = s.replace(/\+\-/g, '\\pm');
  s = s.replace(/~=/g, '\\approx');
  s = s.replace(/!=/g, '\\neq');
  s = s.replace(/<=/g, '\\le');
  s = s.replace(/>=/g, '\\ge');

  return s;
}

console.log(toLatex("x_1 = 0"));
console.log(toLatex("S_{n-1}"));
console.log(toLatex("log_2(x+6)"));
console.log(toLatex("a_15"));
console.log(toLatex("x_2"));
