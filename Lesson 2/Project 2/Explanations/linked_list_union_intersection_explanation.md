# Complexity
### m = number of nodes in linked list 1
### p = numbers of nodes in linked list 2


* Union:
** Time: O(n)
** Space: O(m + p + o) where o = new linked list. Simplified to O(n)

* Intersection:
** Time: O(m + pm + p + pk) where k is the index of the item removed from list 1. Simplified to O(n^2)
** Space: O(m + p + o + l) where o = new linked list and l = list created from linked list. Simplified to O(n)

# Explanation
## Union
Fairly straightforward, the union of two lists is essentially the two lists combined. This solution accepts duplicate values, so you will always have to iterate over each list in its entirety and push each value to the newly created linked list. Therefore, the space/time complexity for this is O(n)

## Intersection
The list lookup within a for loop iterating over the other collection means that the time complexity here is quadratic - O(n^2). I decided to create a to_list() method for the linked list and use that to store the values of one of the linked lists so that I could easily remove a value from the list after it had been found. The reason for this is intersections of lists is slightly different to that of an intersection of a set, where you don't need to account for duplicate values. Lists means that duplicates might be present, so the implementation has to consider each PAIR of values. Consider the below:

list_1 = [1,2,3,3,3]
list_2 = [3]

If you are iterating over list_1 and comparing each values against any of the values found in list_2, if you don't remove the values you find, your intersection results will include three entries for the value 3. Removing the value from the lookup collection when its found will ensure you don't reconsider the same value once it is found. You could argue that writing a clone method for the linked list would be an optimisation over writing a simple to_list method, because delete operations on a linked list are O(1) rather than the O(n) of a list. But you still have to find the value in the linked list - which is O(n).