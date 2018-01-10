def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    if len(nums) <= 1:
            return False
        
    seen = {}
    
    for index in range(len(nums)):
        print seen
        if nums[index] in seen:
            return [seen[nums[index]], index]
        else:
            seen[target-nums[index]] = index
    
    # for index, num in enumerate(nums, 0):
    #     for other_index, other_num in enumerate(nums, 1):
    #         if num + other_num == target:
    #             return [index, other_index]


print twoSum([1,2,3,7], 9)
([1, 5, 5, 3], 10)
