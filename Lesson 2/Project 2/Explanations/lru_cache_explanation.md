# Complexity
* Time: O(1)
* Space: O(n)

# Explanation
I loved this exercise!

I chose to use a Dictionary working in tandem with a Doubly Linked List. The dictionary - rather than directly storing the values of everything in the cache - stores the NODE containing the value in the Linked List. This means that whenever we want to update the location of the node within the Linked List responsible for tracking recent access, we can do that in O(1) time complexity. Using the built-in functionality of dicts in Python, that means that the actual cache access is also O(1). So everything here is O(1) time-complexity.

In terms of space complexity, we are storing each entry in the cache twice (once in the dict once in the linked list) - meaning that our space complexity here is O(2n), simplified as O(n).