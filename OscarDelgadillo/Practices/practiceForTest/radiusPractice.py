import mod.calculateArea, mod.calculatePerimeter

# Create a script to ask to the user of the radio and print both results.

print("Insert the radius of the circle: ", end='')
radius = float(input())

print("Area :", mod.calculateArea.calcAreaCircle(radius))
print("Perimeter :", mod.calculatePerimeter.calcPerimeterCircle(radius))
