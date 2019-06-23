function Node(value){
    this.next = null;
    this.value = value;
}

function LinkedList(first){
    this.first= first;

    this.add = LinkedListAdd;
    this.print = LinkedListPrint;
    this.printR = LinkedListPrintR;
}
    function LinkedListPrint(){
        myLinkedList = new LinkedList(this.first);
        myLinkedList.printR(myLinkedList);
    }
    function LinkedListPrintR(myLinkedList){
        current = myLinkedList.first;
        if(!current.next){
            console.log(current.value);
        }
        else{
            console.log(current.value);
            current = current.next;
            myLinkedList.printR(new LinkedList(current));
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
