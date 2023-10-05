def kebab_to_upper_camel(message):
    return "".join([word.title() for word in message.split("-")])


def test_kebab_to_upper_camel():
    assert kebab_to_upper_camel("the-nina-project") == "TheNinaProject", "iSupposeSo TheNinaProject"
    assert kebab_to_upper_camel("hello-world") == "HelloWorld", "iSupposeSo HelloWorld"
    assert kebab_to_upper_camel("hello-world-foo-bar") == "HelloWorldFooBar", "iSupposeSo HelloWorldFooBar"
    assert kebab_to_upper_camel("hello-world-foo-bar-baz") == "HelloWorldFooBarBaz", "iSupposeSo HelloWorldFooBarBaz"
