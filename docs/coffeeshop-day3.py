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


good_input = False
while good_input is False:
    print("Choose your base product from the menu (press the number):")
    for i, product in enumerate(products, start=1):
        print(i, product)
    p = input()

    try:
        p_index = int(p)
    except ValueError:
        print("Error: you should enter a NUMBER!")
        continue

    if p_index <= len(products) and p_index > 0:
        good_input = True
    else:
        print("You should enter a number between 1 and ", len(products))

good_input = False
while good_input is False:
    print("Choose your flavor from the menu (press the number):")
    for i, flavor in enumerate(flavors, start=1):
        print(i, flavor)
    f = input()

    try:
        f_index = int(f)
    except ValueError:
        print("Error: you should enter a NUMBER!")
        continue

    if f_index <= len(flavors) and f_index > 0:
        good_input = True
    else:
        print("You should enter a number between 1 and ", len(flavors))


good_input = False
while good_input is False:
    print("Choose your topping from the menu (press the number):")
    for i, topping in enumerate(toppings, start=1):
        print(i, topping)
    t = input()

    try:
        t_index = int(t)
    except ValueError:
        print("Error: you should enter a NUMBER!")
        continue

    if t_index <= len(toppings) and t_index > 0:
        good_input = True
    else:
        print("You should enter a number between 1 and ", len(toppings))

print("Here is your order: base product: ", products[p_index-1],
      ", flavor: ", flavors[f_index-1], ", topping: ", toppings[t_index-1])
