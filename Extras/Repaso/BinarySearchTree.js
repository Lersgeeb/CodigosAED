
function BST(){
    this.root = null;

    this.add = BSTAdd;
    this.search = BSTSearch;
    this.remove = BSTRemove; 
    this.addDown = BSTAddDown;
    this.getNode = BSTGetNode;
}
    function BSTAdd(value,current = this.root){
        if(!current){
            this.root = new Node(value);
            return true;
        }
        else{
            if(value>current.value){
                if(!current.rigth){
                    current.rigth = new Node(value);
                    return true;
                }
                else{
                    this.add(value,current.rigth);
                }
            }
            else if(value<current.value){
                if(!current.left){
                    current.left = new Node(value);
                    return true;
                }
                else{
                    this.add(value,current.left);
                }
            }
            else{
                return false;
            }
        }
    }

    function BSTSearch(value,current=this.root){

        if(current){
            if(current.value==value)
                return true;
            else if(value<current.value)
                 return this.search(value,current.left);
            else
                return this.search(value,current.rigth);
        }
        else
            return false; 
    }

    function BSTRemove(value,current = null,prev = null){

        if(!this.root){
            return false;
        }
        else if(current == null){
            current = this.root;
            if(value>current.value && current.rigth){
                return this.remove(value,current.rigth,current);
            }
            else if(value<current.value && current.left){
                return this.remove(value,current.left,current);
            }
            else if(value == current.value){
                
                this.root = null;
                this.addDown(current);
                return true;
            }
            else{
                return false;
            }
        }
        else{
            if(value>current.value && current.rigth){
                return this.remove(value,current.rigth,current);
            }
            else if(value<current.value && current.left){
                return this.remove(value,current.left,current);
            }
            else if(value == current.value){
                
                if(prev.rigth == current){
                    prev.rigth = null;
                }
                else{
                    prev.left = null;
                }
                this.addDown(current);
                return true;
            }
            else{
                return false;
            }
        }
    }

    function BSTAddDown(current){

        if(current.rigth){
            this.add(current.rigth.value);
            myNode = this.getNode(current.rigth.value);
            if(current.rigth.rigth)
                myNode.rigth = current.rigth.rigth;
            if(current.rigth.left)
                myNode.left = current.rigth.left;
        }
        if(current.left){
            this.add(current.left.value);
            myNode = this.getNode(current.left.value);
            if(current.left.rigth)
                myNode.rigth = current.left.rigth;
            if(current.left.left)
                myNode.left = current.left.left;
        }

        return true;

    }

    function BSTGetNode(value,current = this.root){
        if(current){
            if(current.value==value)
                return current;
            else if(value<current.value)
                 return this.getNode(value,current.left);
            else
                return this.getNode(value,current.rigth);
        }
        else
            return false;
    }


