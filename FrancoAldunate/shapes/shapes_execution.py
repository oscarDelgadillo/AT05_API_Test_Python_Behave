# Module execution

from AT05_API_Test_Python_Behave.FrancoAldunate.shapes.area import circle_area
from AT05_API_Test_Python_Behave.FrancoAldunate.shapes.perimeter import circle_perimeter


# Function: Print perimeter and area of circle
def print_data():
    radius = float(input("Insert radius: "))
    print(f"Circle with Radius = {radius}:")
    print("area", circle_area(radius))
    print("perimeter", circle_perimeter(radius))


print("Execution...")
print_data()
