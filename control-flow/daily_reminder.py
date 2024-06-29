task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")

time_bound = input("Is it time-bound? (yes/no): ")

match priority:
  case "high":
    reminder = f"Reminder: '{task}' is a {priority} priority task"
    
    if time_bound == "yes":
      reminder = reminder + " that requires immediate attention today!"
      print(reminder)
    elif time_bound == "no":
      reminder = reminder + ". Consider completing it when you have free time."
      print(reminder)
  case "medium":
    reminder = f"Reminder: '{task}' is a {priority} priority task"
    
    if time_bound == "yes":
      reminder = reminder + " that requires immediate attention today!"
      print(reminder)
    elif time_bound == "no":
      reminder = reminder + ". Consider completing it when you have free time."
      print(reminder)
  case "low":
    reminder = f"Reminder: '{task}' is a {priority} priority task"
    
    if time_bound == "yes":
      reminder = reminder + " that requires immediate attention today!"
      print(reminder)
    elif time_bound == "no":
      reminder = reminder + ". Consider completing it when you have free time."
      print(reminder)