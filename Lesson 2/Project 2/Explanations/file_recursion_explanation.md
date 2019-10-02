# Complexity
### d = number of dirs in total
### f = number of files per dir
### n = d * f

* Time: O(n)
* Space: O(n)

# Explanation
We are interested in finding all the files within a directory that has the file suffix provided. In order to find all files that match a certain condition, we have to visit every entity in the file hierarchy.

As it currently stands, if we assume that there is an even distribution of files between directories, then adding more directories to the parent directory will result in a linear increase in the time required for this algorithm.

The space complexity here is determined by the number of times we call the recursion function in our stack. The initial method call will not be cleared from the stack until all the calls have been resolved/returned. In short, our method will be called the same number of times as we have directories in the parent directory - so it will increase linearly. That means that our space complexity here is also O(n).
