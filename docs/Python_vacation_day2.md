# Python Vacation -- Day 2

## Menus

Next day we started with refreshing our recently acquired Python skills. 

"So, what have we learned yesterday?" I asked Erik.

"Lists! And `enumerate()`!" he answered quickly. 

"Right, that was your last script that used `enumerate()`. What else? Do you remember what we started with?"

"Yes, I remember: we worked with `input()`. We tried to ask questions like 'What flavor do you want?'. But then we decided that menus will work better because people won't order something we don't have."

"Yes, that's right. Now after we have learned how to print out lists and also lists with numbers, we can just add what we learned about `input()` and create our first menu. Why don't you add `input()` after you have listed the choices and get the number your customer pressed? Remember, you have to assign the user's input to a variable? When you got the input, you can print it out."

"Okay," said Erik and started typing. Here is what he's got:

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

for i, product in enumerate(products, start=1):
    print(i, product)
p = input()
print(p)

for i, flavor in enumerate(flavors, start=1):
    print(i, flavor)
f = input()
print(f)

for i, topping in enumerate(toppings, start=1):
    print(i, topping)
t = input()
print(t)
```

He saved the file and ran it in the terminal:

``` console
erik@idea:~$ ./coffeeshop.py
1 chocolate
2 coffee
2
2
1 caramel
2 butterscotch
3 strawberry
4 raspberry
5 blueberry
6 sweetstrawberry
7 marshmallow
8 plain
7
7
1 chocolate
2 sweetstrawberry
1
1
```

"This is good, but in reality you wanted to print out something like 'Here is your order: base product: coffee, flavor: marshmallow, topping: chocolate', right? How would you get products and flavors from the numbers?"

"Yes, you told me yesterday! We'll use them as list indexes!"

"Go ahead!"

Erik came up with this script:

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

for i, product in enumerate(products, start=1):
    print(i, product)
p = input()

for i, flavor in enumerate(flavors, start=1):
    print(i, flavor)
f = input()

for i, topping in enumerate(toppings, start=1):
    print(i, topping)
t = input()

print("Here is your order: base product: ", products[p], 
  ", flavor: ", flavors[f], ", topping: ", toppings[t])
```

He ran it, answered all the questions and got this:

```
Traceback (most recent call last):
  File "./coffeeshop-day2.py", line 26, in <module>
    print("Here is your order: base product: ", products[p], 
TypeError: list indices must be integers or slices, not str
```

"What's this?" he looked puzzled.

"This is your first error message! Congatulations!"

"Why are you so glad??? What's so good about error messages?" Erik was clearly offended. Of course, he was sure that his dad is making fun of him.

"Erik, don't get me wrong. Believe me, I want your application to work as much as you do. That's why I'm glad to see an error message--at least it give us some information. It's much worse when your program just doesn't work and says nothing. Also, you have heard this from me many times already: making mistakes is the best way to learn. Don't worry, we'll fix it."

"But what should we do?"

"You see, in this case Python is pretty clear about what's wrong. It says that list indices must be integers, not strings. Remember, before we started working with menus, when you asked your users about their preferences what did you get?"

"They could answer 'coffee' or 'strawberry'."

"And what are they in Python?"

"Strings?"

"Right, they are strings! And now when your users input '1' or '3', or '7' - they also input _strings_ which consist of numbers. They are not numbers, they are strings consisting of _letters_ '1', '3', '7'. Luckily, in Python we can easily convert them to numbers with function `int()`. You have to do this: take 'p' or 'f' or 't'--the answer you received from the user--and convert it to integer using `int()`. You can do it right after the `input()` call and assign it to something like `p_index`. In Python you can even assign it to the same variable--what used to be a string, becomes integer. But for now let's have separate variables: our program will be more readable this way."

"Like this?"

```python
p_index = int(p)
```

"Yes, exactly."

He made the changes:

