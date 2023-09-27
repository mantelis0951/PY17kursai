import statistics

##1
sarasas = list(range(0,51))
##2
naujas = [x*10 for x in sarasas]
print(naujas)
##3
dalinasiis7 = [x for x in sarasas if x % 7 == 0]
print(dalinasiis7)
##4
kvadratu = [x**2 for x in sarasas]
print(kvadratu)
##5
print(sum(kvadratu))
print(min(kvadratu))
print(max(kvadratu))
print(statistics.mean(kvadratu))
print(statistics.median(kvadratu))
##6
naujas3 = sorted(kvadratu, reverse=True)
print(naujas3)

