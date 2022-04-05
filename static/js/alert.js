function ak() {
    swal({
        title: "Sent Sucessfully!",
        text: "Send Segmented Mails!",
        icon: "success",
        button: "OK",
    })
}
var s = document.getElementById("s").innerHTML;
console.log((s))
if (s == "True") {
    ak();
}