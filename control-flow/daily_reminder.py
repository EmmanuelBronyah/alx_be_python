task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")

time_bound = input("Is it time-bound? (yes/no): ")

reminder = f"Reminder: '{task}' is a {priority} priority task"

match priority:
  case "high":
    if time_bound == "yes":
      reminder = reminder + " that requires immediate attention today!"
      print(reminder)
    elif time_bound == "no":
      reminder = reminder + ". Consider completing it when you have free time."
      print(reminder)
  case "medium":
    if time_bound == "yes":
      reminder = reminder + " that requires immediate attention today!"
      print(reminder)
    elif time_bound == "no":
      reminder = reminder + ". Consider completing it when you have free time."
      print(reminder)
  case "low":
    if time_bound == "yes":
      reminder = reminder + " that requires immediate attention today!"
      print(reminder)
    elif time_bound == "no":
      reminder = reminder + ". Consider completing it when you have free time."
      print(reminder)