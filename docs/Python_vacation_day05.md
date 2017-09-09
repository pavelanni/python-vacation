# Python Vacation -- Day 5

## Working with files

Next day Erik was ready for new Python adventures. He looked more serious---his application was going to become really business critical for him. Customers, orders, delivery, database, online shop---all that sounded very serious now. 

"So, you said we are going to work with files today?". He was eager to start.

"Yes, we have to store your orders somewhere, right? What do we do with files in Python? Do you remember from your course?"

"We can open them, we can read and write. We have to close them when we don't need them anymore."

"That's right. And also we can open files in different _modes_. We can tell Python and the operating system that we want only read from the file and it will guarantee that we don't write to it accidentaly. Might be very helpful. Well, we start working with files. Let's make a plan. What do we need this file for?"

"We want to save our orders and then list them."

"Okay, in Python words it means we want to write and read to and from the file. When do we want to write and when do we want to read?"

"We will write to the file right after taking the order. And we read... wait, we don't have it here yet. We need another function to list the orders!"

"That's right!" I liked the way Erik started to think: in functions. We are on the right track! "Yes, we'll need that function. And also, I think, we'll need a menu in the beginning of the script. Something like: if you want to enter a new order, press 'N', if you want to list orders, press 'L'. But first let's write something to a file."

Erik looked at his script and said, "I think it should be here. Here, after we print 'Here is your order', we have to write it to the file, right?"

"Yes," I said, "good idea. But first we have to open the file. In our case we open it for writing. Or, rather, appending."

"What's the difference?"

"Let me explain. When we work with files we read and write them byte by byte. We read one byte and move to the next one. So we always are located in some _position_ in the file. Like 8th byte, or 247th byte, or 0th byte."

"It's at the beginning of the file, right?"

"Yes, exactly. And when we are at the beginning of the file and we start writing, we replace everything that is already there. Sometimes it's what we want, but sometimes it's not. In our case we'd like to add our orders to those that are already recorded, not erase and replace them. When we open a file for _writing_, we are in the 0th position, but when we open it for _appending_, we are at the position right after the last byte of the file. And everything we write will be added to the end of the file."

I decided that it's time to use a new tool to illustrate this point.

"Let me show another way to work with Python, it's called IPython. It's similar to the standard Python console, but more convenient. Open a terminal window and type `ipython`."

He did it.

```console
erik@idea:~$ ipython
Python 3.6.1 |Anaconda custom (64-bit)| (default, May 11 2017, 13:09:58) 
Type "copyright", "credits" or "license" for more information.

IPython 5.3.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]:
```

"Looks good with colors, I like it!"

"We will play with files in this IPython environment. Instead of writing scripts, saving and running them, this tool is so much easier for simple tasks. Another good thing is that it has a lot of small helpful things, like command completion and others. We can even run Linux commands without leaving the session---and we will need it."

I continued, "We start with opening a file. Write `f = open("a.txt", "w+")`. As you can easily guess, "`a.txt`" is a file name, "`w`" means we open it for writing, and that "plus" sign means: if the file doesn't exist, create it. Exactly what we need."

"What is "`f`?" asked Erik after he typed the string in the IPython session.

"It's a file _object_. You did have something about objects and classes in your course, didn't you?"

"Yes, objects can have _methods_ and they are like functions. We call them by adding a dot and a function name to the object."

"Great!" I was glad Erik was getting up to speed and recalled more and more from his previous course. "So, "`f`" is a file object and we will use its methods, like `read()` and `write()`. Let's write something to the file. Type `f.write('1,2,3')`."

He typed:

```
In [2]: f.write("1,2,3")
Out[2]: 5
```

"What do you think is `5` here?" asked I.

"I have no idea..."

"Remember, most functions return something. In this case this `write()` function returns the number of bytes written in the file. Three digits and two commas. Now let's check the file, if the function worked correctly. We'll use a simple Linux command `cat`, but inside IPython it should start with a percent sign. Type `%cat a.txt`."

```
In [3]: %cat a.txt

```

"Nothing," said Erik.

"Because we haven't closed the file. Usually operating system keeps data in a buffer in main memory before writing it to the file. It physically writes the data to the file when we close it (well, there are other situations and methods, but we'll talk about them later). Now close the file and print it out again with `cat`."

```
In [4]: f.close()

In [5]: %cat a.txt
1,2,3
```

"You see, now it's there," said I. "Let's open it and write something else. You can use 'Up' and 'Down' arrows to access history, like in Linux shell."

Erik repeated several previous commands:

```
In [6]: f = open("a.txt", "w+")

In [7]: f.write("5,6,7")
Out[7]: 5

In [8]: f.close()

In [9]: %cat a.txt
5,6,7
``` 

