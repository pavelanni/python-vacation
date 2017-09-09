#!/usr/bin/python3

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
    while good_input == False:
        for i, option in enumerate(options, start=1):
            print(i, option)
        choice = input()

        try:
            choice_int = int(choice)
        except  ValueError:
            print("Error: you should enter a NUMBER!")
            continue

        if choice_int <= len(options) and choice_int > 0 :
            good_input = True
        else:
            print("You should enter a number between 1 and ", len(options))

    return choice_int-1


name = input("What's your name: ")

print("Choose your base product from the menu (press the number):")
p_index = menu(products)

print("Choose your flavor from the menu (press the number):")
f_index = menu(flavors)

print("Choose your topping from the menu (press the number):")
t_index = menu(toppings)

print("Hello ", name, "! Here is your order: base product: ", products[p_index], 
  ", flavor: ", flavors[f_index], ", topping: ", toppings[t_index])

f = open("orders.txt", "a+")
f.write(",".join((name, products[p_index], flavors[f_index], toppings[t_index]))+"\n")
f.close()
