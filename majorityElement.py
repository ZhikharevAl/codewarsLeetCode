
def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return max(set(nums), key=nums.count)

# import pytest

# from main import majorityElement


# @pytest.mark.parametrize('nums, result', [
#     ([3, 2, 3], 3),
#     ([2, 2, 1, 1, 1, 2, 2], 2),
# ])
# def test_majorityElement(nums, result):
#     assert majorityElement(nums) == result, 'Wrong result'
