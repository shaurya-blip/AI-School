#######################################
# RAILWAY MANAGEMENT SYSTEM
# WRITTEN BY SHAURYA P SINGH
# AND THORIN SON OF THROR
#
# This is a railway management system
# that allows users to create a user
# and book a ticket.(WIP)
#######################################

import re
import random
import json

options = [1]

def ask_for_option():
    validated_option = False
    try:
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
    except KeyboardInterrupt:
        print("\n\nExiting...")
        exit()
    
    return option

def create_user_page(if_incorrect=False):
    print("\033c")
    
    if if_incorrect:
        print("Sorry to hear that!")
        print("Please try again.")
    else:
        print("Welcome to the user creation page!")
        print("Pleas enter the following details.")
    
    validated_option_1 = False
    while True:
        if validated_option_1:
            print("Invalid option")
        name = input("Enter name: ")
        if not bool(re.search(r'\d', name)):
            validated_option_1 = True
            break
        else:
            validated_option_1 = False
            print("Invalid name. Please try again")
            continue
    
    validated_option_lmao = False
    while True:
        if validated_option_lmao:
            print("Invalid option")
        age = input("Enter age: ")
        if age.isdigit():
            validated_option_lmao = True
            break
        else:
            validated_option_lmao = False
            print("Invalid age. Please try again")
            continue
    
    validated_option_2 = False
    while True:
        if validated_option_2:
            print("Invalid option")
        phone = input("Enter phone number: ")
        if len(phone) == 10 and phone.isdigit():
            validated_option_2 = True
            break
        else:
            validated_option_2 = False
            print("Invalid phone number. Please try again")
            continue
        
    
    validated_option_3 = False
    while True:
        if validated_option_3:
            print("Invalid option")
        email_id = input("Enter email id: ")
        if "@" in email_id:
            validated_option_3 = True
            break
        else:
            validated_option_3 = False
            print("Invalid email id. Please try again")
            continue
    
    print()
    print("Customer has been registered!")
    print("Name: ", name)
    print("Age: ", age)
    print("Phone: ", phone)
    print("Email: ", email_id)
    print()
    
    validated_option_4 = False
    while True:
        if validated_option_4:
            print("Invalid option")
        response = input("If the following details above are correct, please enter 'y' to continue: ")
        if "y" == response:
            validated_option_4 = True
            break
        elif "n" == response:
            print("So sorry to hear that! Please try again.")
            create_user_page()
        else:
            validated_option_4 = False
            print("Please try again")
            continue
            
    dict1 = {
        "user_id":name+str(random.randint(1000, 9999)),
        "name":name,
        "age":age,
        "phone":phone,
        "email":email_id
    }
    
    in_file = open("db.json", "r")
    list = json.load(in_file)
    in_file.close()
        
    list_lmao = list.append(dict1)

    out_file = open("db.json", "w")
    json.dump(list_lmao, out_file, indent=4)
    out_file.close()
    
    print("User has been registered!")
    print("Thank you for registering with us!")
    print("Redirecting to main page...")
    ask_for_option()
    return dict1


def save_db(dict, fp):
    with open(fp, "w") as f:
        json.dump(dict, f, indent=4)

def run_option(option_key):
    if option_key in options:
        if option_key == 1:
            print("You have selected option 1")
            print("You will be redirected to the create user page")
            create_user_page()

def create_user_menu(dicts):
    append_str = ""
    
    for dict in dicts:
        append_str += "    Option "+str(dict["option"]) + ": " + dict["name"] + " " + "\n"
        
    print("*******************************")
    print()
    print(" Railway Reservation System")
    print("        By Shaurya             ")
    print()
    print(append_str)
    print()
    print("*******************************")
    print()
