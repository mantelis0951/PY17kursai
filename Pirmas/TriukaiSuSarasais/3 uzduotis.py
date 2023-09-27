listofrandoms = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
##1
int_quantity = sum(type(x) is int for x in listofrandoms)
print(int_quantity)
##2
string_quantity = sum(type(x) is str for x in listofrandoms)
print(string_quantity)
##3
boolean_quantity = sum(type(x) is bool for x in listofrandoms)
print(boolean_quantity)
