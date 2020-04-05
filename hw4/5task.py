from functools import reduce


def my_f(prev_el, el):
    return prev_el * el


li = [i for i in range(100, 1001) if i % 2 == 0]

print(reduce(my_f, li))
