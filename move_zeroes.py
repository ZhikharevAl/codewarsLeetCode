def move_zeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    for _ in range(nums.count(0)):
        nums.remove(0)
        nums.append(0)
    return nums
