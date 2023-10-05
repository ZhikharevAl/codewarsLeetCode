import pytest


def kebab_to_upper_camel(message):
    return "".join([word.title() for word in message.split("-")])


@pytest.mark.parametrize("input_str, expected_output", [
    ("the-nina-project", "TheNinaProject"),
    ("hello-world", "HelloWorld"),
    ("", ""),
    ("no-dashes", "NoDashes"),
])
def test_kebab_to_upper_camel(input_str, expected_output):
    assert kebab_to_upper_camel(input_str) == expected_output
