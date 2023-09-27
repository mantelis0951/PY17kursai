import os
import datetime

os.chdir('C:\\Users\\Mantas\\desktop\\Naujas Katalogas')
# os.mkdir("Naujas Katalogas")

laikas = datetime.datetime.now()
modify_size = os.stat("Failas.txt").st_size
with open ("Failas.txt", "w", encoding="utf-8") as failas:
    failas.write(f"Siandienos laikas: {laikas} bei dydis baitais: {modify_size}")

modify_time = os.stat("C:\\Users\\Mantas\\desktop\\Naujas Katalogas").st_ctime

print(modify_size)
print(datetime.datetime.fromtimestamp(modify_time))e