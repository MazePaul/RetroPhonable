function on() {
  document.getElementById("overlay").style.display = "block";
}

function off() {
  document.getElementById("overlay").style.display = "none";
}

function exit() {
document.getElementById("exit-btn").addEventListener("click", off);
}