from math import sqrt, atan, degrees

x_coordinate = float(input("Enter the x-coordinate: "))
y_coordinate = float(input("Enter the y-coordinate: "))

x_squared = x_coordinate ** 2
y_squared = y_coordinate ** 2
radius = sqrt(x_squared + y_squared)
theta_in_radians = atan(x_coordinate / y_coordinate)
theta_in_degrees = degrees(theta_in_radians)

print("The radius is: " + str(radius))
print("Theta is: " + str(theta_in_degrees))
