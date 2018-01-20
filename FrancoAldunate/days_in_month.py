# Practice
print("Practice: Days in Month")
# Write a function days_in_month which takes the name of a month, and returns the number of days in the month.
# Ignore leap years:
#		days_in_month("February") == 28
#       days_in_month("December") == 31
# If the function is given invalid arguments, it should return None.
print("1. Function that returns the number of days for a month given")

ONE = 1
SEVEN = 7
EIGHT = 8
TWELVE = 12


def days_in_month(month):
    print(f"Month: {month}")
    months = ["January", "March", "May", "July", "August", "October", "December"
        , "April", "June", "September", "November", "February"]
    if month in months:
        index = months.index(month) + ONE
        if index < EIGHT:
            return 31
        elif SEVEN < index < TWELVE:
            return 30
        else:
            return 28


print("days = ", days_in_month("January"))
print("days = ", days_in_month("February"))
print("days = ", days_in_month("November"))
print("days = ", days_in_month("Decmber"))
