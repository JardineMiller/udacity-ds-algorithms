# Complexity
* Time: O(n)
* Space: O(n)

# Explanation
The objective for this problem was to achieve the solution within a single iteration of the input list. As a seconary objective, I decided to attempt to solve this problem in-place to keep the space complexity to a minimum. In terms of analysing the problem, the statement dictates that we are only ever dealing with a maximum of THREE numbers of our input array. As such, in order to successfully sort them, we need to place the smallest o the three numbers at the start of the array and the larger of the three numbers at the end. That will automatically guarantee that the middle number is sorted as well. In order to do this, I needed to keep track of two "runners" that would be responsible for tracking the next suitable position for either the smallest or largest number. These trackers start at the beginning and end of the input list respectively. Every time we find a 0, we shift it to the next suitable min position, and everytime we find a 2 we shift it to the next suitable max position. In order for this to work successfully, we need to shift the position index by one (or minus one) everytime we find a 0 or 2.

Time: The spec for this problem required the solution to be achieved within a single traversal of the input array. The worst case scenario of this solution is O(n).

Space: We are sorting the input array in place and not creating any new elements/collections etc therefore the space complexity for this solution is also O(n).