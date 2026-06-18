const display = document.getElementById("display");
const message = document.getElementById("message");
const buttons = document.querySelectorAll(".btn");
let expression = "";
let justEvaluated = false;
let messageTimeout = null;

function updateDisplay() {
  display.value = expression || "0";
}

function setMessage(text, type = "info") {
  if (!message) return;
  message.textContent = text;
  message.dataset.type = type;
  clearTimeout(messageTimeout);
  messageTimeout = setTimeout(() => {
    if (message.textContent === text) {
      message.textContent = "";
    }
  }, 2500);
}

function isOperator(value) {
  return /[+\-*/]/.test(value);
}

function endsWithOperator(expr) {
  return /[+\-*/]$/.test(expr);
}

function balanceParentheses(expr) {
  let depth = 0;
  for (const char of expr) {
    if (char === "(") depth += 1;
    if (char === ")") depth -= 1;
    if (depth < 0) return false;
  }
  return depth === 0;
}

function validateExpression(expr) {
  const validChars = /^[0-9.+\-*/()]+$/;
  return validChars.test(expr) && balanceParentheses(expr);
}

function appendValue(value) {
  if (justEvaluated && /^[0-9.]$/.test(value) && !endsWithOperator(expression)) {
    expression = value;
    justEvaluated = false;
    updateDisplay();
    return;
  }

  if (expression === "0" && value !== ".") {
    expression = value;
  } else {
    expression += value;
  }

  justEvaluated = false;
  updateDisplay();
}

function clearExpression() {
  expression = "";
  justEvaluated = false;
  updateDisplay();
  setMessage("", "info");
}

function toggleSign() {
  if (!expression || expression === "0") {
    expression = "-";
    updateDisplay();
    return;
  }

  const numberMatch = expression.match(/(-?\d+(?:\.\d*)?)$/);
  if (!numberMatch) {
    if (endsWithOperator(expression) || expression.endsWith("(")) {
      expression += "-";
      updateDisplay();
    }
    return;
  }

  const number = numberMatch[1];
  const start = numberMatch.index;
  if (number.startsWith("-")) {
    expression = expression.slice(0, start) + number.slice(1);
  } else {
    expression = expression.slice(0, start) + "-" + number;
  }
  updateDisplay();
}

function evaluateExpression() {
  if (!expression) return;

  if (!validateExpression(expression)) {
    setMessage("Expresión inválida. Usa números, operadores y paréntesis.", "error");
    expression = "";
    updateDisplay();
    return;
  }

  try {
    const result = Function(`"use strict"; return (${expression})`)();
    if (!Number.isFinite(result)) {
      setMessage("Error: no se puede dividir entre cero.", "error");
      expression = "";
      justEvaluated = false;
      updateDisplay();
      return;
    }

    expression = String(result);
    justEvaluated = true;
    updateDisplay();
    setMessage("Resultado", "success");
  } catch (error) {
    setMessage("Error al evaluar la expresión.", "error");
    expression = "";
    justEvaluated = false;
    updateDisplay();
  }
}

function handleKey(event) {
  const { key } = event;

  if (key === "Enter") {
    event.preventDefault();
    evaluateExpression();
    return;
  }

  if (key === "Backspace") {
    event.preventDefault();
    expression = expression.slice(0, -1);
    updateDisplay();
    return;
  }

  if (key === "Escape") {
    event.preventDefault();
    clearExpression();
    return;
  }

  if (/^[0-9]$/.test(key) || /^[+\-*/().]$/.test(key)) {
    event.preventDefault();
    appendValue(key);
  }
}

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    const value = button.textContent;
    if (value === "C") {
      clearExpression();
      return;
    }
    if (value === "=") {
      evaluateExpression();
      return;
    }
    if (value === "+/-") {
      toggleSign();
      return;
    }
    appendValue(value);
  });
});

document.addEventListener("keydown", handleKey);
