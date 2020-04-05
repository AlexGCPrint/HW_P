from itertools import cycle, count

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

print("-" * 50)

c = 0

for el in cycle("МОСКВА"):
    if c > 17:
        break
    print(el)
    c +=1