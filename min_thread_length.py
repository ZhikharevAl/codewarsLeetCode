def min_thread_length(n, a):
    a.sort() # сортируем координаты гвоздиков по возрастанию
    return sum(a[i+1] - a[i] for i in range(n-1)) # суммируем расстояния между соседними гвоздиками

# тестирование функции
print(min_thread_length(5, [1, 5, 3, 2, 4])) # выведет 4
