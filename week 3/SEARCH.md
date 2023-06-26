# Linear Search (run time: O(n))
* Simplest approach to find an element in a dataset
* Examines each element until it finds a match.

Pseudocode
```
For i from 0 to n-1
  If 0 is behind doors[i]
    Return true
Return false
```

# Binary Search (run time O(log2 n))
* Efficient array search algorithm. Given that the array is sorted.
* Narrows range by half each time.

Pseudocode
```
If no doors left
  Return false
If 50 is behind doors[middle]
    Return true
Else if 50 < doors[middle]
  Search doors [0] through doors[middle - 1]
Else if 50 > [middle + 1] through doors [n - 1]
```
