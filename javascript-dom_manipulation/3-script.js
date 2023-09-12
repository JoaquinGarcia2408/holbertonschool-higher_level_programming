var headerElement = document.querySelector("header");
var toggleHeader = document.getElementById("toggle_header");

toggleHeader.addEventListener("click", function onClick () {
    headerElement.classList.toggle("green");
    headerElement.classList.toggle("red");
    });
