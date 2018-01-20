from area import area_of_circle
from perimeter import perimeter_of_circle

def readTheRadioOfCircle():
    while True:
        print("Please enter the radio of circle:")
        cant=input()
        try:
            cant = int(cant)
            return cant
        except ValueError:
            print("ATTENTION: You must enter a whole number.")


radio = readTheRadioOfCircle()
print(f"The radio of circle is {radio}, the area is:{area_of_circle(radio)}, and the perimeter is: {perimeter_of_circle(radio)}")