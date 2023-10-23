def removeElements(head, val):
    return [x for x in head if x != val]

# import pytest

# from main import removeElements


# @pytest.mark.parametrize('head, val, result', [
#     ([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]),
#     ([], 1, []),
#     ([7, 7, 7, 7], 7, []),
# ])
# def test_isIsomorphic(head, val, result):
#     assert removeElements(head, val) == result, 'Wrong result'
