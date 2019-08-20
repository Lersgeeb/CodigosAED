function Node(value){
    this.value = value;
    this.next = null;

    this.addNext = NodeAddNext;
    
}
    function NodeAddNext(node){
        this.next=node;
    }

   

function LinkedList(){

    this.first=null;

    this.add = LinkedListAdd;
    this.print = LinkedListPrint;
    this.addInposition = LinkedListAddInposition;
    this.getFirst = LinkedListGetFirst;
    this.getLast = LinkedListGetLast;
    this.removeForValue = LinkedListRemoveForValue;
    this.removeForPosition = LinkedListRemoveForPosition;
    this.getLength = LinkedListGetLength;
    this.atPosition = LinkedListAtPosition
     
}
    function LinkedListRemoveForValue(valueToRmv){
      
        current=this.first;
        if(current.value==valueToRmv){
            this.first=current.next;
            return true;
        }
        while(current.next){
            before=current;
            current=current.next;
            if(current.value==valueToRmv){
                before.next=current.next;
                return true;
            }
        }
        return false;        
    }

    function LinkedListRemoveForPosition(n){
        if(n==0){
           this.first=this.first.next; 
           return true;
        }
        else{
            count=0;
            current=this.first;
            while(current.next){
                before=current;
                current=current.next;
                count++;
                if(n==count){
                    before.next=current.next;
                    return true;
                }
            }
            
            return false;
        }
    }

    function LinkedListAdd(value){
        if(!this.first){
            this.first = new Node(value);
           
        }
        else{
            currentNode = this.first;
            while(currentNode.next){
                currentNode=currentNode.next;
            }
            currentNode.next = new Node(value);
            
        }
    
    }
    
    function LinkedListPrint(){
        if(!this.first){
            console.log("NO EXISTE LISTA A IMPRIMIR");
        }
        else{
            currentNode = this.first;
            while(currentNode.next){
                console.log(currentNode.value);
                currentNode=currentNode.next;
            }
            console.log(currentNode.value);
            
        }

    }

    function LinkedListAddInposition(value,n){
        if(n==0){
            queqe = this.first;
            this.first = new Node(value);
            this.first.next=queqe;
            return true;
        }
        else if(n>0){
            count=0;
            currentPosition = this.first;
            while(currentPosition.next){
                beforePosition = currentPosition;
                currentPosition = currentPosition.next;
                count++;
                if(n==count){
                    beforePosition.next = new Node(value);
                    beforePosition.next.next=currentPosition;
                    return true;
                }
            }
            count++;
            if(n==count){
                currentPosition.next = new Node(value);
                return true;
            }
            console.log("No se encontro la posicion en la lista")
            return false;
        }
        else{
            return false;
        }

    }

    function LinkedListGetFirst(){
        return this.first.value;
    }

    function LinkedListGetLast(){
        if(!this.first){
            return false;
        }
        else{
            currentNode = this.first;
            while(currentNode.next){
                currentNode=currentNode.next;
            }
            return currentNode.value;
            
        }

    }
    function LinkedListGetLength(){
        current = this.first;
        length = 0;
    
        while(current.next){
            length++;
            current = current.next;
        }
        length++;
    
        return length;
    }
    
    function LinkedListAtPosition(position){
        currentNode = this.first;
        currentPosition = 0;
        
        if(position > this.getLength()){
            return null;
        }
        else{
            while(currentNode.next){
                if(currentPosition == position){
                    return currentNode;
                }
                else{
                    currentPosition++;
                    currentNode = currentNode.next;
                }
            }
            if(currentPosition == position){
                return currentNode;
            }
        }
    
    }