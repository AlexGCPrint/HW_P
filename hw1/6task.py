a = 10
b = 20
i = 0

while True:
    i += 1
    a = a + a/10
    print(f"{i}-й день: {a:.2f}")
    if a < b:
        continue
    else:
        print(f"Спортсмен достиг результат на {i}-й день")
        break