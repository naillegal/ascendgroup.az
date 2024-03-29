// home-first-slider
var swiper = new Swiper("#home-first-slider .mySwiper", {
  loop: true,
  pagination: {
    el: "#home-first-slider .swiper-pagination",
    clickable: true,
  },
  autoplay: {
    delay: 4000,
    disableOnInteraction: false,
  },
});

swiper.on("paginationClick", function (swiper, event) {
  var clickedBulletIndex = Array.from(swiper.pagination.bullets).indexOf(
    event.target
  );
  swiper.slideTo(clickedBulletIndex);
});

// home-products
var swiper = new Swiper("#home-products .mySwiper", {
  loop: true,
  slidesPerView: 2,
  navigation: {
    nextEl: "#home-products .button-next",
    prevEl: "#home-products .button-prev",
  },
  breakpoints: {
    992: {
      slidesPerView: 3,
    },
  },
});

// home-selected-projects
var swiper = new Swiper("#home-selected-projects .mySwiper", {
  slidesPerView: 2,
  loop: true,
  pagination: {
    el: "#home-selected-projects .swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: "#home-selected-projects .button-next",
    prevEl: "#home-selected-projects .button-prev",
  },
  breakpoints: {
    576: {
      slidesPerView: 2,
    },
    768: {
      slidesPerView: 3,
    },
    1200: {
      slidesPerView: 5,
    },
  },
});

// home-featured-reels
var swiper = new Swiper("#home-featured-reels .mySwiper", {
  loop: true,
  slidesPerView: 1,
  navigation: {
    nextEl: "#home-featured-reels .button-next",
    prevEl: "#home-featured-reels .button-prev",
  },
  breakpoints: {
    576: {
      slidesPerView: 2,
    },
    1200: {
      slidesPerView: 3,
    },
  },
});

const videos = document.querySelectorAll("video");
const playPauseBtns = document.querySelectorAll(".play-pause-btn");

videos.forEach((video) => {
  video.addEventListener("dblclick", toggleFullScreen);
  video.addEventListener("play", handleVideoStateChange);
  video.addEventListener("pause", handleVideoStateChange);
});

playPauseBtns.forEach((playPauseBtn) => {
  playPauseBtn.addEventListener("click", togglePlayPause);
});

swiper.on("slideChange", handleSlideChange);

function toggleFullScreen() {
  const video = this;
  if (!document.fullscreenElement) {
    if (video.requestFullscreen) {
      video.requestFullscreen();
    } else if (video.mozRequestFullScreen) {
      /* Firefox */
      video.mozRequestFullScreen();
    } else if (video.webkitRequestFullscreen) {
      /* Chrome, Safari ve Opera */
      video.webkitRequestFullscreen();
    } else if (video.msRequestFullscreen) {
      /* Internet Explorer ve Edge */
      video.msRequestFullscreen();
    }
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    } else if (document.mozCancelFullScreen) {
      /* Firefox */
      document.mozCancelFullScreen();
    } else if (document.webkitExitFullscreen) {
      /* Chrome, Safari ve Opera */
      document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) {
      /* Internet Explorer ve Edge */
      document.msExitFullscreen();
    }
  }
}

function togglePlayPause() {
  const video = this.parentElement.querySelector("video");
  if (video.paused) {
    video.play();
  } else {
    video.pause();
  }
}

function handleVideoStateChange() {
  const playPauseBtn = this.parentElement.querySelector(".play-pause-btn");
  const playIcon = playPauseBtn.querySelector(".fa-play");
  const pauseIcon = playPauseBtn.querySelector(".fa-pause");

  if (this.paused) {
    playIcon.style.display = "inline-block";
    pauseIcon.style.display = "none";
  } else {
    playIcon.style.display = "none";
    pauseIcon.style.display = "inline-block";
  }
}

function handleSlideChange() {
  videos.forEach((video) => {
    video.pause();
    const playPauseBtn = video.parentElement.querySelector(".play-pause-btn");
    const playIcon = playPauseBtn.querySelector(".fa-play");
    const pauseIcon = playPauseBtn.querySelector(".fa-pause");
    playIcon.style.display = "inline-block";
    pauseIcon.style.display = "none";
  });
}

