def calculateAgeInDays(age):
    return age * 365


def calculateDaysInHours(days):
    return days * 24


def calculateHoursInMinutes(hours):
    return hours * 60


def calculateAge(age):
    days = calculateAgeInDays(age)
    hours = calculateDaysInHours(days)
    minutes = calculateHoursInMinutes(hours)
    print("The {0} years old:".format(age))
    print('Days :', days)
    print('Hours :', hours)
    print('Minutes :', minutes)