"""
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна
завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный
знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать
знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в
качестве делителя.
"""

# Не получается сделать прерывание цикла, если вместо знака операции введен 0

while True:
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    sign_of_operation = str(input('Введите знак операции: '))
    sign = sign_of_operation
    if num_2 != 0:
        if sign == 0:
            exit()
        elif sign == '+':
            print(num_1 + num_2)
        elif sign == '-':
            print(num_1 - num_2)
        elif sign == '*':
            print(num_1 * num_2)
        elif sign == '/':
            print(num_1 / num_2)
    else:
        print('Ай-яй-яй! На 0 делить нельзя')
