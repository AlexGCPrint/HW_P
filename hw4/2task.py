li = [300, 564, 334, 338, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

li2 = []

for i in range(1, len(li)):
    if li[i] > li[i-1]:
        li2.append(li[i])

print(li2)

li3 = [li[i] for i in range(1, len(li)) if li[i] > li[i-1]]

print(li3)

