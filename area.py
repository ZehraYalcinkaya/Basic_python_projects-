import math
def calculate_area(radius):
    area = math.pi*radius*radius
    return area


r= int(input('What is the radius of your circle: '))
print(calculate_area(r))    