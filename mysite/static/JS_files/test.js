

let L = [   
    ["Product", "Cost"],
    ["CPU",     "$100"],
    ["Memory",  "$75"],
    ["SSD",     "$80"]
];
// Create table element
let tbl = document.createElement("table");
// Go through list
for(let i = 0; i < L.length; ++i){
    // Row element
    let row = L[i];
    let tr = document.createElement("tr");
    tbl.appendChild(tr); // append to table
    for(let j = 0; j < row.length; ++j){
        // Column element
        let td = document.createElement("td");
        tr.appendChild(td);
        let txt = document.createTextNode( row[j] );
        td.appendChild( txt );
    }
}
document.body.appendChild(tbl);