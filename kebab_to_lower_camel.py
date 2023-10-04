def kebab_to_lower_camel(message):
    return "".join(word if message.index(word) == 0 else word.capitalize() for word in message.split("-"))


def test_kebab_to_lower_camel():
    assert kebab_to_lower_camel("the-nina-project") == "theNinaProject"
