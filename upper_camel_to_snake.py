import pytest


def upper_camel_to_snake(message):
    if not message:
        return ""

    result = [message[0].lower()]

    for char in message[1:]:
        if char.isupper():
            result.extend(['_', char.lower()])
        else:
            result.append(char)

    return ''.join(result)


@pytest.mark.parametrize("input_str, expected_output", [
    ("TheNinaProject", "the_nina_project"),
    ("", ""),
])
def test_upper_camel_to_snake(input_str, expected_output):
    assert upper_camel_to_snake(input_str) == expected_output
