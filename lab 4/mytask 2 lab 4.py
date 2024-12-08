import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def mtsk() -> None:
    # cчитываем содержимое сsv файла
    with open(INPUT_FILENAME, mode='r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)  # тут мы преобразовываем каждую строку в словарь с заголовками как ключами
        data = [row for row in reader]  # а тут создаем список словарей

    # сохраняем данные в json файл с отступами равными 4
    with open(OUTPUT_FILENAME, mode='w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    mtsk()

    # выводим результат
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
