def binary_search_recursive(array, target, start_index, end_index):
    '''Write a function that implements the binary search algorithm using recursion
    
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
         
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)

def binary_search_recursive_soln(array, target, min, max):
  mid = (min + max) // 2

  if array[mid] == target:
    return array[mid]

  if min == max:
    return -1
  
  if target < array[mid]:
    max = mid - 1
    return binary_search_recursive_soln(array, target, min, max)

  if target > array[mid]:
    min = mid + 1
    return binary_search_recursive_soln(array, target, min, max)


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


print(binary_search_recursive(array, 4, 0, len(array) - 1))
print(binary_search_recursive(array, -1, 0, len(array) - 1))
print(binary_search_recursive(array, 1, 0, len(array) - 1))