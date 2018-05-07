# Python Vacation --- Day 7

## Web Interface

It's been a couple of days since our last lesson with Erik. He was visibly excited about his application. He showed it to Mom, to Grandma, he took orders from them, he changed his welcome message several times. Now the message shouted: `WELCOME *** TO ERIK'S BEST COFFEESHOP *** WELCOME`.

I've been pondering about the best way to start moving toward web application. On one hand, there are plenty of Python-based web frameworks: Flask, Bottle, Django, Pyramid, and others. Of course, for any serious application we would take one of them. But I was going to explain to Erik the basic mechanics of a web application which is usually hidden in such frameworks. So I decided to start with more traditional approach: Apache web server and CGI scripts.

"Are you ready to migrate your application to the web?" I asked Erik after lunch.

"Yes, I really want it. I'd like to show it to my neighborhood friends on my iPad!"

"Okay," I said. "But be prepared, we have to learn a couple of important things on the way. "

I started, "Remember how we created a website for your last science fair project?"

"Yes," answered Erik. "We wrote several HTML files and added some pictures and style sheets to them. People in my school liked it."

"Right, that's what we did. But that website was _static_, which means its content didn't change. On the other hand, most of the sites on the Internet are _dynamic_, they always give you some new information, ask you for input and react to what you say. So we are going to create a website which is dynamic. Let's start with something simple. How does a simple HTML page look like?"

"Well," started Erik, "it has those `<html>` tags and also the `<body>` tags. And the content goes between them."

"That's right. So, a simple HTML page would look like this, right?"

```html
<html>
    <body>
        <h1>Hello!</h1>
    </body>
</html>
```

"Do you remember how this page comes to your browser?" I asked, hoping that this information hasn't completely disappeared from Erik's mind.

"Yes, we created a page called `project.html` and then copied it into a directory---"

"---`/var/www/html`," I helped him.

"Yes. And then from my browser I called `localhost/project.html` and the page showed up in the browser."

"Great! I'm glad you remember this. So, essentially your webserver _sends_ those HTML words to you browser, the browser _receives_ them and _displays_ them. Sometimes people say it _renders_ your page."

"Now let's make it dynamic," I continued. "Remember, HTML is just a markup language, it's not active. To make our page active we have to _execute_ a program. Let's do something simple, like showing current time on the page. Every time we ask the web server for this page it will run a standard program called '`date`' and display its result on the page."

"Will we do it in the same HTML file?" asked Erik. 

"No," I said, "we will create a separate file for that. Even more, we will place it in a different directory. It's a good practice to separate your HTML files from your programs---for security purposes. In our case this directory is called '`/usr/lib/cgi-bin`'. And the program we are going to create with you will be called 'a CGI script'. "

"Like CGI in movies?" asked Erik.

I smiled. "No, that CGI stands for Computer-Generated Imagery. Our CGI means Computer Gateway Interface. Related to computers, anyway. "

"Open the editor," I said to Erik, "and copy your HTML file with 'Hello' into it." It took Erik a couple of clicks. "Now let's convert it into an executable shell script. First, add the 'shebang' line in the beginning. We used it with Python, but I didn't tell you that it's called 'shebang'. For our shell script it will look like '`#!/bin/bash`'. "

Erik added the line. "Now what?"

"Now we should tell Bash (which is our shell) to print out all the lines we want to send to the browser. In Bash we use the command called '`echo`' for that. So you have to put the word '`echo`' in the beginning of each line and put double quotes around each HTML line."

The file was small and it didn't take long to make all the edits. So now the file looked like this:

```
#!/bin/bash
echo "<html>"
echo "<body>"
echo "<h1>Hello!</h1>"
echo "</body>"
echo "</html>"
```

"Almost there!" I said. "Now we have to add two magic lines in the beginning to let the browser know what to expect from this script. First, right after the first line, add another `echo` and this line in quotes: '`Content-type: text/html`'. The second magic line should be empty. Right after this line add '`echo ""`'. "

After Erik had edited the file I said: "Now save it in the directory `/usr/lib/cgi-bin` under the name '`index.sh`'."

!!! note
    I thought it's too early to give Erik root access on his laptop so I ahve just added the write permissions for him on the `cgi-bin` directory. Here is the command: `sudo setfacl -m u:erik:rwx /usr/lib/cgi-bin`.

The file now looked like this:

```
#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html>"
echo "<body>"
echo "<h1>Hello!</h1>"
echo "</body>"
echo "</html>"
```

"Now let's try it," I said. "In the browser type in the location string: '`localhost/cgi-bin/index.sh`'. "

Of course, Erik's got exactly the same page with big 'Hello!' on it. "What's the point?" he asked.

"The point is," I said, "that now it's not just a static HTML file, but a _script_ that generates those HTML words and tags and sends them to the browser. That means we can send any output from any command or script to the browser. Let's add just one line after the 'Hello' line and put the command '`date`' into it."

"Without '`echo`'?" asked Erik.

"Yes, just the command '`date`'. And then reload the page."

Now after the too familiar 'Hello!' there was another line:

```
Sun Jul 23 10:46:02 EST 2017
```

"You see: it's the today's date and time. Now reload it," I said.

No doubt, the line has changed to 

```
Sun Jul 23 10:46:24 EST 2017
```

"It is changing!" exclaimed Erik.

"Of course. That's what I called a 'dynamic' page. It is changing depending on what you are sending to the browser. And now it's up to you---what to send to the browser. We are going to do something very similar, but in Python. We will generate HTML pages with tags and everything, but we'll insert our data into those pages, _on the fly_, from our orders file. Isn't it cool?"

Erik nodded, but it was obvious that he is still digesting what he had learned just now. I said, "Don't worry, the best way to understand something is to start using it. Now, after we played with simple scripts, let's move on to the real task."



