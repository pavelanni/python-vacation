# Python Vacation --- Day 11

## Automate It

"It was quite a challenge last time when we had to connect a database to our web application, wasn't it?" I asked Erik. 

"Yeah... My head is still spinning," said Erik and I knew he was not exaggerating.

"Can you recall what we had to do yesterday? There was a number of steps."

"Well... You gave me access to the virtual machine in our 'home cloud'. Then I installed the PostgreSQL package. Then I connected to Postgres and created a new database called 'coffeeshop'. Also you told me to create a separate database user for my application, so I did that. Then I logged in as that 'coffeeshop' user and created a new table for my orders. Then we made changes in the `get_order.py` and `list_orders.py` scripts to use SQL instead of just files. And then we copied the scripts to the `cgi-bin` directory. Oh, and also you had to change something in the database configuration, but I don't remember what it was."

"This is great, Erik! Honestly, I didn't expect that you remember all the steps in such details. Now let me ask you: could you repeat all the steps youself?"

"Oh, no!" said Erik. It was quite obvious that he enjoyed working with Python code more than doing sysadmin stuff. "It's so boring and I'm afraid I make a mistake somewhere."

"But we'll have to do it again if we want to publish your application on the cloud," I said.

"Could you do that for me?" asked Erik. "Let's separate our duties: I will work with the code and you will do that systems stuff."

I said, "I understand you. Of course, I could help you, but what if I'm not around? And you just have updated your application---like added new flavors and toppings to your menu---and you want to publish it right away? Or you just want to test a new color scheme? I think you should be able to publish your applications yourself. But I have a good news for you."

"What is your good news?" Erik was suspicious. He knew from experience that good news are usually accompanied by bad news, and he expected that he had to learn something new again. But he was curious anyway and he still wanted to get his application published online. 

"Good news is that you can automate this process and next time you'll just run one or two scripts and they will do everything for you."

"But who will write those two scripts?" Erik suspictions seemed to be confirmed.

"You, of course!" I said with a big smile on my face. "Don't worry, I'll help you."

Erik didn't look very happy, but the perspective to type all those commands again was not much better. He said, "So, will we use Python for those automation scripts?"

"No," I said. "There is a tool called 'Ansible' and its language is much simpler than Python, it's called YAML. Yet Another Markup Language. Seriously, I'm not making this up. You will see, it's very easy to read and understand."

"And what do those scripts do, exactly?" asked Erik. "Should I copy all the commands from my history to those scripts?"

"No," I said. "That would be true if you were going to create shell scripts. But Ansible is smarter than shell. With Ansible you don't type Linux commands, you just describe what you want to achieve and it does that for you. More than that, you don't even have to login to the virtual machine where you want to publish your application, Ansible does that for you. Even more, if your application becomes popular and you want more servers on the cloud, Ansible can easily publish your application on as many machines as you need."

"Will it configure a database for me as well?"

"Sure! Not only that---it will install all necessary packages, it will copy your files to the web server, it will copy your scripts to `cgi-bin` and make sure the database and webserver are up and running. You just have to tell it to do that, but believe me, it's much easier than those shell commands you had to type the other day."

"Why didn't you tell me about Ansible earlier? Okay, okay, I know your answer: you wanted me to suffer first. Well, shall we start?"

"Sure. I have already prepared another virtual machine for you to practice. It has just a bare minimum Linux installation and you can connect to it via SSH. Yes, right from your account here. I have installed your SSH key onto it and added you to the group of `sudo` users. That means you can run superuser commands on that machine. I even configured it so you don't have to enter password. Of course, you shouldn't configure your servers in real life this way, but just for educational purposes I made it simple... You can try it right now. `ssh` into that machine: it's IP address is 192.168.1.125. Use the key called '`vbox-erik`' in your current directory. When you're logged in, try to run some command where you need '`sudo`'. Like '`sudo ls -a /root`'. "

Erik typed:

``` console
$ ssh -i vbox-erik erik@192.168.1.125
. . .
erik@vacation:~$ sudo ls -a /root
.  ..  .bashrc  .nano  .profile
erik@vacation:~$ 
```

"Good," I said, "it works. Now exit that machine and try if Ansible works. I have configured you as Ansible user in this directory and also I've included this VirtualBox machine's IP in the list of hosts. In other words, it should work now."

Erik exited the virtual machine and looked inquiringly at me.

I said: "Now type '`ansible all -m ping`'. "

Erik typed and got this:

