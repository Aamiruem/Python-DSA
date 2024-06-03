# https://leetcode.com/problems/maximum-subarray/
''' 
continuously adding new elements to cs and also checking if the current value is greater or not.
if greater then start from current element.
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        cs = 0  # Current Sum
        ms = nums[0]  # Maximum Sum initialized to the first element of the array
        
        for num in nums:
            cs = max(num, cs + num)  # Update current sum
            ms = max(ms, cs)  # Update maximum sum
        
        return ms
    
print()


# Time: O(N)
# Space: O(1)
