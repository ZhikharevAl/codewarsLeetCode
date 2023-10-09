def get_digits_count(message):
    return sum([int(i) for i in message if i.isdigit()])

# import pytest

# from main import get_digits_count


# @pytest.mark.parametrize("message, result", [
#     ("Lorem ipsum dolor sit 123 amet, consectetur adipiscing 456 elit.", 21),
#     ("Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 0),
# ])
# def test_get_digits_count(message, result):
#     assert get_digits_count(message) == result
