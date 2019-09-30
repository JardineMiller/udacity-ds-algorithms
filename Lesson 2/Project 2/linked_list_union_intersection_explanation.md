# Complexity
### m = number of nodes in linked list 1
### p = numbers of nodes in linked list 2
### n = m * p 


* Union:
** Time: O(n)
** Space: O(m + p) simplified to O(n)

* Intersection:
** Time:
*** create list from linked list 1 = m
*** iterate linked list 2 = p
*** check node value in list 1 = m
*** add to new linked list = 1
*** remove from list 1 = k (where k = index of item to be removed)

# Explanation
## Union
Fairly straightforward, the union of two lists is essentially the two lists combined. So you will always have to iterate over each list in its entirety and push each value to the newly created linked list. Therefore, the space/time complexity for this is O(n)

## Intersection
Still linear, but slightly more complex than the Union implemenation. I decided to create a to_list() method for the linked l