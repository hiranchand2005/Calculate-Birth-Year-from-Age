age_years = int(input("How old are you?\n"))
import datetime
now = datetime.datetime.now()
current_year = now.year
print("Your birth year is", current_year - age_years)