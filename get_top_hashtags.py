import re


def get_top_hashtags(message, num_hashtags=5, min_word_length=5):
    message = re.sub(r'\W', ' ', message).lower()
    words = message.split()
    hashtags = ['#{}'.format(word) for word in words if len(word) >= min_word_length][:num_hashtags]
    return " ".join(hashtags)

# import pytest

# from main import get_top_hashtags


# @pytest.mark.parametrize('message, result', [
#     ('Игра престолов - сериал, основанный на романах Джорджа Мартина, рассказывающий о борьбе за власть в вымышленном '
#      'мире Вестероса', '#престолов #сериал #основанный #романах #джорджа'),
#     ('Гладиатор - исторический эпос о римском генерале, который борется за свою свободу и мести', '#гладиатор '
#                                                                                                   '#исторический '
#                                                                                                   '#римском #генерале '
#                                                                                                   '#который'),
# ])
# def test_get_top_hashtags(message, result):
#     assert get_top_hashtags(message) == result, 'Wrong result'
