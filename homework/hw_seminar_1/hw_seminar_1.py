# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

from random import randint
from typing import List

def sort_list_imperative(arr: List[int]) -> List[int]:
    if len(arr) == 0:
            raise ValueError()
    for i in range(0, len(arr) - 1):
        for j in range(len(arr) - 1):
            if (arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

numbers = [randint(0, 100) for i in range(7)]
print(numbers)
print(sort_list_imperative(numbers))



# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

from random import randint
from typing import List

def sort_list_declarative(arr: List[int]) -> List[int]:
    if len(arr) == 0:
        raise ValueError()
    return sorted(arr, reverse=True)

numbers = [randint(0, 100) for i in range(7)]
print(numbers)
print(sort_list_declarative(numbers))