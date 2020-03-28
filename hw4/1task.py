from sys import argv

script_name, virabotka, stavka, premia = argv

try:
    virabotka = int(virabotka)
    stavka = int(stavka)
    premia = int(premia)
    result = virabotka * stavka + premia
    print(result)

except ValueError:
    print("среди аргументов есть Не число")


