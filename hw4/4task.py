li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

li2 = [el for el in li if li.count(el) < 2]
print(li2)