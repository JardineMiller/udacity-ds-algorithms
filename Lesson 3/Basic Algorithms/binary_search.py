def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration
   
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
   
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    min = 0
    max = len(array) - 1
    
    while (min <= max): 
        mid = (min + max) // 2
                
        if array[mid] == target:
            return mid
        
        if array[mid] > target:
            max = mid - 1
            continue
            
        if array[mid] < target:
            min = mid + 1
            continue
        
    return -1


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
target2 = 11

print(binary_search(array, target))
print(binary_search(array2, target2))