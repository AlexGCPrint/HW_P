def my_f():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        print(a/b)
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except ValueError:
        print("Это не число")

my_f()