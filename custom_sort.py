def custom_sort(words):
    sorted_words = sorted(words, key=lambda x: sum(c.isdigit() for c in x))
    result = ', '.join(sorted_words)
    return result

# import pytest

# from main import custom_sort


# @pytest.mark.parametrize("words, result", [
#     (["Action", "Pagination_3", "Controller_24", "Arrows_451", "Elements_451"], "Action, Pagination_3, Controller_24, "
#                                                                                 "Arrows_451, Elements_451"),
#     (["Arrows_451", "Controller_24", "Elements_451", "Pagination_3", "Brave", "Action", "Bold"], "Brave, Action, "
#                                                                                                  "Bold, Pagination_3,"
#                                                                                                  " Controller_24, "
#                                                                                                  "Arrows_451, "
#                                                                                                  "Elements_451"),
# ])
# def test_custom_sort(words, result):
#     assert custom_sort(words) == result
