function compute() {
  const nb1 = Number(document.getElementById("nb1").value);
  const nb2 = Number(document.getElementById("nb2").value);
  document.getElementById("sum").value = nb1 + nb2; // *
}
document.getElementById("add").addEventListener("click", compute);
