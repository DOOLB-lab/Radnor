window.addEventListener('scroll', function () {
    document.querySelector('.navbar').classList.toggle('scrolled', window.scrollY > 50);
});
