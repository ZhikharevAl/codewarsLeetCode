# Ваш модуль с кодом (main.py)
def is_anagram(message1, message2):
    """
    Проверяет, являются ли две строки анаграммами.
    """
    if not isinstance(message1, str) or not isinstance(message2, str):
        raise ValueError("Both inputs must be strings")
    
    return len(message1) == len(message2) and set(message1) == set(message2)

# Ваш файл с тестами (test_main.py)
import pytest
from main import is_anagram

@pytest.mark.parametrize('message1, message2, result', [
    ('нора', 'рано', True),
    ('listen', 'silent', True),
    ('abc', 'def', False),
    ('hello', 'world', False),
])
def test_is_anagram(message1, message2, result):
    assert is_anagram(message1, message2) == result, f'is_anagram({message1}, {message2}) returned {not result}'
