function Random(){

    this.int=RandomInt;
}
    function RandomInt(max = 100, min = 0){

        var myRandomInt = Math.floor(Math.random() * (max - min) + min);
        return myRandomInt; 
    }