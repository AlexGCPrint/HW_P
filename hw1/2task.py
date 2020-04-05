time_sec = int(input("Введите время в секундах: "))
time_h = time_sec//3600
time_m = time_sec%3600//60
time_s = time_sec%3600%60

print("%02i:%02i:%02i" % (time_h, time_m, time_s))