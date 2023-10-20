def containsDuplicate(nums):
    return len(set(nums)) != len(nums)


# import pytest

# from main import containsDuplicate


# @pytest.mark.parametrize('nums, result', [
#     ([1, 2, 3, 1], True),
#     ([1, 2, 3, 4], False),
# ])
# def test_majorityElement(nums, result):
#     assert containsDuplicate(nums) == result, 'Wrong result'
