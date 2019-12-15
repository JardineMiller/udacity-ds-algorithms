# Complexity
* Time: O(log n)
* Space: O(1)

# Explanation
Here, we are using a rudimentary guess & check approach to finding the squre root, guided by a binary search based approach. Our upper and lower bounds are 1 and the number for which we are trying to find the square root (as we can guarantee that the number must be between that range when we start). From that point, we find the middle point of those two bounds and multiple it by itself. Depending on the output, we either adjust the bounds or return the result if it is correct. In order to successfully floor the result (in the event that the square root does not exist as a whole number) we need to store a temporary result when our mid point squared is less than the input number. Once we match the condition in the while loop, we have guaranteed that it will be as close to the actual decimal square root as possible.

Time: This solution utilises a binary search based approach the finding the square root of a provided number. The time complexity of a binary search is O(log n) so the same complexity applies here.

Space: We are only ever storing a maximum of 4 items to memory in the sqrt() method, regardless of the size of the input. That means our space complexity here is a constant and thus can be represented as O(1).
