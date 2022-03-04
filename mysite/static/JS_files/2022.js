// dictionary. key = rank, suit, angle
let cards = {};
let numCardsLeftToLoad = 13 * 4 * 4;
let hand = [];

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
                let filename = "../static/cards/" + rank + suit + " " + angle + ".svg";
                let key = rank + suit + angle;
                let img = new Image();
                img.onload = () => {
                    cards[key] = img;
                    console.log("LOADED:", key);
                    numCardsLeftToLoad -= 1;
                    if (numCardsLeftToLoad === 0)
                        doSomething();
                };
                img.src = filename;
            });
        }
    }
}

function doSomething()
{
    let c = cards["2c0"];
    document.body.appendChild(c);
    c.style.position = "absolute";
    c.style.left = "0px";
    c.style.bottom = "0px";
}