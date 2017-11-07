#!/usr/bin/python3
import sys


products = ["chocolate", "coffee"]
flavors = ["caramel",
           "butterscotch",
           "strawberry",
           "raspberry",
           "blueberry",
           "sweetstrawberry",
           "marshmallow",
           "plain"]
toppings = ["chocolate", "sweetstrawberry", "caramel"]


def menu(options):
    good_input = False
    while good_input is False:
        for i, option in enumerate(options, start=1):
            print(i, option)
        choice = input()

        try:
            choice_int = int(choice)
        except ValueError:
            print("Error: you should enter a NUMBER!")
            continue

        if choice_int <= len(options) and choice_int > 0:
            good_input = True
        else:
            print("You should enter a number between 1 and ", len(options))

    return choice_int - 1


def get_order():
    name = input("What's your name: ")

    print("Choose your base product from the menu (press the number):")
    p_index = menu(products)

    print("Choose your flavor from the menu (press the number):")
    f_index = menu(flavors)

    print("Choose your topping from the menu (press the number):")
    t_index = menu(toppings)

    print("Hello ", name, "! Here is your order: base product: ",
          products[p_index], ", flavor: ",
          flavors[f_index], ", topping: ",
          toppings[t_index])

    f = open("orders.txt", "a+")
    f.write(",".join((name,
                      products[p_index],
                      flavors[f_index],
                      toppings[t_index])) + "\n")
    f.close()

    return


def list_orders():
    f = open("orders.txt", "r")
    for line in f:
        name, product, flavor, topping = line.strip('\n').split(',')
        print("Dear ", name, "here is your order:")
        print("Base product: ", product)
        print("Flavor: ", flavor)
        print("Topping: ", topping)
        print("Guten Appetit!")


def main_menu():
    while True:
        print("Welcome To Erik's Cafe!")
        print("N -- New order")
        print("L -- List All Orders")
        print("X -- Exit")
        user_input = input()
        if user_input == "N" or user_input == "n":
            get_order()
        elif user_input == "L" or user_input == "l":
            list_orders()
        elif user_input == "X" or user_input == "x":
            print("Thank you for visiting, please come again!")
            sys.exit()
        else:
            print("Please enter 'N', 'L' or 'X'!")


if __name__ == "__main__":
    main_menu()
