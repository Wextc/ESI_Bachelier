"use strict";
const Game = {
  level: "",
  seq: "",
  step: "",
};

const btnState = () => {
  document.getElementById("btn").classList.add("hidden");
};

const seqStates = () => {
  let arrayNbr = [1, 2, 3, 4];

  var seq = document.getElementById("seq");
  arrayNbr.forEach((item, index) => {
    let span = document.createElement("span");
    span.setAttribute("id", index);
    span.textContent = item;
    seq.append(span);
  });
};

const noNbr = () => {
  const spans = seq.querySelectorAll("span");
  spans.forEach((el, index) => {
    el.textContent = "X";
  });
};

const startGame = () => {
  btnState();
  seqStates();
  setTimeout(noNbr, 3000);
};

document.getElementById("btn").addEventListener("click", startGame);
