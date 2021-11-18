print('This is a Binary Search')

arr = sorted(['i', 'm', 'a', 't', 'r', 'e', 'e'])

def binarySearch(arr, start, end, x) :
    if end >= start :
        mid = start + (end - start) // 2
        if arr[mid] == x :
            return mid
        elif arr[mid] > x :
            return binarySearch(arr, start, mid - 1, x)
        elif arr[mid] < x :
            return binarySearch(arr, mid + 1, end, x)
        else :
            return 'Not Found'

x = input('Enter the number you want to search : ')
result = binarySearch(arr, 0, len(arr) - 1, x)

print(result)