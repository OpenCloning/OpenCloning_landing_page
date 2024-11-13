// Preloader js


window.addEventListener('load', function () {

    // Initialize slider
    const sliders = document.querySelectorAll('.slow-slider');

    sliders.forEach(slider => {
        // Initialize each slider with options
        $(slider).slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            autoplay: false,
            autoplaySpeed: 15000,
            dots: true,
            arrows: true
        });
    });

    // After this, make the slick-dots button 
    // restart gifs on click
    $('.slick-dots li button').on('click', function () {
        console.log('clicked');
        // Find all gif images in the parent slick-slider
        const gifs = $(this).closest('.slick-slider').find('img.img-fluid');
        // Restart the gifs
        gifs.each(function () {
            const gif = $(this);
            console.log('restarting gif', gif);
            // Force gif reload by updating src
            const src = gif.attr('src');
            gif.attr('src', '').attr('src', src);
        });
    });
});
