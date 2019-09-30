#-*-coding:utf-8-*-
from Algorithms import *
from Performance import *

  
execution = ExecutionTime()
test = TestPerformance()
arrayGenerator = ArrayGenerator()
array = arrayGenerator.generate(1000)

bubbleSort = BubbleSort()
insertionSort = InsertionSort()
selectionSort = SelectionSort()
quickSort = Quicksort()

bubble = test.test(bubbleSort,execution, array[:])

insertion = test.test(insertionSort, execution, array[:])

selection = test.test(selectionSort, execution, array[:])

quick = test.test(quickSort, execution, array[:])

print("Algoritmo  #Datos  Tiempo(ms)")
print(bubble)
print(insertion)
print(selection)
print(quick)