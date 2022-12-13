import pandas as pd

print("*******************************")
print()
print(" Railway Reservation System")
print("       ADMIN INTERFACE        ")             
print()
print("    Option 1: List all users")
print()
print("*******************************")
print()

options = [1]

validated_option = False
while True:
    if validated_option:
        print("Invalid option")
    option = int(input("Enter option: "))
    if option in options:
        validated_option = True
        break
    else:
        validated_option = False
        print("Invalid option. Please try again")
        continue

if option == 1:
    print("You have selected option 1")
    print("Here are all the users.")
    print()
    
    print("Name, Age, Phone, Email")
    data= pd.read_csv("database.txt", sep=",", header=None)
    print(data.to_string(index=False, header=False))
    
    print()
