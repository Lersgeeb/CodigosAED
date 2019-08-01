function Title(){

    this.generate = TitleGenerate;
}

    function TitleGenerate(){
        var s = new Sentence();
        var myTitle = s.generate();
        
        return `${"-".repeat(20)}${myTitle.slice(0,myTitle.length - 2)}${"-".repeat(20)}\n\n`;
    //
    }//