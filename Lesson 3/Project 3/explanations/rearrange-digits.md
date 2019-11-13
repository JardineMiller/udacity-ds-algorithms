# Complexity

* Time: O(log n)
* Space: O(n)

# Explanation
Time: The time complexity here is mostly dictated by the need to sort the input list. I opted for a merge sort here so the time complexity is O(n log n). The seconary part of the problem is a simple, single iteration over the sorted array so is insignificant when compared to the larger complexity of the merge sort.

Space: In terms of space here, it's a linear O(n) based on the original input list. Our use of recursion in the mergesort() method means that each call will persist until the first call has been resolved, meaning we end up having a single method call for each item in the array.