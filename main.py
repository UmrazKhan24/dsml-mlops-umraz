# create quick sort algorithm for sorting list of numbers

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        greater = []
        lesser = []
        for num in arr:
            if num > pivot:
                greater.append(num)
            else:
                lesser.append(num)
        return quick_sort(lesser) + [pivot] + quick_sort(greater)
    
print(quick_sort([5, 3, 7, 2, 8, 4, 1, 9, 6]))
