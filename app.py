print("Welcome to my Python program project!")
hours = input("How many hours did you work today? ")
hours = float(hours)
weekly_hours = hours * 7
print(f"You are on pace to work {weekly_hours} hours this week!")
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
