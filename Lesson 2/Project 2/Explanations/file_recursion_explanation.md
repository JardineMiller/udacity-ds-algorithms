# Complexity
### d = number of dirs in total
### f = number of files per dir
### n = d * f

* Time: O(n)
* Space: O(n)

# Explanation
We are interested in finding all the files within a directory that has the file suffix provided. In order to find all files that match a certain condition, we have to visit every entity in the file hierarchy.

As it currently stands, if we assume that there is an even distribution of files between directories, then adding more directories to the parent directory will result in a linear increase in the time required for this algorithm - hence the time & space complexity of O(n).
