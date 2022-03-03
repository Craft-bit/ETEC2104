/* function makeTable()
{
    let L = [
        ["Product", "Cost"],
        ["CPU",     "$100"],
        ["Memory",  "$75"],
        ["SSD",     "$80"]
    ];
    // same as document.createElement("table")
    let tbl = $("<table>");
    for(let i = 0; i < L.length; ++i){
        let row = L[i];
        let tr = $("<tr>");
        for(let j = 0; j < row.length; ++j){
            let td = $("<td>");
            td.append(row[j]);
            tr.append(td);
        }
        tbl.append(tr);
    }
    let container = $("#tablecontainer");
    container.append(tbl);
}
makeTable(); */
