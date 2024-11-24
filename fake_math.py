def divide(first,second):       # В fake_math создайте функцию divide, которая принимает два параметра first и second.
    if second == 0:             # Функция должна возвращать результат деления first на second,
        return 'Ошибка'         # но когда в second записан 0 - возвращать строку 'Ошибка'.
    else:
        return first / second