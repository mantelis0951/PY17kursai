def pasisveikinti(vardas):
    print(f"Sveikas {vardas}")

pasisveikinti("tomai")
pasisveikinti("Jonai")
pasisveikinti("Petrai")

##############################################
def kvadratu(number):
    square = number ** 2
    return square

a = kvadratu(4)

a += 10

print(a)

###################################################

def sk_sum2(number1=3, number2=10, number3=5):
    sum = number1 + number2 + number3

    return sum

print(sk_sum2())

def sk_sum1(number1, number2, number3=5):
    sum = number1 + number2 + number3

    return sum

print(sk_sum1(1,2))


def sk_sum3(number1=3, number2=10, number3=5):
    sum = number1 + number2 + number3

    return sum

print(sk_sum3(number3=20))

#######################################################################
def sk_suma5(*args): ## viena * paprasti argumentai
    print(args) # tuple (negalima keist ir istrint. atspausdina kaip = LISTAS)
    for number in args:
        print(number**2) ## kvadratu atspausdintu

sk_suma5(0,1,2,3,4,5,6,7,8,9,10)


def spausdinti(pavarde, **kwargs): ## ** key ir value reiksmes
    print(pavarde)
    for key, value in kwargs.items():
        print(key, value)

spausdinti("jonaitis" , metai = 15, vardas = "jonas", ugis = 1.75) ## atspausdina kaip dictionary

##########################################################
globalus = 10

def funkcija(x): ## geriau pasidaryti parametra (X)
    lokalus = 12
    suma = globalus + lokalus
    print(suma)
    return x

# suma = globalus + lokalus ## lokalus nenuskaitomas nes funkcijoje

funkcija(2)

#########################################################################

def funkcija1(sk1, sk2):
    '''  MULTILINE KOMENTARAS
    funkcija grazina dvieju skaiciu sk_suma
    :param sk1: pirmas sveikas skaicius
    :param sk2: antras sveikas skaicius
    :return: dvieju skaiciu suma
    '''
    suma = sk1 + sk2
    return suma


funkcija(2)

###############################################

### LAMBDA #############

def kvadratu(k):
    return k ** 2

kv = lambda x,y, z: x** 2 + y+ z
print(kv(2,1,10))

##############################

sarasas = [2,4,5,6,7,9,1,15]

sarasas2 = map(lambda  x:x**2, sarasas)
for x in sarasas2:
    print(x)

############################

sarasas1 = [1,2,3,4,5,6,7,8]

daugyba_is_saves = [lambda  i=skaicius: i*i for skaicius in range(1,6)]
for vienas in daugyba_is_saves:
    print(vienas())


##################################
sarasas = [2,4,5,6,8,9,11,15]

keliamieji = [lambda  i=metai: i for metai in range(1900,2101)
              if (metai %400==0) or (metai % 100!=0 and metai % 4 ==0)]

for v in keliamieji:
    print(v())

##########################################################################