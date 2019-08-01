//Linked List Jerarquizado de menor a mayor

function Node(value){
    this.value = value;
    this.next = null;
    this.children = null;
}

function LinkedList(){
    this.first = null;

    this.add = LinkedListAdd;

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