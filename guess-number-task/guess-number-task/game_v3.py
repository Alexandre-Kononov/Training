""" Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import numpy as np

number = np.random.randint(1, 101) # загадываем число

def custom_predict(number: int = 1) -> int:
    """Угадываем число. 
    Метод: При каждом шаге делим выборку пополам. На основе обратной связи об отношении загаданного числа 
    к предполагаемому (больше или меньше) определяем в какой половине выборки находится загаданное число 
    и устанавливаем новые минимальный и максимальный предел выборки. 
    Повторяем до получения правильного результата.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    
    max = 101 # Максимальный 
    min = 0   # Минимальный предел выборки
    
    predict_number = 0 # Предполагаемое число  
    
    while True:
        count += 1
        predict_number = (min + (max - min)//2)  # Делим выборку пополам
    
        if predict_number < number: 
            min = predict_number
            
        elif predict_number > number :
            max = predict_number
            
        elif predict_number == number :
            break # выход из цикла если угадали

    return count


def score_game(custom_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        custom_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(custom_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(custom_predict)

