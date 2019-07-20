function Paragraphs(){

    this.generate = ParagraphsGenerate;
}

    function ParagraphsGenerate(){
        var myRandom = new Random();
        var myParagraph = new Paragraph();
        var p = [];
        var r = myRandom.int(8,4);
        for(var i=0;i<r;i++){
            p.push(myParagraph.generate())
        }
    return p.join("\n\n");

    }