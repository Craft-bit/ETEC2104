// dictionary. key = rank, suit, angle
let cards = {};

function main()
{
    let suits = "cshd";
    let angles = [0, 90, 180, 270];

    for(let rank = 2; rank <= 14; rank++)
    {
        for(let si = 0; si < 4; ++si)
        {
            let suit = suits[si];
            angles.forEach( (angle) => {
                let filename = "../static/Images/" + rank + suit + " " + angle + ".svg";
                let key = rank + suit + angle;
                let img = new Image();
                img.onload = () => {
                    cards[key] = img;
                    console.log("LOADED:", key);
                };
                img.src = filename;
            });
        }
    }
}