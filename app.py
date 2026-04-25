# Welcome message
print("Welcome to my Python program project!")
# Ask for user input
hours = input("How many hours did you work today? ")
# Convert Input and Handle Possible errors
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
# Perform Calculations
weekly_hours = hours * 5
# Display the results
print(f"You are on pace to work {weekly_hours} hours this week!")