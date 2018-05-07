# Python Vacation -- Day 1

## Text dialogs

Next day we decided to get right to the Coffee Shop application. Erik has done enough simple exercises already and was eager to write something useful.

"Remember what we did yesterday to take orders from the customers?"

"Yes, we used the `input()` function."

"And then?"

"And then we saved the input to a variable and then printed it like 'You've ordered this and that'. "

"Okay, good. Now let's do the same thing in the script. Open a new file and save it right away. You know, I don't like when you have a bunch of files called `Untitled` in your home directory."

Erik created a file and saved it as `coffeeshop.py`.

"What should be at the beginning of each Python script?" I asked.

"Something about python3 with some cryptic letters in the beginning. Let me check in my `hello.py` file. Oh, right, it should be `#!/usr/bin/python3`. "

"You're right! I'm sure pretty soon you will write it without a cheat sheet! Now write the `input()` dialog, like you did yesterday in the console session. Remember?"

"Yes!" said he and started typing. A couple of minutes later he showed me the script.

``` python
#!/usr/bin/python3
answer = input("Do you want coffee or chocolate?")
flavor = input("What flavor do you want?")
topping = input("What topping do you want?")
print("You have ordered ", answer, " with ", flavor, " flavor and ", topping, " topping. Thanks!")
```

"Good. Let's run it! Remember what to do? You have already placed the python3 string in the beginning, and now you have to do `chmod a+x coffeeshop.py`. Go ahead and then run the script."

``` console
erik@idea:~$ chmod a+x coffeeshop.py
erik@idea:~$ ./coffeeshop.py
Do you want coffee or chocolate?coffee
What flavor do you want?strawberry
What topping do you want?chocolate
You have ordered coffee with strawberry flavor and chocolate topping. Thanks!
erik@idea:~$
```

"Wow, it works! Great job, Erik!"

"Yeah, I copy-pasted the commands from our yesterday session. I didn't close that window," and he smiled as if he has cheated a little.

"That's okay," I said. "There is a saying among programmers: "DRY - Don't Repeat Yourself." So there is nothing wrong with reusing your work. Now let's see how we can improve it. What do you think?"

"I see that they can order a flavor or topping which I don't have. And also it takes too long to type `strawberry`."

"So, what would be your solution?" I asked.

"I would give them a list of flavors and toppings to choose from and ask to type a letter."

"Good solution. But there could be different flavors with the same first letter... For simplicity let's use numbers. Like if you want strawberry flavor, press '2' or something like that. Will this work for you?"

"Yes, that's okay," said Erik. "What should I do now?"

"First, we have to create lists of your flavors and toppings. And your base product--coffee or chocolate--should also be a list. Do you remember how to create lists in Python?"

"With square brackets?"

"Yes! And don't forget that each element inside the brackets should be in quotes. Single quotes or double quotes---whatever you prefer. Let's put the lists at the beginning of the script. Right after the first line make an empty line and put your lists after it."

"Okay," he said and typed:

``` python
#!/usr/bin/python3

products = ["chocolate", "coffee"]
flavors = ["caramel","butterscotch","strawberry","raspberry","blueberry","marshmallow","plain"]
toppings = ["chocolate", "sweetstrawberry", "caramel"]
```

"Good, but let's make a little bit better. Remember, in Python, we want to make programs readable. We are very specific when it comes to spaces, tabs, indents. There is even a document which tells people how to make the code more readable. It's recommended to follow some simple rules. For example, one of the rules is not to make lines longer than 80 characters. You see, in your code, the `flavors` list is too long. Why don't we place every flavor on a separate line? Just make sure you place them one under another. With `gedit` you will use spaces, but other editors usually do it for you."

After tapping [Space] and [Enter] several times Erik came up with this:

``` python
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
```

"Much, much better," I said. "Also, as we are talking about readability, let's rename the variable `answer` to `product`. It will make more sense, don't you agree?"

"Okay, done. What's next? Somehow I should print products, flavors, and toppings and then ask for input, right?"

"Right! How do you print a list line by line? What in Python can do things several times in a row?"

"A loop?"

"Right, a loop. But which loop? What kinds of loops do you know in Python?"

"I remember there is a `while` loop and a `for` loop."

"Right. And what is the difference between them? Which one can help us here with lists?"

"I remember that `while` loop you can run forever. And you repeat the `for` loop step by step several times, " said Erik.

"So, how do you do something with every element in a list in Python? Like, print it, for example. You can Google it, not a problem."

He opened a new tab and asked Google: `python loop list`. After going through several sites, he finally found this page: (http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/). He typed this right after the list definitions in his script:

``` python
for p in products:
    print(p)
```

"Looks good to me. Now try to run it and if it works, do the same for other lists."

``` console
erik@idea:~$ ./coffeeshop.py
chocolate
coffee
Do you want coffee or chocolate?
```

"You can stop it with [Ctrl]-[C] now. We are not going to go through all the dialogs again. We are going to re-write it now," I said. "Remember, you were going to make it like a menu with letters or numbers?"

"Yes, and you said that numbers would be a better choice. But I didn't understand why."

"First, I said that it's quite possible that you have two flavors with names beginning with the same letter. Second, with letters, we would have to write many `if`s, like "if the user presses 'S' that means 'strawberry' and others. Third, adding a new flavor would mean that we have to write a new `if`. Let's start simple, with numbers. You would say 'for strawberry press 2,' and then strawberry would be the _second_ element in your list. Much easier, right?"

"So, I should print numbers and their list entries, right? I remember I can use the `range()` function to print a list of numbers."

"Right. But there is a better, more _Pythonic_ way of doing this. Take a look at the page you've just found. They mention the construct called `enumerate`. This is what we can use here."

Erik scanned the page (http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/) and found the `enumerate` example. In our case, the task was even simpler than in the example, and he wrote this:

``` python
for i, product in enumerate(products):
    print(i, product)
```

He tried to run it and got this:

```
0 chocolate
1 coffee
```

"But it starts with zero!" said Erik. "A-ha, I understand, it's because indexes in Python start with zero."

"Great that you remember that! It's one of the most fundamental concepts in programming! Of course, I'm joking, but only partly joking," I said. "You can change that. Smart people, who wrote the `enumerate()` function, predicted that somebody would need to show such a list to non-programmers and start it with '1'. So you can add this parameter right after `flavors`: add a comma and type `start=1`."

Erik changed his code to this:

``` python
for i, product in enumerate(products, start=1):
    print(i, product)
```

and got the expected result:

```
1 chocolate
2 coffee
```
"Well done!" I said. "Now add the same thing to other lists: flavors and toppings. After that let's take a break. Tomorrow we'll work with menus."

He worked for a while and here is what he's got:

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
toppings = ["chocolate", "sweetstrawberry", "caramel"]

for i, product in enumerate(products, start=1):
    print(i, product)

for i, flavor in enumerate(flavors, start=1):
    print(i, flavor)

for i, topping in enumerate(toppings, start=1):
    print(i, topping)
```

He ran the script and got the expected result:

``` console
erik@idea:~$ ./coffeeshop.py
1 chocolate
2 coffee
1 caramel
2 butterscotch
3 strawberry
4 raspberry
5 blueberry
6 sweetstrawberry
7 marshmallow
8 plain
1 chocolate
2 sweetstrawberry
3 caramel
```
