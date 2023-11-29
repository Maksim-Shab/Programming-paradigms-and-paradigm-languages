# Корреляция
# ● Контекст
# Корреляция - статистическая мера, используемая для оценки
# связи между двумя случайными величинами.
# ● Ваша задача
# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.


import math

def pearson_correlation(array_1, array_2):
   
    # Проверка длины массивов
    if len(array_1) != len(array_2):
        raise ValueError("Массивы не должны быть разной лины длины")
    
    # Среднее значение
    m_x = sum(array_1) / len(array_1)
    m_y = sum(array_2) / len(array_2)
    
    # Поиск первой суммы
    sum_1 = sum([(xi - m_x) * (yi - m_y) for xi, yi in zip(array_1, array_2)])
    
    # Поиск второй суммы в квадратном корне
    sum_2 = (math.sqrt(sum([(xi - m_x) ** 2 for xi in array_1]) * sum([(yi - m_y) ** 2 for yi in array_2])))
    
    # Поиск значения корреляции
    correlation = sum_1 / sum_2

    return correlation


array_1 = [1,2,3,4,8]
array_2 = [6,7,8,9,10]

correlation = round(pearson_correlation(array_1, array_2), 3)
print(f"Корреляция Пирсона: {correlation}")