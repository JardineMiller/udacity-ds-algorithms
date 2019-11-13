# Complexity

* Time: O(log n)
* Space: O(n)

# Explanation
Time: Here we are using a binary search to find the pivot point within the rotating array - a binary search has a time complexity of O(log n). The next step is to use another binary search to find the target within whichever half of input array is likely to contain our target number. Therefore the overall time complexity here is O(log n)

Space: We mostly just need to store the input array so the space complexity here is O(n). We use recursion here so we will have a single method call for each item in the input list.