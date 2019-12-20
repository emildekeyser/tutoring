# don't forget to cast the inputs to the correct type: float
x1_coordinate = float(input("Enter x-coordinate of the first vector: "))
y1_coordinate = float(input("Enter y-coordinate of the first vector: "))
x2_coordinate = float(input("Enter x-coordinate of the second vector: "))
y2_coordinate = float(input("Enter y-coordinate of the second vector: "))

inner_product = x1_coordinate * x2_coordinate + y1_coordinate * y2_coordinate
print("Inner product is: " + str(inner_product))
