$(document).ready(function () {
    $("select").change(function () {
        fetch("/", {
            method: "POST",
            headers: {"Content-Type": "application/x-www-form-urlencoded"},
            body: `lang=${$(this).val().substring(0, 2).toLowerCase()}`,
        })
        .then(response => response.text())
        .then(html => {document.documentElement.innerHTML = html;})
        .catch(error => {console.error("Error:", error);});
    });
});