``` python
. . .

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

print("Here is your order: base product: ", products[p_index], 
  ", flavor: ", flavors[f_index], ", topping: ", toppings[t_index])
```

...and ran the script:

```
1 chocolate
2 coffee
1
1 caramel
2 butterscotch
3 strawberry
4 raspberry
5 blueberry
6 sweetstrawberry
7 marshmallow
8 plain
5
1 chocolate
2 sweetstrawberry
1
Here is your order: base product:  coffee , flavor:  sweetstrawberry , topping:  sweetstrawberry
```

"Wait! It got it all wrong! I asked for chocolate with blueberry and it gave me coffee with sweetstraberry!"

"First of all, let me ask you: 'Who is that 'it' you are talking about?'"

"Python, of course, who else??"

"Erik, dear, please remember: computer and Python do only what **you** told them to do. If _your_ program doesn't work as expected, please don't blame Python for that. Just try to think: what could be wrong here? You converted the strings to numbers, that's fine. You used those numbers as indexes for your lists..."

"A-ha! I understand now! Yesterday we talked about indexes and that they always start with zero. And we used that `start=1` to make our lists more human-readable. Yes, now I see that it took the _next_ element in all three cases! Okay, I will just subtract 1 from the numbers before using them with lists!"

I suggested: "You can do this even inside the square brackets. No need for a separate line of code for that."

He fixed his code:

``` python
print("Here is your order: base product: ", products[p_index-1], 
  ", flavor: ", flavors[f_index-1], ", topping: ", toppings[t_index-1])
```

...and finally got his order right!

"Let me try your program too," asked I.

"Go ahead, order something," Erik was very proud of his first application.

``` console
erik@idea:~$ ./coffeeshop.py
1 chocolate
2 coffee
fgdhjkfjgd
Traceback (most recent call last):
  File "./coffeeshop-day2.py", line 17, in <module>
    p_index = int(p)
ValueError: invalid literal for int() with base 10: 'fgdhjkfjgd'
```

"WHAT ARE YOU DOING???" Erik was outraged.

"I am testing your program," I answered as calmly as possible.

"But you are not supposed to enter things like that! You see, it clearly indicates that the product number should be either 1 or 2! And not these stupid characters that you entered!"

"But I am just a stupid user, I know nothing about your expectations. And I don't read your menus carefully. Or I am a hacker who tries to break into your program. Or I'm a kid who just likes to play with the keyboard. You as a programmer are responsible for checking if the input is correct."

"But how do I do that?"

"There many ways to check your input. One of them is called 'Exceptions' in Python. And we will talk about it tomorrow. Let me try one more time."

"Yes, but please, use just numbers!"

``` console
erik@idea:~$ ./coffeeshop.py
1 chocolate
2 coffee
99
1 caramel
2 butterscotch
3 strawberry
4 raspberry
5 blueberry
6 sweetstrawberry
7 marshmallow
8 plain
0
1 chocolate
2 sweetstrawberry
356
Traceback (most recent call last):
  File "./coffeeshop-day2.py", line 29, in <module>
    print("Here is your order: base product: ", products[p_index-1], 
IndexError: list index out of range
```

"AGAIN??? You broke it again!"

"You see, Python clearly tells you that the index I've entered is out of range. Which means we have to check the input not only for being a number, but also for being a 'good' number, i.e. being in the range of our lists' indexes. And, as far as you can see, for different lists this range is different."

"Okay, okay, I'll do that. But it's so-o boring to check everything!.."

"I completely agree with you. It's probably the most boring part of programming. But at the same time it's one of the most important parts, if we want to write safe programs and be protected from hacker attacks. Believe it or not, a lot of hacker attacks happen just because programmers didn't check the input.

"Let's leave it for tomorrow. We'll have to do two things: check if the input is an integer number and check if it's in the range of list indexes," with this I felt much better: now we had a plan for tomorrow.

TODO: add links to the examples of hacker attacks
