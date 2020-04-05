a = 10
print(a)

currency = input("Укажите валюту (евро или доллар): ")
currency_cost = float(input("Укажите актуальный курс на сегодня: "))
currency_sum = int(input("Укажите сумму в валюте: "))

print(f"За вашу валюту {currency},  в пересчете на российский рубль, можно получить {currency_cost*currency_sum}")







