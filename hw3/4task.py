def my_func(x=2, y=-1):
    return x ** y

def my_func_1(x=2, y=-1):
    for i in range(abs(y-1)):
        x *=x
    return 1/x