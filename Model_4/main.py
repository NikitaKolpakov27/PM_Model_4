import math

main_matrix = [
    [
        (1, 1, 1),
        (4, 5, 6),
        (3, 4, 5),
        (6, 7, 8)
    ],

    [
        (1/6, 1/5, 1/4),
        (1, 1, 1),
        (1/3, 1/2, 1/1),
        (2, 3, 4)
    ],

    [
        (1/5, 1/4, 1/3),
        (1, 2, 3),
        (1, 1, 1),
        (2, 3, 4)
    ],

    [
        (1/8, 1/7, 1/6),
        (1/4, 1/3, 1/2),
        (1/4, 1/3, 1/2),
        (1, 1, 1)
    ]
]

geom_mean_ALL = []  # fuzzy geometric mean

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


# Fuzzy weights:
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


# Clear weights:

clear_weights_ALL = []  # "Чистые" веса

for i in fuzzy_weights_ALL:
    # clear_weights_ALL = []
    a = 0
    for j in i:
        a += j
    clear_weights_ALL.append(
        round(a / len(i), 3)
    )

print("Чистые веса: ", clear_weights_ALL)


# Normalized weights:

normalized_weights_ALL = []
total_non_normal_weight = sum(clear_weights_ALL)

for i in clear_weights_ALL:
    normalized_weights_ALL.append(
        round(i / total_non_normal_weight, 3)
    )

print("Нормализированные веса: ", normalized_weights_ALL)


