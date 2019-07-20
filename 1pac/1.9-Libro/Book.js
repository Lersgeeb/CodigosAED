function Book(){

    this.generate = BookGenerate;
}

    function BookGenerate(){
        var myRandom = new Random();
        var myTopic = new Topic();
        var t = [];
        var r = myRandom.int(8,4);
        for(var i=0;i<r;i++){
            t.push(myTopic.generate())
        }
    return t.join("\n\n");

    }