``` console
$ ansible all -m ping
192.168.1.125 | SUCCESS => {
    "changed": false, 
    "ping": "pong"
}
```

"Cool, Ansible works too!" I said. "Now let me show you a couple of playbooks I have prepared for you. Just to save time I am not going to force you to write a lot of them." Erik smiled. 

I opened several files in the editor and showed the first one. "Look," I said, "first we have to install the web server, right? And here is our first Ansible script. Look if you can read and understand it." 

```yaml
# This installs and starts Apache
- hosts: all
  gather_facts: False
  become: True

  tasks:

    - name: Install Apache
      apt: name=apache2 update_cache=yes

    - name: Enable CGI
      command: a2enmod cgi

    - name: Start Apache
      service: name=apache2 state=restarted
```

Erik looked at the script. "Well, it's even simpler than Python," he said. "I can see the list of tasks: there are three of them. I see that you want to install Apache, enable CGI (yes, I remember we ran this command when we started working with CGI scripts) and start Apache. Pretty simple, I like it! I see that you want to do it on all hosts---but we only have one. I just don't understand '`gather_facts`' and '`become`'. What do they do?"

I was glad he grasped things so quickly. "As you can easliy guess, '`gather_facts`' is about gathering facts. Ansible wants to know as much as possible about the systems it's going to manage. So first it gathers facts about the systems. Like operating system version, IP address and hostname, and so on and so forth. The good thing it that you can use those facts later in your scripts. For example, if the system is Ubuntu Linux, you use the '`apt`' command to install packages and if it's Red Hat, you use '`yum`' for that. In our case we don't need that and I decided to save time and skip this. '`become`' is a little trickier. Remember, I told you that I have created a user account for you at the target machine? Some commands you can't run as a normal user. You have to _become_ a superuser, or `root`."

"Like I did with '`sudo`'?" asked Erik.

"Exactly! You are telling Ansible that you are going to become '`root`' to run certain commands. Sometimes you want to become a different user, and then you explicitly tell that. We'll see it in one of the next scripts."

"And also," I added, "it not me, who wants to install Apache, it's you," I smiled and Erik understood me. "What is the command to run Ansible scripts?" he asked. 

"Playbooks. We call them playbooks. Just type '`ansible-playbook apache-install.yml`'."

Erik typed and watched the output:

```
$ ansible-playbook apache-install.yml
```

"Now try to access the web server at `http://192.168.1.125`," I suggested. Erik opened this URL in his browser and found the default Apache page. 

"You see, instead of typing three commands you typed just one and got Apache installed. What is also good about Ansible that if you needed to install 3, 5, 100 web servers, you'd have to type the same single command and Ansible would install Apache in parallel on all those servers."

"Why would anybody need one hundred web servers?" asked Erik. He looked surpised by the scale of real life applications. I said, "Imaging you are working not on a coffeeshop for your neighborhood friends, but on a big online shop or other web application. And suddenly it becomes very popular. You don't want to lose your customers just because your web server can't handle the load, right? So you start many web servers and put a thing called _load balancer_ in front of them. That's when you need to start many similar servers."

"Okay," said Erik, "what's now?"

"What else do we need? Install the database, of course! Look at this playbook called '`postgres-install.yml`'."

```yaml
# This installs postgres and psycopg2
- hosts: all
  gather_facts: False
  become: True

  tasks:

    - name: Install PostgreSQL
      apt: name="{{ item }}" state=installed
      with_items:
        - postgresql
        - postgresql-contrib

    - name: Replace peer auth with md5 in PostgreSQL
      lineinfile:
        backup: yes
        path: '/etc/postgresql/9.5/main/pg_hba.conf'
        regexp: 'local   all      all                              peer'
        line: 'local   all          all                              md5'

    - name: Install pip3
      apt:
        name=python3-pip update_cache=yes

    - name: Install psycopg2
      pip:
        executable: /usr/bin/pip3
        name: psycopg2

    - name: Start PostgreSQL
      service: name=postgresql state=started
```

Erik looked puzzled. I decided to help him. "I know, you want to ask what are these '`pip3`' and '`psycopg2`'. The latter is a Python module which we need to talk to PostgreSQL database. We used it already in your application, but I had installed it already. And '`pip3`' is a tool to install Python modules. You haven't seen it before because I have installed all the modules beforehand."

