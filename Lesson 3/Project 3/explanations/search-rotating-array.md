# Complexity

* Time: O(log n)
* Space: O(n)

# Explanation
The solution to this problem was to utilise a series of binary searches in order to isolate the potential loaction of our target number. The first step was to find the pivot point of our input list because once we know the point at which the list is pivoted, we can assert which section of the input list might contain the target number (assuming it is indeed contained within the input list). From that point, as we have now guaranteed that the sub-section of the array is ordered, we can use a pure binary search to find our target (or return -1 if it isn't found).

Time: Here we are using a binary search to find the pivot point within the rotating array - a binary search has a time complexity of O(log n). The next step is to use another binary search to find the target within whichever half of input array is likely to contain our target number. Therefore the overall time complexity here is O(log n)

Space: We mostly just need to store the input array so the space complexity here is O(n). We use recursion here so we will have a single method call for each item in the input list.