"You see now---this is what I meant. When you open a file for writing, you start from the beginning and replace everything that was there before. Now open it again, but with the "`a`" mode and try to write something again. Then close and look at the result."

Now Erik didn't need any specific instructions. He went back in history, changed the file's mode and wrote a bunch of numbers to the file again.

```
In [10]: f = open("a.txt", "a+")

In [11]: f.write("7,8,9")
Out[11]: 5

In [12]: f.close()

In [13]: %cat a.txt
5,6,77,8,9
In [14]: 
```

"Why didn't it write it from a new line?" he asked.

"Because you didn't tell it to. You didn't tell Python to write a new line character for you, so it just pasted the numbers next to the existing ones."

"How would I put a new line in the file?"

"Place this in the beginning of your string: "`\n`" and it will do the trick. It looks like two characters, but in reality it's one and it's a new line character. Go ahead."

```
In [14]: f = open("a.txt", "a+")

In [15]: f.write("\n9,10,11")
Out[15]: 8

In [16]: f.close()

In [17]: %cat a.txt
5,6,77,8,9
9,10,11
In [18]: 
``` 

"Yes, now I see a new line," said Erik.

"We will need it to work with your orders. Traditionally we place each record---in your case each order---in a separate line. Then we'll read that file line by line and print out your orders one by one."

"Okay, this is good. But what should I put into the orders? Name, then base product, then flavor and topping?"

"That's right! This is exactly what you need to prepare the beverage. Just make sure you separate them with commas, like you just did in the IPython session. There is a well-known format called 'Comma Separated Values', or 'CSV' and we will follow its rules. You can use one of the string methods called `join()`. Let me show you. Imagine you have several strings and you want to make a single string where they were separated by comma." I took his keyboard and wrote in the IPython session:

```
In [26]: a = "first"

In [27]: b = "second"

In [28]: c = "third"

In [29]: ",".join((a,b,c))
Out[29]: 'first,second,third'
```

"You see," I said, "the object here is the symbol which goes between the elements, and the argument of the method is the collection of the strings we want to join together."

"Why did you put two sets of parenthesis?"

"Because we have to pass a _single_ argument to the `join()` method. So we have to combine the strings together into a single object. In this case I created a _tuple_ (I'm sure they mentioned it in your course) and one set of parenthesis for that. You can create a list and result will be the same. Try to replace the internal set of parenthesis with square brackets." 

Erik typed:

```
In [30]: ",".join([a,b,c])
Out[30]: 'first,second,third'
```

And get the expected result. I continued, "You see, the result of this function is a string which we can use in the `write()` function. Now you have everything you need to write your orders to the file. Oh, don't forget to add "`\n`" to the end of the string. Just use the plus sign in the `write()` argument."

Erik opened his editor and started writing the code. I noticed that he opened the file with "`a+`" mode and named the file "`orders.txt`". He passed the joined string to `write()` and he didn't forget to close the file. It took him a couple of attempts to find the right place for that "`\n`" inside the parenthesis, but he did it right. Here is his code:

```python
. . . (skipped) . . .

print("Hello ", name, "! Here is your order: base product: ", products[p_index], 
  ", flavor: ", flavors[f_index], ", topping: ", toppings[t_index])

f = open("orders.txt", "a+")
f.write(",".join((name, products[p_index], flavors[f_index], toppings[t_index]))+"\n")
f.close()
```

In the console he ran the script, entered his choices and then typed:

```
erik@idea:~$ cat orders.txt 
Erik,chocolate,butterscotch,caramel
```

It worked prefectly. I asked if I can try it too. Erik said, "Yes... But, PLEASE!..." meaning, of course, "Don't ruin my program again!"

I entered my choices and output the file again.

```
erik@idea:~$ cat orders.txt 
Erik,chocolate,butterscotch,caramel
Pavel,coffee,plain,chocolate
```

It worked indeed! It added orders to the file---great! But that was only a half of our task for today. 

"You did a great job," I said. "Now we have to learn how to read from that file. How should we start?"

"With opening the file?" Erik suggested.

"Of course. Remember, we talked about different _modes_ when opening a file? This time we should open it for reading. Let's start with IPython again and try a couple things before writing the script. I think now you can easily guess how to open the file for reading."

Erik looked over his history and typed:

```console
In [33]: f = open("orders.txt", "r")
```

"Good," I said. "Now we have this _object_ `f` again. And this object has some methods. We just used its `write()` method to write our data to the file. Which method should we use to read the data?"

"The `read()` method?" Erik guessed. The answer was too obvoius and Erik expected there was a catch.

"Of course! It's obvious! Try it."

