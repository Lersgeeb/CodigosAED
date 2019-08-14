function makeBlankArray(n){
    h = 2*n - 1;
    w = h;
    matrix = [];
    for(var i=0;i<h;i++){
        row = [];
        for(var j=0;j<w;j++){
            row.push("&nbsp");
        }
        matrix.push(row);
    }
    return matrix;
}

function drawTree(arr = []){
    h = arr.length;
    w = h;
    n = (h+1)/2
    half = Math.floor(w/2)

    arr[0][half] = "*"; //genera la punta

    for(var i=n;i<h;i++){   //genera el tallo
        arr[i][half] = "*";
    }
    
    count = 1;              //genera las ramas
    for(var i=1;i<n;i++){   
        for(var j=half-count;j<=half+count;j++){
            if(j!=half)
                arr[i][j] = "*";
        }
        count++;
    }
}

function arrayToHTMLTableStr(myArray = []){
    stringHtml = "<table border='5'>";

    for(i=0;i<myArray.length;i++){
        stringHtml += `<tr><td>${myArray[i].join("</td><td>")}</td></tr>`;
    }
    stringHtml += "</table>";
    return stringHtml;
}

function makeTableOfTreeOfAsterisk(n){

var arr = makeBlankArray(n);
drawTree(arr);
table = arrayToHTMLTableStr(arr);
document.write(table)
}