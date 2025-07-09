// static/js/fancybox-init.js
document.addEventListener("DOMContentLoaded", () => {
  if (window.Fancybox) {
    Fancybox.bind("[data-fancybox]", {
      Thumbs: { autoStart: true },
      Toolbar: {
        display: ["zoom", "thumbs", "close", "prev", "next"]
      },
      Carousel: {
        infinite: true
      }
    });
  }
});
