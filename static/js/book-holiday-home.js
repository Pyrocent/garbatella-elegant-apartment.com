$(document).ready(function () {

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

    var currentDate = new Date();
    var tomorrowDate = new Date(currentDate);
    tomorrowDate.setDate(currentDate.getDate() + 1);
    var formattedDate = tomorrowDate.getFullYear() + "-" + (tomorrowDate.getMonth() + 1) + "-" + tomorrowDate.getDate();

    flatpickr("#date-01", {
        disable: [],
        minDate: formattedDate,
        plugins: [new rangePlugin({input: "#date-02"})]
    });
    flatpickr("#date-02", {
        disable: [],
        minDate: formattedDate
    });
});