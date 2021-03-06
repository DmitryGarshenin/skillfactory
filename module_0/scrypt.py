import numpy as np


def game_core_v1(number):
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def game_core_v2(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или
    увеличиваем его в зависимости от того, больше оно или меньше нужного.
    Функция принимает загаданное число и возвращает число попыток"""
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали


def game_core_v3(number):
    """Делим нужный отрезок пополам каждую итерацию, меняя пределы в 
    соответствии с проверкой.
    Функция принимает загаданное число и возвращает число попыток"""
    #  print("загаданное число = ", number)
    count = 0
    predict = None
    minimum = 1
    maximum = 101
    while number != predict:
        count += 1
        predict = (maximum + minimum) // 2
        if number > predict:
            minimum = predict
        elif number < predict:
            maximum = predict
    #  print("число затраченных попыток : ", count)
    return count  # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# запускаем первую версию
score_game(game_core_v1)

# запускаем вторую версию
score_game(game_core_v2)

# запускаем третью версию
score_game(game_core_v3)
