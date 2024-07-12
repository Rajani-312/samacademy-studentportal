//for home - slideshow 
let slideIndex = 0;
window.onload = function() {
    showSlides();
};

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}



document.addEventListener("DOMContentLoaded", function() {
    // Your JavaScript code here
    var currentUrl = window.location.href;

    // Get all the navigation links
    var navLinks = document.querySelectorAll('.navbar a');

    // Iterate through the links and add the 'active2' class to the current page
    for (var i = 0; i < navLinks.length; i++) {
        if (navLinks[i].href === currentUrl) {
            navLinks[i].classList.add('active2');
        }
    }
}); 
    
