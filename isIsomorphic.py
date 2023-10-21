def isIsomorphic(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))


# import pytest

# from main import isIsomorphic


# @pytest.mark.parametrize('s, t, result', [
#     ('egg', 'add', True),
#     ('foo', 'bar', False),
#     ('paper', 'title', True),
#     ('bbbaaaba', 'aaabbbba', False),
# ])
# def test_isIsomorphic(s, t, result):
#     assert isIsomorphic(s, t) == result, 'Wrong result'
