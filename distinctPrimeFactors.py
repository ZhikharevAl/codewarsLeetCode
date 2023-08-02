'''
[Тестовое Google] Простые множители произведения массива
Нормальная


Задача
Дан массив целых положительных чисел nums, верните количество различных простых множителей в произведении элементов nums. Функция должна называться distinctPrimeFactors.

Обратите внимание, что:

Число, большее 1, называется простым, если оно делится только на 1 и само на себя.
Целое число val1 является множителем другого целого числа val2, если val2 / val1 является целым числом.
Пример


nums = [2,4,3,7,10,6]
distinctPrimeFactors(nums)
# 4

# Пояснение:
Произведение всех элементов в `nums` равно: `2 * 4 * 3 * 7 * 10 * 6 = 10080 = 25 * 32 * 5 * 7`.
Существует 4 различных простых множителя, поэтому мы возвращаем 4.

nums = [2,4,8,16]
distinctPrimeFactors(nums)
# 1

# Пояснение:
Произведение всех элементов в `nums` равно: `2 * 4 * 8 * 16 = 1024 = 210`.
Существует 1 различный простой множитель, поэтому мы возвращаем 1.
'''


def distinctPrimeFactors(nums) -> int:
    a = set()
    for x in nums:
        j = 2
        while x != 1:
            while x % j == 0:
                x //= j
                a.add(j)
            j += 1
    return len(a)


print(distinctPrimeFactors([2, 4, 3, 7, 10, 6]))
