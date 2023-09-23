$(document).ready(function () {

    fetch("/disable_days", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        }
    })
        .then((response) => response.json())
        .then((dates) => {
            disableDays = []
            disableDays.push(...dates);

            flatpickr("#days", {
                mode: "range",
                minDate: "today",
                disable: disableDays,
                locale: $("#locale").val(),
                dateFormat: $("#dateFormat").val()
            });

        })
        .catch((error) => {
            console.error(error);
        });

    $("#languages").change(function () {
        fetch("/", {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
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

    $("#calender").click(function () {
        $("#days").click();
    });

});