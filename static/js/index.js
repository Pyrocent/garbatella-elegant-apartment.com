$(document).ready(function () {

    $("#languages").change(function () {
        fetch("/", {
            method: "POST",
            headers: {"Content-Type": "application/x-www-form-urlencoded"},
            body: `lang=${$(this).val().substring(0, 2).toLowerCase()}`,
        })
        .then(response => {
            if (response.status === 200) {
                window.location.reload();
            }
        })
        .catch(error => {
            console.error(error);
        });
    });

    $(".book").click(function () {
        window.location.href = "/book-holiday-home"
    });

    $("#slider-for").slick({
        fade: true,
        arrows: false,
        slidesToShow: 1,
        slidesToScroll: 1,
        asNavFor: "#slider-nav"
    });

    $("#slider-nav").slick({
        arrows: false,
        autoplay: true,
        vertical: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        focusOnSelect: true,
        pauseOnHover: false,
        pauseOnFocus: false,
        autoplaySpeed: 3000,
        asNavFor: "#slider-for",
        responsive: [{
            breakpoint: 768,
            settings: {
                vertical: false
            }
        }]
    });
});