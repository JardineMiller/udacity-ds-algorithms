# Complexity

* Time: O(log n)
* Space: O(n)

# Explanation
For this problem, a two-step process was required. Firstly, we needed to sort the array so that we confidently target the number in the list in descending order. From there, we simply iterate over the resulting sorted list and use two runners to alternate over the numbers to construct the highest possible combination of numbers. From there, we convert that back into a number and append it to the resulting array.

Time: The time complexity here is mostly dictated by the need to sort the input list. I opted for a merge sort here so the time complexity is O(n log n). The seconary part of the problem is a simple, single iteration over the sorted array so is insignificant when compared to the larger complexity of the merge sort.

Space: In terms of space here, it's a linear O(n) based on the original input list. Our use of recursion in the mergesort() method means that each call will persist until the first call has been resolved, meaning we end up having a single method call for each item in the array.