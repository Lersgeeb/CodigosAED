function Sentence(){
    
    this.generate = SentenceGenerate;
}

    function SentenceGenerate(){
        var myRandom = new Random();
        var myWord = new Word();
        var words = [];
        var r = myRandom.int(12,7);
        for(var i=0;i<r;i++){
            if(i==0){
                FirstWord = myWord.generate();
                FirstWord = `${FirstWord[0].toUpperCase()}${FirstWord.slice(1,FirstWord.length-1)}`;
                words.push(FirstWord);  
            }
            else{
                words.push(myWord.generate());
            }
        }

        return `${words.join(" ")}.`;
    }