import json

list_vpluse = []
companies = {}
average_profit = {}
li_total = [companies, average_profit]
n = 1

with open("text_7.txt", encoding='utf-8') as file:
    for line in file:
        li = line.split()
        pribil = int(li[2]) - int(li[3])
        if pribil > 0:
            list_vpluse.append(pribil)
        companies["firm_"+str(n)] = pribil
        n +=1

average = sum(list_vpluse) / len(list_vpluse)
average_profit["average_profit"] = average
print(li_total)

with open("text_777.json", "w", encoding='utf-8') as write_f:
    json.dump(li_total, write_f)
