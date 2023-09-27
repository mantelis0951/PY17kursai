a = int(input("Įveskite pirmą skaičiu "))
sign = input("pasirinkite matematini veiksma (+,-,*,/) ")
b = int(input("Įveskite antra skaičiu "))

if sign == '+':
     print( a + b )
elif sign == '-':
     print( a - b)
elif sign == '*':
     print( a * b)
elif sign == '/':
     print (a / b)
else:
     print("Netinkamas ženklas")

