var animateButton = function (e) {
  e.preventDefault;
  e.target.classList.remove("animate");
  e.target.classList.add("animate");
  setTimeout(function () {
    e.target.classList.remove("animate");
  }, 700);
};

var bubblyButtons = document.getElementsByClassName("bubbly-button");
for (var i = 0; i < bubblyButtons.length; i++) {
  bubblyButtons[i].addEventListener("click", animateButton, false);
}
const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");
const links = document.querySelectorAll(".nav-links li");
hamburger.addEventListener("click", () => {
  navLinks.classList.toggle("open");
  links.forEach((link) => {
    link.classList.toggle("fade");
  });
  hamburger.classList.toggle("toggle");
});

let params = new URL(document.location.toString()).searchParams;
let batch = params.get("b");
let day = params.get("day");

if (batch == null) {
  let last_batch = get_last_batch();
  if (last_batch != null) {
    let loc = `/batch?b=${last_batch}`;
    if (day != null) {
      loc += `&day=${day}`;
    }
    location.href = loc;
  }
} else {
  set_last_batch(batch);
}

function batch_change() {
  let b = document.getElementById("batch_input");
  let d = document.getElementById("day");
  if (b.value != "None") {
    set_last_batch(b.value);
  }
  let loc = `/batch?b=${b.value}&day=${d.value}`;
  location.href = loc;
}
function today() {
  let b = document.getElementById("batch_input");
  if (b.value != "None") {
    set_last_batch(b.value);
  }
  let loc = `/batch?b=${b.value}`;
  location.href = loc;
}

function get_last_batch() {
  return localStorage.getItem("batch");
}

function set_last_batch(batch) {
  localStorage.setItem("batch", batch);
}
