def perform_operation(num1, num2, operation):
  
  match operation:
    case "add":
      result = float(num1) + float(num2)
      return result
    case "subtract":
      result = float(num1) - float(num2)
      return result
    case "multiply":
      result = float(num1) * float(num2)
      return result
    case "divide":
      if num2 == 0:
        result = "Cannot divide by zero."
        return result
      else:
        result = float(num1) / float(num2)
        return result