# Linear Search (run time: O(n))
https://cs50.harvard.edu/x/2023/shorts/linear_search/
* Simplest approach to find an element in a dataset
* Iterates an array from left to right until it finds a match.

| Worst case | Best case|
|------------|----------|
| **0(N):** We have to look through the entire array of n elements, either because the target element is at the very end or because no match exists. | **Ω(1):** The target element is the first element in the array and so we can stop looking immediately after we start.|

Pseudocode
```
For i from 0 to n-1
  If 0 is behind doors[i]
    Return true
Return false
```


# Binary Search (run time O(log n))
Divide and conquer!
* Efficient array search algorithm. Given that the array is sorted - sorting can be costly.
  * We need the array sorted so tht we know what we are discarding.
* Narrows range by half each time.

| Worst case | Best case|
|------------|----------|
| **O(log N):**  | **Ω(1):** The target element is the first element in the array and so we can stop looking immediately after we start.|

Pseudocode
```
Repeat until the (sub)array is of size 0:
  Return false
If target is behind (sub)array[middle]
    Return true
Else if target < (sub)array[middle]
  Search (sub)array[0] through (sub)array[middle - 1]
Else if target > (sub)array[middle + 1] through (sub)array[n - 1]
```
