function set_padding() {
  let navbarHeight = document.getElementById("navbar").scrollHeight;
  let currentScrollPos = window.pageYOffset;
  if (currentScrollPos > navbarHeight) {
      document.getElementById("sidebar").style.paddingBottom = "calc(2rem - 12px)";
  } else {
      document.getElementById("sidebar").style.paddingBottom = "calc(2rem + 56px - " + currentScrollPos + "px)";
  }
}

window.onscroll = set_padding