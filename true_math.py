from math import inf            # Бесконечность можно импортировать из встроенной библиотеки math (from math import inf)

def divide(first, second):      # В true_math создайте функцию divide, которая принимает два параметра first и second.
    if second == 0:             # Функция должна возвращать результат деления first на second,
        return inf              # но когда в second записан 0 - возвращать бесконечность.
    else:
        return first / second