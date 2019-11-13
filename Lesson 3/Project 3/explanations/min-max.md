# Complexity
* Time: O(n)
* Space: O(1) (exclude input) or O(n) (include input)

# Explanation
Time: This solution uses a single traversal of the input array therefore is has a time complexity of O(n)

Space: This depends on whether or not the input array is included in our consideration of space complexity. My answer is based on the exclusion of the input array; we are only ever storing 2 values for the min & max values and variations on the size of the input array will never alter that constant. Therefore, our space complexity here is O(1). If we were to include the input array then our time complexity would be O(n)