Erik typed:

```
In [59]: f.read()
Out[59]: 'Erik,chocolate,butterscotch,caramel\nPavel,coffee,plain,chocolate\n'
``` 

I said: "You see, it was easy. Python read the whole file and printed it out as a string. Now we have to decide what to do with this data."

"What do you mean? I thought we were going to print out all orders and here they are."

"Yes, but they don't look pretty. I suggest we split them into separate orders first and then figure out what is the base product, what is the flavor, etc. This way we will be able to print it in a nice way. Like: 'Dear Erik! Here is your order...' and then all components line by line."

"Like in a receipt!" Erik was glad it's going to look like 'real life' thing. "I like it, let's make a receipt!"

"Let's make it!" I agreed. "But first we have to rewind the file."

"What do you mean--`rewind`?" asked Erik. 

"Well, many years ago files were stored on magnetic tapes. Like in a cassette player," I said and suddenly realized that Erik doesn't know what a cassette player is.... "Okay, forget about 'rewind'. Let me show you. Type the same command again."

Erik did. "Nothing," he said. "It showed nothing this time. Where is my file?"

"Don't worry, your file is safe. Remember I told you about the position where we read or write something in the file? In this case we have read the whole file byte by byte and reached its end. And there is nothing left to read, that's why you see nothing. We have to get back to the beginning. There is a file method called `seek()` which moves our position in the file to any place we want. If we want to go to the beginning, what position would it be?"

"Zero!" said Erik. 

"Of course! Now use this method to move to the beginning of the file and try to read it again."

Erik typed:

```
In [61]: f.seek(0)
Out[61]: 0

In [62]: f.read()
Out[62]: 'Erik,chocolate,butterscotch,caramel\nPavel,coffee,plain,chocolate\n'
```

"Very good. Now let's read it order by order, meaning line by line. Luckily, Python has a simple method for this. As soon as we are going to repeat some action a number of times, we are going to use---you guessed it right---a `for` loop! Let me show you." 

```
In [64]: f.seek(0)
Out[64]: 0

In [65]: for line in f:
    ...:     print(line)
    ...:     
Erik,chocolate,butterscotch,caramel

Pavel,coffee,plain,chocolate

```

"You see, here we're looping through the file and doing something with each line of the file. We don't want just to print them, we want to split them into products, flavors, toppings. So, naturally, we'll use the method `split()` for that. Look how it works:"

```
In [67]: for line in f:
    ...:     name,product,flavor,topping = line.split(',')
    ...:     print(name)
    ...:     print(product)
    ...:     print(flavor)
    ...:     print(topping)
    ...:     
    ...:     
Erik
chocolate
butterscotch
caramel

Pavel
coffee
plain
chocolate

```

I explained, "We use the method `split()` for each line here. And we tell it that we want to split the lines into pieces that are separated by comma. When we split it, we assign all pieces to respective variables on the left side of this statement. In Python it's pretty common when there are several variables  at the left side of the assignment statement. "

"I like it!" said Erik. "With this I know now how to print it like a receipt. I'll just add word like 'Dear' and 'your product is' and print the variables."

"Sounds like a plan to me," I said. "I just want to clean up it a little bit. Type `topping`."

Erik did it:

```
In [68]: topping
Out[68]: 'chocolate\n'
```

I pointed to the output and said, "You see this '`\n`' character at the end? It's a newline symbol and we don't need it. We should strip it from the line after we took it from the file. And, believe it or not, there is a special method to strip characters from strings. And it's called..."

"...Strip?" guessed Erik. 

"Yes, '`strip()`. We can put it right before `split()`, like this: `line.strip('\n').split(',')`. Isn't it cool that you can 'chain' methods together in one line? Try it yourself."

Now Erik was ready to reuse the code written my me. He didn't forget to move the position to the beginning and he also added something from himself.

```
In [73]: f.seek(0)
Out[73]: 0

In [74]: for line in f:
    ...:     name,product,flavor,topping = line.strip('\n').split(',')
    ...:     print("Dear ", name, "here is your order:")
    ...:     print("Base product: ", product)
    ...:     print("Flavor: ", flavor)
    ...:     print("Topping: ", topping)
    ...:     print("Guten Appetit!")
    ...:     
Dear  Erik here is your order:
Base product:  chocolate
Flavor:  butterscotch
Topping:  caramel
Guten Appetit!
Dear  Pavel here is your order:
Base product:  coffee
Flavor:  plain
Topping:  chocolate
Guten Appetit!
```

"I see that your German lessons with Grandma are not a waste of time," I said. "Great job, Erik. Let's take a break for now---we have done a lot today. Tomorrow we'll make another function to list orders and also a main menu."