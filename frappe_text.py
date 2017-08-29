#!/usr/bin/python3
import sys
import pickle


products = ["chocolate", "coffee"]
flavors = ["caramel",
           "butterscotch",
           "strawberry",
           "raspberry",
           "blueberry",
           "sweetstrawberry",
           "marshmallow",
           "plain"]
toppings = ["chocolate", "sweetstrawberry"]
orders = []


def choice(options):
    for i in range(len(options)):
        print(i+1, options[i])
    input_is_valid = False
    while input_is_valid == False:
        user_input = input()
        try:
            val = int(user_input)
            if val > 0 and val <= len(options):
                input_is_valid = True
            else:
                print("Sorry, the number must be between 1 and ", len(options))
        except:
            print("Sorry, you must enter a number!")

    return (val-1)

def take_order():
    first_name = input("What's your name? ")
    first_name = first_name.capitalize()

    print("Would you like COFFEE or CHOCOLATE?")
    p = choice(products)

    print("What would you like your FIRST flavor to be? Type the number: ")
    f1 = choice(flavors)

    print("What would you like your SECOND flavor to be? Type the number: ")
    f2 = choice(flavors)

    print("What would you like for your TOPPING? Type the number: ")
    t = choice(toppings)

    print("Customer name: -- ",first_name)
    print("Base Product: --- ",products[p].upper())
    print("First Flavor: --- ", flavors[f1].upper())
    print("Second Flavor: -- ", flavors[f2].upper())
    print("Topping: -------- ", toppings[t].upper())

    orders.append([first_name, p, f1, f2, t])

def list_orders():
    for o in orders:
        print("Customer name: -- ",o[0])
        print("Base Product: --- ",products[o[1]].upper())
        print("First Flavor: --- ", flavors[o[2]].upper())
        print("Second Flavor: -- ", flavors[o[3]].upper())
        print("Topping: -------- ", toppings[o[4]].upper())
        print("======================================================")

    print("That's all!")


try:
    with open('my_pickled_list.pkl', 'rb') as f:
        orders = pickle.load(f)
except EnvironmentError:
    print("No file found. Will create a new file.")

while True:
    print("Welcome To Erik's Cafe!")
    print("N -- New order")
    print("L -- List All Orders")
    print("X -- Exit")
    user_input = input()
    if user_input == "N" or user_input == "n":
        take_order()
    elif user_input == "L" or user_input == "l":
        list_orders()
    elif user_input == "X" or user_input == "x":
        with open('my_pickled_list.pkl', 'wb') as f:
            pickle.dump(orders, f)
        print("Thank you for visiting, please come again!")
        sys.exit()
    else:
        print("Please enter 'N', 'L' or 'X'!")