// home-partners
var swiper = new Swiper("#home-partners .mySwiper", {
  slidesPerView: 2,
  loop: true,
  pagination: {
    el: "#home-partners .swiper-pagination",
    clickable: true,
  },
  breakpoints: {
    576: {
      slidesPerView: 3,
    },
    992: {
      slidesPerView: 5,
    },
  },
});

// home-statistics
function animateCounters() {
  let valueDisplays = document.querySelectorAll("#home-statistics .count");
  let interval = 1400;

  valueDisplays.forEach((valueDisplay) => {
    let startValue = 0;
    let endValue = parseInt(valueDisplay.getAttribute("data-val"));
    let duration = Math.floor(interval / endValue);
    let counter = setInterval(function () {
      startValue += 1;
      valueDisplay.textContent = startValue;
      if (startValue == endValue) {
        clearInterval(counter);
      }
    }, duration);
  });
}

function isCountersInViewport() {
  let valueDisplays = document.querySelectorAll("#home-statistics .count");
  for (let valueDisplay of valueDisplays) {
    let rect = valueDisplay.getBoundingClientRect();
    if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
      return true;
    }
  }
  return false;
}

window.addEventListener("load", function () {
  if (isCountersInViewport()) {
    animateCounters();
  }
});

let animationStarted = false;

window.addEventListener("scroll", function () {
  let currentScrollPos =
    window.pageYOffset || document.documentElement.scrollTop;
  if (
    !animationStarted &&
    isCountersInViewport() &&
    currentScrollPos > lastScrollTop
  ) {
    animateCounters();
    animationStarted = true;
  }
  lastScrollTop = currentScrollPos <= 0 ? 0 : currentScrollPos;
});

window.addEventListener("DOMContentLoaded", function (event) {
  animateCounters();
});

//layout.js
const closeBtn = document.getElementById("menuClose");
const menuBtn = document.getElementById("menuIcon");
const menu = document.getElementById("menu");
const bottom_overlay = document.getElementById("bottom-overlay");
const body = document.body;

menuBtn.addEventListener("click", function () {
  menu.classList.add("active");
  bottom_overlay.classList.add("active");
  body.style.overflow = "hidden";
});

closeBtn.addEventListener("click", function () {
  menu.classList.remove("active");
  bottom_overlay.classList.remove("active");
  body.style.overflow = "auto";
});

function toggleList(listId) {
  var list = document.getElementById(listId);

  if (!list.classList.contains("open")) {
    list.classList.add("open");
    list.style.maxHeight = list.scrollHeight + "px";
  } else {
    list.classList.remove("open");
    list.style.maxHeight = "0";
  }
}

window.addEventListener("scroll", function () {
  var header = document.getElementById("header");

  if (window.scrollY > 100) {
    header.classList.add("scrolled");
  } else {
    header.classList.remove("scrolled");
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const menuClose = document.getElementById("menuClose");
  const bottomOverlay = document.getElementById("bottom-overlay");
  const sideMenu = document.getElementById("menu");

  menuClose.addEventListener("click", function () {
    body.style.overflow = "auto";
  });

  bottomOverlay.addEventListener("click", function () {
    sideMenu.classList.remove("active");
    bottomOverlay.classList.remove("active");
    body.style.overflow = "auto";
  });
});


// copyright year
var date = new Date();
var year = date.getFullYear();
var copyrightcontent = "© " + year + " All rights reserved";
document.getElementById("copyright").innerHTML = copyrightcontent;

// products-slider
var swiper = new Swiper("#laminate-slider .mySwiper", {
  loop: true,
  pagination: {
    el: "#laminate-slider .swiper-pagination",
    clickable: true,
  },
  autoplay: {
    delay: 4000,
    disableOnInteraction: false,
  },
});

swiper.on("paginationClick", function (swiper, event) {
  var clickedBulletIndex = Array.from(swiper.pagination.bullets).indexOf(
    event.target
  );
  swiper.slideTo(clickedBulletIndex);
});
