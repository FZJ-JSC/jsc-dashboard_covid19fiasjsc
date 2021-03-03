window.onscroll = function() {
  let navbarHeight = document.getElementById("navbar").scrollHeight;
  let currentScrollPos = window.pageYOffset;
  if (navbarHeight < currentScrollPos) {
      document.getElementById("sidebar").style.paddingBottom = "2rem";
  } else {
      document.getElementById("sidebar").style.paddingBottom = "calc(2rem + 56px)";
  }
} 