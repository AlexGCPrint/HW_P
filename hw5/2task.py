count_lines = 0

with open('text1.txt', encoding='utf-8') as file:
    for line in file:
        count_lines += 1
        count_words = len(line.split())
        print(f"Количество слов в строке {count_lines} : {count_words}")
    print(f"Количество строк в иходном файле: {count_lines}")
