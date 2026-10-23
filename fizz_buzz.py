def fizz_buzz(num):
  str1 = ""
  if(num%3 == 0):
    str1 = str1 +"Fizz"
  if(num%5 == 0):
    str1 = str1+"Buzz"
  if(num%3 != 0 and num%5 != 0):
    str1 = str1 + str(num)
  return str1
