function Heap(){
    this.build = HeapBuild;
    this.printHeap = HeapPrintHeap;
}
    function HeapBuild(list){
        n = list.getLength();
        h = Math.ceil( Math.log2( n + 1) );
        mi = Math.pow(2, h-1) - 1;
        mf = mi * 2 ;
        w = mf + 1;

        console.log(list)
        console.log("n: " + n )
        console.log("h: " + h )
        console.log("mi: " + mi )
        console.log("mf: " + mf )
        console.log("w: " + w )
        
        matrix = [];
        for(var i=0;i<h;i++){
            row = [];
            for(var j=0;j<w;j++){
                row.push("&nbsp&nbsp&nbsp&nbsp");
            }
            matrix.push(row);
        }
        
        half = Math.floor(w/2);
        count = 0;
        matrix[0][half] = list.atPosition(count).value; //Primera fila
        count++;
        
        for(var i=1;i<h;i++){
            for(var j=0;j<w;j++){
                if(j == 0){
                    bp = Math.pow(2, h-i) - 1 ; //BlankSpace
                    bsi = Math.floor(bp/2); //BlankSpaceInit
                    j += bsi;
                    matrix[i][j] = list.atPosition(count).value;
                    count++;
                }
                else if(j + bp < w && count<n){
                    j += bp;
                    matrix[i][j] = list.atPosition(count).value;
                    count++;
                }
            }
        }
        this.printHeap(matrix);
    }

    function HeapPrintHeap(myArray = []){
        stringHtml = "<table border='5'>";

        for(i=0;i<myArray.length;i++){
            stringHtml += `<tr><td>${myArray[i].join("</td><td>")}</td></tr>`;
        }
        stringHtml += "</table>";

        document.write(stringHtml);
    }
