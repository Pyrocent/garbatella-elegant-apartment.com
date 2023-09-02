const flags = document.getElementsByClassName("flag");

Array.from(flags).forEach(flag => {
    flag.addEventListener("click", function () {
        fetch("/", {
            method: "POST",
            headers: {"Content-Type": "application/x-www-form-urlencoded"},
            body: `lang=${this.getAttribute('id')}`,
        })
        .then(response => response.text())
        .then(html => {document.documentElement.innerHTML = html;})
        .catch(error => {console.error("Error:", error);});
    });
});