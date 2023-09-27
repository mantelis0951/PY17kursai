leaps = []

for leap in range(1900, 2101):
    if leap % 4 == 0 and (leap % 100 != 0 or leap % 400 == 0):
        leaps.append(leap)

print(leaps)
