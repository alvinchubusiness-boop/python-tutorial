import random

def insertion_sort(arr):
  
    for i in range(1, len(arr)):
        key = arr[i]          
        j = i - 1

       
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        
        arr[j + 1] = key

    return arr


nums = [random.randint(1, 100) for _ in range(10)]
print("Random list of numbers:", nums)


sorted_nums = insertion_sort(nums)
print("Insertion sorted list of numbers:  ", sorted_nums)
