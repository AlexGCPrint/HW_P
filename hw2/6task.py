goods = []
while input("Добавьте новый продукт, введите y/n: ") == 'y' or input("Добавьте новый продукт, введите y/n: ") == 'д':
    number = int(input("Введите номер продукта: "))

    product = {}
    keys_list = ["Название","Цена","Количесвто","ед"]
    for k in keys_list:
        product_value = input(f"Введите, пожалуйста {k} ")
        product[k] = product_value
    goods.append(tuple([number, product]))

print(goods)

analitics = {}
for good in goods:
    for product_key, product_value in good[1].items():
        if product_key in analitics:
            analitics[product_key].append(product_value)
            analitics[product_key] = set(analitics[product_key])
        else:
            analitics[product_key] = [product_value]
print(analitics)