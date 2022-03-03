function myCanvas() {
    let cvs = document.getElementById("headCanvas");
    cvs.width = window.innerWidth;
    cvs.height = 100;

    let ctx = cvs.getContext("2d");
    ctx.fillStyle = "white";
    ctx.beginPath();
    ctx.rect(0, 0, cvs.width, cvs.height);
    ctx.fill();
}
myCanvas();