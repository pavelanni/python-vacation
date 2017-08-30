
# Python Vacation -- Day 0

It all started on 4th of July. My 13-year old son came home with an idea. 

"I want to treat my neighborhood friends with Frappuccino to celebrate Independence Day!" said Erik.

"Good idea! Do you have everything you need?"

"Yes, I have coffee, I have chocolate, I have several flavors to add and I have chocolate cream for toppings! I will take orders on my iPad and prepare them here. Just a moment!" and off he went.

He came back with notes on his iPad, prepared six drinks for his friends and left again.

"Wasn't it a good idea?" he asked me when he came home with six empty plastic cups. "Yes, great idea," said I. "But..."

"What 'BUT'??" said Erik.

"You see, you used your iPad to take orders, but you used it just as a notepad. It would be much easier to take just a notepad and a pencil with you for that. With iPad, you can do it in much better way..."

"How?"

"You could create a small application to take orders where you or your friends would just click on the available choices for flavors and toppings."

"Like radio buttons, right?"

"Yes, something like that. You've taken that Python course at Codeacademy haven't you? Don't you want to create something real with Python, rather than doing exercises in their sandbox?"

"Yes, that would be cool!" said Erik. "But it must be difficult---to make it look like a real online coffee shop..."

"Don't worry, we'll do it step by step. Open your laptop and start a terminal."


I have to admit, my son uses Linux on his laptop. I know, it's torture for a 13-year old, but my way of thinking was: "He will learn Windows or Mac OS later anyway---at school or with friends. I'll give him a chance to work with Linux at home. It won't hurt to know a bit of Linux."

## First lines of code

"In the terminal type 'python3'," I said to Erik. Yes, I know there is a never-ending discussion "Python 2 vs. Python 3", but at least it seems there is a consensus that if you are just starting learning Python, it's better to start with Python 3. Your mileage may vary, of course. 

```console
erik@idea:~$ python3
Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
```
```pycon
>>> 
```

"Done. What's next?" asked my son.

"Well, we want to take orders, right? So we have to ask our customers what they want. And get some __input__ from them, right? What did you start with when taking orders from your friends?"

"I asked them if they want coffee or chocolate. Some of them are young and they don't drink coffee."

"Okay, let's do that. Do you remember how to ask for input in Python?"

"Barely..."

"Well, I'll help you. There is a function called `input()`. It can ask a question and you put this question in quotes into parenthesis. And then the function waits for the user to type something and press <kbd>Enter</kbd>. After that, the function __returns__ a value. You can take that value and assign it to a variable. "

Erik's face showed that he is beginning to recall something from that Python course. Suddenly there was a connection between abstract things like __functions__ and his friends and cups of Frappuccino. "And to assign something to a variable I type its name and then 'equal' sign and then the value, right?"

"Exactly! Go ahead. Let's name that variable `answer` and assign to it what we get from the `input()` function. How would you write it?"

```pycon
>>> answer = input()
```

"Nothing happened," said Erik.

"What did you expect?"

"I thought it will ask me what I want..."

"Remember: computer only does what you tell it to do. Did you tell it to ask you a question?"

"No... A-ha, I know! You said that I have to put the question between the parenthesis. But what should I do now? It doesn't show the prompt."

"It's because it is waiting for your input. Say something and press <kbd>Enter</kbd>"

```pycon
coffee
>>> 
```

"Now type this `input()` function again, but with a question."

```pycon
>>> answer = input("Do you want coffee or chocolate?")
Do you want coffee or chocolate?coffee
>>> 
```

"Now let's test if it gets the answer. Type `print(answer)`"

```pycon
>>> print(answer)
coffee
>>> 
```

"It works!", Erik was happy. One thing is to do course exercises in their sandbox environment and another thing is to get something working on your own computer. More than that---it's not just an __exercise__, you are working on your own project!


## More options

"Well, it works," I said. "What were your other components?"

"I asked them which flavor they want and also which topping."

"Go ahead and ask those questions with Python. But you will need more variables, right? This time let's use `flavor` and `topping`, Okay?"

"Okay," said Erik and typed:

```pycon
>>> flavor = input("What flavor do you want?")
What flavor do you want?strawberry
>>> topping = input("What topping do you want?")
What topping do you want?chocolate
>>> 
```

"Good. Now test the variables if you get the order right."

```pycon
>>> print(flavor)
strawberry
>>> print(topping)
chocolate
>>> 
```

"Now you can type something like: 'You have ordered coffee with strawberry flavor and chocolate topping," said I and thought to myself: "How could they even drink this??? Coffee with strawberry?? I don't understand..."

"I don't remember how to do it with `print`. Can I google it?"

"Of course! It's not a test, it's your own project. Go ahead!"

In a couple of minutes Erik found the right example and typed:

```pycon
>>> print("You have ordered ", answer, " with ", flavor, " flavor and ", topping, " topping. Thanks!")
You have ordered  coffee  with  strawberry  flavor and  chocolate  topping. Thanks!
>>> 
```

"Cool! It works like a real thing! But how can I save it as a program to run it again?"

"Good question. And just in time. I was just going to switch to the editor. Open some text editor."

"Like LibreOffice?"

"No, LibreOffice is not good for that. You need a __text__ editor, not a word processor. Something like `gedit` will work perfectly. Later you will discover Atom, Sublime Text and, maybe, even Vim."


## First script

"Let's start with something simple, just to try it. You know it's a long tradition that the first program people write in any language is 'Hello, World!'. Let's follow the tradition."

"But I wrote 'Hello, World' already in my online Python class!"

"Well, but you haven't tried it yet on your own computer, have you? If you have already done it in that class, it must be easy for you now."

Erik opened a new file in `gedit` and wrote:

``` python
print('Hello, World')
```

"Good," said I. "Now let's run it. Save the file with any name, just make sure it ends with `.py`. Then go to the terminal and type `python3 ` and the name of your file."

He typed:

```console
erik@idea:~$ python3 hello.py
Hello, World
```

"It works!" said Erik. 

"Of course, it works, why shouldn't it? That was easy. Now let's make two things which will convert our script into an application. First, place the following string at the very beginning of your script: `#!/usr/bin/python3`. This will tell Linux that it's a Python script and that we want to use Python 3 for it. Second, go to the terminal and make this script executable."

"How do I do that?"

"Yeah, it seems you need another course, on Linux basic commands... Okay, this time I will help you. Type `chmod a+x hello.py`. After that, you will be able to run your script without `python3` in front of it, just like this `./hello.py`. "

"And what does this 'dot-slash' mean?"

"It means that you want to run __this particular__ application in your current directory, and not something else. But this is part of 'Linux basics', we will discuss it later."

After Erik has done these two steps, he tried to run the application:

``` console
erik@idea:~$ ./hello.py
Hello, World
```

"Great, now you can run it as any other application. Congratulations, you've created your first application!"

"But that was very simple. I want to work on my Coffee Shop application!"

"Let's take a break and continue tomorrow, Okay?"

