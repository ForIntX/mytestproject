document.getElementById("close-button").addEventListener("click",closeWarning);



function closeWarning(e) {
    e.preventDefault()
    warnings = document.querySelector(".alert-div")
    warnings.remove()
}