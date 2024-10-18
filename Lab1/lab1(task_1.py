numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_new = sum(numbers[:4]) + sum(numbers[5:])
len_numb = len(numbers)
avarage = sum_new/len_numb
numbers[4] = avarage
print("Измененный список:", numbers)
