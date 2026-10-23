def damage(damage, speed, time):
  if(damage < 0 or speed < 0):
    return "invalid"
  damage *= speed
  if time == "second":
    return damage
  damage *= 60
  if time == "minute":
    return damage
  else:
    return damage * 60
