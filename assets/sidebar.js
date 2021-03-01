var verticalOffset = 56;

window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (verticalOffset < currentScrollPos) {
      document.getElementById("sidebar").style.paddingBottom = "2rem";
  } else {
      document.getElementById("sidebar").style.paddingBottom = "calc(2rem + 56px)";
  }
} 