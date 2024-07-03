FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_fahrenheit(celsius):
  result = CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32
  print(f'{float(celsius)}°C is {float(result)}°F')
  return result

def convert_to_celsius(fahrenheit):
  result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  print(f'{float(fahrenheit)}°F is {float(result)}°C')
  return result

temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

if unit == "C".lower():
  convert_to_fahrenheit(temperature)
elif unit == "F".lower():
  convert_to_celsius(temperature)
else: 
  print("Invalid temperature. Please enter a numeric value.")