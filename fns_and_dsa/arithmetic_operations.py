def perform_operation(num1, num2, operation):
  
  if operation == "add":
    result = float(num1) + float(num2)
    return result
  elif operation == "subtract":
    result = float(num1) - float(num2)
    return result
  elif operation == "multiply":
    result = float(num1) * float(num2)
    return result
  elif operation == "divide":
    if num2 == 0:
      result = "Cannot divide by zero."
      return result
    else:
      result = float(num1) / float(num2)
      return result