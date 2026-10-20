def calculator(num1, operator, num2):
  
  def add(num1, num2):
    return num1 + num2
  
  def subtract(num1, num2):
    return num1 - num2
  
  def divide(num1, num2):
    if num2 == 0:
      return "Can't divide by 0!"
    return num1 / num2
  
  def multiply(num1, num2):
    return num1 * num2
    
  if operator == '+':
    return add(num1, num2)
  if operator == '-':
    return subtract(num1, num2)
  if operator == '/':
    return divide(num1, num2)
  if operator == '*':
    return multiply(num1, num2)
    
