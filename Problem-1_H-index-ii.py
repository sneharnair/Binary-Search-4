# APPROACH 1: BRUTE FORCE
# Time Complexity : O(n), n: len(citations)
# Space Complexity : O(1) 
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
#
#
# Your code here along with comments explaining your approach
# 1. For each element of the array, calculate the number of elments of the array greater than or equal to the element at that index.
# 2. Check if the above sum is greater than or equal to the element at that index
# 3. If so, return the sum. 

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        if citations is None:
            return None
        
        for ind in range(len(citations)):
            if len(citations) - ind <= citations[ind]:
                return len(citations) - ind
            
        return 0


# APPROACH 2: BINARY SEARCH 
# Time Complexity : O(lg n), n: len(citations)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
#
#
# Your code here along with comments explaining your approach
# 1. start Binary Search with low-> 0 and high -> len(citation) - 1
# 2. If the number of elments of the array greater than or equal to the element at that index is same as the element at that index itself, return the sum
# 3. if above sum < element -> shift to right half, if above sum > element -> shift to left half
# 4. (if we dont find the exact equal, we will eventually find the first point where the sum > element), no need to keep track of the max found so far and keep going left. Instead,
#    out of BS while loop, low will be at right position.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        if citations is None:
            return None
        
        low, high = 0, len(citations) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            diff = len(citations) - mid
            
            if citations[mid] == diff:
                return diff
            
            elif citations[mid] < diff:
                low = mid + 1
                
            else:
                high = mid - 1
                
        return len(citations) - low
