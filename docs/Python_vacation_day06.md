# Python Vacation --- Day 6

## More Functions and Main Menu

"So, what did we learn yesterday?" I asked Erik the next day.

"We printed out all orders from the file."

"Right. When would you need it?" I tried to show the "business value" of it to Erik.

"When I collected all orders from my friends and got back home, I need a list of what I have to prepare and who's ordered what."

"So it would be nice to have such a function in your program, right? Before that your application had only one function: to get the order. Now we can add another function: list orders. And we have to add a main menu to choose from those functions. This is how most applications work, right? They give you a choice of several functions."

"Wait, but I have only one function for the menu. The rest is just my program which gets orders. Do you mean I have to make it a function?" asked Erik.

"Exactly! Usually your main program doesn't do anything except calling various functions. And functions can call other functions too. In our case we'll write a function to get orders and it will call the `menu()` function which you have created already. Also you'll write a function to list the orders and a main menu function."

"So many functions!" sighed Erik. "Okay, let me start with the first one which gets orders. I think I only have to add the word `def` to my code."

"Almost. Don't forget to name your function and don't forget to indent the code."

Erik started working. He called his function `get_order()` and moved the lines of code to make a proper indentation.

"What should I return from this function?" asked Erik. "In the `menu()` function we returned the flavor number, but what should we do here?"

"You don't _have_ to return anything. Usually when you return something from a function you are going to use this value somehow. Like with our `menu()` function we assigned the flavor number to a variable and then used it to get the flavor from the list. In this case we aren't going to use anything from this function so we can just place `return` at the end, or nothing at all. Functions like this often return some code to indicate if the operation was successful."

"Like opening a file?" asked Erik.

"Yes, exactly. We can analyze the code to decide if we can move forward or do something else. For simplicity in this project we are not going to do this. I suggest you just place `return` at the end as a reminder that some day we _might_ want to return a code."

Erik finished his function and got the following:

```python
def get_order():
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

    return
```

"Okay," I said, "now we have to create a `list_orders()` function. Remember, yesterday we did it in IPython dialog, now put it into a function. Then we can start working on the main menu."

Luckily, the window with our yesterday's IPython session was still open on the Erik's computer, so it was pretty easy for him to copy the code. Here is his function to list all orders:

```
def list_orders():
    f = open("orders.txt", "r")
    for line in f:
        name, product, flavor, topping = line.strip('\n').split(',')
        print("Dear ", name, "here is your order:")
        print("Base product: ", product)
        print("Flavor: ", flavor)
        print("Topping: ", topping)
        print("Guten Appetit!")
``` 

"Now I have only functions!" said Erik. "Should I write a menu to call them now?"

"Yes, it's going to be our main menu. Think about options you want to include in it."

"That's easy," said Erik. "Press 'N' to place a new order, press 'L' to list all orders, press 'X' to exit. It will be similar to the flavors menu."

"Yes," I said. "You can make it function, too. Usually in Python programs everything is a function and the main program just calls them. Let me show how we usually do it in Python."

```
if __name__ == "__main__":
    main_menu()
``` 

"Yes, I  understand that everything is a function. But why don't you just call `main_menu()`, why do you use this `if` and these strange names with underscores?" asked Erik.

"This is something we haven't talked about yet. When you write a Python application there is a good chance it's going to have several _modules_. Usually people group functions into files--this is what we call modules. When you want to use those functions, you have to _import_ that module. But the same module can be executed as a separate program too. For example, there is a module called `calendar` which you can import and use to calculate what day of the week was that specific date."

"Like my birthday?"

"Oh, I remember it vividly---it was Sunday. I don't need to calculate it. But also you can use this module as a standalone program. Run `python -m calendar`."

Erik entered this command and got a nicely formatted calendar for this year on the screen.

"So you see: you can run it as a program _or_ you can import and use functions from it. In your case, you've already written a couple of functions, who knows---they might be so good that you want to use them in your future programs. Or somebody else will use them. Then they will import your module. But now we want to run it as a standalone program, that's why we include this `if` in it. It tells Python that if we a running it as a standalone program, then it should execute the `main_menu()` function. If it's just imported---then it will not be execured. Later we will do more experiments with this, but for now just add these two lines at the end of the file and write your `main_menu()` function _above_ them. Usually in Python we define functions before calling them."

Erik listened to me, but I could tell from looking at his face that it was not 100% clear to him. "Okay," I said, "don't worry too much about that right now. Just write the main menu and don't forget to check user's input, okay?"

"Okay," answered Erik and started to type. 10 minutes later his main function looked like this:

``` python
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
        else:
            print("Please enter 'N', 'L' or 'X'!")

He tried to run it and everything was fine: he placed an order, he listed all orders... Then he said: "I can't exit! I pressed 'X' and got back to the menu!"

"Let's look at your code," I said. "You see, you are running an infinite loop and you don't have any way to exit it. When the user presses 'X' you should tell Python that you want to exit the loop. And the whole program too."

"How do I do that?"

"We have to use a system function called `exit()`. It belongs to a module called `sys`, so you have to import it first. We didn't do that before, but it's easy. Just go to the beginning of the file and type `import sys` after the first line with `/usr/bin/python3`. Then, right after printing 'Thank you', call the function as `sys.exit()`."

Erik added these two lines and tested his application again. It worked perfectly! And it looked like a real one!

"Are you happy now?" I asked.

"Yes, it works! Wow, and I wrote it myself! You see, almost 100 lines of code---it's a big program! You were right---it's so much better when you write something useful instead of those stupid exercises!"

"Don't say that about exercises, they are good," I said. "Without them I had to explain all the basics to you from the very beginning."

"But how can I use this program on my iPad?" Erik changed the topic. "I remember you told me it is possible to run it online and use my browser to take orders."

"Yes, of course it's possible," I was glad he didn't want to stop here. That meant we have more opportunities to explore Python together. "We have developed the main logic of your application, we can store your orders in the file. Now we are ready to convert it to a web application! Next time we'll start working on it. Now go ahead and tell your friends about your huge success."

"I will," said Erik and off he went.

