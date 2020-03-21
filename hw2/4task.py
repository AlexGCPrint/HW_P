string = input("Ведите пожалуйста, слова через пробел и хотя бы одно длинее 10 символов")

new_string = string.title().split()


# for i, item in enumerate(new_string):
#     if len(item) > 10:
#         print(i+1, item[:10])
#     else:
#         print(i+1, item)

for i, item in enumerate(new_string):
    print(i+1, item[:10]) if len(item) > 10 else print(i+1, item)
