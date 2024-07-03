def perform_operation(num1, num2, operation):
  
  operations = ["add", "subtract", "multiply", "divide"]
  
  if operation in operations and operation == "add":
    result = float(num1) + float(num2)
    return result
  elif operation in operations and operation == "subtract":
    result = float(num1) - float(num2)
    return result
  elif operation in operations and operation == "multiply":
    result = float(num1) * float(num2)
    return result
  elif operation in operations and operation == "divide":
    if num2 == 0:
      result = "Cannot divide by zero."
      return result
    else:
      result = float(num1) / float(num2)
      return result