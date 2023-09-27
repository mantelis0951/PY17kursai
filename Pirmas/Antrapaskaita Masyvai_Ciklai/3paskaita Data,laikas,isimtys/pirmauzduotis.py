import datetime

while True:
    try:
        input_first_date = input("iveskite pirma data, formatu - (2000/01/01) : ")
        input_second_date = input("Iveskite antra data, formatu - (2000/01/01) : ")
        start_date = datetime.datetime.strptime(input_first_date, "%Y/%m/%d")
        end_date = datetime.datetime.strptime(input_second_date,"%Y/%m/%d")

        all_seconds = end_date - start_date
        print(f"Laikas sekundemis: {all_seconds.total_seconds()}")
        break
    except ValueError:
        print("Blogas formatas! Iveskite skaiciu ")