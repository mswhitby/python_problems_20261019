import math
def circle_or_square(rad, area):
  if(rad*2*3.14 > math.sqrt(area)*4):
    return True
  else:
    return False
