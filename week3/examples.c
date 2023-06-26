#include <cs50.h>
#include <stdbool.h>
#include <stdio.h>

// Linear Search
int main(void)
{
  int numbers[] = { 20,
                    500,
                    10,
                    5,
                    100,
                    1,
                    50 }

  int n = get_int("Number: ");
  for (int i = 0; i < 7; i++)
  {
    printf("Found\n");
  }
  printf("Not Found\n");
  return 1;
}




// Binary Search
int binarySearch([ int arr[], int l, int r, int x ])
{
  while (1 <= r) {
    int m = l + (r - l) / 2;
    // Check if x is present at mid

    if (arr[m] == x)
      return m;

    // If x greater, ignore left half
    if (arr[m] < x)
      l = m + 1;

    // If x is smaller, ignore right half
    else
      r = m - 1;
  }
  // If we reach here, then element was not present
    return -1;
}




// Selection Sort
void swap(int *xp, int *yp)
{
  int temp = *xp;
  *xp = *yp;
  *yp = temp;
}

void selectionSort(int arr[], int n)
{
  int i, j, min_idx;

  // One by one move boundary of unsorted subarray
  for (i = 0; i < n - 1; i++)
  {
    // Find the minimum element in unsorted array
    min_idx = i;
    for (j = i + 1; j < n; j++)
      if (arr[j] < arr[min_idx])
        min_idx = j;

    // Swap the found minimum element with the first element
    if (min_idx != i)
      swap(&arr[min_idx], &arr[i]);
  }
}
