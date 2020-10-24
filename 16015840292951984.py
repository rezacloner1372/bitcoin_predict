#!/usr/bin/env python3

from datetime import datetime, date

print("Your date of birth (yyyy/mm/dd)")
try:
    date_of_birth = datetime.strptime(input("--->"), "%Y/%m/%d")
    def calculate_age(born):
        today = date.today()
        print(today.year - born.year - ((today.month, today.day) < (born.month, born.day)))
    age = calculate_age(date_of_birth)

except ValueError:
    print('WRONG')

