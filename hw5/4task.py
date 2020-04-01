li_rus = ["Один", "Два", "Три","Четыре", "Пять"]
n = 0

f_res = open("text_4write", "w", encoding="utf-8")

with open("text_4.txt", encoding="utf-8") as file:
    for line in file:
        li_eng = line.split()
        new_line = line.replace(li_eng[0],li_rus[n])
        print(new_line)
        n += 1
        f_res.write(new_line)
