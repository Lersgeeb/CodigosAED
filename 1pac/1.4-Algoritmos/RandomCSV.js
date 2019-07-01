function RandomCSV(){

    this.generate = RandomCSVGenerate;
}

    function RandomCSVGenerate(){
        r=Random2Int(10,20);
        c=Random2Int(10,20);
        columb = [];
        row = [];


        for(j=0;j<c;j++){
            
            for(i=0;i<r;i++){
                columb.push(Random2Int());    
            }
            row.push(columb);
        }

        return row;
    }