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
toppings = ["chocolate", "sweetstrawberry"]

for i, product in enumerate(products, start=1):
    print(i, product)
p = input()
p_index = int(p)

for i, flavor in enumerate(flavors, start=1):
    print(i, flavor)
f = input()
f_index = int(f)

for i, topping in enumerate(toppings, start=1):
    print(i, topping)
t = input()
t_index = int(t)

print("Here is your order: base product: ", products[p_index-1], 
  ", flavor: ", flavors[f_index-1], ", topping: ", toppings[t_index-1])