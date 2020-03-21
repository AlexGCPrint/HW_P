list = list(input("Введите значения для списка: "))



print(list)

n = 1

while n < len(list):
    list.insert(n, list[n-1])
    list.pop(n)
    list.insert(n-1, list[n])
    list.pop(n+1)
    n += 2
    continue

print(list)