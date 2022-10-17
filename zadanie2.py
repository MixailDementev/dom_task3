# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

N = int(input('-> '))
numbers = []
for i in range(N):
    numbers.append(randint(-10, 10))
print(numbers)


def mult_num(numbers):
    new_len = len(numbers)//2+1 if len(numbers) % 2 != 0 else len(numbers)//2
    new_numbers = [numbers[i]*numbers[len(numbers)-i-1] for i in range(new_len)]
    print(new_numbers)


mult_num(numbers)


def mult_num(numbers):
    if len(numbers) % 2 != 0:
        for i in range(len(numbers)//2+1):
            print(numbers[i]*numbers[len(numbers)-i-1], end=' ')
    else:
        for i in range(len(numbers)//2):
            print(numbers[i]*numbers[len(numbers)-i-1], end=' ')


mult_num(numbers)


