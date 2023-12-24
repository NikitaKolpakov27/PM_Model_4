import math

"""
    Колпаков Н.С. 19-я группа. Вариант 2, Стартап, Нечёткий МАИ
    
    Стартап:
        Онлайн-сервис для организации спортивных командных игр между любителями.
    
    Критерии:
        - Стоимость реализации
        - Внешний вид (интерфейс)
        - Востребованность
        - Масштабность
"""


# Шкала нечетких парных сравнений
main_matrix = [

    [
        (1, 1, 1),
        (3, 4, 6),
        (4, 6, 7),
        (5, 6, 9)
    ],

    [
        (1/6, 1/4, 1/3),
        (1, 1, 1),
        (1/3, 1/2, 1/1),
        (2, 3, 5)
    ],

    [
        (1/7, 1/6, 1/4),
        (1, 2, 3),
        (1, 1, 1),
        (2, 3, 6)
    ],

    [
        (1/9, 1/6, 1/5),
        (1/5, 1/3, 1/2),
        (1/6, 1/3, 1/2),
        (1, 1, 1)
    ]
]

geom_mean_ALL = []  # Нечеткое геометрическое среднее

for i in range(0, len(main_matrix)):
    geom_mean = []
    a = 1
    index = -1
    for j in range(0, len(main_matrix[i])):

        if index != 2:

            index += 1
            a = 1

            for k in range(0, len(main_matrix[i])):
                a *= main_matrix[i][k][index]

            geom_mean.append(
                round(
                    math.pow(a, (1 / len(main_matrix[i]))), 2
                )
            )

    geom_mean_ALL.append(geom_mean)

print("Нечеткое геометрическое среднее: ", geom_mean_ALL)


# Множители для 2-ой таблицы:

mnos_ALL = []  # Множители для 2-ой таблицы
index = -1
for j in range(len(geom_mean_ALL[0]) - 1, -1, -1):
    index += 1
    a = 0

    for k in range(0, len(geom_mean_ALL)):
        a += geom_mean_ALL[k][j]

    mnos_ALL.append(round((1.0 / a), 3))

print("Множители для весов: ", mnos_ALL)


# Нечеткие веса:
fuzzy_weights_ALL = []

for i in geom_mean_ALL:
    fuzz_weight = []
    a = 1
    for j in range(0, len(i)):
        fuzz_weight.append(
            round(i[j] * mnos_ALL[j], 3)
        )

    fuzzy_weights_ALL.append(fuzz_weight)
print("Нечеткие веса: ", fuzzy_weights_ALL)


# "Чистые" веса:
clear_weights_ALL = []

for i in fuzzy_weights_ALL:
    a = 0
    for j in i:
        a += j
    clear_weights_ALL.append(
        round(a / len(i), 3)  # Center of Area (COA)
    )

print("Чистые веса: ", clear_weights_ALL)


# Нормализованные веса:
normalized_weights_ALL = []
total_non_normal_weight = sum(clear_weights_ALL)

for i in clear_weights_ALL:
    normalized_weights_ALL.append(
        round(i / total_non_normal_weight, 3)
    )

print("Нормализованные веса: ", normalized_weights_ALL)


