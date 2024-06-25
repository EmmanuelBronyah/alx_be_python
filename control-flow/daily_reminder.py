task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
  case "high":
    if time_bound == "yes":
      reminder = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
      print(reminder)
    elif time_bound == "no":
      reminder = f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."
      print(reminder)
  case "medium":
    if time_bound == "yes":
      reminder = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
      print(reminder)
    elif time_bound == "no":
      reminder = f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."
      print(reminder)
  case "low":
    if time_bound == "yes":
      reminder = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
      print(reminder)
    elif time_bound == "no":
      reminder = f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."
      print(reminder)