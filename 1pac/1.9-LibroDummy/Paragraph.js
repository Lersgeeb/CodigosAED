function Paragraph(){

    this.generate = ParagraphGenerate;
}

    function ParagraphGenerate(){
        var myRandom = new Random();
        var mySentence = new Sentence();
        Sentences = [];
        var r = myRandom.int(13,7);
        for(var i=0;i<r;i++){
            Sentences.push(mySentence.generate())
        }
    return Sentences.join(" ");

    }