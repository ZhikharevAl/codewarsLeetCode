# Написать функцию, принимающую два аргумента - слово и букву. Функция должна посчитать, сколько раз эта буква
# встречается в данном слове, и вернуть полученное число вхождений. И то же самое без учета регистра.


def repeat(word: str, char: str) -> int:
    return sum([1 for i in word if i == char])