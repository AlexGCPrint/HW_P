with open("text_5.txt", 'w', encoding="utf-8") as file:
    data = input("Вводите числа через пробел: ")
    file.write(data)
    li = (data.split())
    result = 0
    for i in li:
        numb_i = float(i)
        result += numb_i
    print(result)
