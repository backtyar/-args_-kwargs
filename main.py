# Задача 1
# Напишите функцию `max_value`, которая принимает произвольное
# число аргументов и возвращает максимальное значение среди них.

def max_value(*args):
    return max(args)

print(max_value(1, 9, 84, 4, 100, 8.5))
print(max_value(4,85,63))


# Задача 2
# Напишите функцию `merge_lists`, которая принимает
# произвольное число списков в виде аргументов *args и возвращает
# новый список, содержащий все элементы этих списков.
# Пример использования: print(merge_lists([1, 2, 3], [4, 5], [6, 7, 8, 9]))
# Вывод: [1, 2, 3, 4, 5, 6, 7, 8, 9]

def merge_lists(*args):
    new_list = []
    for lst in args:
        for element in lst:
            new_list.append(element)
    return new_list

print(merge_lists([1,2,3],[4,5],[7,8,9,10],['Anna']))

#
# Задача 3
# Напишите функцию `print_user_data`, которая принимает произвольное
# число именованных аргументов **kwargs,представляющих информацию о
# пользователе (имя, возраст, город и т.д.), и выводит эту информацию
# в отформатированном виде.
# Пример использования:
# print_user_data(name="John", age=30, city="New York", occupation="Programmer")
#
# Вывод:
# Name: John
# Age: 30
# City: New York
# Occupation: Programmer

def print_user_data(**kwargs):
    for key, value in kwargs.items():
        print(key,':',value)



print_user_data(name="John", age=30, city="New York", occupation="Programmer")