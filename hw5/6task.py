d = {}

with open("text_6.txt", encoding="utf-8") as file:
    for line in file:
        new_line = line.split()
        predmet = new_line[0][:-1]
        # print(predmet)
        chasi = 0
        for i in new_line[1:]:
            if i != "-":
               chasi +=int(i[:i.find('(')])
        # print(chasi)
        d[predmet] = chasi

print(d)
