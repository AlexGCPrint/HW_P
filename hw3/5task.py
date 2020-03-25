def my_f():
    result = 0
    while True:
        numbers = input('вводите через пробел список чисел или введите символ "*" для выхода: ').split()
        for i in numbers:
            try:
                if i == '*':
                    print(f'Сумма: {result}. Exit')
                    return
                else:
                    result += int(i)
            except ValueError:
                print('Вводите число или символ "*"')
        print(f'Сумма: {result}')

my_f()