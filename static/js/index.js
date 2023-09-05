$(document).ready(function () {

    width = $(window).width();
    if (width <= 425) {
        document.documentElement.style.setProperty("--scale", width / 250);
    } else if (425 < width && width <= 768) {
        document.documentElement.style.setProperty("--scale", width / 250 - 2);
    } else if (768 < width && width <= 1024) {
        document.documentElement.style.setProperty("--scale", width / 250 - 2.5);
    } else if (1024 < width && width <= 1440) {
        document.documentElement.style.setProperty("--scale", width / 250 - 3.5);
    }

    setTimeout(function() {
        $("main").css({"display": "block"})
    }, 1000);

    $("select").change(function () {
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

    $("#book").click(function () {
        window.location.href = "/book"
    });

    $("#carousel").slick({
        arrows: false,
        infinite: true,
        autoplay: true,
        slidesToShow: 2,
        slidesToScroll: 2,
        autoplaySpeed: 3000
    });
});