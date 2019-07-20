function Topic(){

    this.generate = TopicGenerate;
}

    function TopicGenerate(){
        var p =  new Paragraphs();
        var t = new Title();

        return `${t.generate()}${p.generate()}`;
    }