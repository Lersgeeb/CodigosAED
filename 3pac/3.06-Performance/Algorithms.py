class InsertionSort:
    
    def sort(self, data = []):
        for i in range(1,len(data)):
            #element to be compared
            current = data[i]

            #comparing the current element with the sorted portion and swapping
            while i>0 and data[i-1]>current:
                data[i] = data [i-1]
                i = i - 1
                data[i] = current

        return data

class SelectionSort:

    def sort(self,data = []):
        #Traverse through all array elemenets
        for i in range(len(data)):
            #find the minimum element in remaining
            #unsorted array
            min_idx = i
            for j in range(i+1, len(data)):
                if data[min_idx] > data[j]:
                    min_idx = j
            #swap the found minimum element with
            #the first element 
            data[i],data[min_idx] = data[min_idx],data[i]

        return data

class BubbleSort:

    def sort(self,data=[]):
        for i in range(len(data)):
            for j in range(len(data)):
                if data[j]<data[i]:
                    temp = data[i]
                    data[i] = data[j]
                    data[j] = temp
        return data
                
class Quicksort:
    
    #this function takes last element as pivot, places 
    #the pivot element at its correct position in sorted
    #array, and places all smaller (smaller than pivot)
    #to left of pivot and all greater element to right
    #of pivot
    def partition(self,arr,low,high):
        i = (low-1)     #index of smaller element
        pivot = arr[high]   #pivot

        for j in range(low,high):
            #if current element is smaller than or
            #equal to pivot 
            if arr[j] <= pivot:  
                #increment index of smaller element
                i = i+1
                arr[i],arr[j] = arr[j],arr[i]

        arr[i+1],arr[high] = arr[high],arr[i+1]
        return (i+1)

    #the main function that implement QuickSort
    #arr[] --> Array to be sorted
    #low  --> Starting index
    #high --> Ending index

    #function to do Quick Sort
    def quickSort(self,arr,low,high):
        if(low < high):

                #pi is partion index, arr[p] is now
                #at rigth place
                pi = self.partition(arr,low,high)

                #Separately sort elements before
                #partion and after partion
                self.quickSort(arr,low,pi-1)
                self.quickSort(arr,pi+1,high)

    def sort(self,data=[]):
        self.quickSort(data,0,len(data)-1)
        return data

class MergeSort:

    def sort(self,values= []):
    
        if len(values) <= 1:
            return values

        middle_index = len(values) // 2
        left_values = self.sort(values[:middle_index])
        right_values = self.sort(values[middle_index:])
        sorted_values = []
        left_index = 0
        right_index = 0
        while left_index < len(left_values) and right_index < len(right_values):
            if left_values[left_index] < right_values[right_index]:
                sorted_values.append(left_values[left_index])
                left_index += 1
            else:
                sorted_values.append(right_values[right_index])
                right_index += 1
        sorted_values += left_values[left_index:]
        sorted_values += right_values[right_index:]
        
        return sorted_values

