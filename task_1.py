print('Задача 1. Урок информатики 2')


# В прошлый раз учитель написал программу,
# которая выводит числа в формате плавающей точки, однако он вспомнил,
# что не учёл одну важную штуку: числа-то могут идти от нуля.
# 
# Задано положительное число x (x > 0).
# Ваша задача преобразовать его в формат плавающей точки,
# то есть x = a * 10 ** b, где 1 ≤ а < 10
# 
# Обратите внимание, что x теперь больше нуля, а не больше единицы.
# Обеспечьте контроль ввода.
# 
# Пример 1:
# 
# Введите число: 92345
# 
# Формат плавающей точки: x = 9.2345 * 10 ** 4
# 
# Пример 2:
# 
# Введите число: 0.0012
# Формат плавающей точки: x = 1.2 * 10 ** -3

while True:
    number = input('Введите число: ')
    numberValid = True
    for symbol in number:
        if symbol == '.' or symbol.isdigit() is True:
            None
        else:
            numberValid = False
            break

    if numberValid is False or number == '0':
        print('Ошибка ввода')
        continue

    dot_pos = number.find('.')
    if dot_pos == -1 and number[0] != '0':
        print(f'Формат плавающей точки: x = {number[0]}.{number[1:]} * 10 ** {len(number) - 1}')
    elif dot_pos == -1 and number[0] == '0':
        print('Ошибка ввода')
        continue
    elif dot_pos == 1:
        count = 0
        for digit in number[2:]:
            print(digit)
            if digit != '0':
                break
            count += 1
        print(f'Формат плавающей точки: x = {number[count + 2]}.{number[(count + 3):]} * 10 ** {len(number) - (3 + count)}')
    else:
        before_dot = number[:dot_pos]
        print(f'Формат плавающей точки: x = {number[0]}.{number.replace('.', '')[1:]} * 10 ** {len(number.replace('.', '')[1:])}')
