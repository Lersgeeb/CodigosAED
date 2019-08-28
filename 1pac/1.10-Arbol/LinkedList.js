//Linked List Jerarquizado de menor a mayor

function Node(value){
    this.value = value;
    this.next = null;
    this.children = null;
}

function LinkedList(){
    this.first = null;

    this.add = LinkedListAdd;
    this.getLength = LinkedListGetLength;
    this.atPosition = LinkedListAtPosition;

}

    function LinkedListAdd(value){

        if(!this.first){
            this.first = new Node(value);
            return true;
        }
        else{
            //si el primero es mayor
            var c = new Compare();
            current = this.first;

            if(c.compare(value,current.value) < 0){
                this.first = new Node(value);
                this.first.next = current;
                return true;
            }
            else if(c.compare(value,current.value) == 0){
                this.first = new Node(value);
                this.first.next = current.next;
                return true;
            }
            else{
                    while(current.next){
                        previous = current;
                        current = current.next;
                        if(c.compare(value,current.value) < 0){
                            previous.next = new Node(value);
                            previous.next.next = current;
                            return true;
                        }
                        else if(c.compare(value,current.value) == 0){
                            previous.next = new Node(value);
                            previous.next.next = current.next;
                            return true;
                        }
                    }           
                    current.next = new Node(value);
                    return true;
            }
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