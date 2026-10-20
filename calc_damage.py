def damage(damage, speed, time):
  if time == "second":
    multiplier = 1
  elif time == "minute":
    multiplier = 60
  elif time == "hour":
    multiplier = 3600
  else:
    multiplier = 0
    
  if damage < 0 or speed < 0: 
    return "invalid"
    
  return damage * speed * multiplier
