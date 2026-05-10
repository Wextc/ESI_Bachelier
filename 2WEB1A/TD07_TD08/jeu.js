"use strict";

const game = {
  level: 0,
  sequences: [],
  step: 0,
};
const p = document.getElementsByName("p");

const sequencesContainer = document.getElementById("sequence");

const startGame = () => {};

// Add 4 span

const initialSpanState = (sequencesContainer) => {
  for (let i = 1; i < 5; i++) {
    const span = document.createElement("span");
    span.textContent = i;
    sequencesContainer.appendChild(span);
  }
};
initialSpanState(sequencesContainer);
document.getElementById("btn").addEventListener("click", startGame);
