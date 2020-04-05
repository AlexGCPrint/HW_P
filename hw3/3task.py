def my_func(a=2, b=8, c=10):
    li = []
    x = a+b
    y = a+c
    z = b+c
    li.append(x)
    li.append(y)
    li.append(z)
    print(max(li))

my_func(1, 5, 8)