#пишу комментарии, тк был на прошлой конференции в тимсе и вы жаловались на плагиат, поэтому буду обьяснять, что делал

import json


def mtsk() -> float:
    # открываем наш JSON файл
    with open('input.json', 'r') as file:  # Укажите путь к файлу здесь
        data = json.load(file)

    # складываем произведения score и weight
    total_sum = sum(entry["score"] * entry["weight"] for entry in data)

    # ну и округляем:)
    return round(total_sum, 3)


print(mtsk())
