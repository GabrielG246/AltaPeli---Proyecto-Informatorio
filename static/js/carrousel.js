var timer = 4000;
var i = 0;
var sliderItems = document.querySelectorAll('#slider__container > li');
var max = sliderItems.length;

sliderItems[i].classList.add('active');
sliderItems[i].style.left = '0';
sliderItems[i + 1].classList.add('active');
sliderItems[i + 1].style.left = '25%';
sliderItems[i + 2].classList.add('active');
sliderItems[i + 2].style.left = '50%';
sliderItems[i + 3].classList.add('active');
sliderItems[i + 3].style.left = '75%';

setInterval(function () {
    sliderItems.forEach(item => item.classList.remove('active'));

    sliderItems[i].style.transitionDelay = '0.25s';
    sliderItems[i + 1].style.transitionDelay = '0.5s';
    sliderItems[i + 2].style.transitionDelay = '0.75s';
    sliderItems[i + 3].style.transitionDelay = '1s';

    if (i < max - 4) {
        i = i + 4;
    } else {
        i = 0;
    }

    sliderItems[i].style.left = '0';
    sliderItems[i].classList.add('active');
    sliderItems[i].style.transitionDelay = '1.25s';

    sliderItems[i + 1].style.left = '25%';
    sliderItems[i + 1].classList.add('active');
    sliderItems[i + 1].style.transitionDelay = '1.5s';

    sliderItems[i + 2].style.left = '50%';
    sliderItems[i + 2].classList.add('active');
    sliderItems[i + 2].style.transitionDelay = '1.75s';

    sliderItems[i + 3].style.left = '75%';
    sliderItems[i + 3].classList.add('active');
    sliderItems[i + 3].style.transitionDelay = '2s';

}, timer);
