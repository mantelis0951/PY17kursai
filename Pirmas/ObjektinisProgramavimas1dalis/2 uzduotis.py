import datetime

now = datetime.datetime.today()

month_to_days = 0.03287671
seconds_to_hours = 0.00027778
seconds_to_minutes = 0.01666667

class Sukaktis:
    def __init__(self, years, month, days, hours, minutes, seconds):
        self.years = years
        self.month = month
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def years_difference(self):
        today = datetime.datetime.today()
        sukaktis_date = datetime.datetime(self.years, self.month, self.days, self.hours, self.minutes, self.seconds)
        years_difference = today - sukaktis_date
        return years_difference.days

    def counting_years(self):
        years = self.years_difference()/365
        print(f"Years since the anniversary: {int(years)}")

    def counting_months(self):
        month = self.years_difference() * month_to_days
        print(f"Month since the anniversary:{int(month)}")

    def counting_day(self):
        days = self.years_difference()
        print(f"days since the anniversary: {int(days)}")

    def counting_hours(self):
        hours = self.years_difference() * 24
        print(f"hours since the anniversary:{int(hours)}")

    def counting_minutes(self):
        minutes = self.years_difference() * 1440
        print(f"minutes since the anniversary:{int(minutes)}")

    def counting_seconds(self):
        seconds = self.years_difference() * 86400
        print(f"seconds since the anniversary:{seconds}")

    # def leap_year(self):
    #     input_year = int(input("Iveskite metus: "))
    #     if (input_year % 400 == 0) or (input_year % 100 != 0 and input_year % 4 == 0):
    #         print("Metai yra keliamieji.")
    #     else:
    #         print("Metai nėra keliamieji.")

    # leap_year()

while True:
    input_anniversary_date = input("Enter anniversary date (yyyy-MM-dd HH:mm:ss) : ")
    try:
        anniversary_date = datetime.datetime.strptime(input_anniversary_date, "%Y-%m-%d %H:%M:%S")
        anniversary = Sukaktis(anniversary_date.year, anniversary_date.month, anniversary_date.day, anniversary_date.hour,
                                  anniversary_date.minute, anniversary_date.second)

        anniversary.counting_years()
        anniversary.counting_months()
        anniversary.counting_day()
        anniversary.counting_hours()
        anniversary.counting_minutes()
        anniversary.counting_seconds()
        # anniversary.leap_year()

    except ValueError:
        print("Bad input. Try Again..")