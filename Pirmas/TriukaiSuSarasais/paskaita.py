###### 1 variantas #######
#
# sarasas = [4,2,3,22,11]
# sarasas_2 = []
# for x in sarasas:
#     sarasas_2.append(x**2)
#     print(sarasas_2)
#
# ###### 2 variantas #######
#
# naujas = map(lambda x: x**2, sarasas)
# print(naujas)
# print(list(naujas))

#########################

# data = "2001-11-15"
#
# y,m,d = map(int, data.split("-"))
# print(y)
# print(m)
# print(d)

############################# pavertimas i float

# skaiciai = "4,3,2,1"
#
# pirmas,antras,trecias,ketvirtas = map(float, skaiciai.split(","))
# print(pirmas)
# print(antras)
# print(trecias)
# print(ketvirtas)

########################################

# sarasas = [4,3,2,1]
#
# def daugiau_nei_2(sarasas_lokalus):
#     sarasas2 = []
#     for element in sarasas_lokalus:
#         if element > 2:
#             sarasas2.append(element)
#     return sarasas2
#
# print(daugiau_nei_2(sarasas))

######################

# sarasas = [4,3,2,1]
#
# def daugiau_nei_2(sarasas_lokalus):
#     sarasas2 = []
#     for element in sarasas_lokalus:
#         if element > 2:
#             sarasas2.append(element)
#     return sarasas2
#
# print(daugiau_nei_2(sarasas))
#
# naujas = filter(lambda x: x>2, sarasas)
# print(list(naujas))

# import calendar
#
# metai = list(range(1900, 2150))
#
# naujas = filter(calendar.isleap, metai)
# print(list(naujas))

########### jis sudeda 4+3 tada 7+2 tada 9 + 1 eina is kaires i desine
# import functools
# #
# sarasas = [4, 3, 2, 1]
# #
# naujas = functools.reduce(lambda x,y: x + y, sarasas)
# print(naujas)

####################

# sarasas = [4, 3, 2, 1]
# stringas = "labas"
# print(sum(sarasas))
# print(min(stringas))
# print(max(stringas))

###########norint rasti mediana arba vidurki
# import statistics
#
# sarasas = [4,3,2,1,55,3]
# [1,2,3,3,4,55]
# print(statistics.mean(sarasas))
# print(statistics.median(sarasas))

###############################

# sarasas = [4,3,2,1]
#
# naujas = [x**2 for x in sarasas]
# print(naujas)
#
# naujas2 = [x for x in sarasas if x > 2]
# print(naujas2)
#
# sarasas2 = list(range(20))
#
# lyginiai = [x for x in sarasas2 if x % 2 == 0]
# print(lyginiai)

###########################

# sarasas = [4, 3.0, "Labas", True, 20, 111]
#
# int_kiekis = sum(type(x) is int for x in sarasas)
# print(int_kiekis)
#
# ###rasti string'us
# str_kiekis = sum(type(x) is str for x in sarasas)
# print(str_kiekis)

####################

# sarasas = [2, 5, 6, 4, 8, 9, 11, 21, 0]
# sarasas.sort(reverse=True)
# print(sarasas)
#
# naujas = sorted(sarasas)
# print(naujas)

################

# zodynas = {"vardas": "Jonas", "Pavarde": "Jonaitis", "Amzius": 20}
# #
# # naujas = sorted(zodynas)
# # print(naujas)

####

# sarasas = [-5, -10,5,0,2,1]
# # print(abs(-5))
# naujas = sorted(sarasas, key=abs, reverse=True)
# print(naujas)

#####
# class Darbuotojas:
#     def __init__(self, vardas, pavarde,atlyginimas):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.atlyginimas = atlyginimas
#
#     def __repr__(self):
#         return f"{self.vardas} {self.pavarde} {self.atlyginimas}"
#
# d1 = Darbuotojas("tadas", "Padaitis", 1000)
# d2 = Darbuotojas("Zuolas", "KUozaitis", 1200)
# d3 = Darbuotojas("Petras", "Metraitis", 1400)
#
# darbuotojai = [d1, d2, d3]
# print(darbuotojai)
#
# def rusiavimas(darbuotojas):
#     return darbuotojas.pavarde # galima keisti .atlyginimas arba .vardas arba .pavarde
#
#
# sort1 = sorted(darbuotojai, key=rusiavimas)
# print(sort1)
#
# sort2 = sorted(darbuotojai, key=lambda e: e.atlyginimas)
# print(sort2)

# import operator ## reikalingas tik tam
#
# sort3 = sorted(darbuotojai, key=operator.attrgetter("vardas"))
# print(sort3)