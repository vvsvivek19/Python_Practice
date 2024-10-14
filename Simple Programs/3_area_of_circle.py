from math import pi
radius = float(input("Radius: "))
def circ_area(r):
    area = round((pi * r**2),4)
    return area
area = circ_area(radius)
print("Area: " + str(area))