with open('text1.txt', 'w') as file:
    while True:
        content = input("Введите контент, пустая строка == завершение ввода: ")
        if content == '':
            break
        file.write(content+"\n")

