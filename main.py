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


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    
def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result

print(merge_sort([5, 3, 7, 2, 8, 4, 1, 9, 6]))


