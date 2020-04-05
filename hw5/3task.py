count = 0
new_li = []

with open('text_3.txt', encoding='utf-8') as file:
    for line in file:
        li = line.split()
        new_li.append(float(li[1]))
        count += 1
        if float(li[1]) < 20000:
            print(f"Сотрудник с з/п меньше 20000 : {li[0]}")

    print(f"Средняя зарплата на {count} сотрудников: {sum(new_li) / count}")
