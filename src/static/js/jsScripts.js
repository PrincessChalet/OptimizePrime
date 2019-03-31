function hideShow() {
    var el = document.getElementById("test");

    if(el.style.display === "none") {
        el.style.display = "block";
    }
    else {
        el.style.display = "none";
    }
}