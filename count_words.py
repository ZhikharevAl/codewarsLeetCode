import pytest


def count_words(message):
    return len([word for word in message.lower().split() if word[0] == word[-1]])


@pytest.mark.parametrize("message, result", [
    ("Привет Анна", 1),
    ("Привет Лия", 0),
])
def test_count_words(message, result):
    assert count_words(message) == result
