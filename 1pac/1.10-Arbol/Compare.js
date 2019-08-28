function Compare(){

    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    this.compare = CompareCompare;
    this.greaterLength = CompareGreaterLength;
    this.lesserLength = CompareLesserLength;

    
}


    function CompareGreaterLength(str1, str2){
        var g = str1.length;
        if(str2.length > g) g = str2.length;

        return g;
    }

    function CompareLesserLength(str1, str2){
        var l = str1.length;
        if(str2.length < l) l = str2.length;

        return l;
    }

    function CompareCompare(object1, object2){
        
        //object 1
        if(typeof object1 == "number"){
            num1 = object1
            object1 = `${object1}`.trim();
        }
        if(typeof object1 == "object")
            object1 = `${object1.name}`.trim();
            
        
        //object 2
        if(typeof object2 == "number"){
            num2 = object2
            object2 = `${object2}`.trim();
        }

        if(typeof object2 == "object")
            object2 = `${object2.name}`.trim();

        
        if(typeof num1 == "number" && typeof num2 == "number"){
            if(num1<num2)
                return -1
            else if(num1>num2)
                return 1
            else
                return 0
        }

        var lesser = this.lesserLength(object1,object2);
        for(var i = 0; i<lesser; i++){
            if(alphabet.indexOf(object1[i]) > alphabet.indexOf(object2[i]))
                return 1;

            else if(alphabet.indexOf(object1[i]) < alphabet.indexOf(object2[i]))
                return -1;
        
        }

        if(lesser == this.greaterLength(object1,object2))
            return 0;

        else if(object1.length == lesser)
            return -1;

        else
            return 1;
        
    }