def get_ext(path):
    return path.split('.')[-1]

# import pytest

# from main import get_ext


# @pytest.mark.parametrize('path, result', [
#     ('/Users/lia/hello-world/hello-world.js', 'js'),
#     ('/hello-world/foo.html', 'html'),
# ])
# def test_get_idx(path, result):
#     assert get_ext(path) == result, 'Wrong extension'
