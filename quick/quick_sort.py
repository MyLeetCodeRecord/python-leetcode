def quick_sort(arr, left, right):
    if left >= right:
        return
    pivot = (left+right)//2
    pivot = partition(arr, left, right, pivot)
    quick_sort(arr, left, pivot-1)
    quick_sort(arr, pivot+1, right)

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    
def partition(arr, left, right, pivot):
    swap(arr, right, pivot)
    cursor = left
    for i in range(left, right):
        if arr[i] <= arr[right]:
            swap(arr, i, cursor)
            cursor += 1
    swap(arr, cursor, right)
    return cursor

arr = [ int(i) for i in "49 59 88 37 98 97 68 54 31 3".split(" ")]
quick_sort(arr, 0, len(arr)-1)
print(arr)
