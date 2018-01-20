# Module calculator

MINUS_ONE = -1


# Function: Create age in minutes
def calculate_age_in_minutes(age: int):
    if age > MINUS_ONE: return age * 525600


# Function: Create age in minutes
def calculate_age_in_hours(age: int):
    if age > MINUS_ONE: return age * 8760


# Function: Create age in days
def calculate_age_in_days(age: int):
    if age > MINUS_ONE: return age * 365
