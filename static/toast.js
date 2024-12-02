function showToast() {
    var toast = document.getElementById("toast");
    toast.style.visibility = "visible";
    setTimeout(function(){ toast.style.visibility = "hidden"; }, 3000);
}
