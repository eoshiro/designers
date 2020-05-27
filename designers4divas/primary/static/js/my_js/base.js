// Navbar Scroll
$(window).on('scroll',function(){
if ($(window).scrollTop()){
    $('nav').addClass('scrolled-black');
    $('nav').removeClass('.ttw-base-navbar');
  }
  else
    {
      $('nav').removeClass('scrolled-black');
    }
  })

  // Navbar Stop Scroll at 1000px



  // Unused Hamburger Function

  function hamburgerFunctionBase() {
    var x = document.getElementById("navbar-header-links");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }
