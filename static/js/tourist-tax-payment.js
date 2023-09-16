$(document).ready(function () {

    $("#name").click(function () {
        window.location.href = "/"
    });

    $("#languages").change(function () {
        fetch("/tourist-tax-payment", {
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

    $(".copy").click(function () {
        var $this = $(this);
        navigator.clipboard.writeText($this.find("p").text());
        $this.find("img").attr("src", "static/assets/icons/checkmark.png");
        setTimeout(function () {
            $this.find("img").attr("src", "static/assets/icons/copy.png");
        }, 1000);
    });

    $("#paypal").click(function () {
        window.location.href = "https://www.paypal.me/"
    });

});