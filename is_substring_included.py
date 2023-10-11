def is_substring_included(message1, message2):
    return message1 in message2 or message2 in message1

# import pytest

# from main import is_substring_included


# @pytest.mark.parametrize('message1, message2, result', [
#     ('Hello World', 'World', True),
#     ('Hello World', 'hello', False),
#     ('Лия', 'Привет, Лия', True),
#     ('', '', True),
# ])
# def test_custom_sort(message1, message2, result):
#     assert is_substring_included(message1, message2) == result
