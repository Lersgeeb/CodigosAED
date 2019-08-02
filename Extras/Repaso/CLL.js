function Node(value){
    this.value = value;
    this.next = null;
}

function CLL(){
    this.first = null;

    this.add = CLLAdd;
    this.print = CLLPrint;
}

    function CLLAdd(value){
        if(!this.first){
            this.first = new Node(value);
            this.first.next = this.first;
        }
        else{
            current = this.first;
            while(current.next != this.first){
                current = current.next;
            }
            current.next = new Node(value);
            current.next.next = this.first;
        }
    }
    
    function CLLPrint(){
        
        if(!this.first){
                console.log("N.A");
        }
        else{
            current = this.first;
            while(current.next != this.first){
                console.log(`\n\nValor nodo actual: ${current.value}\nValor nodo Siguiente: ${current.next.value}\n\n`);
                current = current.next;

            }
            console.log(`\n\nValor nodo actual: ${current.value}\nValor nodo Siguiente: ${current.next.value}\n\n`);
        }
    }