"""
Given a sorted array, remove the duplicates in-place 
such that each element appear only once and return the new length.

Do not allocate extra space for another array, you 
must do this by modifying the input array in-place with O(1) extra memory.
"""


def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                nums.remove(num)
        
        length = len(nums)
        
        return length, nums

print removeDuplicates([1,1,2])
