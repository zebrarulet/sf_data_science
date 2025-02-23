"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
Усовершенствованная вверсия игры game_v2.py
"""

import numpy as np

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    low = 1
    high = 100
    predict = (low + high) // 2  # Начальное предположение - середина диапазона

    while number != predict:
        count += 1
        if number > predict:
            low = predict + 1
        elif number < predict:
            high = predict - 1
        predict = (low + high) // 2
    # Ваш код заканчивается здесь

    return count

score_game(game_core_v3)