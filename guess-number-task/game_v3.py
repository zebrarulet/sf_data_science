"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

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

if __name__ == "__main__":
    # RUN
    game_core_v3(random_predict)