def validate():
    ##mylist = [1,2,3,4,5,6]
    personalcode_input = input("Iveskite asmens koda: ")

    if len(personalcode_input) == 11:
        personalcode_list = list(map(int, str(personalcode_input[0:])))
        if personalcode_list[0] >= 1 and personalcode_list[0] <=6:
            print("pavyko")
        else:
            print("nepavyko")
    else:
        print("Kodas ne 11 asmenu ilgio")
    # if len(personal_code) != 11:
    #     return False
    # elif personal_code[0] <= 0 or personal_code[0] > 6:
    #     print("POabyko")
    # else:
    #     return True


result = validate()