#importing the Mat class
from math import pi

# Finction that calculates the area of the given circle a radius
# r parameter that is the radius of the circle
def area_of_circle(r):
    return pi * r ** 2

#Function that read of the keyboard the radio of the circle,
# radius is greater of 10
def readOnlyGreater10():
    while True:
        print("Please enter the radius of the circle value only greater of 10")
        cant = input()
        try:
            cant = int(cant)
            if cant > 10:
                return cant
            else:
                print("ATTENTION: only greater of 10.")
        except ValueError:
            print("ATTENTION: You must enter a whole number.")


#Use of the functions
radius=readOnlyGreater10()
print(f"The area of the circle with radios {radius} is: ",area_of_circle(radius))
