#-*-coding:utf-8-*-
from Algorithms import *
from Performance import *

  
execution = ExecutionTime()
test = TestPerformance()
arrayGenerator = ArrayGenerator()
array = arrayGenerator.generate(10000)

bubbleSort = BubbleSort()
insertionSort = InsertionSort()
selectionSort = SelectionSort()
quickSort = Quicksort()
mergeSort = MergeSort()

bubble = test.test(bubbleSort,execution, array[:])

insertion = test.test(insertionSort, execution, array[:])

selection = test.test(selectionSort, execution, array[:])

quick = test.test(quickSort, execution, array[:])

merge = test.test(mergeSort, execution, array[:])

print("Algoritmo\t\t\tTiempo(ms)")
print("BubbleSort time: \t\t%s" % bubble[1])
print("InsertionSort time: \t\t%s" % insertion[1])
print("SelectionSort time: \t\t%s" % selection[1])
print("QuickSort time: \t\t%s" % quick[1])
print("MergeSort time: \t\t%s" % merge[1])