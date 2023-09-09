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

    $("#for").slick({
        fade: true,
        arrows: false,
        slidesToShow: 1,
        asNavFor: "#nav",
        slidesToScroll: 1
    });

    $("#nav").slick({
        arrows: false,
        autoplay: true,
        vertical: true,
        slidesToShow: 3,
        asNavFor: "#for",
        slidesToScroll: 1,
        focusOnSelect: true,
        pauseOnHover: false,
        pauseOnFocus: false,
        autoplaySpeed: 3000,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    vertical: false
                }
            }
        ]
    });
});