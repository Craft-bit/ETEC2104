function temp() 
{
    let cvs = document.getElementById("myCanvas");
    cvs.width = 512;
    cvs.height = 512;

    let ctx = cvs.getContext("2d");

    // Draw blue line
    ctx.strokeStyle = "blue";
    ctx.beginPath();
    ctx.moveTo(10, 20);
    ctx.lineTo(100, 200);
    ctx.stroke();

    // Draw red rectangle
    ctx.fillStyle = "red";
    ctx.strokeStyle = "yellow";
    ctx.lineWidth = 10;
    ctx.beginPath();
    ctx.rect(50, 70, 100, 20);
    ctx.fill();
    ctx.stroke();

    // Draw image
    var img = new Image();
    img.onload = () => {
        ctx.drawImage(img, 70, 90, 200, 200);
    }
    img.src = "../static/Images/hello_world.png";

    // draw purple ellipse : click
    cvs.addEventListener("click", (ev) => {
        let x = ev.clientX - cvs.offsetLeft;
        let y = ev.clientY - cvs.offsetTop;
        ctx.strokeStyle = "purple";
        ctx.beginPath();
        ctx.ellipse( 
            x, y, 10, 10, 0, 0, 2.0 * Math.PI, true
        );
        ctx.stroke();
        ctx.drawImage(img, x, y, 20, 20);
    })
}

function spriteSheet()
{

}

temp();