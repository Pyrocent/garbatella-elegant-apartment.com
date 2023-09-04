$(document).ready(function () {

    screen = $(window).width();
    if (screen <= 425) {
        document.documentElement.style.setProperty("--scale", screen / 250);
    } else if (425 < screen && screen <= 768) {
        document.documentElement.style.setProperty("--scale", screen / 250 - 2);
    } else if (768 < screen && screen <= 1024) {
        document.documentElement.style.setProperty("--scale", screen / 250 - 2.5);
    } else if (1024 < screen && screen <= 1440) {
        document.documentElement.style.setProperty("--scale", screen / 250 - 3.5);
    }

    $("#carousel").slick({
        arrows: false,
        infinite: true,
        autoplay: true,
        autoplaySpeed: 3000,
        slidesToShow: 2,
        slidesToScroll: 2
    });

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
});