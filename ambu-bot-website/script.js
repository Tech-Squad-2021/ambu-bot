var navLinks = document.getElementById("navLinks");

function showMenu(){
    navLinks.style.right = "0";
}


function hideMenu(){
    navLinks.style.right = "-200px";
}


var counter = document.querySelector(".counter");




fetch("AIzaSyAJ16M03Q0vdQZq9LxOSmfErmai-MgcOKk")
    .then(res => res.json)
    .then(data => console.log(data))

