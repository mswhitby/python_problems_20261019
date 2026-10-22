import math

def circle_or_square(rad, area):
  circle_circumference = 2 * 3.14 * rad
  square_perimeter = math.sqrt(area) * 4
  
  if circle_circumference > square_perimeter:
    return True
  else:
    return False
