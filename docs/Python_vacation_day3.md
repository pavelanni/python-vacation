# Python Vacation -- Day 3

## Errors and what to do about them

Next day Erik was in better mood. It seemed he forgot how I tortured his beautiful program. But we were going to talk about errors and exceptions so I had to remind him about yesterday.

"Remember what we did last time?"

"Yes, you did some stupid things with my program. I didn't know that you are so ignorant and have no idea about how to use computers. If the menu says: Choose between 1 and 2, you should press 1 or 2, and not that garbage you typed last time."

"Well, a lot of developers think this way. But life has more variety than a choice between 1 and 2. I told you already that you should expect a stupid user, who doesn't read menus, a hacker who wants to break in, a kid who is just playing with the keyboard. It's all your responsibility to react to bad input and make sure your program doesn't break."

"Okay, okay... You said something about 'exceptions' last time. What is it?"

"There are a lot of situations when a Python program could break. Wrong input, division by zero, wrong list index--if your list has 5 elements and you are trying to access its 10th element. If you don't do anything about these cases, your Python program just breaks and stops. Sometimes it's okay, if something really bad is happening. But most of the times you shouldn't stop your program and just inform the user that an error happened and she should repeat her input. For example, if instead of a number she enters letters, we should tell her that it's not what we expect and return back to the input prompt. By the way, you haven't created an input prompt so far. I think you should add something like 'Please, choose from this list of base products or flavors'. " 

"That's easy," said Erik. "I can do that right now. But I will need your help with those 'excephtions'. And also, how do we return back to the input?"

"What do we use in Python, when we have to repeat something?" asked I.

"A loop?" guessed Erik.

"That's right! But which loop? In this case we have to repeat our input prompt until the user enters the _right_ thing. Or, in other words, while he continues entering the _wrong_ thing. You see where I am going?"

"Of course! It should be a `while` loop!" said Erik.

I decided to help him a little bit. "I suggest using a variable like `good_input` and set it to False initially. Then it will be a condition of the loop: if the input is not good yet, conitnue. If the input is good, i.e. is integer and in the right range, then exit from the loop. Let's put aside the exceptions part for now and work on the number ranges. You know what to check, right?"

"Yes, let me try it," said Erik and started coding.

Here is what he's got:

``` python
good_input = False
while good_input == False:
    print("Choose your base product from the menu (press the number):")
    for i, product in enumerate(products, start=1):
        print(i, product)
    p = input()
    p_index = int(p)
    if p_index < len(products):
        good_input = True
```

"Now try it," said I.

``` console
erik@idea:~$ ./coffeeshop.py
Choose your base product from the menu (press the number):
1 chocolate
2 coffee
99
Choose your base product from the menu (press the number):
1 chocolate
2 coffee
2
Choose your base product from the menu (press the number):
1 chocolate
2 coffee
```

"Hmmm... It doesn't let me enter 2... A-ha, I see! It should be less or _equal_ the length of the array!" 

He changed `<` to `<=` and it worked now. 

"Try minus 3...", I whispered, trying to sound like a voice from the left shoulder.

He entered `-3` and the program was okay with that. "I know, I know," he said and added `and p_index > 0` to that `if` statement. Now it worked fine both for big numbers and negative ones.

I suggested: "It might be a good idea to let people know what's wrong with their input. Like 'You number should be between this and that'. You can use `else` in your `if` statement."

"Good idea!" rejoiced Erik and made his `if` statement look like this:

``` python
    if p_index <= len(products) and p_index > 0 :
        good_input = True
    else:
        print("You should enter a number between 1 and ", len(products))
```

"Great!" said I. "Now you can copy this code to other menus. If you have several similar pieces of code, it's a good practice to make one of them work like you want it to work and then copy it to the other pieces. Even better is to use functions for that, but let's leave it for the other day."

"Can I use the same `good_input` variable for other loops?" he asked. 

"Yes, go ahead. It's a disposable variable, reuse it as you like. No need to create a new one for each loop."

Erik has copied the loop code to the other two menus. Now his program looked like this:

``` python
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


good_input = False
while good_input == False:
    print("Choose your base product from the menu (press the number):")
    for i, product in enumerate(products, start=1):
        print(i, product)
    p = input()
    p_index = int(p)
    if p_index <= len(products) and p_index > 0 :
        good_input = True
    else:
        print("You should enter a number between 1 and ", len(products))

good_input = False
while good_input == False:
    print("Choose your flavor from the menu (press the number):")
    for i, flavor in enumerate(flavors, start=1):
        print(i, flavor)
    f = input()
    f_index = int(f)
    if f_index <= len(flavors) and f_index > 0 :
        good_input = True

good_input = False
while good_input == False:
    print("Choose your topping from the menu (press the number):")
    for i, topping in enumerate(toppings, start=1):
        print(i, topping)
    t = input()
    t_index = int(t)
    if t_index <= len(toppings) and t_index > 0 :
        good_input = True

print("Here is your order: base product: ", products[p_index-1], 
  ", flavor: ", flavors[f_index-1], ", topping: ", toppings[t_index-1])
```

"Well, it works now. Time to talk about Exceptions. Try to run your program again and type some gibberish instead of numbers. Let's see what Python tells us about our input."

Of course, Erik didn't want to see those nasty error messages again, but now he understood the importance of input checking. Or least it seemed so. So he ran the program and typed some letters:

```console
erik@idea:~$ ./coffeeshop.py
1 chocolate
2 coffee
ghkflkjhdg
Traceback (most recent call last):
  File "./coffeeshop-day3.py", line 21, in <module>
    p_index = int(p)
ValueError: invalid literal for int() with base 10: 'ghkflkjhdg'
```

"Look at this last message. You see: Python tells us that we have entered an invalid literal for integer number. Which means: anything besides letters from 0 to 9. Also it's interesting that Python tells us that they are invalid for 'base 10'. Which means for decimal system. If we tried to convert it as a hexadecimal number, some letters wouldn't be complete gibberish. Like for example if you would enter `ffdfdffdfd` and tried to convert it as hexadecimal number (i.e. with base=16), it would be absolutely fine. But I digressed.

"`ValueError` is the word which tells us that there is an exception and we should handle it somehow. There are other errors: `SyntaxError`, `ZeroDivisionError`, `TypeError`... You can find some examples in the Python official tutorial here: (https://docs.python.org/3/tutorial/errors.html). Let's take an example from the tutorial, it does exactly what we want. Look:"

``` python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
```

"Let's do something very similar in your code. But first let's think about this: which input check should come first--checking if we can convert it to an integer or checking if it's in the right range?"

Erik thought for a second and said: "I think checking for gibberish should come first."

"That's right!" I said. "So we ask for input and continue the loop until we see a valid string which we can convert to an integer. And only then, after we converted it, we check if it's in the right range. When changing your code, please keep track of the indents and remember about the flow."

"Yes, sure," said Erik and get to the editor.

