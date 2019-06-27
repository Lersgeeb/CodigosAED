function Node(value){
    this.next = null;
    this.value = value;
}

function LinkedList(first){
    this.first= first;

    this.add = LinkedListAdd;
    this.print = LinkedListPrint;
    this.printReverse = LinkedListPrintReverse;
    this.printList = LinkedListPrintList;
  //  this.printR = LinkedListPrintR;
}
    /*
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
    }*/
    function LinkedListPrint(current=this.first){
        if(current.next){
            console.log(current.value);
            this.print(current.next);
        }
        else{
            console.log(current.value);
        }
    }
 /*
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
    }*/
    function LinkedListAdd(value, current=null){
        if(!this.first){
            this.first=new Node(value);
            return true;
        }
        else{
            if(!current)
                current=this.first;
            if(current.next)
                this.add(value,current.next);
            else{
                current.next=new Node(value);
                return true;
            }
        }
    }
    
    function LinkedListPrintReverse(head = this.first){
        if(head.next){
            queue=head.next;
            this.printReverse(queue);
            console.log(head.value);
        }
        else{
            console.log(head.value);
        }
    }

    function LinkedListPrintList(current = this.first, trail = null){
        if(trail==null)
            trail = "[ " + this.first.value;
        if(current.next){
            current = current.next;
            trail = trail + " , " + current.value;
            this.printList(current,trail); 
        }
        else{
            trail = trail + " ]";
            console.log(trail);
        }        
            

    }
