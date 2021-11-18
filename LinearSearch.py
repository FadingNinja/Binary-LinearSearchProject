print('This is a Linear Search')

arr = ['i', 'a', 'm', 'a', 't', 'r', 'e', 'e']

def linearSearch(arr, x) :
    searchedItems = []
    for i in range(len(arr)) :
        if arr[i] == x :
            searchedItems.append(i)
    
    if len(searchedItems) > 0 :
        return f'Found {x} at : {searchedItems}'
    else :
        return 'Not Found'

x = input('Enter the number you want to search : ')
result = linearSearch(arr, x)

print(result)