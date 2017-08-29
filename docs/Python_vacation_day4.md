# Python Vacation -- Day 4

"Remember where we stopped last time?" I asked Erik.

"Yes, you said that we are going to work with functions and that will make my program shorter."

"...And easier to read and understand!" added I. "What do you remember about Python functions from your online class?"

"They start with `def`. You have to indent lines inside the function. You can call functions from your main program."

"Good! Also very important that you can pass _parameters_ into functions so you can call them many times and they will do slightly different things depending on the parameters. Like saying 'Hello' and then a person's name."

"Yes, I remember, we did this in our online course!" exclaimed Erik. It was good to see that those couple weeks were not lost completely.

"You said in your program you had to copy and paste some pieces of code several times. What did that code do?"

"Don't you remember?" Erik tried to be patient. "I have three menus in my coffee shop program: one for base product, one for flavor, and one for topping. And in all three menus I have to do that garbage checking, number checking and all that."

"Okay," I said. "Why don't we create a function that will do all these boring things and call it three times?"

"Yes, that would be good. And also if I want to change or add something, I'll do it in one place, instead of copying it three times. But I have different flavors and toppings---how will this function know which menu I want to use?"

"You said you had to change something while copying pieces of code into the menus. What was that?"

"Oh, all different variables. The variable for the `input()` function, the index variable. And also the list name---to print out the menu and to calculate its length."

"Good. So, as far as I can see, the only thing which needs to change is the list of options. It's either base product, flavor, or topping. Input variable and list index can be the reused inside the function. We'll just return the index as a result."

"What do you mean---'return'?" asked Erik.

"Well, imagine I asked you: 'Erik, please go to your room and count how many model planes you have.' You would go and count them and return to me with a number, right? Functions do the same thing: they perform some action and come back with the result. And usually I don't care how they do what I asked them to do, I'm interested in the result. Like when I asked you to count your planes, I don't care if you use your fingers, or a piece of paper, or any more sophisticated method. In our case we have to write a function which will take a list of options, print it out as a menu and let the user chose from the menu. When the user makes their choice---a number in the menu---the function will remember it and bring it to us. There is a special word for that in Python: `return`. We are not going to return the name of a flavor, we'll just return its index in the list."

"Yes, I remember that `return` from the class!" said Erik.

"Good. Now we have to make a very difficult decision: how to name our function. Don't laugh, it is really very serious. When you write programs just a little longer than this one, it's pretty easy to get lost in different variable and function names. So, please, always think about naming. Don't call your functions `f()` or `d4()` --- you will never remember what this means. Choose some meaningful names that show what this function does. The same applies to variables. Only if it's just a simple obscure index in a loop, then it's okay to call it `i` or `k`. In other cases, please use something readable. Also, in Python we use underscore to combine words for variable and function names. Like  `base_product` or `good_input`."

"I saw names without underscores, but with lower and upper case letters," said Erik.

"Yes, it's called CamelCase. You see, it looks like camel humps? In Python we usually use them to define classes. We'll talk about classes later."

"Okay, I'm ready. Let's call our function `menu`. I know that I have to use `def` to start writing it. And also I have to put something inside the parenthesis. Should it be the list of options?"

"Exactly!" said I. I was proud of my boy. You know, teenagers are always like that: sometimes they surprise you with their brilliant minds, but sometimes they struggle with simple arithmetics. "Call it `options`, for example. You do remember that you should put the colon after parenthesis and indent the function body, don't you? You can copy most of the function body from what you have written already. Don't forget to return the index and don't forget that when we show `1` to the user, we have `0` in mind. So add some necessary arithmetics to the function. Enough instructions, go ahead and write it!"

Erik started writing and copying and in a couple minutes his function looked like this:

```
def menu(options):
    good_input = False
    while good_input == False:
        print("Choose your base product from the menu (press the number):")
        for i, option in enumerate(options, start=1):
            print(i, option)
        p = input()

        try:
            p_index = int(p)
        except  ValueError:
            print("Error: you should enter a NUMBER!")
            continue

        if p_index <= len(options) and p_index > 0 :
            good_input = True
        else:
            print("You should enter a number between 1 and ", len(options))

    return p_index-1
```

"What should I do with this prompt? It asks about the base product, but I want to use this function for flavors and toppings too," asked Erik.

I said, "Good question. If you want to reuse your function, you should move everything that is specific to some particular case, outside of the function. I suggest we ask this question _before_ calling the function, in the main program. You will ask about base product and call the function with the list of base products, you ask about flavors and pass the list of flavors as a parameter."

"Okay," said Erik. "I'll remove it. Now I have to rewrite the main program and use function in it, right?"

"Go ahead!"

He started working. After a while he asked, "I use `p_index` both in the function and in the main program. Should I rename it?"

"From Python prespective, that's OK. It sees those variables differently. `p_index` in the main program and `p_index` inside a function are different variables. But from a readability perspective, I'd suggest to rename it inside the function. It's better to avoid using same variable names inside functions and in the main program. Unless, of course, they are as simple as `a`, `i`, `x`, which are usually temporary variables. So, rename it inside the function to something short but meaningful."

"It will be `p_int`," said Erik. Then he thought for a while and said, "But it starts with `p` because I copied it from the products menu. In the function it doesn't make sense anymore. I'll rename `p` to `choice` and `p_index` to `choice_int` because we convert it to integer."

"Great idea!" I said.

He worked a bit more and discovered, "Now I don't have to subtract 1 from the indexes in my final `print`, because I have already done it in the function!"

He finally came up with this:

```
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


print("Choose your base product from the menu (press the number):")
p_index = menu(products)

print("Choose your flavor from the menu (press the number):")
f_index = menu(flavors)

print("Choose your topping from the menu (press the number):")
t_index = menu(toppings)

print("Here is your order: base product: ", products[p_index], 
  ", flavor: ", flavors[f_index], ", topping: ", toppings[t_index])
```

He tested it and it worked perfectly! He even tried to enter "wrong" choices and always received error messages until his choice was "right".

"Congratulations!" I said. "We've covered a lot of stuff during these days and you are moving very quickly. This is great!"

Erik was happy. He was so happy that he even suggested: "I want to add something to the program. Like we did in that online course, I want to ask the customer for his name and then print it out together with his order!"

"Good idea!" I said. After a while his program printed out: `Hello, Erik! Here is your order ...`

"Much better now," I said. "Now, let's plan our next steps."

"What next steps? I thought we are done with this menu. I like it!"

"Yes, but as far as I remember, you have prepared 6 cups of beverage for your friends last time. Which means you have to collect and _save_ all their orders somehow, instead of just printing them out."

"Right... Yes, I understand now. I have to collect orders first and then print them out to know what I have to prepare."

"And to whom to deliver it," added I. "Tomorrow let's try to use files: open, write, read. But this is for tomorrow. Go play outside now."