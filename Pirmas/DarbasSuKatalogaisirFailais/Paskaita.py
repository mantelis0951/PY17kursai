import os
import datetime


modify_time = os.stat("naujas_aplankalas/naujas").st_mtime


currentpath = os.getcwd()

print(currentpath)

os.chdir('D:\Projects\Pirmas\DarbasSuKatalogaisirFailais')

os.mkdir("Naujas_aplankas2/naujas/naujas2/naujas3/naujas4") # nesukuria aplankalu jeigu ju nera

os.makedirs("Naujas_aplankas2/naujas/naujas2/naujas3/naujas4", exist_ok = True) # sukuria aplankalus

print(os.stat("naujas_aplankalas/naujas/naujas2/a"))

