import math
import datetime
def inputsum(number1=5, number2=12, number3=33):
    inputsum = number1 + number2 + number3
    return (inputsum)

print(inputsum())
#22222222222222222222222222222222222222222222222
sarasas1 = [1,2,3,4,5,6,7,8,9,10]

def my_list(sarasas1):
    sum+=sarasas1
    return sarasas1
print(sum(sarasas1))
#33333333333333333333333333333333333333333
def maximus (*args):
    print(max(*args))

maximus(1,2,3,4,5,332,231,51231,412,321,21,321,321)
#444444444444444444444444444444444444444444444444
def reverse(word):
    return word[::-1]

text=reverse("Zodis ne zvirblis")
print(text)

#555555555555555555555555555555555555555555555555
def count_words_and_uppercase(text):

    words = text.split()

    uppercase_count = 0
    lowercase_count = 0
    numeric_count = 0
    for character in text:
        if character.isupper():
            uppercase_count += 1
        elif character.islower():
            lowercase_count += 1
        elif character.isnumeric():
            numeric_count += 1

    return len(words), uppercase_count, lowercase_count, numeric_count


tekstas = "asa3s MANTAS2 pasalpa1"
word_count, uppercase_count, lowercase_count, numeric_count = count_words_and_uppercase(tekstas)
print("Word Count: ", word_count)
print("Uppercase Count: ", uppercase_count)
print("Lowercase Count: ", lowercase_count)
print("Numbers in string: ",numeric_count)
#66666666666666666666666666666666666666666666666666666666
sarasas2 = [1,2,1,1,2,3,4,5,6,7,8,9,10,151,515,151]

def my_list(sarasas2):

    sarasas2 = my_list(sarasas2)
    return (sarasas2)
print ("The list after removing duplicates : " + str(set(sarasas2)))
###############################7777777777####################
def prime_numbers(number):
    if number < 1:
        return "Nera pirminis"
    for i in range(2, number):
        if(number % i) == 0:
            return "Nera pirminis"
    return "Pirminis"
###############8888888888888888888888
def reverse_words(words):
    reversed_list = words[::-1]
    return reversed_list

word_list = ["pasalpa", "zodis", "zvirblis", "seat"]
reversed_list = reverse_words(word_list)
print(reversed_list)

#####################999999999999999999
def leap_year():
    input_year = int(input("Iveskite metus: "))
    if (input_year % 400 == 0) or (input_year % 100 != 0 and input_year % 4 == 0):
        print("Metai yra keliamieji.")
    else:
        print("Metai nėra keliamieji.")

leap_year()
#######################10##################

