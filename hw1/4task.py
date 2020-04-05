numb = int(input("Введите положительное целое число: "))

r = -1

while numb > 0:
    d = numb % 10
    numb //=10
    if d > r:
        r = d
print(r)