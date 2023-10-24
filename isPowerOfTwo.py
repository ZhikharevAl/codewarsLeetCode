def isPowerOfTwo(n):
    return n and (n & (n - 1)) == 0


# import pytest

# from main import isPowerOfTwo


# @pytest.mark.parametrize('n, result', [
#     (1, True),
#     (16, True),
#     (3, False),
# ])
# def test_isPowerOfTwo(n, result):
#     assert isPowerOfTwo(n) == result, 'Wrong result'
