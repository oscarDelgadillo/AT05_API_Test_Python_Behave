#the function returns the number of days that the month contains
# If the name of the month is invalid returns nome
# Param month is the name of the month

def daysInMonth(month):
    monthDict={'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31,
               'August': 31, 'September':30, 'October':31, 'November':30, 'December':31}
    if month in monthDict.keys():
        return  monthDict[month]
    else:
        return "None"

month="February"
print (f"Days of the month of {month} is: ", daysInMonth(month))
month="March"
print (f"Days of the month of {month} is: ", daysInMonth(month))
month="May"
print (f"Days of the month of {month} is: ", daysInMonth(month))
month="Mayy"
print (f"Days of the month of {month} is: ", daysInMonth(month))