"use strict";
const Game = {
  level: "",
  seq: "",
  step: "",
};

const startGame = () => {
  btnState();
  seqState();
};

const btnState = () => {
  document.getElementById("btn").classList.add("hidden");
};

const seqState = () => {
  let arrayNbr = [1, 2, 3, 4];

  let seq = document.getElementById("seq");
  arrayNbr.forEach((item) => {
    let span = document.createElement("span");
    span.textContent = item;
    seq.append(span);
  });
};

document.getElementById("btn").addEventListener("click", startGame);
