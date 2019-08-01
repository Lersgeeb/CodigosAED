function RandomCSV(){

    this.generate = RandomCSVGenerate;
}

    function RandomCSVGenerate(){
        r=Random2Int(10,20);
        c=Random2Int(10,20);
        c=10;
        row = [];
        
        for(j=0;j<r;j++){
            columns = [];

            for(i=0;i<c;i++){
                columns.push(Random2Int());    
            }
            row.push(columns.join(","));              
        }

        return row.join("\n");
    }