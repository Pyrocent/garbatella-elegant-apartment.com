$(document).ready(function () {

    $("#name").click(function () {
        window.location.reload();
    });

    $("#languages").change(function () {
        fetch("/", {
            method: "POST",
            headers: {"Content-Type": "application/x-www-form-urlencoded"},
            body: `lang=${$(this).val()}`,
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
        slidesToShow: 1,
        slidesToScroll: 1,
        asNavFor: "#slider-nav",
        prevArrow: "<button class = slick-prev><</button>",
        nextArrow: "<button class = slick-next>></button>"
    });

    $("#slider-nav").slick({
        arrows: false,
        autoplay: true,
        slidesToShow: 3,
        touchMove: false,
        slidesToScroll: 1,
        mobileFirst: true,
        focusOnSelect: true,
        pauseOnHover: false,
        pauseOnFocus: false,
        autoplaySpeed: 3000,
        asNavFor: "#slider-for",
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    vertical: true,
              }
            }
        ]
    });

    $(".tab-button").click(function() {
        $(".tab-content").removeClass("active");
        $(".tab-button").removeClass("active");
        var $this = $(this);
        $this.addClass("active");
        $("#" + $this.data("tab")).addClass("active");
    });

});