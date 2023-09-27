import time

while True:
    try:
        seconds = float(input("Irasykite sekundes: "))
        word = input("irasykite zodi: ")
        input_times = int(input("Iveskite kiek kartu norite kartoti: "))

        for i in range(input_times):
            print(word)
            time.sleep(seconds)

    except ValueError:
        print("Ivedete ne skaiciu. Bandykite dar karta ")

    except KeyboardInterrupt:
        print("Programa issijungia, VISO!")
        break


