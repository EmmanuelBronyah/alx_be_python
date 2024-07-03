FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  print(f'{float(fahrenheit)}°F is {float((fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR)}°C')
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  print(f'{float(celsius)}°C is {float(CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32)}°F')
  return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32

temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

if unit == "C".lower():
  convert_to_fahrenheit(temperature)
elif unit == "F".lower():
  convert_to_celsius(temperature)
else: 
  print("Invalid temperature. Please enter a numeric value.")