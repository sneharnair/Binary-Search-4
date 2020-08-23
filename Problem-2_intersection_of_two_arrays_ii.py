# APPROACH 1: HASHMAP
# Time Complexity : O(n1 + n2), n: len(nums1), n2: len(nums2)
# Space Complexity : O(min(n1, n2)) - space of hashmap
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
#
#
# Your code here along with comments explaining your approach
# 1. Always ensure that the first array is of shorter length
# 2. Store the frequency of each element of first array in hashmap
# 3. For each element of second array, if the element is in hashmap, dec it's count and add to result. if the count becomes 0, delete that hashmap entry.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 is None or nums2 is None:
            return None
        
        if len(nums1) > len(nums2):
            self.intersect(nums2, nums1)
            
        hashmap = defaultdict(int)
        for num in nums1:
            hashmap[num] += 1
          
        result = []
        for num in nums2:
            if num in hashmap:
                hashmap[num] -= 1
                result.append(num)
                if hashmap[num] == 0:
                    del hashmap[num]
                    
        return result
        
        
# APPROACH 2: TWO POINTERS
# Time Complexity : O(n1 lg n1 + n2 lg n2), n: len(nums1), n2: len(nums2) (due to sort)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
#
#
# Your code here along with comments explaining your approach
# 1. Always ensure that the first array is of shorter length. Sort both arrays. 
# 2. Have 2 pointers, one at the start of each list. If elements at ptrs are same, add to result and inc both of them
# 3. If either of them is less, then inc only that ptr. 

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 is None or nums2 is None:
            return None
        
        if len(nums1) > len(nums2):
            self.intersect(nums2, nums1)
            
        nums1.sort()
        nums2.sort()
        result = []
        
        low, high = 0, 0
        while low < len(nums1) and high < len(nums2):
            if nums1[low] == nums2[high]:
                result.append(nums1[low])
                low, high = low + 1, high + 1
                
            elif nums1[low] < nums2[high]:
                low += 1
                
            else:
                high += 1
                
        return result
          
          
          

# APPROACH  3: BINARY SEARCH
# Time Complexity : O(n1 lg n1 + n2 lg n2), n: len(nums1), n2: len(nums2) (due to sort)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
#
#
# Your code here along with comments explaining your approach
# 1. Always ensure that the first array is of shorter length. Sort both arrays. 
# 2. For each element of the first list, do binary search for that element in second list.
# 3. In binary search, if element is found, make sure that the element is first occureence of that element else search in left half.
# 4. After each binary search call, update low to the found index + 1, so that we dont search the already found elements again (as duplicates are allowed). 

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 is None or nums2 is None:
            return None
        
        if len(nums1) > len(nums2):
            self.intersect(nums2, nums1)
            
        nums1.sort()
        nums2.sort()
        result, low = [], 0
        
        for num in nums1:
            search_result = self.binary_search(nums2, low, len(nums2) - 1, num)
            if search_result != -1:
                result.append(num)
                low = search_result + 1
                
        return result
    
    
    def binary_search(self, arr, low, high, target):
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] == target:
                if mid == low or arr[mid - 1] < arr[mid]:
                    return mid
                else:
                    high = mid - 1
                    
            elif arr[mid] < target:
                low = mid + 1
                
            else:
                high = mid - 1
                
        return -1
                
          
