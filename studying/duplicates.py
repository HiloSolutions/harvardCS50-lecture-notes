# Hash Set
# since sets can only hold unique values, we can add the numbers in an array to a set then determine if there are any duplicates
#time complexity: O(N) where the complexity increases as the number of umber increases.
# space complexity: 0(N) complexity is related to number of items in the set.

def containsDuplicatesA(nums):
    unique_set = set()

    for x in nums: 
      if x in unique_set:
        return True
      unique_set.add(x)

    return False


print(containsDuplicatesA([1, 2, 3, 4, 5, 6]))  # false
print(containsDuplicatesA([1, 2, 2, 4, 5, 6]))  # true


#Binary search with selection sort
# time complexity: O(N * LogN) FOR LOOP IS N and merge sort from sort fn is about LogN
def containsDuplicatesB(nums):
   nums.sort() #a hybrid sorting algorithm derived from merge sort and insertion sort.
   iterations = range(len(nums) - 1)
   
   for i in iterations:
      if nums[i] == nums[i + 1]:
         return True
   return False


print(containsDuplicatesB([1, 2, 3, 4, 5, 6]))  # false
print(containsDuplicatesB([1, 2, 5, 4, 5, 6]))  # true
