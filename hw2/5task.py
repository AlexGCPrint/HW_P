my_list = [7,5,3,3,3,2]

numb = int(input("Введите, пожалуйста любое целое число: "))
insert = False

for k in my_list:
    if numb > k:
        my_list.insert(my_list.index(k), numb)
        insert = True
        break

if not insert:
    my_list.append(numb)


print(my_list)