import re


def detect_case(message):
    if re.match(r'^[a-z]+(-[a-z]+)*$', message):
        return "kebab-case"
    elif re.match(r'^[a-z]+(_[a-z]+)*$', message):
        return "snake_case"
    elif re.match(r'^[a-z]+[A-Z][a-z]+', message):
        return "loserCamelCase"
    elif re.match(r'^[A-Z][a-z]+[A-Z][a-z]+', message):
        return "UpperCamelCase"
    else:
        return "unknown"


import pytest

from main import detect_case


@pytest.mark.parametrize("message, result", [
    ("the-monster-and-the-superhero", "kebab-case"),
    ("the_monster_and_the_superhero", "snake_case"),
    ("theMonsterAndTheSuperhero", "loserCamelCase"),
    ("TheMonsterAndTheSuperHero", "UpperCamelCase"),
    ("The Monster And The Superhero", "unknown"),
])
def test_count_words(message, result):
    assert detect_case(message) == result
