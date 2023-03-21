date = new Date();
document.getElementById("footerContent").innerText = document
  .getElementById("footerContent")
  .innerText.replace("{date}", date.getFullYear());

let burger = document.querySelector(".burger");
let navbar = document.querySelector(".navbar");
let navlist = document.querySelector(".navlist");
let rightnav = document.querySelector(".rightNav");
let logo = document.querySelector(".logo");

burger.addEventListener("click", (e) => {
  navbar.classList.toggle("h-resp");
  navlist.classList.toggle("v-resp");
  logo.classList.toggle("v-resp");
  rightnav.classList.toggle("v-resp");
  burger.classList.toggle("change");
});
