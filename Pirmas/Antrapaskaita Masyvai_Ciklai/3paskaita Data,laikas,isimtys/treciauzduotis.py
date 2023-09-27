import datetime
import math

now = datetime.datetime.today()

days_to_month = 0.03287671
seconds_to_hours = 0.00027778
seconds_to_minutes = 0.01666667
while True:
    try:
        input_first_date = input("iveskite pirma data, formatu - (2000/01/01 12:00:00) : ")
        start_date = datetime.datetime.strptime(input_first_date, "%Y/%m/%d %H:%M:%S")

        time_past_all = now - start_date
        print(f"praejo laiko: {time_past_all}")

        time_past_year = time_past_all.days/365
        print(f"Praejo metu:  {math.floor(time_past_year)}")

        time_past_month = time_past_all.days * days_to_month
        print(f"Praejo menesiu: {math.floor(time_past_month)}")

        time_past_days = time_past_all.days
        print(f"Praejo dienu: {math.floor(time_past_days)}")

        time_past_hours = time_past_all.total_seconds() * seconds_to_hours
        print(f"Praejo valandu: {math.floor(time_past_hours)}")

        time_past_minutes = time_past_all.total_seconds() * seconds_to_minutes
        print(f"Praejo minuciu: {math.floor(time_past_minutes)}")

        time_past_seconds = time_past_all.total_seconds()
        print(f"Praejo sekundziu:{math.floor(time_past_seconds)}")

        break
    except ValueError:
        print("Blogas formatas! Iveskite skaiciu ")

        #time_past_days = time_past_all - start_date.day
        # print(f"Praejo dienu: {time_past_days}")
        #
        # time_past_hours = now.hour - start_date.hour
        # print(f"Praejo valandu: {time_past_hours}")
        #
        # time_past_minutes = now.minute - start_date.minute
        # print(f"Praejo minuciu: {time_past_minutes}")
        #
        # time_past_seconds = now.second - start_date.second
        # print(f"Praejo sekundziu: {time_past_seconds}")