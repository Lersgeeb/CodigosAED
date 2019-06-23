from function import LinkedList

myList = LinkedList()
myList.add("Valor 1")
myList.add("Valor 2")
myList.add("Valor 3")
myList._print()
print("First:",myList.getFirst())
print("Last:",myList.getLast())
print("---------------------------------------------------------------")
print("\nAgregando nuevos elementos")
myList.addInPosition("Valor 2.5",2)
myList.addInPosition("Valor 3.5",4)
myList._print()
print("First:",myList.getFirst())
print("Last:",myList.getLast())
print("---------------------------------------------------------------")
myList.removeForValue("Valor 2.5")
myList.removeForPosition(3)#eliminando el ultimo
myList.removeForPosition(0)#eliminando el primero
myList._print()
print("First:",myList.getFirst())
print("Last:",myList.getLast())