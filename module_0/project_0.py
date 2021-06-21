import numpy as np


def game_core_v1(number):  # функция угадывания числа
    number = [int(x) for x in str("%03d" % number)]  # перевод загаданного числа в список цифр

    predict_number = np.random.randint(1, 101)  # наше первое число
    predict_number = [int(x) for x in str("%03d" % predict_number)]  # перевод нашего первого числа в список цифр

    def find_dig(index):  # функция угадывание цифры для заданного индекса:
        count_dig = 0
        dig = number[index]
        predict_dig = predict_number[index]
        while predict_dig != dig:
            count_dig += 1
            if predict_dig < dig:
                predict_dig += 1
            elif predict_dig > dig:
                predict_dig -= 1
        return count_dig  # выход из цикла когда угадали цифру

    count = 1
    for i in range(3):  # по очереди угадываеи все три цифры
        count += find_dig(i)
    return count  # общее количество предпринятых попыток угадывания числа


def score_game(game_core):  # запускаем игру 1000 раз
    count_ls = []
    # np.random.seed(1) ## если хотим одинаковый список каждый раз когда запускаем код
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))  # получение результата из функции угадывания и его запись в список
    score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v1)
