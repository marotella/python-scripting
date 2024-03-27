user_input = input("How far do you wnat to travel in miles? ")
user_miles = int(user_input)
if user_miles < 3:
    print("Walk.")
    
elif user_miles < 300:
    print("drive")
else:
    print("fly")