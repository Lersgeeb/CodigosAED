function Word(){

    this.generate = WordGenerate;
}

    function WordGenerate(){
        
        var myRandom = new Random();
        //var letters = "abcdefghijklmnopqrstuvwxyz";
        var vocal = "aeiou"
        var consonant = "bcdfghjklmnpqrstvwxyz";
        var myWord = [];
        var r = myRandom.int(10,4);

        for(var i=0; i<r/2; i++){
            myWord.push(consonant[myRandom.int(consonant.length - 1,0)]);
            myWord.push(vocal[myRandom.int(vocal.length - 1,0)]);
        }

        return myWord.join("");
        
        
        
    }