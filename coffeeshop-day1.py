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

for i, product in enumerate(products, start=1):
    print(i, product)

for i, flavor in enumerate(flavors, start=1):
    print(i, flavor)

for i, topping in enumerate(toppings, start=1):
    print(i, topping)