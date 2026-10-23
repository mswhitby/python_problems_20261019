def area_of_country(name, area):
  total = 148940000
  percent = round(area/total*100,2)
  return name + " is "+ str(percent) +"% of the total world's landmass"
