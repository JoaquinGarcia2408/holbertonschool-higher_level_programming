var redElement = document.getElementById("red_header");
redElement.addEventListener("click", function() {
    var headerElement = document.querySelector("header");
    headerElement.classList.add("red");
});