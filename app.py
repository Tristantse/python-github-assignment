print("Welcome to my Python program project!")
Hours = Input("How many hours did you work today? ")
Hours = float(Hours)
weekly_hours = Hours * 7
print(f"You are on pace to work {weekly_hours} hours this week!")
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
    