"Also look at the first task," I continued. "You see this '`{{ item }}`' and '`with_items`' things? We can use them in Ansible similar to loops in Python. Like here, we want to install several packages from the list. Second task is needed because we are going to create a user in PostgreSQL, but not in Linux, so we can't use peer authentication. Don't worry about that right now, we'll discuss it later. Everything else should look familiar to you already. Go ahead and run this playbook too."

Erik typed:

```
$ ansible-playbook postgres-install.yml
PLAY [all] *******************************************************************************************************

TASK [Install PostgreSQL] ****************************************************************************************
changed: [192.168.1.125] => (item=[u'postgresql', u'postgresql-contrib'])

TASK [Replace peer auth with md5 in PostgreSQL] ******************************************************************
changed: [192.168.1.125]

TASK [Install pip3] **********************************************************************************************
changed: [192.168.1.125]

TASK [Install psycopg2] ******************************************************************************************
changed: [192.168.1.125]

TASK [Start PostgreSQL] ******************************************************************************************
ok: [192.168.1.125]

PLAY RECAP *******************************************************************************************************
192.168.1.125              : ok=5    changed=4    unreachable=0    failed=0   

```

"Good," I said. "The database server is up and running. Now we have to create a database and a user to work with it. And again, we are going to use Ansible modules for that."

"It seems there is an Ansible module for everything!" exclaimed Erik.

"Well, almost. There are over 1300 modules currently. And if you can't find a module you need, you can write it yourself---in Python---and it will become part of Ansible---of course, if you wrote it well. Look at this playbook which creates a database and a user. I'm sure now you'll understand everything."

```yaml
# This creates a CoffeeShop database and a user
- hosts: all
  gather_facts: False
  become: True
  become_user: postgres

  tasks:
    - name: Create a database for the CoffeeShop application
      postgresql_db:
        name: coffeeshop
        state: present
        login_user: postgres

    - name: Create a user coffeeshop
      postgresql_user:
        name: coffeeshop
        password: coffeeshop
        role_attr_flags: NOSUPERUSER,CREATEDB,LOGIN
        state: present
        db: coffeeshop
```

"A-ha, now I see that you want it to become a different user, not '`root`'. I remember, you told me it's a user who manages the whole database. Like '`root`' for PostgreSQL." Erik ran the playbook and watched its output. Everything was in place for his application. Well, almost.

"But I also need a table for orders. Can I do it with Ansible?" 

I liked that he started thinking the "Ansible way" and tried to solve his problems with this new tool. I said, "Yes, but now you have to use SQL for that. There is no Ansible module specifically to create a table. After all, what would it do? It would call a SQL statement anyway. So in our case we'll create a simple SQL script and execute it on the target machine. That will be our next playbook. Now go ahead and run this one."

```
$ ansible-playbook postgres-createdb.yml

PLAY [all] *******************************************************************************************************

TASK [Create a database for CoffeeShop application] **************************************************************
changed: [192.168.1.125]

TASK [Create a user coffeeshop] **********************************************************************************
changed: [192.168.1.125]

PLAY RECAP *******************************************************************************************************
192.168.1.125              : ok=2    changed=2    unreachable=0    failed=0   

```

"Well," I said, "now we have a database and a user. We can ask this user to run a SQL script for us. And it will be a simple script to create a table for your orders. Remember, when we just started working with databases we just ran a simple '`CREATE TABLE`' command and told PostgreSQL about the columns and types we wanted to have in the table. Now we'll create a script with this command, send it to the target machine and run it as a user '`coffeeshop`'. Look here, this is the script:"

```
---
- hosts: database
  gather_facts: False
  become: True
  become_user: postgres

  tasks:
    - name: Copy the table creation script
      copy: >
        src="files/create-table-orders.sql" 
        dest="/tmp/create-table-orders.sql"

    - name: Execute sql script to create the table
      command: >
        psql -h localhost 
        "user={{ postgres_user }} password={{ postgres_password }}" 
        -f /tmp/create-table-orders.sql

    - name: Delete sql script
      file: path="/tmp/create-table-orders.sql" state=absent

```




```
$ ansible-playbook --ask-vault-pass create-table-orders.yml
Vault password: 

PLAY [database] **************************************************************************************************

TASK [Copy the table creation script] ****************************************************************************
changed: [192.168.1.166]

TASK [Execute sql script to create the table] ********************************************************************
changed: [192.168.1.166]

TASK [Delete sql script] *****************************************************************************************
changed: [192.168.1.166]

PLAY RECAP *******************************************************************************************************
192.168.1.166              : ok=3    changed=3    unreachable=0    failed=0   
```
