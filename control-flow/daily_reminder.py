task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")

time_bound = input("Is it time-bound? (yes/no): ")

match priority:
  case "high":
    reminder = ""
    
    if time_bound == "yes":
      reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
      print(reminder)
    elif time_bound == "no":
      reminder = f"Note: '{task}' is a high priority task. Consider completing it when you have free time."
      print(reminder)
  case "medium":
    reminder = ""
    
    if time_bound == "yes":
      reminder = f"Reminder: '{task}' is a medium priority task that requires immediate attention today!"
      print(reminder)
    elif time_bound == "no":
      reminder = f"Note: '{task}' is a medium priority task. Consider completing it when you have free time."
      print(reminder)
  case "low":
    reminder = ""
    
    if time_bound == "yes":
      reminder = f"Reminder: '{task}' is a low priority task that requires immediate attention today!"
      print(reminder)
    elif time_bound == "no":
      reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
      print(reminder)