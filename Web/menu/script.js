const hamburger = document.querySelector(".hamburger");
const navLink = document.querySelector(".nav__link");

hamburger.addEventListener("click", () => {
  navLink.classList.toggle("hide");
});

/*
Call a function when a button is clicked:
 <button onclick="myFunction()">Click me</button>

 Call a function when a user changes the 
 selected option of a <select> element:
  <select onchange="myFunction()"> 

  Call a function when a form is submitted:
    <form onsubmit="myFunction()">
        Enter name: <input type="text">
        <input type="submit">
    </form> 
*/
