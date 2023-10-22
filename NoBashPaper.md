# NoBash - Creating a programming language
The PC operating system market space is dominated by Windows and MacOS, leaving very little room for competition. Still, there is a very small minority of PC users which prefer to run Linux, though this still has not made a dent in the current duopoly held by Windows and MacOS. When looking at servers, Linux catches up and is considered a very popular choice. Some more tech-literate users like to automate frequent tasks by using small programs they create. Instead of spending ten seconds doing something every day, they instead spend five minutes writing a small "script" (or program) which will do said task for them in the future. I personally have written such scripts before, such as a small program which automatically deletes old screenshots which I no longer need. Bash is the most popular programming language for performing simple, everyday tasks on Linux. Bash has a very tight integration with Linux, making it much easier to perform common administrative tasks like creating or moving files, starting various programs when the computer is booted up, or automatically sorting all entries in a table alphabetically. 

Just like how human languages have different vocabulary and grammar, programming languages are written differently as well. While Bash makes it easy to do something in Linux, I would argue that its grammar is much more confusing than that of popular programming languages outside of Linux. They are much more convenient to write in and more straightforward to learn and understand. In my opinion, Python has the easiest grammar of all programming languages. Still, the integration Linux has in Bash is unparalleled in every other language, in which it is a lot more difficult to code the aforementioned administrative tasks. The world needs a language that is as simple to write as Python but can work with the Linux system as efficiently as Bash. 

Enter NoBash, a brand new language with a nearly identical grammar to Python but the ability to make working with Linux as trivial as when using Bash. This sounds great; a significant market gap is addressed after decades, but one minor issue remains: NoBash does not exist yet. However, throughout the next couple of chapters, you will see its creation bit by bit, with an explanation of every step, why something works the way it does, and what this will achieve. Everything will be explained so that a reader with no programming experience can understand every step and learn some coding skills along the way. Brace yourself as you will see programming history re-imagined right before you. Without further ado, you may now delete your old programs written in Bash, as you will need no more Bash and only NoBash!

# Linux
When you work with a computer, you work with the computer's hardware and software. Hardware is the physical component of the computer, the parts one can touch and see. Software consists of the data, such as programs, stored on the machine. Arguably, the most mission-critical software on a computer is the operating system (OS). The OS lets the user interact with the hardware. When you move the mouse, this data is transferred to the computer, which then needs to work with this information. One example of what the OS does is work with the data transmitted by the mouse, like moving the cursor around accordingly. 

*Linux* is a kernel written by Linus Torvalds, a Finnish programmer. A kernel is a part of the operating system. The kernel focuses on letting programs interface with the hardware, effectively connecting the software and the hardware. When you take a picture on your phone, the kernel plays an integral part in the process and lets the camera application work with the physical camera. iOS, android, windows, and MacOS also work with a kernel. A comparison to this could be the car. The kernel is to the operating system what the engine is to the rest of the car. The car needs an engine to work; it lies at its core, but an engine without a car is also useless. The user cannot interact with the kernel directly. The engine needs a chassis, wheels, and a steering wheel (and a lot more) to work as a functional car. Examples of what an operating system must also include are a program to show the desktop or a way to launch programs. 

Over the years, colloquially, Linux started to refer to the kernel and the operating system as a whole. Without any programs, the Linux kernel cannot act as an operating system, which is where distributions come into play. Linux distributions are a package of programs, with the Linux kernel being a core part of these, which together act as an operating system. There are thousands of these "distros," with each distribution having its own goal or purpose. For example, Arch Linux is a distribution with minimal additional software installed, letting the user install and configure their system to a very personal degree. The downside is that Arch is considered more challenging to set up than some other distributions. This is because the users themselves must set up many parts of the system to provide said degree of customizability. Ubuntu can be seen as the polar opposite of this, as it has a very user-friendly install process but comes with much software preinstalled, which can slow down the system or waste resources. 

This may raise the question of how so many different versions of one operating system may exist. The answer is that Linux is "free and open source". In this context, free has two meanings, two of which apply: Linux does not cost, making its price *free*. However, Linux also gives everyone complete liberty over how they want to use it or gives them the *freedom to view, modify, study, and share the code. This also brings us to the second part of "free and open source" (FOSS): the fact that Linux has its code publicly available. This lets any user check Linux' code for any malware or trackers to ensure they are safe. Though there is more nuance to this, which will be covered in the next chapter, for now, one can imagine that a programmer does not share their code. Instead, a particular piece of software reads their code (which a human can read and understand) and turns it into ones and zeros (which a human cannot understand, but a computer can). This process can also be reversed, but because most software is not *free*, one can be met with legal consequences. Additionally, with more extensive programs such as Windows or MacOS, the complexity of the code makes this infeasible. 

It should be noted that when the code is freely available for a program, this is only the case when it is distributed explicitly by the programmer. Anything a user does on their end is not shared or reflected in the code in any way. It is comparable to having the blueprints of a car: just because someone has these blueprints made by the manufacturer does not mean that they can see where you are driving. This is the same with code, as the code serves as a blueprint for the final program to be created. This, however, may raise another concern, one which is justified. If someone had a blueprint for your car or house, they could find potential weak points in their security to steal the vehicle or break into the house. This is true. However, on the flip side of the coin, with millions of talented engineers looking over a car's blueprint, such flaws in the design would be pointed out almost immediately and fixed just as fast. Even if a thousand car thieves were reading the blueprint to find any problems they could exploit, millions more would be looking for these same issues to fix them. Additionally, these individuals could fix minor problems or add new features. 

This concept applies to open-source code as well. It works even better with code, as it is much easier to code a fix for an error than to start manufacturing new car parts to achieve security. If you do not like something in a program or there is a missing feature you would like to have, you can program it yourself using the existing code of the software and send it to the owner or the program. They can then verify through the code you submitted to ensure it works and does not do anything it is not supposed to. If all is well, they can add your changes to the program, which all users download. This is how nearly 15'000 people have contributed to the Linux kernel already. As previously mentioned, this is also the case with security problems, with tens of thousands of people reading through the code for problems (Note that more people read the code than write to it). In the case of proprietary code (which is not open source), neither hackers nor security researchers can read the code, which creates "security through obscurity". This means that the security of the code is only ensured because of the secrecy around it.
An example would be a website's secret page displaying all users' passwords: `www.example.com/passwords.html`. This is a problem as anyone can access everyone else's password if they know about the web page. If the website owner only removed all links to that page from the other website pages, this would be security of obscurity. A regular visitor would never find that page, making this "secure" against people randomly stumbling across the data. However, the practice is still not secure, as there are many ways to find this secret page. Instead, the website owner could make the page password-protected. This concept also applies to Linux's and Windows's security: While many users ensure Linux stays safe, a much smaller team is doing the same for Windows. It is security through obscurity, as Windows is closed-source, which is "protecting" it. As we have seen, it is better to fix the problem than to hope that no one finds it.

These and many other reasons are why Linux has become a relatively popular PC OS. On servers, however, Linux has become the most dominant OS, with many servers running on it for various reasons. Windows dominates the market first and foremost, with MacOS lagging behind quite a bit. Linux pales compared to the two giants, but its market share is growing ever so slightly year after year. The FOSS nature of Linux, the security that comes with it, and its customizability are all important reasons why Linux has become as popular as it is now. As will be covered in the next section, we will see that Linux has a powerful "programming language" it is tightly integrated with, which is what we aim to replace with NoBash.

# Programming and Bash
It is relatively common knowledge that computers work with ones and zeros. In this regard, one could say that humans and computers speak different languages: machines can only understand binary (ones and zeroes), whereas humans can only work with human-readable languages. This creates a problem, as a programmer needs to tell a computer what to do in English (as programming languages are usually written in English), but the computer cannot understand this. Alternatively, humans could learn to read and write in binary, which the computer could then work with. This used to be how programs were written, but it is impractical and nigh impossible for more extensive programs. Instead, a middle ground has been found which lets both parties work with their preferred language.  

This is where compilers and interpreters come into play. These programs take the programmer's code and turn it into machine-readable instructions (in binary), which the computer can run. However, the difference between them lies in how this data is stored (or not stored in the case of interpreters). A compiler will take these binary instructions and save them to a file. This file is a computer program, like Firefox, Microsoft Word, or even an OS like Windows. This type of program is also sometimes called an "executable" or "binary" as the file can both be executed (or "run") and has its data written in binary. The executable can then be distributed to others who can run the program. However, there are some limitations to this, as a program compiled for Windows typically cannot be run on MacOS for various reasons. It should be noted that, just like how the compiler turns code into binary, some programs translate Windows programs into ones for Linux (for example), though this is more complex and error-prone.

Interpreters, on the other hand, do not save the binary computer instructions in a file. Instead, they directly execute them on the fly while translating the code. This means the interpreter is run whenever the user wants to run some code. One benefit is that the code can be run on any device and OS as long as the interpreter works on said computer. Additionally, while humans cannot read a binary file, the interpreter requires code that a human can understand. This makes virtually all interpreter programs open-source, bringing the advantages described in the Linux chapter and letting the user check the program for any malware or tracking. However, this is also a double-edged sword. Companies or individuals looking to profit off their code cannot do so as trivially as with a binary file, as any checks for whether or not the user has paid can easily be stripped out of the code.
Additionally, interpreted programs tend to be much slower than binaries, as they must be translated while running. The final glaring shortcoming of interpreters to be touched on is the reliance on the interpreter. A binary can be sent to a friend or customer and run on their machine without issues. The interpreter, however, needs to be on a system on which code should be run. If the system does not have the interpreter installed, it must be installed alongside the code. This can prove impractical and inconvenient for large businesses trying to make the installation of their product as simple as possible.
A real-world example of this is Minecraft. The player would have to download Java and the Minecraft application to play if it was not previously installed. However, Java is a special case language, as it is compiled and interpreted. Strictly speaking, compilation only refers to transforming code from one language into another, though it most commonly refers to turning code into binary. In the case of Java, however, the finished "Java bytecode" file is not run by the OS directly, as is the case with regular binaries. Instead, the Java virtual machine (JVM) runs this file, leaving us with a language that first compiles into an intermediary language between code and binary, which an interpreter runs.

Bash is commonly used in Linux to perform various tasks to work with the system. Its name is an abbreviation for the "bourne again shell". This is a wordplay, as it sounds very similar to "born again shell". It is "born again" as it is meant to be a FOSS replacement of *sh* (bourne shell). *sh* was named after its creator and, therefore, (partially) shares its name with him. These days, Bash has become the default shell for most popular Linux distributions. A shell is an interpreter that lets a user talk directly to the system using text commands. For example, to retrieve a list of files in the folder the user is currently in, they would type: `ls`. This runs the *ls* program on the system, which has the abovementioned functionality. The `firefox` command opens Firefox, assuming it was installed on the system. The shell offers more functionality than simply opening programs. For example, one can supply an application with additional information before it starts up (so-called "arguments"), which do various things depending on the program. The following line opens Firefox and opens the website supplied as the first argument (which is `google.com` in this case):
`firefox google.com`

Another interesting feature of Bash is pipes. The following command outputs the text contained in the file supplied as the first argument:
`cat phonebook.txt`
As one can imagine, a phone book is massive and would take up the entire screen tenfold if printed out as such. Additionally, one is typically only interested in one entry (that of the person one wants to call), so seeing all entries simultaneously is redundant. Enter the `grep` command, which takes an input and finds all lines that contain the first argument it is given. The following command lists out all lines in a (currently nonexistent) input which contains the word `bob`:
`grep bob`
On their own, both of these commands will not help us much. However, by plugging the output of the `cat` command into the word-finding ability of `grep`, we can find anyone's phone number and filter out all other entries. The way that these commands can be connected is by using a pipe `|` as follows:
`cat phonebook.txt | grep bob`
This will first read all of the phone books contents and (instead of outputting them) send them over to `grep`, where all lines containing the word `bob` are finally output. If Bob's phone number is in the same line as his name, we can retrieve his number as well. These are relatively simple yet common examples of what Bash can do. In the early history of computing, such commands were the only way to interface with machines, as graphical user interfaces (GUIs) did not exist back then. These days, Windows and MacOS prominently feature their GUIs, letting users click, type, or drag various buttons, icons, or sliders to do something. Most Linux installations on desktops also feature a GUI instead of only a shell. Still, one can easily open a shell on all of those three operating systems and work with that instead. Many IT professionals still frequently use shells for various reasons. For example, many people claim it is faster to do typical administrative tasks, like creating a folder, using a shell rather than a GUI.

Bash refers to not only the shell but also a programming language. It is also POSIX compliant. POSIX is a set of standards made to create compatibility between different OSs. There are various shells that are also POSIX compliant, all of which can run the same scripts that Bash can. It should be noted, however, that while Bash is POSIX compliant, it also has some extra functionality, so other Shells may be unable to run specific Bash commands if they use these features. Therefore, most of its syntax is not unique to Bash, which will be important later. The language to be created here, NoBash, aims to replace Bash in some regards.
However, It should be noted that many of the problems that NoBash aims to fix are targeted at the syntax (how a programming language is written) stemming from the POSIX standard rather than the Bash interpreter itself. The language is called this way as it should be used instead of Bash in specific scenarios rather than attempting to replace it outright. A lot of code integral to the OS is written in a POSIX-compliant language, so using a POSIX-compliant shell at the system core is essential. Additionally, NoBash is meant to run code as an interpreter and is not to be used as an interactive shell where the user can type in commands on the go. It is only meant to replace Bash when a user writes a program to automate some administrative task in Linux, such as renaming all images in a folder or deleting all files containing a word in their name. It is not supposed to act as an interactive shell (like in the previous phone book example) or replace Bash at the system level. It is not POSIX-compliant and would break the system because very important scripts cannot be run anymore. 

# Programming fundamentals
This section aims not to teach the reader how to program in any language fully. However, it is important to understand the basics of various coding concepts. It is also beneficial, though not required, to be able to read some code. This chapter will introduce the concepts, whereas the next will familiarize the reader with actual code syntax. The syntax of a programming language represents the grammar of it, a set of rules to write in that language.

## Functions
Suppose the year is 2030, and you just bought yourself a humanoid robot that will complete various tasks for you. All you have to do is write the different chores down on a piece of paper and feed it into the robot, and it will do them for you. Here is such a list:
```Python
do the laundry 
make a coffee
wake me up
take the dog for a walk
drive me to work
```
This could be considered a programming language. The robot must know how to do all of these tasks before you can tell him to perform them, so you could consider these to be "functions" of the robot. The robot has many more "functions" built into it, and we must choose which ones we want it to perform and when. The robot reads this paper and does all of these steps, one after another. After all, it would not make sense to drive you to work before being woken up. So, the robot goes through each *function* described here and starts doing them. In programming terms, he *calls* the *functions*. This concept surrounds us in our daily lives: When we tell a smart assistant like Siri or Alexa to do something for us, we tell it to do something. The device then calls the respective function internally. This scenario is, therefore, not quite as far-fetched as one may think. 

## Arguments
Now, this robot does not know where you got to work. Let us suppose you currently work at Google, seeing as you are learning programming right now. We must tell the machine that you work at Google so that they can drive you there. In the previous chapter, we touched on "arguments". When we ran the `cat` command, we passed the file `phonebook.txt` as an argument:
`cat phonebook.txt`
We will use this same principle again and pass `Google` as an argument this time: 
`drive me to work Google`
However, this raises an issue, as the machine cannot tell if we are trying to call a function called `drive me to work Google,` call a function `drive` and pass `me,` `to,` `work,` `Google` as arguments or any other such combination. Let us instead wrap all arguments in brackets as follows:
`drive me to work (Google)`
This makes it clear that Google is an argument. We can also remove all spaces to clarify that the function contains all words, not just `work`. The brackets indicate that an argument is being passed, but lines may contain more than just function calls, as we will soon see. It will be important to show what belongs to the function call described by the brackets. Let us remove the brackets:
`driveMeToWork(Google)`
It should be noted that functions can have multiple arguments. For example, the `driveMeToWork` function may require two things: Where you work and what time you need to arrive. When the engineers built the robot, they had to define in which order which argument does what. In our case, they defined the first argument as the location. The second argument, on the other hand, will always be the time. Both arguments are written in brackets but with a comma dividing them. This leaves us with the following line: 
`driveMeToWork(Google, 9:00am)
When we apply this to all other instructions (and leave the brackets empty if the function does not require any arguments):
```Python
doTheLaundry() 
makeACoffee()
wakeMeUp()
takeTheDogForAWalk()
driveMeToWork(Google, 9:00am)
```

## Return values
Let us introduce two new functions: `say` and `whatDateToday`. Say takes one argument and says it out loud. WhatDateToday "returns" the current date. "Returning" can be thought of as the function, after it was called, being turned into the value it returns (or into the "return value"). So, let us suppose today is the `24.12`. The following line would run:
`whatDateToday()`
and would turn into the current date:
`24.12`
If the function were to be called the day after, it would output the 25th. The following line also says the current date, so one could wonder why one would use this function:
`say(24.12)`
The problem with so-called "hardcoded" values (where the value is written out in the script and cannot change) is that they are unchanging. While this function call would work today, we would have to manually create a new instructions list daily to add the proper date. At that point, we do not need the robot to tell us the current day, as we had to hardcode it into him ourselves. Instead, we can use the following line:
`say(whatDateToday())`
We have previously only faced lines containing one function call, so this may be confusing at first. Like in math, the robot will first call functions that are contained in the innermost brackets from left to right. So, it would run `whatDateToday()` first and replace the function call with the result it returned (which is the current date):
`say(24.12)`
At this point, the robot would call the second function `say` and tell you the current date. 

## Variables
Let us introduce a new function called `tell`. Tell operates virtually the same way that `say` does, but it takes a second argument specifying to whom it should say the first. Here is an example of this:
```Python
tell(me, Good monring!)
tell(Alice, Good monring!)
```
The robot should tell you and Alice, "Good morning!". However, as you may have spotted already, we mistyped "morning" and wrote "monring" instead. If we were to extend this program to wish everyone we know a good morning, we would have to correct this error hundreds of times. Additionally, we may have avoided making a typo, but we wanted to change our message for another reason. Either way, there are more elegant solutions. Instead, we should use variables. These work just like in math. We can define a variable using an equal sign. The letter or word to the left is the variable, and everything to the right is the variable:
```Python
message = Good morning!
```
Instead of writing out the message everywhere now, we can instead give the variable name:
```Python
message = Good morning!
tell(me, message)
tell(Alice, message)
```
We can now edit the value in the variable assignment if we ever want the robot to say anything else. There remains one problem. The robot does not know whether we want him to say what is contained in the variable `message` or to literally say "message". We must indicate whether this is a "string" or a variable. In programming, strings are a sequence of characters. A single letter, number, sentence, or an entire book are all sequences of characters and, therefore, are strings. Traditionally, in programming, strings are defined by being enclosed in quotes. This means that we have to change the first line a bit:
`message = "Good morning!"`
The robot can now tell that `message` is a variable and that `"Good morning!"` is a string. However, what if your message needs to contain a quote? The following example would not work:
`"I just wanted to say "Hello" to you!"`
The robot would read this as two strings: `"I just wanted to say" ` and `" to you!"`. With `Hello` in the middle. The robot could not work with this and probably shut down. Instead, the backward slash (`\`) is commonly used as an "escape" character. It removes functionality from special characters, such as the quote. Let us insert it into our previous example: 
`"I just wanted to say \ "Hello\" to you!"`
Now, the robot will not interpret the quotes around `Hello` as string terminating/starting but as literal quote characters. The slashes will not be said or interpreted by the robot.

## Various types
We have already encountered strings and variables, but several other data types in programming regularly occur. `integers` are whole numbers, or numbers that do not have a decimal point. Examples include 1, 2, -3, and 0. `floats` or `floating-point numbers` are the opposite of integers, as they are all numbers including a decimal point. Examples of these are 1.4, -3.4, and 12.05. True and false are `booleans` or `bools`. Sometimes, there is nothing, and this must be represented. We have the nonetype for these cases, though this is called differently in various languages. Some typical implementations are: `none`, `nil`, and `null`. The last types we will go over here, which are more complex than the rest, are a `list` and `dictionary`. Lists are stored for other values. In many languages, they are represented by square brackets. They can contain various items like strings, integers, or even other lists. For example, the robot may need a list of friends to say "Good morning!" to. This would look as follows, as square brackets denote the list, and commas separate the individual list items:
`["me", "Alice", "Bob", "Jim"]`
Lists are helpful as we can access various entries at different indexes (or locations). For example, the name at index number one is `"Alice"` while `"me"` is at index zero. Although this may take some time to get used to, indexes typically start at zero in programming since computers themselves start counting from there. Finally, we are left with the `dictionary` or `dict`. While the lists use the index of a value to locate it, dictionaries use strings. Here is an example of a dictionary which contains each person and their age:
`{"me": 17, "Alice": 21, "Bob": 20, "Jim": 18}`
Each name has a corresponding age assigned to it, separated by a colon. Just like with the list, each set of these "keys" (the name) and "values" (the age) is separated by a comma. If we wanted to access the element at index zero in a list stored within the `names` variable, we would write:
`names[0]`
If, instead, we wanted to get the age of Alice in the dictionary shown above saved in the variable `ages`, we would write the following:
`ages["Alice"]`


## Control flow constructs
An essential feature of programming is control flow constructs. Although they may vary slightly from language to language, these are the three most common control flow tools: `if`/`else`/`elif`, `for`, and `while`. It should be said that Python uses "elif" while many other languages use "else if". These are called "control flow constructions" as they change (*control*) the order and execution (*flow*) of all functions that are a part of it (part of the *construction*)
### If, Else and Elif
The robot should not drive you to work on Sunday. Additionally, you only have to be at work at 10:00 a.m. rather than 9:00 a.m. on Thursdays. With the current construction, the robot would drive you to work at the same time every day. The function `getDayOfTheWeek` returns the day of the week. Let us add a check which only drives us if today is not Sunday. This time, let us look at the code first and break it down after:
```Python
if getDayOfTheWeek() != "Sunday":
	driveMeToWork("Google", "9:00 a.m.")
	say("Have fun at work!")
```
We can break this down into the condition and the consequent. The condition is the following:
`if getDayOfTheWeek != "Sunday":`
First, we start the line with an `if` to show that we are making an if condition here. We end the line with a colon, indicating that the following pieces of code are a part of this construction. In Python, we can denote which lines are affected by the condition in Python by indenting them (or having them pushed back relative to the condition by a fixed amount). The following two lines are both pushed inwards a bit, indicating that they are affected by the condition. The actual requirement which must be met is the following: 
`getDayOfTheWeek() != "Sunday"`
Assuming that today is Monday, the function would return this, and the line would look as follows during the execution of the script:
`"Monday" != "Sunday"`
In programming, `==` means "is the same", `!=` not the same, `>` greater than, `>=` greater than or equal to, `<` smaller than, `<=` smaller than or equal to. One thing to mention is that both `=` and `==` exist in programming. The difference is that `=` is used to set a variable, and `==` is used only to check whether two things are equal. In our example, we are therefore comparing whether or not `"Monday"` and `"Sunday"` are different or not. They are not the same; therefore, the check passes, and we get a result of the `True` boolean. If both values had been the same, the check would have failed since they are not different. The line, therefore, looks as follows:
`if True:`
Now, `if` checks whether or not `True` is true, or, in other words, if the previous check has passed. It has, and therefore we move on to the consequent. In this case, the consequent contains function calls to drive us to work and say bye. These functions are then called. If the condition was not met, in which case it is Sunday, all lines that are indented are skipped over, and we are not driven to work. Nevertheless, we are still met with the problem of coming to work later than usual. Let me restructure the example and add two more conditions: `elif` and `else`:
```Python
day = getDayOfTheWeek()
if day == "Sunday":
	say("It's Sunday, no work for you! Have fun!")
elif day == "Thursday":
	say("It's thursday, we can leave later! Have fun!")
	driveMeToWork("Google", "10:00 a.m.")
else:
	say("Have fun at work!")
	driveMeToWork("Google", "9:00 a.m.")
```
In this example, we first check whether it is Sunday or not. If it is, the robot tells us to have fun on our day off. Then, we move on to an `elif`. The `elif` is like an `if` statement, except it only runs the check if the previous `if` and `elif's` failed. It knows that they are linked up since they are in a line. Here is an example outlining this:
```Python
if True:          # If number one
	...
elif True:        # Elif number one
	...

if False:         # If number two
	...
elif True:        # Elif number two
	...
```
In our example, it may not be apparent why we can't just use another `if` condition. This is a valid point, so here is another example which demonstrates why the `elif` is so important:
```Python
x = 5
if x < 10: # If x is smaller than ten
	say("x is smaller than ten!")
elif x < 20: # If x is smaller than 20!
	say("x is smaller than 20 but bigger than 10!")
```
In this case, we only want the `elif` condition only to work if the previous one failed. If we used an `if` comparison instead of `elif`, both `if`s would run as 5 is smaller than 10 and twenty. This would not work as we want the second condition only to pass if `x` is larger than ten but smaller than twenty. By using an `elif`, because the first condition would be true, the `elif` would not run. If the first condition was false but `x` is smaller than 20, the `elif` check would pass. In such cases it is imperative that a condition may only pass if the latter didn't.

You may have noticed the pound symbols followed by some text in this code snippet. The pound symbols indicate a comment. Them and all subsequent text is marked as a "comment" and the robot safely skips over them. They are meant to leave messages to you and other programmers to explain what your code does. In this example, the comments number each condition. In `if` and `elif` number one, the `if` condition is met (as it is `True`). The `elif` construction, even though it is also met, does not run. This may make more sense with the name other languages give it: `else if`. In other words: "Check if all previous conditions were met. *Else*, if they were not, check *if* this one is met". This also leads us to the third and final conditional, the `else`. While the `elif` still checks whether its condition was met or not, the `else` runs if all previous checks failed, like so:
```Python
# This else will run
if False:
	...
elif False:
	...
else:
	...       # This runs as nothing before it did

# This else will not run
if False:
	...
elif True:    # This condition was met
	...
else:
	...       # This does not run, as a previous
	          # condition was met

``` 

### For
In a previous example, we have looked at saying "Good morning!" to multiple people and at lists. Instead of copying a line and changing the name of each individual to greet them, we can automate this process. Let us look at an example of what *not* to do:
```Python
tell("me", message)
tell("Alice", message)
# insert 50 more messages)
tell("Bob", message)
```
As you can see by the comment, this task could become 53 messages long and would take a long time to write. Worse yet, if you want to change something, like have the robot say two messages to someone, you would have to edit every single line or write another 53 lines. This is why programmers are told never to copy-paste code very early on. Instead, they should write it once and call it several times using programming logic. Instead, let us use a `for`-loop. First, we will have to create a list with all the names as follows:
```Python
names = ["me", "Alice", "Bob"]
for name in names:
	tell(name, message)
```
As with the conditionals, everything that is indented after the `for` loop will be affected by it. Let us look at the loop:
`for name in names:`
Again, just like with the conditionals, the `for` and the semicolon indicate that this line denotes the start of a `for`-loop and that the following lines belong to it respectively. As for `name in names`, this part tells the robot to repeat the indented lines for every name stored in the value to the right (here, this is the list `names`). So, the robot will return the `tell` line three times, as there are three names. Additionally, each time it runs the line, it will set the variable before the `in` keyword (`name` in this case) to the current item of the list. For example, during the first "iteration" (or loop) `name` will be `"me"`. During the second iteration, when repeating all of this code, `name` will be `"Alice"`. The robot will, therefore, run `tell(name, message)` three times, with `name` being set to each friend (or yourself) in the list each time. 

### While
Now that we have looked at `if` and `for`, `while` can be seen as a mixture of the two. Here is a slightly more example in which the robot counts to 100:
```Python
x = 1
while x != 100:
	say(x)
	x = x + 1
say("That's it!")
```
In the first line, a new variable `x` is set equal to one. Then, a while loop is started. Like a `for` loop, a `while` loop will repeat all indented instructions. However, when it starts the loop, and during each iteration, it will check whether the condition is true and only perform the loop if it is true. In our example, `x` is initially 1, which is not 100. Therefore, the robot performs all indented code. First, it says the number. It then sets `x` to itself plus one, or, in other words, increments `x` by one. It then repeats this loop. Now, `x` is two, which the robot will say, then three. This continues until `x` is 99. The robot will still say 99, but this time, when one is added to `x`, `x` becomes 100, and the condition (that `x` is not 100) is no longer met. The loop stops, and all unindented code is run following the loop. In this case, the last line is no longer indented; the robot will run it only once when the loop is done.

## Defining functions
Again and again, we have encountered reasons why we should refrain from repeating code. We have used variables to save different values and loops to repeat consecutive lines. Nevertheless, one case is not been accounted for yet:
```Python
wakeMeUp()
# make me breakfast, but there is no function for this
cleanTheHouse()
# make me lunch, but there is no function for this
walkTheDog()
# make me dinner, but there is no function for this
```
As the comments say, the robot currently has no function to cook anything. What it does have, however, are the following functions: `startStove`, `stopStove`, `putInPan` (which takes a food as an argument to put in the pan), `prepareFoodForPan` (which takes a food as an argument again), `serveFood` and `letPanSit`. So, if we wanted to cook some eggs for breakfast, we could write the following:
```Python
startStove()
prepareFoodForPan("eggs")
putInPan("eggs")
letPanSit()
stopStove()
serveFood()
```
However, this would be quite a lot of code to repeat three times, once for each meal in the day. We also cannot use a `for` or `while` loop this time since there is some code in between the cooking (`cleanTheHouse()` and `walkTheDog()`), which we do not want to add into the loop. Instead, we will create our own function. Previously, we have always only called functions, but they can also be defined. A function is just a collection of code that can be run anytime. Let us define this function for cooking eggs in Python:
```Python
def cookEggs():
	startStove()
	prepareFoodForPan("eggs")
	putInPan("eggs")
	letPanSit()
	stopStove()
	serveFood()
```
Just like with the control flow constructs, we must first use a keyword (like `if` or `for`) to tell the robot that this line will define (hence: `def`) a new function. This makes sense as we tell the computer what this function entails (or *define* what it will do). Next, we must write the function name, `cookEggs` in our case. It does not matter what you call the function, but it is easier to understand the code if you choose something descriptive. We then add two brackets, as if we were calling the function, and end the line using the colon we have seen before. Then, we indent all subsequent lines which should be a part of the function. We are finally done writing our function and can finally call it. This is done just as we have been doing it with functions we have not defined ourselves. Here is an example of us asking the robot to cook eggs four times:
```Python
cookEggs()
cookEggs()
cookEggs()
```
While eating eggs is fine for breakfast, we want to eat something else for lunch and dinner. Let us add arguments to our function to change what we want to cook dynamically. To do this, we will have to change the function definition a little bit:
`def cookFood(food):`
We added ' food ' inside the brackets, where arguments usually go when calling a function. We also renamed the function to be more general, as we want to cook more than just eggs now. `food` is now a parameter. When we pass a value to a function when calling it, this value is an `argument`. When we define a function and tell it to accept a value, this value is stored in a variable called a `parameter`. It is easiest to demonstrate this using our above example:
```Python
def cookFood(food):
	[...] # Code was left out for readability
	prepareFoodForPan(food)
	[...] # This is not Python and just for readability

cookFood("eggs")
```
Here, we can see the `cookFood` function being defined along with one parameter: `food`. Inside the function, `prepareFoodForPan` is called, and an argument is passed. This argument is `food`. `food` is a variable. Specifically, it is a parameter of the function. Finally, `cookFood` is called along with `"eggs"` as a parameter. All the code inside `cookFood` is called when the function is called. Additionally, inside `cookFood`, a new variable exists, `food`. Food contains `"eggs"`, as it was passed to the function as an argument. If you want to pass more than one argument, you can also add more parameters as such:
`def cookFood(food, time):` and `cookFood("eggs", "12mins")`
Since we used parameters to cook various dishes, let us see this in action:
```Python
def cookFood(food):
	[...]
	prepareFoodForPan(food)
	[...]

wakeMeUp()
cookFood("eggs")
cleanTheHouse()
cookFood("fish")
walkTheDog()
cookFood("steak")
```
In this example, all the code contained in `cookFood` will run three times. First, the robot will wake you up. The first time `cookFood` is run, `food` will be `"eggs"`. `food` is then passed on to `prepareFoodForPan`, so the robot will prepare eggs. It will then clean the house. The second time the robot cooks something, we pass `"fish"` as an argument, which is saved in the `food` variable (or parameter). The third meal will be a steak. Finally, let us take a look at return values. We have already seen that functions can return something, like how `whatDateToday()` gives us the current date. We can do the same in our function. Let us introduce a new function, `checkFridge`. This function takes one type of food as an argument and checks whether you have it in your fridge. After all, you cannot cook what you do not have. If you do not have the food, it will return `False`; otherwise, it will return `True`. So, let us introduce a check to see whether or not you have the food you want to eat and tell us if something went wrong:
```Python
def cookFood(food):
	if checkFridge(food) == False:
		return "We don't have the food!", "Sorry!"
	[...]
	return "Food was cooked!", "Enjoy!"

resultOne, resultTwo = cookFood("steak")
say(resultOne)
say(resultTwo)
```
We must use the `return` keyword here. Usually, we have to call functions using brackets. `return` is not a function, and we can omit the brackets. When `return` is used, the function will immediately exit, and we will continue with the code after the function call. As such, if `checkFridge` is false, we use `return` and do not execute any of the subsequent lines in `cookFood`. Additionally, we are returning two values in this case. The first is a message telling us that we no longer have that type of food, and the second tells us that the robot is sorry. If, on the other hand, the robot does find this food in the fridge, the return is *not* triggered, and the rest of the code is run. Functions automatically return when their end is reached, but we can also manually return and set return values. In this case, if the code has gotten this far, we know that everything went all right (as otherwise, we would have returned at the previous check for food availability). After we have returned, we save the two messages in two different variables as follows:
`resultOne, resultTwo = cookFood("steak")`
The first message, telling us whether everything went well, is stored in `resultOne` as it is also the first message to be returned in both cases. The second message containing "Sorry!" or "Enjoy!" is stored in `resultTwo` as those exclamations are the second values to be returned, and the variable is the second to the left. Here is a final example showing all of the orders of both parameters and return values:
```Python
def returnSomething(x, y, z):
	return x, y, z

x, y, z = returnSomething("x", "y", "z")
say(x) # The robot says "x"
say(y) # The robot says "y"
say(z) # The robot says "z"
```

# NoBash syntax
The end goal of NoBash is to be as simple as Python while being as tightly connected to Linux as Bash. It should be repeated that the syntax Bash uses is neither unique to it nor invented by it. Instead, the Bash syntax merely adheres to the standard set by POSIX. Bash is, therefore, one of many languages with such a syntax. However, it is one of the most popular and recognizable POSIX-compliant Shells. That is also why Bash is specifically "targeted" in this language's name, as "NoBash" is to be read as "no Bash", implying that this new language replaces Bash. 

One critique I have against Bash is the various design choices in the syntax. Many people, including me, still use it, even though we agree that the syntax has flaws. The only reason why we still do so as it has great utilities and integration with the Linux OS. This is subjective, but I find the syntax of Bash confusing and not pleasant to look at. I would only use it to run various programs and to pipe their different inputs into one another. As soon as more complex programming logic is involved, I prefer Python. The problem with Python, however, is that while it is very convenient to implement programming logic, it is a lot more challenging to interact with the operating system, like running different programs, reading their output, or writing to a file. Let us first look at some Bash syntax. This script will calculate the factorial of a number:
```bash
#!/bin/bash

fileName="numbers.txt"

countThree=0
countFive=0

while IFS= read -r line; do  # Repeat this for all lines
					# and store the line in "line" 
	if [[ "$line" == *"3"* ]]; then
		countThree=$((countThree + 1))
	fi
	if [[ "$line" == *"5"* ]]; then
		countFive=$((countFive + 1))
	fi
done < "$fileName" # Take the lines from the file stored
                   # in the variable fileName

echo "Threes: $countThree"
echo "Fives: $countFive"
```
Some of the more complicated lines are explained with comments. We will not go over every line in this script, but we should closely examine a couple of spots in it. For example, you cannot add arbitrary spaces in many locations. This, for example, is not allowed:
`countThree = 0`
Python is very lenient regarding spacing, letting users have a near-free reign over how they want to space everything. Even the indentations can be one tab or two tabs, consist of spaces, or be one space. Python will allow it as long as the indentation is consistent. Next, we have a `while` loop. This `while` loop goes over every line in a file we are trying to read:
```bash
while IFS= read -r line; do
	[...]
done < "$fileName"
```
When we use `< "$fileName"`, we feed the file's name into the loop. The loop then uses the `read` tool to read the file's contents. Additionally, we use special tricks like `IFS=` and `-r` to ensure the lines are correctly formatted. Finally, we store each line in the `line` variable. Inside the loop, we have two `if` comparisons:
```bash
if [[ "$line" == *"3"* ]]; then
	countThree=$((countThree + 1))
fi
```
First, we must wrap our condition in two sets of square braces. Instead of a simple colon, we must end it with `; then`. Also, instead of using indentation, we must end the condition with the reverse spelling of it (`fi` instead of `if`). `while` and `for` must end with `done`. We compare the line with `*"3"*` in the condition. The asterisks mean "anything". So, the check is for whether the line is equal to anything to the left of a three, followed by anything. In other words, we are checking whether the line contains a three. In Python, this entire line would look like this:
`if "3" in line:`
This can be read nearly like English: `"if 3 (is) in (the) line:"` If this comparison turns out to be true, we set the variable `countThree` equal to itself plus one. However, instead of simply writing this like in Python, we must enclose any mathematical operation with `$(( ))`. In Python, this can be written in one of two ways:
`countThree = countThree + 1`
`countThree += 1`
As a comparison, here is this entire program written in Python:
```Python
countThree = 0
countFive = 0

with open("numbers.txt", "r") as file:
	data = file.readlines()

for line in data:
	if "3" in line:
		countThree += 1
	if "5" in line:
		countFive += 1

print("Threes:", countThree)
print("Fives:", countFive)
```

In the previous chapter, we have been working with Python when programming the robot. However, there is one function we still need to cover. The robot has a "say" function, which makes the robot say something out loud. Python has the `print` function, which will output (or *print*) anything passed as one or more arguments to the screen. As previously mentioned, Python is not as tightly integrated with the operating system as Bash is. This is why reading the file is the most challenging part of the script: 
```Python
with open("numbers.txt", "r") as file:
	data = file.readlines()
```
In the first line, we open the file `"numbers.txt"` in read mode (`"r"`) since we want to read the data. If we wanted to write to the file, we would use write mode (`"w"`). `as file` tells Python to save a reference to the opened file (but not its contents) in the `file` variable. We then run `file.readlines()`. `readlines()` is a method. Methods can be thought of as very similar to functions, except that they specifically do something with the variable in front of them. In this case, the function reads all the lines of the file stored in the `file` variable. The lines are returned to us in a list, whereby each line is an item in the list. These lines are then saved in `data`. This means that we can run `for line in lines:` and have `line` contain an actual line from the file sequentially.

However, there are two things that Bash does "better" than Python. The first is that Python uses indentation to demonstrate which lines belong to a construction. The approach that Bash takes, namely full words to close a construction (`fi`, `done`), can be very messy, so most languages use curly braces like so:
```
if x == 10 {
	say("X is ten!")
}
```
If two programmers write Python code, they might use different programs to write the code. One program may insert two spaces to indent a line, whereas another might add a tab. This will break the Python code as the indentations are no longer consistent, which Python requires to work correctly. On the other hand, curly braces are the same in all IDEs (A type of program to code in) and across all devices. This makes braces ideal for collaborating on code. The second issue with Python is a beneficial feature in most cases, so it would be unfair to call it something Bash does "better". We have already encountered methods previously (`file.readlines()`). Methods are usually handy, but in our case, when writing only small scripts to complete small tasks on the system, they are unnecessary and can be confusing for people who have just started to code. As such, NoBash will not feature methods. Therefore, the syntax of NoBash will be like that of Python but without methods or forced indentation; it will rely on curly braces instead. Here is the program from above in NoBash:

```
countThree = 0
countFive = 0

data, worked = readlines("numbers.txt")

for line in data {
	if "3" in line {
		countThree += 1
	}
	if "5" in line {
		countFive += 1
	}
}

print("Threes:", countThree)
print("Fives:", countFive)
```

NoBash is syntactically similar to Python. The only differences are the aforementioned curly braces, some small changes in keywords (defining functions is done with `func` rather than `def`) and lack of methods. In terms of functionality, it borrows heavily from Bash. Everyday operations like reading or creating a file, running a command, or starting an application should be trivial to do. Linux usually comes with the GNU core utils, which are a group of programs like `ls` (which lists the contents of a folder), `cd` (to move inside a folder), or `cat` (which, among other things, reads out a file). NoBash should have built-in functions that act as a bridge between NoBash and the common core-utils, letting programmers efficiently use any of the tools by simply calling a function. It should be as pleasant to write in as Python while being as powerful in Linux as Bash. Here is an overview of how to do a couple of things in NoBash:

```
// Comments are started with a double slash

// Functions are called like in Python
// Do not separate the function name and brackets
// NoBash uses put instead of print or say
// Put combines two arguments and outputs them both
put("hi", "how are you?") 
// Will say: "hi how are you?"

// Variables are set using =
x = 10

// Functions are declared using func, same as Python
// Defined parameters x and y
func giveBack(x, y) { 
	x += 1 // This is like: x = x + 1
	y *= 2 // This works with all operators
	return x, y    // You can return like in Python
} 
// Started and ended with curly braces

// Multiple return values can be saved using commas
x, y = giveBack(1, 2) 

// If/elif/else
if x == 2 {
	put("x is 2!")
} elif x == 3 {
	put("x is 3!")
} else {
	put("x is neither 2 nor 3!")
}

// In nobash, you use a function to make a list...
l = list(1, 2, 3)

// and a dictionary. Key: Values are made like in Python
d = dict("a": 1, "b": 2, "c": 3)

// for loops are just like in Python
for item in l {
	put(l)
}

condition = true
// while loops as well
// This loop will only run once
while condition == true {
	condition = false
}

// It is advised not to put numbers 
// in variables or functions names
hello1 = "hi"     // Not recommended
helloOne = "hi"   // Recommended

// Negative numbers are created using the
// neg function like so:
x = neg(1)
put(x)
```

# Making NoBash: An overview
Making a programming language is a complex and difficult task. However, by breaking up this monstrous challenge into several minor hurdles to overcome, the prospect of finishing such a large-scale project becomes more feasible and attainable. A child who has never cooked before would struggle greatly when told to bake a cake. However, if said child was told to split up this challenge into smaller parts, such as mixing the ingredients, baking in the oven, cooling the cake down, and decorating it, the child could take on each step at a time and create a cake without too much of a hassle. When broken down, the problem seems very manageable as the individual challenges are small and easy to overcome. When seen as a whole, however, the distinction between "smaller issues" and "massive undertaking" becomes blurry even though the end goal, like baking a cake, has not changed.

The creation process of NoBash relies on this exact principle. Everything will be split up into smaller steps, called "*levels*". Each level takes up an entire chapter and will tackle a specific feature the program must have. Like lone Lego bricks, the levels do nothing on their own, but when put together and working together, like the Lego bricks mentioned above put together to create a life-size statue, they will create the end product. Each brick plays a crucial role, acting as a foundation for bricks above it and expanding on the ones below it. 

Returning to the example of baking a cake: Each step individually will not work. Without mixing the ingredients, for example, you have nothing to bake. You must refrain from reordering any of these steps, as decorating the cake before mixing the ingredients would destroy any decorations. This also applies to the levels. Level one must always act as the foundation for all subsequent ones and may not be reordered. Level two take what level one produced and build on top of it. This continues until the final level, at which point the program has done its job successfully.

This project will be split into a "compiler" and an "interpreter" part. Both of these parts are then split up into levels. The programmer first writes their code. The compiler then transforms this code into what NoBash calls "instructions". The interpreter part then picks up where the compiler had left off, taking these instructions and running them. The instructions convey the exact same commands as the code the programmer wrote albeit in a format that the computer can work with more easily. However, they are not very easy to read, nor are they convenient to write for the programmer. This approach , therefore, combines the best of both worlds, as the programmer works in an simple coding language, which is then transformed into instructions that the computer can read well. 

## The compiler
In the grand scheme of things, the compiler can be compared to a translator. A person who only speaks German may want to communicate with an English speaker. It would be inconvenient for both parties to start speaking a language they do not know well. Instead, a German sentence can be translated into English using a translator. Crucially, no information is lost; the words and grammar may change, but the data they convey is left unaltered. 

The programmer is a German speaker. For the programmer, a language that is easy to write and readable at a glance is important. The computer, in this case, would speak English. For it, English must conform to stringent rules, as it, unlike humans, is terrible at detecting patterns and relies on the language spoken to it to remain uniform. In turn, however, it can quickly process data that is nigh-unreadable for us humans as long as it adheres to a set of rules. German represents the programmer's traditional coding language, whereas the NoBash instructions are English.

A practical example of this would be the following:
*Code:*
`put("Hello, how are you?")`
*Instructions*
```
0, 1, put, "Hello, how are you?"
```
In the code, a function "put" is called with the string "Hello, how are you?" being passed as a parameter. The "put" function is the equivalent of the Python "print" function. Anything passed as an argument will be out*put* to the screen (hence the name). The interpreter would therefore read this instruction, detect that we are trying to call the `put` function and pass `"Hello, how are you?"` as an argument. It will then perform said action, outputting the string to the screen, before moving on to the next instruction and running that.

The instructions are composed of two numbers followed by the function to be called (here it is "put") and the argument(s). Each element is separated from the next by a comma. The first number is the *instruction number*. Just like how the pages of some books have line numbers, every instruction is numbered too. The instructions are derived from a line of code, the number of which is specified by the second number. Multiple instructions may originate from the same line, so a distinction between the number for the instruction and the line it comes from is essential. Here is an example of one line containing two instructions:
*Code:* 
`put(add(1, 2))`
*Instructions:*
`0, 1, add, 1, 2`
`1, 1, put, ret0`
In this example, the `put` function should output the result of adding one and two. In code, this is done by passing the `add` call as an argument to `put`. Since instructions can only contain one function call per line, we must split the line up into two instructions and specify that we want to pass the returned value from the `add` instruction as an argument to `put`. This can be done using the `ret` system. When `add` is run and returns three, that value will be saved under the variable `ret0`. The `ret` indicates that it contains a returned value and the subsequent number (`0` in this case) is the number of the instruction the value was returned from. In this case, we are told that `put` should output the return value of instruction zero. The instruction numbers are used not only for the return system, but also to identify specific instructions. The interpreter needs the instruction number to know which instruction to run specifically. If any instruction fails, the programmer needs to know what they must fix. To them, the instruction number is irrelevant as they never directly work with the instructions. They therefore need to know on which code line an operation failed, which is why the line number in the instructions is so important as well.

The compiler does not output only raw instructions but also other information important to the script. For example, it must somehow convey on which instruction number a function starts and what parameters it takes. Information must therefore be classified. NoBash uses the approach of "sections". The `Instructions` section contains instructions whereas the `Functions` section contains function definitions. A section is defined using the following format: `# [Section name]`, whereby `[Section name]` is the name of the section. All lines following this definition belong to said section. This continues until either the last line is reached or a new section is defined.

*Code:*
```js
1. put("hello") // Outputs 'Hello' 
2. put(1 + 3.5) // Would be 'print(1 + 3.5)' in Python
3. // Note that the interpreter ignores comments
4. 
5. func sayHi() { // Defines a new function 'sayHi'
6.    put("hi") // This is ran in the 'sayHi' function
7.    put("how are you?")
8. } //everything past here is not part of the function
9. 1 + 1 // This is calculated, but not output
10. put("End of program!")
```
*Instructions:*
```
# Instructions
0, 1, print, "hello"
1, 2, add, 1, 3.5
2, 2, print, ret1
3, 8, print, "End of program!"
4, 8, __exit__
5, 6, print, "hi"
6, 7, print, "how are you?"
7, 7, __return__
# Functions
sayHi, 6
```

## The interpreter
Once the compiler has generated the instructions, the interpreter takes over and runs them. When it comes upon an instruction, the interpreter tells Python what to do and has it actually performs the computational actions to produce the desired effect. For example, when the interpreter finds an `add` instruction, it will get Python to actually add two numbers together rather than doing so itself.

Function calls are not the only ones turned into instructions. Control flow elements such as `if` conditionals are also turned into instructions. Even things like closing braces ("}") are turned into instructions. No information can be lost during the translation process, so these elements must be turned into instructions, too.

It should be noted that even though it is Python that gets the computer to perform a task like adding two numbers, NoBash is not simply Python. In the same vein, Python itself does not execute anything itself either. Instead, it is the C programming language that does this. However, you would be hard-pressed to find someone telling you that Python is not a real language because it was written in C. 


# The Compiler

## Reading the code file (Level 1)

The programmer writes their code and saves it in a file, ending with a ".nb "extension, standing for "**N**o**B**ash ". A possible example of a file name may be: "script.nb ". The code is stored as a file on the system. The compiler has not yet read the contents of the file, which needs to have this code to be able to work with it. In this level, we will create a system that reads the code contained in the file.

At this point, a valid question may be why this file must be read when it is already saved on the computer. You will probably still remember what you had for breakfast this morning, but you aren't constantly actively thinking about it. There are simply too many things to be paying attention to for your brain to think of arbitrary facts like this, but you still remember it. When you do need this information, such as when you are asked about it, you recall what you ate in the morning, and the answer is only then present in your mind. 

Machines work similarly. All files, like pictures, are saved in their *storage*, this being either a "hard disk drive" or a "solid state drive". When these pictures are actively being worked with, like when they are being edited in Photoshop, they are loaded from *storage* into "*memory*" (or "RAM"). *Storage* is extremely slow when compared to *memory*, so working with files is only reasonable when they are in *memory*. Once there, they can then be modified or viewed freely. However, memory space is a lot smaller than *storage* space, so it would be wasteful to keep unneeded data in *memory*. So, when done changing the picture, the altered version is saved back in *storage*, replacing the old one. It is then deleted out of *memory* to free the space for new files you may want to work with next.

This level does just that, taking the location of the code file, such as "`C:\Users\Bob\Desktop\script.nb`" if it is saved on the Desktop of the user Bob, and moves its contents from storage into memory. Because we are reading a file, we must simultaneously make sure that we correctly handle any errors that might arise. For example, we may not have permission to read the file, or it may not exist altogether. Finally, because we are doing this from within a function, we can return the code lines to the main program. We must also create a basic error-handling system that lets us call an "`error`" function when something goes wrong. When the function is called, it will stop the compiler and give the programmer information on what went wrong and how they can fix the problem. 

As this is the first level, besides creating the aforementioned file-reading functionality, there is some groundwork that must be laid down for future levels. For example, a `compiler.py` file must be created. This will serve as a "hub" for all levels. The functions from level one are called from here. Their output is then saved in a variable and passed on to the functions from level two as arguments. This cycle then repeats, where the output of one level is used as an input for the next until the final level is run. The `compiler.py` file is, therefore, the backbone of the compiler program, stitching together all levels and their respective functions.

There must also be a way to handle errors. When a problem is encountered during compilation, a function called `error` is called. This will then stop the compiler and display where in the code the error occurred and what went wrong. The programmer can then use this information to fix the problem. An error code specific to that problem is passed as an argument to the `error` function. For example, attempting to read a file that does not exist may have an error code of 6. Any additional information, such as the name of the non-existent file, can also be passed on. Finally, the `error` function outputs a message specific to the error code, such as "Error: tried to read non-existent file {name}", where "{name}" is replaced with the name of the file we passed as an argument. 

As the final step for this level, we create a "`readInput.py`" file. This file contains the `readFile` function, which reads the file at the specified location passed as an argument using the following line:
```python
with open(fileLocation, "r") as f:
```
It then calls the `error` function if something went wrong and returns a list of all the lines in the file. When the user presses the enter key to create a new line, this must somehow be saved in the file using characters that can be turned into ones and zeroes. Newline characters ("`\n`" in our case) are used for this exact purpose, indicating where a new line should be inserted. Each line of code ends on such a character, so these must be removed as they do not convey any information relating to the code.
```python
return [line[:-1] if line.endswith("\n") else line for line in f.readlines()]
```


## Creating a metadata section (Level 2)
Metadata is defined as data that describes other data. For instance, you might have seen that every photo saved on your phone also has a timestamp and location of when and where it was taken saved along with it. This extra information is a good example of metadata. NoBash saves data like the compiler version in the final instructions file. 

The compiler creates the instructions that the interpreter must work with. However, if, say, a script was compiled months ago using a (now) old version of the compiler, the instructions file might have small differences from what a newer compiler would output. When this outdated instructions file is run using a new interpreter, which expects the instructions to be made by an equally new compiler it was made for. These small differences may stop the interpreter from working correctly. Therefore, the interpreter must only run instructions made by a compiler, which creates output in a format it expects.

With the compiler's version number stored, a programmer can tell that there will be version incompatibilities. For example, a script may be compiled at some point. As time passes, NoBash receives an update in which methods are added. As a quick refresher, Methods can, for this example, be thought of as slightly different from functions. Whether or not an instruction is for a method is indicated by a boolean as the final argument as follows:
`0, 1, copy, true`
In this case, the "copy" function is shown to be a method as the final argument is true. The interpreter is updated to add this feature and now expects instructions to have their last argument be a boolean. The old compiler, however, has created a script in which this feature is not a thing yet, and therefore, the final boolean does not exist in most instructions. When these instructions are run using the new interpreter, it will attempt to look for a boolean at the end of each instruction. It will, of course, not find one and error. However, by saving the compiler version, the programmer can tell that the compiler used to create the instructions is now outdated. They can then re-compile the script with a more modern compiler, one that now adds the boolean to the end of each instruction. Now, the interpreter will find the previously missing boolean and work properly.  

We also want to store the operating system, as a script made for Arch Linux may not work on Debian due to subtle differences between the two operating systems. MAC addresses are unique numbers assigned to each device by their manufacturer so that each device has its own MAC address. It can, therefore, be used to identify the machine the code was compiled on, along with the current date and time. Finally, a hash of the code file is made. A hash is a unique alphanumeric number generated from an input. This hash is calculated using mathematical formulas. There are also several different hashing algorithms. This is best demonstrated using an example: If the word "hello" is hashed using MD5, the resulting hash is the following: 
`b1946ac92492d2347c6235b4d2611184`
The hash for "hallo", where only one letter was changed, is the following: 
`aee97cb3ad288ef0add6c6b5b5fae48a`
As can be seen, even the slightest differences in two inputs result in completely different hashes. When the same input is hashed multiple times, the resulting hash will always be the same. If you were to hash "hello", you would, therefore, get the same hash as the one shown above. As such, by having the hash of a file, you can detect whether it was changed or not, as the resulting hash of a modified file would be vastly different from that of the original one. 

Compiling scripts would be redundant when the script hasn't changed from the last compilation, as the instructions would remain the same and would not have to be recalculated. To detect whether the code file has been changed since it was last compiled (and would therefore need to be re-compiled), one can use hashes. Along with all the other metadata stored, the hash of the code file is also stored in the instructions file. When a script is run, NoBash first checks if an instructions file with the same name exists (For example, if "script.nb" were to be run, NoBash would check for a file named "script.nbc"). If it does, the hash stored in said instructions file is compared to that of the code file. If they are the same, then the code file was left unchanged and must not be re-compiled. 

This level is comprised of many different parts, each of which gathers one piece of information, be it the hash, time, or MAC address. Some of the data can be gathered relatively easily, whereas others have some small hurdles to overcome. The data is then labeled and saved so that the MAC address is not accidentally confused for the hash later, for example. Finally, the collected data is returned back to the `compiler.py` file, which will write it to the instructions file in the final level.

As a first step, we will create a `versions` file that will store the current version number of both the interpreter and the compiler. We will update the version numbers every time we release a new version of any of the NoBash programs. 
```Python
with open(path.expanduser("~")+"/.nobash/versions.json", "r") as f:
	data = json.load(f)
```
As a next step, we will create a function `getFileHash`. It will read the code file in a bytes format instead of as a string. Then, in blocks, it will read the file and finally hash it with the "sha256" algorithm using the `hashlib` library. Libraries are code you can import into your own project so that you do not have to implement the logic yourself. Many programmers will want to hash something, so it would be redundant for each individual to have to implement hashing themselves. Instead, one programmer writes the code needed to hash something and saves it in a "library". Other programmers can then download it and use the code contained within it. The `hashlib` library makes creating this level a lot easier for us, as we do not have to implement any of the hashing logic on our own:
```Python
with open(fileLocation, 'rb') as file:
	while True:
		chunk = file.read(fileHash.block_size)
		if not chunk:
			break
		fileHash.update(chunk)
return fileHash.hexdigest()
``` 
We can get the MAC address of the current machine by importing the `getnode` function from the `uuid` library. However, this gives us the address as a decimal number instead of the usual "hex" format that MAC addresses are usually written in. After turning it into such a hex number with the `hex` function, we can then insert a colon after every two characters to finally give the MAC address its usual format. 
```Python
def getMacAddress() -> str:
	mac = str(hex(getnode()))[2:]
	return ":".join([mac[i*2:i*2+2] for i in range(6)])
```
The time is given to us by the `time` function in the library going by the same name. The current OS can be found using the `platform` function, which also shares its name with the library it is from.
```Python
str(time())
platform()
```
Finally, we store all of this data in a dictionary using descriptive names as keys to easily tell which value tells us what and return it.
  

## Replacing all strings with placeholders (Level 3)
In the following example, we will see a call to a function ` foo`, with a string passed as parameters: `foo("2, 3 ")`. Humans are very good at detecting patterns. We, therefore, do not struggle to see that there is only one argument passed: `"2, 3" `. However, a computer may read this as two arguments, namely `"2` and `3 "`, with the comma not being a part of the string but as a delimiter between arguments. The compiler will always look for certain keywords and symbols, such as a comma, and treat them as a part of the script. If strings were kept in each line, the compiler would have to decide whether or not a symbol is part of a string. Depending on the result of this decision, it would then either work with it or ignore the symbol respectively. By simply removing all strings (and therefore all contained symbols), the compiler can be sure that everything it works with can be treated as a part of the script.  

This step requires an algorithm to detect all strings in a line, save their contents for later, and finally replace them with a placeholder so they can be reinserted in the final level. All escaped quote characters (`\"`) must be replaced by a placeholder so that the compiler does not accidentally confuse them with a proper quote. As a quick reminder: escaped quotes are an actual part of the strings contents rather than a signal to stop the string. An example of this is the following string: `"Then I said: \ "Hello, Bob!\"  "`. The string-detection algorithm works independently of trailing or leading characters, meaning that the backslash would be disregarded and the escaped quote be reintroduced as a "live" one, terminating a string. By replacing escaped quotes with other characters, they can't be confused with a proper quote but can still be reinserted later. It must also be ensured that all strings are properly terminated so that no string is ever started and not ended.

As a very first step, all instances of the character sequence `\" ` must be replaced by the placeholder `&QUOTE`. Because escaped quotes are temporarily exchanged with this replacement, the compiler must only deal with "proper" quotes, which serve to open or close a string. When &QUOTE is met by the interpreter, real quotes can be reinserted and used normally when they no longer affect the compiler. In the compiler, this replacement process is done by the following line:
```Python
line = line.replace("\\\"", "&QUOTE")
``` 

The algorithm will then go over every character in the line and save the index of all quotes in a list. Every string must start and end with a quote, meaning that for each string in a line, there must be two quotes. This also means that every line must have an even amount of quotes. We can, therefore, run a check to see whether there is an even amount of quotes in the line. An odd amount would signify that a string was merely started but not ended, in which case an error would need to be thrown: 
```Python
indexList = []
    [indexList.append(i) for i, letter in enumerate(line) if letter == '"']
    if len(indexList) % 2 != 0:
        error(4, [lineIndex])
```

Finally, the algorithm keeps a counter, which is incremented for every string found. It then replaces the discovered string with a reference using the format" `str#`", whereby the `#` character is replaced with the counter. Each time a string is replaced, the counter is incremented by one, making sure that each string has its own unique identifier. The string is then stored in a dictionary as a value, with its key being the identifier we just created. 
```Python
for i in range(len(indexList)//2):
        string = line[indexList[i*2]:indexList[i*2+1]+1][1:-1]
        identifier = "str"+str(stringCounter)
        stringDictionary[identifier] = string
        line = line[:indexList[i*2]] + " "+identifier + " " +line[indexList[i*2+1]+1:]
        stringCounter += 1
```

  

## Indexing curly braces (Level 4)

When a condition of an `if` block is not met, we want to jump past all the code contained in it to the closing bracket. Alternatively, during a `while` loop, we want to jump back to its beginning if the condition is still met. The interpreter will, therefore, need to know what closing bracket to jump to in order to get to the end of an `if` block. In the case of `while` loops, it will need to know what opening bracket the loop started at to jump back to. By connecting each opening and closing bracket using identifiers (IDs), we can always find the counterpart of any opening or closing brace by jumping to whichever bracket has the same ID. This level simply adds a unique number to the end of each corresponding brackets (e.g: `{12` belongs to `}12` and `{5` to `}5`).

As a first step, we can run some basic checks to make sure that no grammar rules were broken by the programmer now that all strings have been removed. For example, there cannot be anything after an opening curly brace or before a closing brace. We will then have to detect curly braces at the beginning and at the end of every new line. We then need to create a new algorithm that iterates over every line and connects the corresponding opening and closing braces with the unique ID appended to them. The algorithm will also store the lines that control flow constructions start and end at. This info consists of their starting and ending lines and what control flow statements start on both of those (as `else` starts on the same line as `if` ends).

Once again, we iterate over every line and make sure that the indexes of all opening and closing curly braces are at the start and end of the line, respectively. If this is ever not the case, we must throw an error. After all, there will never be a case when an opening bracket is not at the end of a line like so: `print({, "hello")`. This is the code responsible for these checks:
```Python
if line.index("{") != len(line)-1:
                error(6, [index])
// ...
if line.index("}") != 0:
                error(8, [index])
```
However, trailing or leading white spaces could cause this check to error, as a space character might now be at the start of an indented line, so the line has to be trimmed first. In programming, "trimming" typically refers to removing all spaces at the start or end of a string. In this example, there is a space character after the opening brace (note that the single quotes are used to illustrate the beginning and end of the line):
`'while true { '`
The compiler would first detect that the line included an opening brace and would subsequently check whether or not it was at the end of the line. This check, however, would fail, as the last character would be a space instead of the opening brace. By removing all leading and trailing white spaces, the last character would be the opening brace again, and the line would pass all checks:
```Python
def trimLines(lines):
    return [line.strip() for line in lines]
```


A separate check ensures that every opening curly brace has a matching closing brace. This can be done by creating a counter, which we will call `curlyCounter`. Every time a line contains an opening brace, the counter is subsequently increased by one. If a closing brace is found instead, it is decreased by one instead. Every time the counter goes into the negative, we know that there is one closing brace too much. We can also store the line at which the counter increased to one last. If, at the end of all lines, the counter is greater than zero, that line had an opening brace that was not closed. Here is the code responsible for this:
```Python
for index, line in enumerate(lines):
	index += 1
	if "{"in line:
		if line.count("{") != 1:
			error(5, [index])
		[...]
		counter += 1
		if counter == 1:
			firstOpen = index
	if"}" in line:
		if line.count("}") != 1:
			error(7, [index])
		[...]
		counter -= 1
		if counter < 0:
			error(9, [index])
if counter > 0:
	error(10, [firstOpen])
```

If the line ends with a curly brace, we have to find the control flow statement at the beginning of the line. However, as this line could be an `else` or `elif` statement, we will also have to check the second word in the line, as the first one would then be the closing brace of the previous conditional (`} else {`). We then have to store all of this information in a dictionary called `bracesInfo` to be able to recall this data in the future, as it will come in very handy later on. Each opening brace must now be matched up with its corresponding closing one by appending a unique ID to all braces in each set. Here is an example of the expected output:

```go
func countUnevens() {0
	x = 0
	while true {1
		if x % 2 != 0 {2
			put(x)
		}2
		if x > 100 {3
			break()
		}3
	}1
}0

if true {4
	countUnevens()
}4
```
An incorrect example in which the braces don't line up would be the following:
```go
x = 15
if x < 20 {1
	if x > 10 {2
		put("x is between 10 and 20!")
	}2
// Note: a closing brace is missing!
```

The algorithm pertaining to this works as follows: first, we create three variables: `bracesInfo`, `activeList` and `maxIdentifier`:
```Python
bracesInfo = {}
activeList = []
maxIdentifier = 0
```
While iterating through all lines, the algorithm checks whether there are any opening or closing curly braces in the current line: 
```Python
for index, line in enumerate(lines):
        if line.startswith("}"):
            // ...
        if line.endswith("{"):
	        // ...
```
If there are, we append the current integer stored in `maxIdentifier` (which starts at zero) to the brace:
```Python
line.replace(braceType, braceType+str(id)+" ")
```
The algorithm then also appends `maxIdentifier` to `activeList` and increments it by one.
```Python
activeList.append(maxIdentifier)
maxIdentifier += 1
```
If the line contains a closing brace, we both remove the last value of `activeList` from it and instead add it to the end of the brace. 
```Python
uniqueID = activeList.pop()
```
This system ensures that no ID is ever duplicated thanks to `maxIdentifier`, as it is used as an ID and is always subsequently incremented. This means that each new ID will always be one higher than the last. The system also makes sure that all opening and closing braces are matched correctly, as the last value `activeList` contains will always match the ID of the last open brace. Here is a quick representation of the above example, with every line also showing both `maxIdentifier` and `activeList`:

```go
func countUnevens() {0           // 1, [0]
	x = 0
	while true {1                // 2, [0, 1]
		if x % 2 != 0 {2         // 3, [0, 1, 2]
			put(x)
		}2                       // 3, [0, 1]
		if x > 100 {3            // 4, [0, 1, 3]
			break()
		}3                       // 4, [0, 1]
	}1                           // 4, [0]
}0                               // 4, []

if true {4                       // 5, [4]
	countUnevens()
}4                               // 5, []
```
   
  

## Storing lines in a dictionary (Level 5)
All humans make mistakes, especially programmers. Typically, when this happens, the error may be a logical one, in which case the programs code is technically correct and will run, but the program does not do what was expected of it. Alternatively, the programmer attempts to do something that is not possible, such as reading a file that does not exist, calling a function that was not defined, or adding a string to an integer. When the latter mistake happens, the compiler or the interpreter will raise an error, resulting in the program ending abruptly (or "crashing"). Typically, the programmer will then be told what went wrong and on which code line the error occurred. 
```go
counter = 1
put(conter) // Note the misspelling!
```
In a program of hundreds of lines, it may prove to be difficult to find a simple typo in a variable name, like attempting to access "conter" instead of "counter" in the example above. The programmer is told what error occurred. In this case, the programmer instructed the interpreter to use a variable that was never defined, as "conter", which is missing a "u", is accidentally introduced. The interpreter will notice that the variable does not exist and, not knowing what to do, will output an error and stop running. Of course, the programmer could look through every line manually and check whether the spelling mistake occurred in it, but this would simply take too long and is very inefficient. To point the programmer in the right direction, the line number is output along with the error that occurred. The programmer can then go to the specified line immediately and attempt to fix the error specified by the interpreter. In order for this to work, we must now connect each instruction with the line number from which it originates.

Currently, we may simply read every line in order and deduce its line number that way. The first line will be line number one in the code file, the second line will be number two, and so on. However, in future levels, we will get rid of empty lines and reorder function calls. The order in which each line appears will, at some point, no longer indicate its line number. It is, therefore, important to save the line number now while the code of the programmer is unchanged and each line is at the same position as it is in the programmer's code file. 

A new dictionary must be created which will tie every line together with its number. We will have the line number be the key and the line itself be the value. However, we do not simply store the line as a string. Instead, we store the line within a list, as this will be important later. We then store this list in the dictionary. If an `add` and a `sub` call were the only lines in a file, the dictionary could look something like this:
```Python
{
	"1": ["add(1, 2)"],
	"2": ["sub(2, 1)"]
}
```
It is important to note that looking up items in a list is faster than in a dictionary, as the latter uses hashing. One might, therefore, propose to store the lines in a list instead, as the first line stored in the list could be taken as the first line in the code file. Here is what the above example would look like using lists:
```Python
[
	["add(1, 2)"],
	["sub(2, 1)"]
]
```
Regardless of the loss of speed, using a dictionary rather than a list works better, as comments and empty lines will be removed in future levels. Additionally, functions will be moved to their own dictionaries in the next step. In a list, after all the empty lines are removed, the index of all following lines is made smaller to fit the now empty gap. If the first line of a script was empty and thus removed in the next step, the second line of the script would take its place and would erroneously become line number one. If we then wanted to report errors in the script, we would falsely report the second line to be the first one in the script based on its location in the list. In order to make sure that each line will always be saved under its correct line number, we will use a dictionary. 

Here is an example in which empty lines are removed in a dictionary:
```Python
{
	"1": ["x = 10"],
	"2": [""],
	"3": ["x += 1"]
}

{
	"1": ["x = 10"],
	"3": ["x += 1"]
}
```
As can be seen, the line numbers do not shift as they are manually defined by the compiler. The line two can be removed without affecting subsequent lines. However, as is apparent in the following example using a list, by removing the second line, the third line takes its place and "becomes" the second line instead:
```go
[
	["x = 10"],  // 1.
	[""],        // 2. 
	["x += 1"]   // 3.
]

[
	["x = 10"],  // 1.
	["x += 1"]   // 2.
]
```
If an error would now occur on line number three, the interpreter would mistakenly report line number two as the culprit. In the original script, line number two is empty, leading to the programmer attempting to fix an error in the wrong line.

Only one new function must be created. In this function, we define an empty dictionary. We then iterate over every line, saving both its contents and its index in separate variables. The index of the line is currently its line number in the code file as well. After turning the index into a string (as dictionaries can't use integers as keys), we use it as a key in the `lines` dictionary and assign an empty list to it. Finally, we append the line to this list before repeating this process with all other lines. These operations are quite frequently done in Python, so "list comprehension" was added to Python as a feature. This allows for the entire functions contents to be written in one line at the cost of readability:
```Python
def turnLinesToDict(linesList):
    return {str(index): [line] for index, line in enumerate(linesList)}
```



## Strip out functions and empty lines and remove comments (Level 6)
Because comments are meant to be ignored by the compiler and interpreter, this level will remove all comments from each line to avoid any potential problems. Additionally, all empty lines will be removed as they carry no useful information. Lastly, function definitions must be removed from the main instructions and saved separately. These include instructions, but they should only be run when the function is called. In this context, instructions are run one after another. Instructions contained within function definitions must, therefore, be separated from the rest of the script. If they were not, the interpreter would execute each instruction, including those within a function definition. This can be done by inserting a call to the function "`__exit__`" in between the script and function definition instructions, which will terminate the program before the latter can be reached. Here is an example of this:
```Python
0, 1, put, "Hello!"
1, 1, __exit__
2, 4, put, "This is a function!"
3, 5, __funcReturn__
```
Here, instructions two and three are both a part of a function. When the interpreter goes over every instruction now, instead of running a function when it was defined, it will first run the `__exit__` instruction, ending the program. If the function is ever called, the interpreter can jump to instruction two and execute all subsequent instructions. For this to work, however, this level must identify and remove all function definitions so that they can be correctly written after the `__exit__` call in the final level. 

We must go over every line and read through the contained line. If it contains the character sequence "`//`", indicating a comment, we will remove everything past and including the "`//`". After this step, we can check whether the string for that line is empty. If it is, we can simply remove it from the dictionary. If a line consists of only a comment, removing it would then cause the line to become empty. It is, therefore, important to remove comments first and delete empty lines afterward in order to remove lines containing only a comment. As a final step, we want to find all function definitions and move them into their own list, separate from the main instructions. For this, we must find the start and end of all function definitions. We then copy all lines in between into a new list specifically made for function definitions before we delete the lines from the original lines dictionary. 


Most levels begin by iterating over all lines, and this one is no exception. However, since we are now working with a dictionary, we must also get the key along with every line (the key being the line number). We can then scan the line within the list for the "`//`" character sequence, indicating a comment. If one is found, it itself and everything following it is removed:
```Python
if "//" in line:
	line = line[:line.index("//")].strip()
```
The line is then replaced with this shortened version of itself. *Whitespaces* are characters representing blank spaces in text and can, among other ways, be created by pressing the space, enter, and tabs key. They are treated the same as letters and numbers, so they may stop the compiler from working properly. For example, `"password "` is not the same as `"password"`. Because the programmer presumably inserted spaces in between the code and the comment, these must also be removed using the `strip` function. Otherwise, in the following line, the interpreter may read the variable `var` as `var `, which it would not recognize:
`var = 1 + var // This adds one to var`

Empty lines contain no useful information, which would have to be turned into instructions. Empty lines must thus either be removed or ignored by the compiler, as there is nothing of value to be extracted from them. The compiler uses the first solution and strips out any empty lines from the dictionary. This approach has the advantage of creating smaller instruction files and leaving out unnecessary empty instructions, which creates added complexity and, thus, more room for errors. Therefore, we now check whether the line contains anything. If it doesn't, we remove the empty line from the dictionary using its key. Note that this is not possible during iteration, as Python does not allow the deletion of keys while iterating through a dictionary. Instead, we will have to store the keys of empty lines and remove them afterward when not iterating through the dictionary. This is the code responsible for this action:
```Python
for index, lineList in lines.items():
	line = lineList[0]
	[...]
	if not line:
		emptyIndexes.append(index)

for index in emptyIndexes:    
	del lines[index]
```


As for function definitions, we will create a new function called `seperateFunctions`, which takes in all lines and the `bracesInfo` dictionary from level 4 as arguments. As a quick reminder: `bracesInfo` contains data on what lines contain braces and what control flow operator they are tied to. We will go over every entry in `bracesInfo` and check whether a set of braces belongs to a function definition. If it does, we can retrieve the lines of the starting and ending braces:
```Python
for info in bracesInfo.values():
	[...]
	if info["ctrlFlowStatement"] != "func":
		continue
	startOp, endOp = int(info["startOp"]), int(info["endOp"])
```

We can then iterate over all lines between them, saving them to a new dictionary just for functions and finally adding it to a `funcs` list, which will store the dictionary of the lines of all function definitions. As a last step, we remove all the lines we just copied from the original `lines` dictionary:
```Python
for op in range(startOp, endOp+1):
	currentFunc[str(op)] = lines[str(op)]
	removeOps.append(str(op))
for op in removeOps:
	del lines[op]
```
Back in `compiler.py`, we create a new function that automatically performs all future levels on both the `lines` and on all lines stored within the `funcs` list. Finally, we may return the "cleaned up" lines dictionary along with the functions back to the `compiler` function. 

  

## Changing operands into functions (Level 7)

When a programmer writes `1 + 2`, in the background, the code is transformed, and a function `add` is called with `1` and `2` as arguments. Therefore, writing `x = 1 + 2` is no different from `x = add(1, 2)`, as the former is simply transformed into the latter. Similarly, `1 == 1` is turned into `isEqual(1, 1)`. Keywords such as `while true` are also turned into function calls, such as `doWhile(true)`. NoBash executes instructions by calling the functions specified in them. Instead of having instructions be a mixture of mathematical operations, control flow constructions, and instruction calls, each requiring a different way of working with them, instructions are uniformly kept as function calls. This level converts the control flow constructions and mathematical operations into function calls.

This level can be seen as one of the most difficult to implement. This is not necessarily because it requires a lot of code but instead, because we have to find an algorithm that works in a lot of very specific edge cases. Additionally, these two levels require a deeper understanding of syntactical analysis. This algorithm will work as follows: first, we need to give it a list of all keywords and operands in order. This is important, for example, due to the order of operations in math. If operators were to be turned into function calls from left to right, `1+2*3` may turn into the following:
`multiply(add(1, 2), 3)`
In this list of keywords and operands, multiplication must, therefore, take precedence over addition. Instead, we must go over the line multiple times. During the first check, all exponent symbols are turned into functions first. During the second sweep, multiplication and division are tackled. Finally, addition and subtraction are dealt with in the third and last iteration. Otherwise, we might add before we multiply, which results in errors. However, there are also other orders which must be kept other than those of the mathematical symbols. For example, we must convert all `==` into functions before we convert `if`s as shown in the following example:
```Python
// Code in question:
if 1 == 1 {

// Correct:
1. if isEqual(1, 1) {
2. __checkIf__(isEqual(1, 1)) {

// Wrong:
1. __checkIf__(1) == 1 {
2. isEqual(__checkIf__(1), 1) {
```
We would compare the `if` to something else, which would become problematic. There are two possible types of transformations an operator can undergo. Which one is used is dependent on the operator in question. The first case is used to perform an operation on values to the left and right of the operator. In this case, the values are turned into arguments and the operator into a comma to separate the two. The function is then inserted before the arguments, and they are wrapped with brackets. This typically occurs when two values are compared or combined together in some way. Possible examples of this are the following, with x and y being the values to the left and right respectively:
```Python
x + y -> add(x, y)
x * y -> mul(x, y)
x == y -> isEqual(x, y)
x and y -> __bothTrue__(x, y)
x in y -> __eachIn__(x, y)
```
In the second case, only the value to the right of the operator is used as an argument. This case, on the other hand, applies when only one value should be worked with, which is the case with control flow operators or operations like `not`. Possible examples of operations resulting in these transformations are as follows:
```Python
if x -> __checkIf__(x)
while x -> __doWhile__(x)
```
There is one notable exception to this rule:
```Python
return 1, 2                   -> __funcReturn__(1, 2)
```
Return works similarly to the two examples given earlier, as the only arguments passed are values to the right of the keyword. However, this time, not only one value is passed, but every value following the keyword. The values are already separated by commas by the programmer, so the keyword must only be turned into a function call with an opening bracket. Additionally, a closing bracket is inserted at the end of the line, as everything following the keyword on the same line must be passed as an argument. As a last preparation step, we must specify what function we should turn every operation into. In the previous examples, we saw that `+` becomes `add` and `if` becomes `__checkIf__`. Overall, the system must take the following things into account:
- Should this word or symbol be transformed?
- Are there any symbols in the line that take precedence over the current one?
- What should the word or symbol be turned into?
- Should values to the left of it also be added as arguments?
- Is this a special case, like return, in which there may be multiple arguments to the right?


We must now iterate over every line, perform the upcoming changes on it, and save it back in the line dictionary. For every line, the algorithm cycles through operators in the order of operations. This means that, for example, exponents will be transformed first, followed by multiplication and division. However, we must design this in such a way that certain mathematical operations (like `+` and `-`) have the same priority. The compiler should not look for addition before subtraction. In these cases, it does not matter which is stored first in our list of operators, but rather which occurs first in the line before the other. Therefore, in cases where two operators have the same priority but the order matters, then both are looked for one after another. If both are found, the first appearances of both operators are considered. The locations of both are then taken into account, with the one that appears first being converted first. This can be visualized well using an example:
`1 + 2 * 4 - 2 + 8`
The first operation to be converted will be the multiplication to comply with the order or operations. The calculation will be performed here to visualize the example better. Instead of calculating the result, NoBash would actually convert the operations into functions, but this would become quite unreadable for this small example fairly fast. We are, therefore, left with the following:
`1 + 8 - 2 + 8`
At this point, we are left with only addition and subtraction. Multiplication and division take priority over addition and subtraction, but within the group, the position is important. We can, therefore, look at the first occurrences of addition and subtraction, respectively. In our case, the first plus symbol is the second character, whereas the minus symbol is the fourth one. There is another plus, though, because this is not the first occurrence of it, this specific addition will be ignored for now. Because the addition of one and eight occurs before the subtraction of eight and two, the addition is done first:
`9 - 2 + 8`
Finally, the minus lies before the final addition, so the calculation is done respectively:
`7 + 8`
This leads to:
`15`
`
The next challenge to overcome will be the bracket placement. Consider the following examples:
```Python
1 + 2             -> add( 1, 2 )
(1 + 2) * 2       -> mul( (add(1, 2)), 2 )
add(1, 2) * 2     -> mul( add(1, 2), 2 )
```
In each case, the compiler must determine where to place the brackets so that all arguments are correctly included. This may be simple when the arguments are simply two stand-alone values but quickly becomes quite complex when one or both arguments are either enclosed in brackets or are function calls. The brackets can no longer simply surround the first value it finds to the left and right of the operation but must also enclose any brackets surrounding it. If this was not the case, something like this might occur:
```Python
(1 + 2) * 3 -> (1 + mul( 2), 3 )
```
In the demonstration above, the multiplication symbol places the opening bracket behind the first value it finds, which is `2`. This should not happen. Instead, the compiler should notice that the `2` is within a set of brackets. It should then go over more values to the right until the bracket is closed. In this case, this would be behind `(1`. This is what the correct placement should look like: 
```Python
(1 + 2) * 3 -> mul( (1 + 2), 3 )
```
Therefore, the systems that detect where to place the brackets to the left and right of the operation must have some added checks in place to ensure that function calls and brackets are included properly.

Because a bracket must be placed both to the right and to the left of the arguments, two different functions must be made for each case. The compiler first inserts spaces around all braces and operators:
`a*(b+c) -> a * ( b + c )`
A new function, `findRightWhiteSpace`, is responsible for finding the closing bracket's correct position. It will look at every character to the right of the operator in order, searching for spaces. The compiler will only add braces after having found a sequence of characters first to ensure that the closing bracket is not placed immediately in between the operator and value:
```js
// Wrong:
a * ) b          // No waiting for value

// Correct:
a * b )          // Waited for value first
```
A new problem occurs when brackets are introduced. The compiler can no longer wait for empty spaces following a character sequence, as the brackets may encapsulate several values, which all must be taken into account. The following examples demonstrate how the bracket must be placed around any preexisting brackets. Note that the underscore denotes where the bracket would be placed in each case, though this is only for illustrative purposes:
```js
// Problem:
a * ( b + c )

// Wrong:
// The compiler would take the opening brace following the
// operator as the value, at which point it places the
// closing brace right after it
a * ( _ b + c )

// Correct:
// The compiler notices the preexisting opening brace and
// waits for it to be closed again:
a * ( b + c ) _
```
As is demonstrated, the compiler can fix the problem by waiting for any already present brackets to be closed.

This entire process must be mirrored for the opening bracket, which will be done in the function `findLeftWhiteSpace`. However, there will be some small tweaks. For starters, the function name is placed before the opening brace, making the function call. It would create `add(1, 2)` instead of merely `(1, 2)`. Additionally, as previously described, in cases such as `elif`, we do not want to include any values which may be present before the operator. In such cases, the function simply replaces the operator with the correct function name and opening brace immediately: 
``` js
// Problem:
} elif true {

// Wrong:
// The compiler tries to include a fictitious value
// to the left of the operator
__checkIfElse__( } , true ) {

// Correct:
// The compiler notices the exception and simply replaces
// the elif with a function name and opening brace:
} __checkIfElse__( true ) {
```


We can implement this by first looping over every line in the lines dictionary. We then insert spaces around every operator. 
```Python
for i, line in lines.items():
    line = " " +line[0] + " "
```
Now, we go over every set of operators in the list from left to right. Specifically, they are sets of operators, because, as previously described, the "`+`" operation should not take precedence over the "`-`" one just because it is saved earlier in the list. We must save these special operators that are of equal significance in a list together. Even operators that are not special (like the `=` sign) must be saved in a list like so:
```Python
oop = ["*/", "+-", ":", ["=="], ["!="], "=", [...], ["for"], ["return"]]
```
We can then iterate over the current operators list and compare their indexes in the list. Whichever operator is first in the list is turned into a function call first in order to preserve the order of operations:
```Python
def getFirstOp(line, ops):
    lowestIndex = -1
    lowestOp = ""
    # We go over both operators
    for op in ops:
        if " "+op+" " in line:
	        # We get the first index of the operator
            index = line.index(" "+op+" ")+1
            if lowestIndex < 0 or index < lowestIndex:
	            # if the index is lower than
		        # the previous index, save it
                lowestIndex = index
                lowestOp = op
    # If either or both operators appear,
    # we return the one that has a 
    # lower index
    return lowestIndex, lowestOp


def doMain(line):
    line = insertSpaces(line)
    # Here, we go over every set of operators
    for ops in oop:
	    # firstOpIndex is the location of the first operator
	    # firstOp is the operator which appears first
        firstOpIndex, firstOp = getFirstOp(line, ops)
```

For example, let's imagine our operators lists would look like this: `[["*", "/"], ["+", "-"]]` 
and our example line is the following:
`2 * 3 - 1 + 4`.
We first cycle through the outermost list from left to right, therefore looking at `["*", "/"]` first. This cycling ensures that multiplication and division are considered before addition and subtraction, complying with the order of operations. In the line, we are now looking for the characters `*` and `/`. The line does include an asterisk but no division, and therefore, we must convert only the multiplication. Note that, once again, the mathematical operation will be calculated in this example for illustrative purposes. In NoBash, the operation would simply be converted into a function call. The line now looks like this:
`6 - 1 + 4`
Because both multiplication and division were now taken care of, we moved on to the next set of operators, `["+", "-"]`. However, at this point, because the line includes both multiplication and division, we should no longer consider the order in which the operations occur in the list. Instead, just like in traditional mathematics, whichever occurs first in the line from left to right is converted first. NoBash goes through every character and set of characters in the line one by one and checks whether it is contained in the current set of operators. The first and second characters are `6` and ` `, respectively, neither of which are contained in the set of operators. The next character, however, is `-`, and therefore is a part of the current operators set. Even though in terms of positioning, `-` is behind `+` in the list `["+", "-"]`, this is ignored, and the `-` is converted immediately. The line, therefore, now looks like this:
`5 + 4`
Now, the other characters are looked at once again, from left to right. The next and last character to be a part of the operators set will be the `+`, finishing the operation:
`9`

We repeat this process for every set of operators until none of the contained elements appear in the list, in which case we continue on to the next set. If we find the first operator, we get its index in the line and store it. First, we remove it from the line and replace it with a comma. We only replace it with a comma in some instances, though, as keywords like `not` do not need to be replaced. We would not want `not false` to turn into `__makeNot__(,false)`:
```Python
def removeOp(i, line, op):
	# We replace the operator with a comma only
	# if it is required
    replacer = "," if op not in noLeftOps else ""
    # This means: 
    # everything up to the operator +
    # the comma +
    # everything after the operator
    return line[:i] + replacer + line[i+len(op):]
```
The comma will separate the arguments in the future (e.g: `a + b -> add(a , b)`). We then run the `findRightWhiteSpace` function. This function iterates over all characters in the line after our current operator. In it, a variable `hitChar` is set to `False`. The algorithm it uses checks for the next empty space after the one separating the operator from the right parameter. 

As previously described, the `findRightWhiteSpace` function needs some special logic when preexisting brackets are involved. The problem is that the compiler can no longer insert an opening bracket at the first space it finds but must instead place it outside any bracket construction, as shown in the previously made example:
```js
// Problem:
a * ( b + c )

// Wrong:
// The compiler would see the opening brace following the
// operator as the value, at which point it places the
// closing brace right after it
a * ( _ b + c )

// Correct:
// The compiler notices the preexisting opening brace and
// waits for it to be closed again:
a * ( b + c ) _
```

We can do this by using a (to us) familiar technique: we create a new counter. Every time we find an opening bracket to the right, we increment the counter by one. If we find a closing bracket, we decrease it. Upon hitting a character that is not a whitespace, we can set `hitChar` to `true`. Only when the counter is at zero, we have found a whitespace, and `hitChar` is true may we place our closing bracket at that location:
```Python
def findRightWhiteSpace(i, line, skipAmount=0):
	hitChar = False
    skippedAmount = 0
    bracketCounter = 0
    fullLine = line
    line = line[i:] # The line is everything
	# to the right of the operator
    for newI, char in enumerate(line):
	    # Check if the character is not a whitespace and set hitChar accordingly
        if char in string.ascii_letters + string.digits + "_":
            hitChar = True
        elif char in "()":
            if char == "(":
                bracketCounter += 1
            elif char == ")":
                bracketCounter -= 1
        elif char == " ":
            [...]
            if bracketCounter == 0 and hitChar:
                # A closing bracket is inserted
                new = insert(fullLine, i+newI, " ) ")
                return new
```
Here is an example demonstrating this in action. Underneath each character, the bracket counter is displayed, and an asterisk represents the location where the bracket is finally placed:
```js
// Problem:
a + ( b * c + ( d - e ) ) _
0 0 1 1 1 1 1 2 2 2 2 1 0 *
    +         +       - -

// * -> This is the first space where the bracket counter
// is 0. This demonstrates that a bracket can be placed 
// here.
```

This entire same algorithm also applies to `findLeftWhiteSpace`, which effectively does the same. However, there are some small differences. For example, we now look from right to left, starting at the operator, as we want to place the opening bracket. Additionally, we not only insert the opening bracket but also the correct function name for the operation. We can find it by creating a new dictionary, in which each operation has the function it should turn into specified:
```Python
opFuncs = {">": "__greater__", "<": "__lesser__", "<=": "__lesserOrEqual__", ">=": "__greaterOrEqual__", [...], "or": "__bothOr__"}
```
We can use this dictionary and insert the correct function's name and an opening bracket at the first whitespace outside of any brackets. 

In the case of the control flow keywords like `if` or keywords like `not`, we do not need to use this algorithm. Instead, we simply insert the function name and the opening bracket at the same location where the keyword was before to create something like `__doIf__(true)` or `__makeNot__(true)` (in the case of `not true`). There is a list of operands which require this special modus operandi. When `findLeftWhiteSpace` is called, it checks whether or not the operator is stored in this list:
```Python
noLeftOps = ["if", "elif", "for", "return", "else", "while", "for", "not"]

def findLeftWhiteSpace(i, line, funcToBeInserted, op):
    [...]
    fullLine = line
    [...]
    if op in noLeftOps:
	    # Inserts the function where the operator is
        return insert(fullLine, i, " "+funcToBeInserted+"( ")

```
If this is the case, then the operator is simply replaced with its corresponding function name and a subsequent opening bracket:
```js
// Problem:
false == not true

// Wrong:
false __makeNot__(==, true)
// We do not want the function call to include any
// tokens before the operator in this case

// Correct:
false == __makeNot__(true)
// "not" was simply replaced by "__makeNot__(", 
// making the only argument the following value
```

Because our system relies on empty space, we will also create a function that inserts spaces around all operations. Here is an example of how differently the algorithm would work without this step: `a*b+c_` instead of `a * b_ + c`. Here, we can clearly see that without the required whitespace everywhere, the algorithm would only find empty spaces at the beginning and end of the line, breaking the system. This can be accomplished by going over every operator and simply replacing it with a version of itself that has a space before and after it:
```js
"+"
// We replace '+' with ' + '
" + "
```
This creates a new problem. When `=` is replaced with ` = `, this will also cause `==` to become ` =  = `. Python will not treat two equal signs as one but will add spaces around both of them instead. This also to other keywords and operators:
- `!=` becomes `! = `
- `+=` becomes ` +  = `
- `-=` becomes ` -  = `
- `/=` becomes ` /  = `
- `*=` becomes ` *  = `
NoBash solves this problem using the `removeSpaces` function. The compiler assumes that, when it finds two equals signs separated by two spaces, the user initially wrote `==`. It then deletes the two spaces and, therefore, puts the operator back together:
```Python
def removeSpaces(line):
    toBeRejoined = ["=  =", "! =", "el if", "+  =", "-  =", "/  =", "*  ="]
    for item in toBeRejoined:
        line = line.replace(item, item.replace(" ", ""))
    return line
```


`for` loops are also a special case, as we must first replace the `in` keyword with a comma (to separate the iterator variable from the list). As an example, `for fruit in fruits` must become `__doFor__(fruit, fruits)` rather than `__doFor(fruit in fruits)` as the latter is not a proper function call. Then, we must place the closing bracket around two arguments rather than one (namely, the ones referenced before). We can solve this by creating a `skipAmount` variable and setting it equal to one if the current operator is a `for` keyword. We then skip over as many correct positions for a closing bracket as high as `skipAmount` is:
```Python
def findRightWhiteSpace(i, line, skipAmount=0):
    [...]
    for newI, char in enumerate(line):
        [...]
        elif char == " ":
            if skippedAmount != skipAmount and hitChar:
                skippedAmount += 1
                hitChar = False
                continue
            if bracketCounter == 0 and hitChar:
                [...]
```
That way, we will skip over the first argument and place the bracket after the second one instead. Here is an example in which `skipAmount` is set to both zero and one:
```js
// skipAmount == 0
__doFor__(fruit,) fruits

// skipAmount == 1
__doFor__(fruit, fruits)
```
As can be seen here, even though fruit would usually be a valid value after which the closing bracket would normally be placed, `skipAmount` dictates that we must wait for a second proper value until actually inserting the bracket.

Additionally, we also need to implement special exceptions for `if`, `elif`, `else`, `for`, `while`, and `return` statements. For example, when a condition in an `if` clause is not met, we jump past all instructions contained in said `if` construction. NoBash knows where to jump to as the instruction number of the closing bracket is passed as the second argument to the `__checkIf__` function, with the first argument being the actual condition. Currently, this still looks something like this:
```js
__checkIf__(ret0, {0)
```
For now, the second argument will simply be the opening bracket following the `if` clause along with its unique ID. In level 11, we will replace the opening bracket with a reference to the instruction that the closing bracket is in. To add the brace as a second argument, you first have to insert a comma in front of the opening curly brace to separate the two arguments. This can easily be done by replacing all occurrences of the string "`{`" with "`, {`", creating the wanted separator:
```Python
if firstOp in ["if", "elif", "else", "while", "for", "return"]:
				line += ")"
                if firstOp != "else":
                    if ",{" not in line:
                        line = line.replace("{", ",{")
```

As a final step, instead of calling `findRightWhiteSpace`, we would only have to append a closing bracket at the end of the line, as we want to include everything after the `if` statement as a parameter. This example demonstrates the desired effect:
```js
// Problem:
if true {1
// {1 means that the bracket has an ID of one

// 1. step: Determine whether the operator is an if,
// elif, else, for, while, or return statement:
"if true {1" contains "true" == true

// 2. step: place opening bracket and replace operator
__checkIf__(true {1

// 3. step: add a comma before the bracket
__checkIf__(true, {1

// 4. step: add a closing bracket at the end of the line
__checkIf__(true, {1  )

```

The `return` keyword is very similar in this regard, as we want everything to the right of it to be used as arguments. However, because the programmer already separated all the values according to the NoBash syntax, we will not have to insert any commas ourselves:
```js
// Problem:
return a, b

// Correct:
__funcReturn__(a, b)
// Note that this worked just like in the "if" example,
// but this time, no commas had to be placed
```



## Making a closing brace return system (Level 8)

During a `while` loop, all code between the opening and closing brace is meant to run for as long as the supplied condition is true. In terms of instructions, every instruction contained in the loop is run one at a time until finally reaching the last instruction before the closing brace. At this point, the interpreter must jump back to the beginning of the loop and check whether or not the specified condition is met. This can be done by a function call at the end, which is unique to each control flow construction. For instance, at the end of an `if` block, the function serves as a point to jump to if the condition is not met and the contained code should be skipped. At the end of a function, the interpreter is told to return, and in the case of a `for` and `while` loop, it jumps back to the beginning of the loop. This function must be at the end of the construction, which is denoted by the closing bracket. 

We can, therefore, simply replace the closing bracket with this function call and pass the ID of the bracket as a parameter. In future levels, a system will find the instruction number that contains the opening bracket with the same ID. Depending on the type of the construction, such as `for` or `while`  loops, the function may use this data to jump back to its start.
As an example, this code snippet will loop ten times. For clarity, the `for` has not been turned into a function call, and the line numbers will also be supplied to the left:
```js
1. for i in range(10) {1
2. }1
```
This level aims to replace the closing brace on line 2 with a function call. This call will then have the brace ID one as a parameter, which, in turn, will, in later levels, refer to the correct instruction number. For simplicity, in this example, it will point towards the line number.
```js
1. for i in range(10) {1
2. __jumpBackFor__(1)
```
One can imagine `jumpBackToFor` to simply jump to the instruction number passed as an argument. Note that for now, though this is changed in later levels, the parameter is neither the instruction number nor the line number, but the bracket along with its ID. This system is called the „bracket return system“, as the interpreter „returns“ back to the start of a loop using brackets to find the location to go to.


As a first step, we must figure out both in which lines we must replace closing braces and with what function call. The former bit of information is outright stored in the `bracesInfo` dictionary we created in level 5, along with the data we need to figure out the latter question. So, we will first look at the `bracesInfo` dictionary and get info on all closing curly braces, like the lines they appear on and what control flow statement each one is tied to. Now that we know what line they are on, we can jump to them. "*cbrf*" is a term coined by NoBash and stands for the "closing brace return function". In other words, it is the function unique to each control flow operator we want to replace the closing bracket with. For example, the *cbrf* for a `for` is `__jumpBackFor__()`. Using a dictionary containing the relevant *cbrf* for each control flow statement, we can figure out what function we must put at the end of each control flow construction. This is possible because the `bracesInfo` dictionary tells us what control flow construction is terminated by a closing brace on a specific line. We will also pass the closing bracket along with its unique ID as an argument to the *cbrf*, which the function will be able to use in a later level to determine which instruction number it has to jump back to.

We first iterate over every value in the `bracesInfo` dictionary. Each of these values will, once again, be a further dictionary. The key bits of information each one contains will be "`endOp`" and "`ctrlFlowStatement`". 
```Python
for id, info in bracesInfo.items():
        endOp, ctrlFlowStatement = info["endOp"], info["ctrlFlowStatement"]
```
The former will tell us what line the closing bracket is on, whereas the latter reveals what control flow statement initiated the curly braces. Here is a potential example of what this may look like, with line numbers being displayed on the left:
```js
1. if true {0
2.      put("This was true!")
3. }0

// BracesInfo dictionary:
{
	"0": {      // This entry pertains to bracket ID 0 
		"ctrlFlowStatement": "if",
		"endOp": 3        // The if block ends on line 3
	}
}
```

In order to apply this modification to all brackets in a script, we must go over every entry in the `bracesInfo` dictionary:
```Python
# id will contain the brackets ID and info will
# contain what line the closing bracket is on
# and what control flow statement it is connected to
for id, info in bracesInfo.items():
```
In this `for` loop, we can find the line the bracket is located on under the `endOp` key in the entry. We can then take the line number as given to us by `endOp` to jump to the line containing the closing brace like so:
```Python
endOp = info["endOp"]
ctrlFlowStatement = info["ctrlFlowStatement"]
# We check whether or not the line actually exists
if str(endOp) in lines.keys():
	# This is the line containing the closing brace
	lines[str(endOp)][0]
```
We already have the ID of the bracket saved in a variable, so we can remove the bracket from the end of the line. We will reinsert it in the correct position later. Here is the code responsible for removing the brace:
```Python
lines[str(endOp)][0] = lines[str(endOp)][0].replace("}"+str(id), "")
```
This may look very confusing at first, so let us clean this up a bit:
```Python
# First, we get the line number that contains the brace
lineIndex = str(endOp)

# Using this line number as a key, we can get the
# line out of the lines dictionary. Remember that
# we stored the line inside of a list before putting
# it inside of the lines dictionary.
# currentLineList currently stores something like:
# ["}0"]
currentLineList = lines[lineIndex]

# We access the first item of currentLineList, 
# which is the string containing the line
currentLine = currentLineList[0]

# braceWithID should contain the closing brace along
# with its ID appended to it. It is identical to
# the brace stored in the line: "}0"
braceWithID = "}"+str(id)

# We replace the brace with its ID with nothing
# in the line. By replacing it with nothing, we
# effectively removed it
currentLine = currentLine.replace(braceWithID, "")

# Lastly, we save this modified line back in the 
# lines dictionary
lines[str(endOp)][0] = currentLine
```
At this point, we have the line without the brace. If the line is empty without it, we can delete it, as we will replace it entirely in the next step. If the line contains an `elif` or `else` statement, it will not be empty as `}0 else {1` will become ` else {1`. In this case, we need to keep the line so as not to delete the `elif` or `else`. An `if` check can determine whether the line is empty or not, and we can delete it accordingly:
```Python
if not lines[str(endOp)][0].strip():
	del lines[str(endOp)][0]
```
Because the `lines` dictionary stores each line within a list rather than as a string, we can append the *cbrf* to the end of the list. This may sound confusing at first, as we are effectively storing two "lines" under one line number as demonstrated in the following example:
```Python
# Here is an example program with line numbers to the left:
1. if 1 == 1 {
2. } else {
3. }

# This is what lines would look like:
lines = {
	"1": [
		"if 1 == 1 {0"
	],
	"2": [
		"else {1",# Line number two contains this else...
		"__cbrfIf__(}0)" # ... and this cbrf!
	],
	"3": [
		"__cbrfElse__(}1)"
	]
}
```
While this may not make immediate sense, it comes in very handy. Even though it is not explicitly written by the programmer, line two actually plays two important roles rather than only one:
- The *cbrf* acts as a safe instruction the interpreter can jump to when the `if` condition is not met
- It also contains an `else`, which is important to the programs logic
We have, therefore, merely separated this one line into two. However, we must still store them under the same line number, as that is where they both originated from. It is important that we do this since an instruction can only hold one function call at a time. Without splitting up the one line into two, it would look something like this:
```Python
# Note that the else has been replaced with its function in level 7.
# This fact has been left out up until now to make
# the examples more clear
__cbrfIf__(}0) __doElse__({1)
```
The code above does not work and would crash the compiler. This is why it is imperative that we split up the two function calls onto separate lines, even if we do so using the same line number. Let us now create the code to append the *cbrf* to the line's list. 

In order to do so, we must first create a way to determine which *cbrf* should be inserted. A `for` loop must be closed using a *cbrf* specifically designed to jump back to the beginning of the loop. The *cbrf* at the end of an `if` condition acts completely differently. Therefore, every control flow statement must have its own *cbrf*. We have already saved what control flow statement was ended by the brace in the `ctrlFlowStatement` variable. A simple solution would, therefore, be creating a dictionary. The control flow statement acts as a key, and the value is the corresponding *cbrf*:
```Python
closingBracketReturnFunctions = {"for":"__jumpBackFor__(}", "if": "__cbrfIf__(}", [...], "while": "__jumpBackWhile__(}"}
```
Using this dictionary, we can retrieve the *cbrf* to add to the current line using the following code:
```Python
closingBracketReturnFunctions[ctrlFlowStatement]
```
It should be pointed out that the dictionary does not contain the full function call for the *cbrf*. Instead, it has an opening bracket and brace after the function name. Crucially, it is still missing the brace's ID and the closing bracket to finish the function call. This can be added like so:
```Python
# id contains the ID of the brace
closingBracketReturnFunctions[ctrlFlowStatement]+str(id)+")"
```
We can then append this to the list responsible for containing the line at the current line number:
```Python
lines[str(endOp)].append( closingBracketReturnFunctions[ctrlFlowStatement]+str(id)+")")
```
If the line consisted only of the closing brace, because we deleted the line earlier, the closing brace has been replaced with a *cbrf*. If, instead, the line of code also included an `else` or `elif`, the list containing the code has been expanded to also hold the *cbrf*. There is one exception to this: functions. Functions do not need to know where they started, so passing the brackets ID to it is redundant. The dictionary containing *cbrf*s, therefore, makes an exception for functions. The *cbrf* for the function is stored as a complete call (`_funcReturn__()`) rather than a partial one with a brace (`__jumpBackFor__({`). We, therefore, also do not have to add the brackets ID and a closing bracket to the end of the *cbrf*:
```Python
# If the control flow statement is not a function:
# get the cbrf and add the ID and closing bracket
if ctrlFlowStatement != "func":
	lines[str(endOp)].append( closingBracketReturnFunctions[ctrlFlowStatement]+str(id)+")")
# If it is a function:
# Don't add this info to the end
else:
	lines[str(endOp)].append( closingBracketReturnFunctions[ctrlFlowStatement])
```

## Parsing function definitions (Level 9)
Function definitions need to be processed in the same way as all other lines. In the following example, a function by the name of `sayHello` is defined with one parameter called `name`. As the name of the function suggests, the function greets a person using their name. Here is the definition of the function without its body: 
`func sayHello(name) {`
In this level, the function name and parameters are both extracted and saved. 

Imagine you just moved into a new house. When you enter the living room, you see three different light switches. Each one has a small piece of paper stuck to it explaining which lamp each switch controls. This is very useful as you can immediately identify which switch you must flick to toggle a certain lamp on or off. After having lived in the house for a while, the paper is no longer useful as you have already memorized what each switch is connected to. 

This example is comparable to a function definition:
```go
func lightSwitchLivingRoom() {
	light("living room")
}
```
The function definition `func lightSwitchLivingRoom() {` is important in the code initially. However, because NoBash works using instructions, this definition must either be turned into an instruction or left out entirely. NoBash uses the latter option. In level 6, we stored functions in a separate location from the main script. The function definition in of itself, therefore, has become redundant: it is already known to the compiler that the function code is not a part of the main script. Because the function name and parameters are also extracted and stored in a dictionary during this level, there is no more use for the function definition, and it can safely be removed. In the final level, the information will be written out in such a way that the interpreter can immediately find it and gather all the data quickly. 

The alternative to this approach would be turning the function definition into an instruction. This would result in unnecessary additional instructions. It would also be harder to work with for the interpreter. By separating the function information from the instructions, the interpreter can find all the relevant information much faster. Otherwise, it would have to:
- go through each instruction,
- determine whether or not it is a function definition,
- extract information such as the name and parameters,
- and finally save its instruction number to be able to jump to it later


The first line of each function will always be a function definition. The syntax for creating a function is always the same: `func funcName(param1, param2, [...], paramN) {`. The function name will always be between the `func` keyword and the opening bracket. The only other bit of information we want will be the parameters, which will be in between the opening and closing brackets, separated by commas. We can gather all of this information and save it properly. We can tell where to find what information because we know where everything is located relative to each other, as described above. Finally, we have to remove the function definition line. Nearly everything in NoBash is a function call, with only some exceptions, such as function definitions. These will be stored in their own section. Keeping the function definitions would result in them being written down as erroneous instructions, which we have to avoid.
  

By iterating over every function within the `funcs` list and retrieving the first line of each, we will already have every function definition of the script. 
```Python
for index, func in enumerate(funcs):
        for lineNumber, line in func.items():
            line = line[0]
```
We can define a function `getFunctionName`, which will attempt to extract the name of the defined function by simply reading everything after the fourth character until we hit an opening bracket. The `func` keyword, which "initiates" the function name definition, will always be four characters long. Here is an example of this:
```go
// Here is a function definition:
func functionName() {

// We now take away the first four characters
// of the definition:
 functionName() {
// The "func" is now gone

// We now go over each character until we hit
// an opening bracket:
 functionName

// Lastly, we remove any trailing or leading 
// spaces:
functionName
```
and here is the code that does it:
```Python
name = ""
for char in line[5:]:
        if char in string.ascii_letters + " ":
            name += char
        elif char == "(":
            break
        [...]
return name.strip()
```

We should then run a check on whether the line has exactly one opening and closing brace, raising an error if this is not the case. Why this must be is best demonstrated by showing a function definition:
```go
func hello(x, y) {

// As can be seen here, the only opening and closing 
// brackets in a function definition should be used
// to encapsulate parameters 
```
Here is the code responsible for making this check:
```Python
# If this condition is met...
if line.count(")") == line.count("(") == 1:
    return # Return out of the check function
# If we did not return, the condition was not met
# and we should raise an error
error(15, [lineNumber])
```

Once the syntax check is passed, we can attempt to read out all arguments. Using the function `getParameters`, we can do this by reading the string between the two brackets and calling the `split` method on it, passing a comma as a parameter. As a refresher: `split` takes in a string and a "delimiter". It will return a list that contains everything to the left and right of each delimiter as an item. Here is an example of this:
```Python
numbers = "1,2,3".split(",")
print(numbers)
# This will print:
# ["1", "2", "3"]

arguments = "param1, param2, param3".split(",")
print(arguments)
# This will print:
# ["param1", " param2", " param3"]
# We will have to remove all spaces between
# the commas and parameters ourselves
```

This will give us a list with all parameters as new elements:
```Python
line = line[line.index("(")+1:line.index(")")]
return [param.strip() for param in line.split(",")]
```

Finally, we can save this new data by creating two dictionaries. One dictionary will replace the `funcs` list. The only difference between the two is that the function's name is used as a key in the dictionary rather than an arbitrary index with the list. This lets the compiler easily connect a function name with the instructions it contains. The second dictionary will also use the function's names as keys but will save the respective parameter list for each function instead. This dictionary is important as it both stores the parameters each function accepts and ties these together with the name of the function they belong to. The compiler can, therefore, easily get the list of parameters for every defined function when this information is written to the instructions file in the final level. Finally, we may return these two new dictionaries. Here is an example of a script containing one function definition along with the two dictionaries it may produce:
```go
func hello(name) {
	put(name)
}
```

```Python
# This dictionary stores function instructions
# with the function name as the key. 
{'hello': {'1': ['put(name)']}

# This dictionary stores the parameters of functions
{'hello': ['name']}
```


## Split up nested function calls and make "return value variables" (Level 10)
Instructions contain one function call each. However, for convenience, programmers typically use multiple functions in one line. Additionally, things like setting variables were turned into function calls. For example, in this line, a programmer adds together two numbers and outputs the sum: `put(add(1, 2))`. In another case, we might see the sum being stored in a variable `x`, like so: `x = 1 + 2`. However, as mathematical operations were previously turned into function calls, this line would now look as follows: `__setVar__(x, add(1, 2))`. A call to a function passed as an argument is called "*nested function call*".

The compiler needs to turn lines into instructions. Therefore, a line that contains more than one function call poses an issue, as an instruction may only ever contain one function call. The compiler must, therefore, split up such lines and turn each function call into its own instruction. The latter example, once split up so that each function call is on a separate line, would look something like this: 
```Python
1. add(1, 2)
2. __setVar__(x, )
```
When functions are used as arguments for other functions, the value which it returns is used in its place. When the function is extracted, the value it returns is no longer supplied to the second function. This can be seen in the second line of the above example since a second argument is missing. In line two, there is now a gap where the returned value of the first function would have been. Therefore, there must be some sort of placeholder that tells the compiler to use the returned value from the previous function. NoBash uses the „ret“ system to accomplish this. When the first instruction is run, it will return `3`. This value will then be stored and can later be accessed using the instruction number where it was returned from. For example, `3` would be saved as the value returned by instruction 1. Additionally, the instruction number 2 would look like this: `setVar(x, ret1)`. In this context, `ret1` is a reference to the returned value of the first instruction. These "references" are called "return value variables" in NoBash, or *RVV* for short. Similarly, `ret2` does the same for the second instruction, and so on. When the interpreter finds such a `ret` value, it will replace it with the value returned by the instruction at the specified index. The example, therefore, would look like this:
```Python
1. add(1, 2)
2. setVar(x, ret1)
```
It is important to note that this also works for several functions passed as parameters. A simpler, albeit flawed, solution would be inserting the returned value of the instruction above into any gaps. This approach would not work when there are two or more arguments passed, with both being function calls, such as here: `sub(add(1, 2), mul(1, 1))`. Using the `ret` system, this line can easily be turned into instructions as follows:
```Python
1. add(1, 2)
2. mul(1, 1)
3. sub(ret1, ret2)
```


This level will be the hardest to implement overall. We will have to create an algorithm that recursively finds all function calls passed as an argument. Here is an example of this:
```Python
# The original line:
lines = {
	"1": [
		"add(sub(1, 2), 3)"
	]
}

# A function call, which is also an argument, is found:
# sub(1, 2)
```
Once one has been found, we must append it to the end of the list, which contains the line it is in like so:
```Python
# The argument is appended as a new line:
lines = {
	"1": [
		"add( , 3)",
		"sub(1, 2)"
	]
}

```
We can then replace it with its RVV:
```Python
# The RVV is inserted into the gap
# The "instruction numbers" are noted to the right
# At the end, the list will be reversed so that 
# instruction one comes before two
lines = {
	"1": [
		"add(ret1, 3)",  # instruction 2
		"sub(1, 2)"   # instruction 1
	]
}
```
We must then repeat this recursively, for there may be more function calls in the arguments of the function we have just extracted. When something happens "recursively", the same action which produced the first result is applied to this same product. In this case, this would mean extracting any nested function calls from a function call that was just extracted:
```Python
# This is the line initially
add(sub(mul(2, 3), 4), 7) 

# We now extract the function call within add:
sub(mul(2, 3), 4)

# The above line is the result of one extraction.
# It still contains another function call, so
# this must be extracted as well:
mul(2, 3)

# We have now recursively extracted function calls,
# as we took the result of one extraction and
# extracted another call out of it.
```
Additionally, we can't know the instruction number of a function while it is being extracted, as it may contain more function calls as arguments, which would push it down further in the instructions list, thereby also changing its instruction number. We must therefore create a "placeholder RVV". Once we are done extracting all nested function calls in one line, we must then go back over all "placeholder RVVs" in it and replace them with the true number of the instruction they are pointing at. We must then repeat this process for all lines until we have finally extracted all nested function calls. For example, consider the following script containing two lines and watch the RVVs be determined:
```go
// Stage 0: Script
["put(\"hello\")"] 
["put(add(1, 2))"]  

// Stage 1: Placeholder RVVs
["put(\"hello\")"]   // this is instruction 0
["add(1, 2)", "put(ret0)"] // and this 1 and 2 respectively
// Even though add is not the first instruction, the compiler
// still uses ret0 (0 as the computer starts counting from zero)
// Instead, it uses ret0 because it is the first instruction
// of the line rather than the entire script

// Stage 2: Proper RVVs
["put(\"hello\")"] 
["add(1, 2)", "put(ret1)"]
// The compiler went back through all instructions, this time
// counting instruction numbers across the whole script
// rather than just the current line. It then replaces the 
// temporary ret value, which is line specific, with a
// value which takes all previous lines into account, giving
// us the "proper" ret index.
```



First, we must create a function `runSplit` which will repeat the entire process for both every line in the main script and all the ones contained in functions:
```Python
def splitFuncCalls(lines, funcs):
    [...]
    # Split up all lines in the main script
    lines, [...] = runSplit(lines, [...])
    # For every function...
    for functionName, functionLines in funcs.items():
        [...]
        # ... split up said function
        funcs[functionName], [...] = runSplit(functionLines, [...])
    # And return the lines and functions as instructions
    return lines, funcs, [...]
```

As can be seen in the above code snippet, the lines in both all functions and the main script are passed to a `runSplit` function. It is responsible for going through every line given to it and calling `splitFunctionCalls` and `insertProperRetVals` on them. The former function takes a full line of code in as an argument and splits it up into instructions. These will then be returned in a list. These instructions still include the "placeholder" RVVs rather than the proper ones. `insertProperRetVals` therefore comes into play now, changing all of the temporary RVVs into proper RVVs.
```Python
def runSplit(lineDict, retCounter):
    newDict = {}
    for index, lineList in lineDict.items():
        lineList = splitFunctionCalls(lineList)
        newDict[index], retCounter = insertProperRetVals(lineList, retCounter)
    return newDict, retCounter
```

Let us look at `splitFunctionCalls` more closely. Let us first focus on it's start as it is quite a long function:
```Python
def splitFunctionCalls(lineList, firstCall=True):
    [...]
    for lineIndex, line in enumerate(lineList):
        checkBracketValidity(line, newLineList)
        firstBracketLine, secondBracketLine = getOutermostBrackets(line)
    [...]
```
`splitFunctionCalls` iterates over every "instruction" in the current line, though there will typically only be one instruction initially. In every instruction, it will first make sure that all brackets are properly placed. This will stop erroneous bracket placement like: `put)"hello"(` or `put("hello"`. These checks are done by the `checkBracketValidity` function. Its algorithm has been used previously in NoBash, as the function relies on counting the brackets. If there is ever a closing bracket more than there are opening ones, an error will be raised. If, on the other hand, an opening brace was not closed, it will also inform the programmer of this and exit:
```Python
# lineIndex is the line number
def checkBracketValidity(line, lineIndex):
    bracketCounter = 0
	# Go over every character in the line
    for index, char in enumerate(line):
        if char == "(":
	        # Add one if it is an opening bracket
            bracketCounter += 1
        elif char == ")":
	        # Subtract one if it is a closing bracket
            bracketCounter -= 1
            # If the counter is negative, then
	        # there is one closing bracket too much
            if bracketCounter < 0:
                error(12, lineIndex)
    # If the opening and closing brackets don't
    # cancel each other out, there are too many
    # opening brackets
    if bracketCounter != 0:
        error(13, [lineIndex])
```

If these checks are passed and the compiler is still running, `splitFunctionCalls` will then need the outermost set of brackets. It will get the location of these by calling `getOutermostBrackets`:
```Python
def getOutermostBrackets(line):
    if "(" not in line or ")" not in line:
        return -1, -1
    brCounter = 0
    for closeIndex, char in enumerate(line):
        if char == "(":
            brCounter += 1
        elif char == ")":
            brCounter -= 1
            if brCounter == 0:
                break
    return line.index("("), closeIndex
```
`getOutermostBrackets` must only implement logic to find the **closing** bracket that belongs to the first opening one. The index of the first opening bracket can be found by calling the `index` method built into Python on the line, which will return the index of the first opening brace: `line.index("(")`. 

As for the closing braces index, we must first create a counter. We then go over every character in the line. If we find an opening bracket, we increase the counter by one and decrease it upon finding a closing bracket. When we find a closing bracket that takes the counter down to zero, we know that this bracket closes the first opening one. In order for the counter to reach zero, there must have been an even amount of opening and closing braces to balance each other out. Here is an example of this in action:
```go
// Here is a potential line of code
put( add( 1, 1) )
// 1    2     1 0
// Under each bracket, you will see the counter
// The last bracket is connected to the opening 
// bracket here

// Here is another example of two nested function calls:
put(add(1, 1), sub(2, 1))
// If we want to find the opening braces inside of
// put's arguments, the algorithm also works:
[...] add(1, 1), sub(2, 1) [...]
//       1    0     1    0
// The first set of brackets is therefore that
// of the add function, as its closing bracket
// reached zero before that of the sub function
```
Here is the code responsible for this logic:
```Python
def getOutermostBrackets(line):
	# If there are no brackets, there is nothing
	# to index
    if "(" not in line or ")" not in line:
        return -1, -1
    brCounter = 0
    # Go through each character in the line
    for closeIndex, char in enumerate(line):
        if char == "(":
	        # If it is an opening bracket, add one
            brCounter += 1
        elif char == ")":
	        # Subtract one if it is a closing bracket
            brCounter -= 1
            # If the opening and closing brackets
            # cancel each other out, the current
            # location is the closing index
            if brCounter == 0:
                break
    return line.index("("), closeIndex
```
If we were to simply find the first closing bracket instead, the following would mistakenly be seen as a pair of brackets:
```go
put( add( 1, 1 ) )
   ^___________^
// The carrot symbols point at the "pair" of brackets
// and their contents are underlined
```

Once the brackets have been found, NoBash will attempt to detect the name of the function being called using the `detectFunctioncall` function. The function name will always be a list of characters immediately in front of the opening bracket (`add(`). The algorithm NoBash uses works as follows. Let us use the code line `"1 + add(2, 3)"` as an example throughout: 
1) First, everything past and including the opening brace is removed from the line
2) The line is then reversed. This causes the flipped function name to be at the end of the line
3) Go through every character in the line
4) If the current character is a letter or an underscore, this must be a part of the function name. For every letter found, increase a counter by one. This counter indicates how long the function name is
5) If the current character is not a letter or an underscore (like a space), we are past the function name and can stop going through all characters
6) We can get the index of where the function name starts by subtracting the length of the name from the index of the opening bracket. If the bracket is at index seven and the name immediately behind it is three characters long, we can calculate that it must start at index 4.
```Python
def detectFunctionCall(line, index):
    fullLine = line
    line = line[:index] # Step 1
    # 1 + add(2, 3) -> 1 + add
    line = line[::-1] # Step 2
    # dda + 1
    foundFunctionChars = False
    lastFunctionChars = 0
    for char in line: # Step 3
        if char in string.ascii_letters + "_":
            lastFunctionChars += 1 # Step 4
            # lastFunctionChars will be 3
	        # as "add" is three characters long
        else:
            break # Step 5
    [...]
    return index - lastFunctionChars, fullLine
```


However, the programmer may add brackets around values without using them to call a function. They may do this to change the order of operations in math (e.g: `(1 + 2) * 3`. Note how there is no function call around `(1 + 2)`). In these cases, we will prepend the function `__noopReturn__` in front of the brackets. This makes the brackets a valid function call now. The function simply returns back all values that it received as arguments. The alternative to this operation would be detecting all brackets not tied to function calls and removing them, but this would be more error-prone than this method, with the only upside being slightly faster interpreter execution speed. Here is a demonstration of this in action. Please note that at this point, operators such as `+` would have already been converted, but to make this example clearer, they are still kept in:
```go
// Problem:
a  *  (  b  +  c  )

// Step 1: Find the outermost brackets
a  *  (  b  +  c  )
      ^           ^

// Step 2: Add __noopReturn__ if brackets do nothing
a  *  __noopReturn__( b  +  c  )
```
The code for this is also located in the `detectFunctionCall` function. This is how it works:
```Python
def detectFunctionCall(line, index):
    [...]
    if not lastFunctionChars > 0:
        fullLine = insertFunctionCall("".join(fullLine), index)
        lastFunctionChars = len("__noopReturn__")
    return index - lastFunctionChars, fullLine
```
If the length of the function name is zero, it does not exist. The brackets, therefore, are not a part of a function call. If this is the case, we pass the line and index of the opening brace to `insertFunctionCall`. The length of the function name can be determined with `len("__noopReturn__")` because it remains the same. `insertFunctionCall` returns the original line but with the `__noopReturn__` function inserted right before the opening bracket.

As a next step, the algorithm finds all arguments of the function call. It must simply take the string between the opening and closing bracket and split it based on commas. This is all done by the function `getArguments`:
```Python
def getArguments(firstBracket, secondBracket, line):
	# Args will store all the extracted arguments
    args = []
    # currentArg will temporarily hold the argument
    # being read being read
    currentArg = ""
    [...]
    # We cut the line to only include text
    # between the opening and closing brackets.
    # This space will be the arguments supplied.
    # Note that this only changes the line variable in
    # the getArguments function and not 
    # in the entire compiler.
    line = line[firstBracket+1:secondBracket]
    # We go through every character between the
    # brackets
    for char in line:
	    # If the char is a comma, separating two
	    # arguments, we can add the argument in the
	    # currentArg variable to the args list
        if char == "," [...]:
            args.append(currentArg)
            currentArg = ""
            continue # Continue makes Python jump
	        # to the next character instead of
	        # executing the rest of the code
	        # in the for loop.
        [...]
        # Spaces should be ignored
        elif char == " ":
            continue
        # If the character is neither a space nor
        # a comma, it must be a part of the arguments
        # name. We can add this character to the
        # end currentArg variable.
        currentArg += char
    args.append(currentArg)
    return args
```

One difficulty is needing to differentiate between commas separating arguments in the current function call or in nested function calls. Here is a visualization of this:
```Python
# Here is a nested function call:
add( sub(1, 2), 3)
# We want the following list of arguments:
["sub(1, 2)", "3"]
# We can tell that the sub() and 3 are separate arguments
# because they have a comma between them:
add( sub(1, 2), 3)
#             ^

# A nested function call might also have arguments
# itself, like the sub call:
sub(1, 2)
# When we are separating the arguments for the 
# add() call, we do not want to separate the arguments
# of the sub() call as well. This is what would
# happen if we separated the arguments of the
# sub function call as well:
["sub(1", "2)", "3"]
``` 
`getArguments` uses the tried-and-tested method of creating a bracket counter, increasing it for every opening bracket found and decreasing it for every closing bracket discovered. Only when this counter is at zero can we consider the comma to be from the current function and not from a nested function call. When this happens, there must have been an equal amount of opening and closing brackets, meaning that they canceled each other out:
```go
// Problem:
// Separate arguments of add function while the sub function
// call should remain unseparated
add( sub(1, 2), 3)
   ^             ^
// Note that the outermost brackets have already been found

// Step 1: Focus on items inside outermost brackets
sub(1, 2), 3

// Step 2: Go through each character, making a bracket counter
sub(1, 2), 3
000111110000
// The bracket counter is displayed under each character

// Step 3: Identify whether the current character is a comma
sub(1, 2), 3
     ^   ^
000111110000

// Step 4: Separate arguments using commas with a counter of 0
argumentOne = sub(1, 2)
argumentTwo = 3
// It is important that the arguments are only split when the 
// bracket counter is at 0. In any other case, nested function
// calls may be split up like so:
// argumentOne   = sub(1
// argumentTwo   = 2)
// argumentThree = 3 
```
This is all done with the following code that was hidden when we looked at `getArguments` before:
```Python
def getArguments(firstBracket, secondBracket, line):
    args = []
    currentArg = ""
    # Set the bracket counter to zero
    bracketCounter = 0
    line = line[firstBracket+1:secondBracket]
    for char in line:
	    # Only add the argument if the bracketCounter
	    # is zero
        if char == "," and bracketCounter == 0:
            args.append(currentArg)
            currentArg = ""
            continue
        if char == "(":
	        # If the character is an opening bracket,
	        # increase the counter by one
            bracketCounter += 1
        elif char == ")":
	        # and decrement it if we are dealing
	        # with a closing bracket
            bracketCounter -= 1
        elif char == " ":
            continue
        currentArg += char
    args.append(currentArg)
    return args
```

Back in `splitFunctionCalls`, we can then iterate over every argument of the current function. `splitFunctionCalls`, therefore, currently looks like this:
```Python
def splitFunctionCalls(lineList, firstCall=True):
    [...]
    for lineIndex, line in enumerate(lineList):
        [...] # get the brackets locations
        # If there are no brackets, continue to
        # the next instruction in the line
        if firstBracketLine == secondBracketLine and secondBracketLine == -1:
            continue
        # Get the function call
        startIndex, line = detectFunctionCall(line, firstBracketLine)
        # Get the arguments passed
        args = getArguments(firstBracketLine, secondBracketLine, line)
        # Go through each argument
        for index, arg in enumerate(args):
	        [...]
```
We are now going through every argument to repeat this same process on it this time, as it could be a nested function call itself. Once again, we look for the first outermost brackets in the argument and the function to be called (or insert `__noopReturn__` if we only find brackets). Note that if we do not find brackets, there are no nested function calls, and we can safely skip over all the next steps. The current argument can remain unchanged:
```Python
def splitFunctionCalls(lineList, firstCall=True):
	[...]
    for lineIndex, line in enumerate(lineList):
        [...]
        for index, arg in enumerate(args):
	        # Get the locations of the first brackets
	        # in the argument
            firstBracket, secondBracket = getOutermostBrackets(arg)
            # If the brackets don't exist, we 
            # can "continue", meaning that we 
            # skip past all the code remaining
            # in this for-loop and move on to
            # the next argument.
            if firstBracket == secondBracket and secondBracket == -1:
                continue
```

If `getOutermostBrackets` does not find any, it will return the indexes of both brackets as negative one. This can be used to determine whether any brackets were found at all, as the index of both the opening and closing brackets can't be the same in any other case, let alone be negative. If we do find another function call, we must copy the entire argument we just found and append it to the lines list.  

We must now replace the extracted argument with an RVV. However, because the list of instructions will be reversed near the end of this level, we can't currently know whether there are any more nested function calls that would increase the instruction number of the current one. Here is an example of this:
```Python
# This is the line we start with:
add(sub(mul(1, 2), 3), 4)
# These instructions are our end goal:
0, 1, mul, 1, 2
1, 1, sub, ret0, 3
2, 1, add, ret1, 4
# The list of instructions consists of just the line currently:
instructions = ["add(sub(mul(1, 2), 3), 4)"]

# NoBash first finds the nested sub function and extracts it:
add( , 4)
# It is then added to the instructions list:
instructions = ["add( , 4)", "sub(mul(1, 2), 3)"]
# Currently, the add instruction is before the sub one
# The list of instructions
# must therefore be reversed for the proper order:
instructions = ["sub(mul(1, 2), 3)", "add( , 4)"]

# The RVV now has to be inserted. Currently, 
# the sub instruction would be the zeroth:
add(ret0, 4)

# But the sub instruction still contains another
# nested function call. When this is extracted, 
# sub would no longer be the zeroth instruction,
# as that place would now be occupied by mul:
instructions = ["mul(1, 2)", "sub(, 3)", "add(ret0, 4)"]
# ret0 would now point to mul, though add actually
# wants the result of sub. We can't know the 
# instruction number while functions are still being
# extracted.
```

Because the instruction numbers are not set in stone, we will make the RVV temporary. We make it the "ret" suffix plus the index of the nested function call in the lines list. Let us apply this to the example above:
```Python
# This time, we do not reverse the order of the 
# instructions until the end of this level
instructions = ["add( , 4)", "sub(mul(1, 2), 3)"]

# The RVV now has to be inserted. No matter how
# many arguments we add to the instructions list,
# the sub function will always be the second item 
# at index one. sub() will, therefore, be replaced
# with ret1 temporarily.
add(ret1, 4)

# Here is the proof. The mul function call has
# been extracted out of sub(), but the index
# of sub still remained the same.
instructions = ["add(ret1, 4)", "sub(ret2, 3)", "mul(1, 2)"]
```

In other words, equal to the length of the lines list (as it was appended to the end, making its index always be the length of the list). 
```Python
def splitFunctionCalls(lineList, firstCall=True):
	for index, arg in enumerate(args):
		[...]  # We can only get this far if arg contains
		# a nested function call
		startIndex, arg = detectFunctionCall(arg, firstBracket)
		# We can add the function call to the end 
		# of the instructions list
		newLineList.append(arg)
		# The function call argument must now be
		# replaced with the RVV. Since the argument
		# was added to the end of the list, we know
		# that its location is the length of
		# the list
		args[index] = "ret"+str(len(newLineList))+" "
	# Finally, we replace the current function call
	# with a version of itself that has all of
	# the nested arguments replaced by their
	# RVVs.
	newLineList[lineIndex] = line[:firstBracketLine+1] + ", ".join(args) + line[secondBracketLine:]
```

We will then run `splitFunctionCalls` again, passing the new instructions list, which contains the extracted nested function calls, as an argument. This means that we will continuously run this entire process, extracting the nested function calls out of all the other nested function calls using the power of recursion. 

```go
// Problem: 
add(sub(mul(4, 3), 2), 1)

// First cycle:
["add(ret2, 1)", "sub(mul(4, 3), 2)"]
// The entire subtraction argument was cut out and replaced
// by "ret2". This is because it is now the second instruction
// in the list currently, with the "add" call being the first.
// A keen observer may have realized that, even though computers
// start counting from zero, this is not reflected here. This is
// because we are using the length of the list and not the 
// index. A length of 0 would indicate an empty list, so an 
// length of one refers to a list with one element.

// Second cycle:
["add(ret2, 1)", "sub(ret3, 2)", "mul(4, 3)"]

```

Once we are done, and there are no more nested function calls in the current line, we will reverse the lines list to make nested functions be executed before the function that expected their returned value as an argument:
```Python
# This is the line we start with:
add(sub(mul(1, 2), 3), 4)
# These instructions are our end goal:
0, 1, mul, 1, 2
1, 1, sub, ret0, 3
2, 1, add, ret1, 4

# We currently have this instructions list:
instructions = [
	"add(ret2, 4)", 
	"sub(ret3, 3)",      # This returns ret2
	"mul(1, 2)"          # and this ret3
]

# If we reverse this, the instructions are in the correct order:
instructions = [
	"mul(1, 2)",         # This returns ret3
	"sub(ret2, 3)",      # and this ret2
	"add(ret1, 4)"
]

```
However, the RVVs we set are still simply placeholders, as can be seen in the example above. Therefore, we must create a new function, `insertProperRetVals,` which turns these placeholders into the real RVVs using the correct instruction numbers. It will search every instruction of a line for a string matching the pattern "`ret`":
```Python
def insertProperRetVals(line, retCounter):
    for indx, segment in enumerate(line):
        newSegment = ""
        while "ret" in segment:
        [...]
```
After checking that there is a number immediately following the matched string (to make sure it has not matched a `return` statement, for instance), it will use the following formula to calculate the proper instruction number of the instruction that returns the RVV: 
1) First, it will determine the index of the instruction in the line now that the line is completed and its length is known:
```Python
len(line) - int(ret[3:])
```
   Because the current RVV index is set equal to the index of the instruction in the list before it was reversed, we can find out its current index by subtracting the current RVV index from the current length of the lines list. 
   For example, if the index of an instruction used to be one in a list that, after being reversed, is now five elements long, then it will be the fourth element after the list was reversed (5 - 1 = 4). 

2) We now have the instruction number within the list, but we need to add the sum of the length of all previous lines to this value. This means that we add the count of all instructions up to this line together. We then combine this with the index of the instruction within the current line, giving us the correct index of the instruction. 

Once all of this is done, we can return the line, as we have extracted all nested functions and given all RVVs the correct index. Here is another example detailing this entire process:
```go
// Problem: script
put(1)
put(add(1, 2))

// Problem: instructions
["put(1)"]
["put(ret2)", "add(1, 2)"]

// Step 1: Reverse instructions lists
["put(1)"]
["add(1, 2)", "put(ret2)"]
// This will lead to the instructions being in the right order:
// put(1)
// add(1, 2)
// put(ret2)

// Step 2: Assign proper RVVs (Instruction number to the left)
0. put(1)
1. add(1, 2)
2. put(ret1) // Changed from ret2 to ret1, as add(1, 2) is at
// index number one overall
```
  
## Replacing braces and making if-chains (Level 11)

In level 8, all closing curly braces (`{`) have been replaced with their respective *cbrf*s (e.g: `__jumpBackFor__`), which are integral to control flow constructions. Currently, the arguments of these functions are still braces along with their IDs appended to them (e.g:`__jumpBackFor__({1)`. In order to keep the instructions readable, all tokens should be alphanumeric. To keep up with this standard, all opening braces are replaced with the string „`obrs`“ (standing for „opening brace return system“) and closing braces becoming „`cbrs`“ (standing for „closing brace return system“) in this level. This has no functional effect. A more important change in this level is the detection of „if-chains“.  In NoBash, "if-chains" is a name given to a construction consisting of an "`if`" condition block followed by "`elif`" and "`else`" blocks until the chain is terminated. This is important as the code contained in an "`else`" block may only run if the preceding "`if`" condition was not met. As such, the interpreter must know which `if` the `else` is connected to. Then, it can find out whether the condition was met and run the code contained in the `else` clause accordingly. In this level, the compiler determines which conditionals are a part of an if-chain and stores its findings.  


Replacing all brackets with either the string "`cbrs`" or "`obrs`" can be done by looping over all lines and using the `replace` method to do all of this work for us. As for making the if chains: We will first need to find all lines containing an `if`/`else`/`elif` keyword. Then, we must check whether any of these control flow constructs end on the same line as another one starts. If this is the case, we know that they are connected and must store this finding.
  

The first step will be creating a function `replaceCBRS` which iterates over every line and uses the `replace` method to replace all occurrences of "`{`" with "`obrs`" and "`}`" with "`cbrs`" respectively:
```Python
def replaceCurlyBraces(lines):
	# Go through every line
    for lineNumber, line in lines.items():
	    # Go through every instruction in the line
        for index, segment in enumerate(line):
	        # Replace the braces in the instruction
            lines[lineNumber][index] = segment.replace("{", "obrs").replace("}", "cbrs")
    return lines
```

The second goal of this level requires us to use the `bracesInfo` dictionary once again. We must iterate over every `key: value` pair stored within it, with these being the corresponding `ID` and `info` about the control flow construct, respectively:
```Python
def getIfChains(bracesInfo):
    ifChains = []
    ends = {}
    conditionals = ["if", "else", "elif"]
    for braceID, info in bracesInfo.items():
	    [...] # We will implement this now
```
We can then check the `info` dictionary to see what kind of keyword it relates to. If it relates to any of the conditional keywords, this could mean that it is part of an if-chain:
```Python
def getIfChains(bracesInfo):
	[...]
	conditionals = ["if", "else", "elif"]
	for braceID, info in bracesInfo.items():
		# Store the keyword in ctrlFlowStatement
		ctrlFlowStatement = info["ctrlFlowStatement"]
		# If the keyword of the line is not one
		# of the conditionals, continue to
		# the next brace stored
		if ctrlFlowStatement not in conditionals:
			continue
```

In a dictionary called `ends`, we store the ending line numbers of all of these conditionals along with their respective IDs. We can, therefore, look through `ends`, checking to see if any conditional ended on the same line as this one started:
```Python
def getIfChains(bracesInfo):
    [...]
    # This is the line the conditional started on
	startOp = info["startOp"]
	# And this is where it ended
	endOp = info["endOp"]
	# We store the brace ID in the ends dictionary
	# and use the line it ended on as a key
	ends[str(endOp)] = braceID
	# We can then check if the line it started on
	# is the same as where another brace ended:
	if str(startOp) in ends: # we check if it is
		# in the keys of ends.
		[...]
```
If we find such a match, we must add or create a new if-chain in the `ifChains` list, where we store them. Each if-chain is composed of a list which will contain the IDs of all cbrs in the chain. The list may look something like this:
```Python
ifChains = [
	["0", "1", "3"], # This is one if chain
	["5", "8"]       # Here is another
]
```

Upon finding a match in the `ends` dictionary, giving us the relevant ID of the conditional ending on the line the current conditional starts on, we can search the `ifChains` list for a chain containing that ID. Finally, we append the current conditional we have identified to be a part of the chain to the `ifChains` list. If the chain does not exist yet, we can create it by adding the ID to an empty if-chain list:
```Python
def getIfChains(bracesInfo):
    [...]
	if str(startOp) in ends:
		# Get the ID of the brace which closes
		# on the same line as this one starts on
		endCtrlId = ends[str(startOp)]
		# Go through every stored if-chain
		for indx, chain in enumerate(ifChains):
			# If the ID of the previous brace is
			# in the chain currently being looked at
			if endCtrlId in chain:
				# Add the current brace ID to the chain
				chain.append(braceID)
				break
	else:
		# If the chain has not been started yet,
		# create one.
		ifChains.append([braceID])

	return ifChains
```
We then continue doing this for all other braces in `bracesInfo`.


## Calculating all cbrs instruction numbers (Level 12)
When an `if` condition is not met, the interpreter must jump to the instruction following all of the code meant to be skipped. In the case of a `for` loop, when its end is reached, the interpreter should jump back to the start of the loop to continue the cycle. In both cases, the interpreter will need to know which instruction to jump to. In code, this is denoted using curly braces. When an `if` statement is not met, all the code until the closing brace is skipped. Because the interpreter deals with instructions rather than code, we must translate the location of the opening and closing brackets into an instruction number to which it should jump. This is the goal of the current level.


The system behind this level simply goes over every instruction, counting them along the way. This way, the compiler knows that the first instruction is at index zero, the second instruction is at index one, and so on. When the instruction contains either the string "obrs" or "cbrs", it can be assumed that the following numbers are the ID of a brace. The count mentioned before is the instruction number before the brace, be it an opening or closing one, can now be assigned the instruction number it shows up in:
```go
0, 1, __checkIf__, true, cbrs1 // if true {1
[...]

// cbrs1 was found in instruction zero, so if we need
// to jump to {1 in the future, this is the location
// we must go to
cbrs1Location = 0
```

However, there is one small caveat, this being that the interpreter might have to jump to an instruction before that in which the opening brace shows up in. This is the case in `while` loops. For instance, take the following code snippet:
```go
while x == 1 {
```
This would be split up into two instructions, one which compares the two values and another which leaves the loop if the comparison ever turns out to be `false`:
```go
0, 1, isEqual, x, 1
1, 1, __doWhile__, ret0, cbrs1
```
When the end of the `while` construction is met and the interpreter wants to jump back to the start, with the current system, it would jump to instruction number one, as this is the line which contains "cbrs". However, this would not work, as the check in instruction number 0 would then never be made. This would essentially create an endless loop, as the check would only be run once when starting the loop, and the result of the check would be used and never re-evaluated in future checks. The system, therefore, must not jump to the instruction containing the brace but to the first instruction of the *line* containing the brace. This ensures that all instructions of the `while` loop are made.

The function responsible for this level will be `gteBracketInstruction`. Inside of it, we first add the functions to the end of the lines. This ensures that when counting instructions, we do not restart the counter when we iterate over a new function. All instructions, whether they originate from a function or not, should be counted in order. We then iterate over all lines in every instruction, followed by every instruction within that line. During all of this, we always save the number of the first instruction of the current line:
```Python
def getBracketInstruction(lines, funcs):
	# First, we create one list containing both all
	# lines in the main script and those in the 
	# functions together.
    instructions = [lines]
    instructions += [func for func in funcs.values()]
    # Brackets will contain a list of every bracket
    # and what instruction it is on
    brackets = {}
	# This variable will hold the instruction number
	# of the current instruction
    instructionCounter = 0
    # lastLine holds the number of the line the
    # current instruction is from. The second
    # variable contains the first instruction
    # number from that line
    lastLine, lastLineFirstInstruction = 0, 0
	# We then go through each line
    for lines in instructions:
        for lineNumber, line in lines.items():
	        # We then go through each instruction
	        # in the line
            for section in line:
	            # If we have moved to a new line,
	            # we must save the current instruction
	            # number. It is the first instruction
	            # in the current line. We will use
	            # this to jump to the first
	            # instruction on the line a brace
	            # is from.
                if lineNumber != lastLine:
                    lastLineFirstInstruction = instructionCounter
                # We also save the current line number
                lastLine = lineNumber
                # Then increment the instruction
                # counter by one as we will move
                # to the next instruction now.
				instructionCounter += 1
```
At this point, we have the first instruction in every line. This means that in the previous example, even though the brace occurs in instruction one, we can trace the first instruction of the line back to the comparison. 
```Python
0, 1, isEqual, x, 1
1, 1, __doWhile__, ret0, cbrs1

# Even though cbrs1 occurs in the second instruction,
# the compiler knows that it must jump back to the
# __isEqual__ comparison instead as it is the first
# instruction in the line containing the bracket.
```
To complete this level, we must now actually detect instructions containing braces. We then need to save the first instruction of the line the brace appears on in a dictionary. The interpreter can later use this dictionary to jump to the proper instruction when encountering a brace:
```Python
def getBracketInstruction(lines, funcs):
    [...]
    [...] # For each line:
		for section in line:
			[...]
			# Repeat the following process for both
			# opening and closing braces
			for bracketType in ["obrs", "cbrs"]:
				# If the instruction contains a brace
				if bracketType in section [...]:
					# Get the ID of the brace
					obrsId = bracketType + getBracketWithIds(section, bracketType)
					# Save the current instruction
					# as the location of the 
					# brace. This will apply to
					# closing braces specifically.
					brackets[obrsId] = instructionCounter
					# If the brace is an opening one,
					# we should instead save the 
					# instruction number as that
					# of the first one in the line.
					if bracketType == "obrs":
						brackets[obrsId] = lastLineFirstInstruction
			[...]
    return brackets
```


## Writing all the data into a file (Level 13)
At this point, we have finished making all instructions, and the interpreter can now run them. Currently, the instructions are stored in memory (RAM), which, as described earlier, will be erased when the computer is shut down. However, if the same script is run again after the computer is shut down, the compiler would have to re-compute all instructions. Additionally, computers typically don't have a huge amount of RAM, so data should be saved there sparingly. NoBash, therefore, writes the instructions in a file to the computer's storage, which has a lot more space, and data is stored on it persistently even after the computer is shut down. When the interpreter wants to run the instructions, it can read the file containing them, thereby loading the instructions into the valuable RAM space only when they are needed. 

We will first need all of the data we have gathered over the course of nearly all levels. This includes all instructions, if-chains, and info on braces, just to name a few. The way we save the data in the file differs from data to data. For example, instructions need to have their starting instruction and line written at the very beginning like so:
```Python
0, 1, put, "This is an instruction"
```
Info on functions immediately starts with the function name and has the instruction they start on listed after:
```Python
foo, 0   # Foo starts on line 0
```
It is important to mention that all compiled scripts are saved in the same location. Specifically, they are stored in `~/.nobash/compiledScripts/`, whereby `~` stands for the user's home directory (e.g: `/home/alice`). When a NoBash script is run, NoBash first checks whether a compiled instructions file already exists for the given script in that folder. If the compiled files were saved in the same directory as the original script, this would produce a lot of clutter in a folder. The downside of this approach is that only one script of a certain name can stay compiled at once. If `script.nb` was run in one directory, `script.nbc` would be saved in `compiledScripts`. Then, if a different script going by the same name was run in another directory, its compiled file would overwrite that. However, when two scripts are called differently, the compiled files can be stored simultaneously without issue. 

To start this level, we should create a main function, `writeDataToFile`. It will then call each function specialized in saving a certain type of data. `writeDataToFile` is also responsible for initially creating the file all other functions will write to. Here is its code:
```Python
def writeDataToFile(lines, [...], metadata):
    try:
	    # We first get the location to store the
	    # compiled script in. "expanduser" will
	    # turn the "~" into the home path of
	    # the user.
        pathPrefix = expanduser("~/.nobash/compiledScripts/")
        # We then create a new version of the script
        # name, this time with an "nbc" extension
        # rather than "nb". While "nb" stands for
        # "NoBash", "nbc" stands for "NoBash compiled"
        newName = scriptName.replace(".nb", ".nbc")
        # We then try to create the file at the
        # central location and with the name we
        # just gave it.
        with open(pathPrefix+newName, "w") as file:
	        # First, we write the metadata
            writeMetadataToFile(file, metadata)
            # Then the instructions of the main script
            writeLinesToFile(lines, functions, scriptName, stringDictionary, file)
            # Then all functions
            writeFuncsToFile(funcInfos, functionStartInstructions, file)
            # Finally, we write info on the braces,
            # such as if-chains.
            writeBracesInfoToFile(ifChains, bracesInfo, file, bracesInstructions)
    # If something goes wrong during this process,
    # like if the "compiledScripts" folder does not
    # exist, we must report that as an error
    except Exception as e:
        error(16, scriptName.replace(".nb", ".nbc"))
```
We will not look at how every type of data is written to the file, as the code typically always stays the same with only some minor changes. There is, however, an interesting part of the function responsible for writing instructions we should look at:
```Python
# This function is responsible for inserting
# strings back in for their replacements ("str#").
def insertStrings(line, stringDictionary):
	# First, we reverse the dictionary of strings. 
	# We want to replace str10 before str1, as when
	# we replace str1 we may accidentally target str10
	# instead. This is because "str1" is contained in
	# "str10", leading to potential errors. 
	reverse = reversed(list(stringDictionary.items()))
	# We then go through every string replacement 
	# in the reversed dictionary along with
	# the string it represents
    for replacer, string in dict(reverse).items():
	    # We then replace all instances of the
	    # the replacement in the line with the
	    # proper string. This is also the step which
	    # requires us to reverse the dictionary, as
	    # when replacing "str1", we might accidentally
	    # replace the "str1" out of "str10". When 
	    # reversing the dictionary, we remove all 
	    # instances of "str10" before "str1", fixing 
	    # the issue.
        line = line.replace(replacer, '"'+string+'"')
    return line
```


# The Interpreter

## Reading the instructions (Level 1)
In order to run any code, the interpreter needs a complete list of instructions. It would be inefficient to recompute all instructions each time the same unaltered script is executed. Therefore, the compiler writes all instructions to a file and passes the file's location on to the interpreter. The interpreter then reads the file at the specified location. The goal of this level is to read the file at the specified location and present the instruction file's lines in a usable format, specifically as a list, to the rest of the program.


The location of the instructions is passed as an argument to the program, so executing a file containing nobash instructions called "cleanup.nbc" within the home directory of user bob may be done with the following commands:
`nobash -i /home/bob/cleanup.nb` 
or (assuming that the script is called from within the same directory as the instructions file):
`nobash -i cleanup.nb`. 
The `-i` flag specifies that the following file should be interpreted immediately and not compiled first. This location is then passed on to a function that handles reading the file while ensuring no errors occur during the operation. 
  

This entire level can be done in one function in around five lines. It only takes the file location as an argument and returns the lines the file contains inside a list. First, we have to create a file that calls the other levels. We will call it `interpreter.py`. Inside it, we can try getting the first argument passed:
```Python
try: 
    fileLocation = argv[1]
except Exception as e:
	error(218)
```
If no argument was passed, an error is raised. This works in the same manner as it does in the compiler. We can then pass this file location to a `readFile` function we will create now. This will be where we write the bulk of the code required for this level:
```Python
def readFile(fileLocation):
    try:
        with open(fileLocation, "r") as file:
            return [line[:-1] if line.endswith("\n") else line for line in file.readlines()]
    except Exception:
        error(94, [fileLocation])
```
We must wrap the file processing in a try-except block, as multiple things may go wrong while reading the file at the given position. For example, there may not be a file at the passed position, or the interpreter may not have permission to read it. If any of this fails and an exception is thrown, we pass this data on to our error handler, which then communicates the issue to the user. If everything goes according to plan, we can use the built-in "`readlines`" method on the opened file, which gives us all of the file's lines separated as a list:
```Python
file.readlines()
```
We must now only remove any potentially leftover newline characters at the end of each line:
```Python
# We first create a new list. We then go through 
# every line in the file. If the file ends with
# a newline character, we remove it. We then add
# this line to the list.
[line[:-1] if line.endswith("\n") else line for line in file.readlines()]
```
Once this is done, we may return the list of lines back to `interpreter.py`.

  

## Separate the file into sections (Level 2)

Instruction files do not only include raw instructions but also metadata and function definitions. These different pieces of information are all written down in different ways. For example, a line containing an instruction may look like this:
```Python
4, 3, put, „hello“
```
whereas a line containing a function definition may look like this:
```Python
# Notice how the first two integers are missing
printResult, 5, 7
```
If the interpreter tried to interpret a function definition as it would an instruction, the interpreter would crash trying to convert a string to an integer. Additionally, a lot of the meaning would be lost from different lines, and the program would not function properly. Therefore, we must separate the lines of the file based on what section they belong to. The interpreter knows how to handle lines from each section; we only have to tell it what section a line belongs to.

In the instructions file, instructions are already separated into sections. Therefore, we have to read through every line in the file and check whether the current line is a section definition or not. If it is, we can determine what section is being started. All subsequent lines belong to that section. They must, therefore, also be stored in such a way that we can easily find out what kind of data any given line carries.

New sections are declared like this: „`# [section name]`“, whereby „`[section name]`“ is the name of the section. The lines after the declaration belong to it until there is either a new section definition or the end of the file is met. We must only read through every line one by one and use the „`startswith`“ method on the current line:
```Python
def splitSections(rawLines):
    [...]
    # Go through every line
    for line in rawLines:
	    # If the line starts with a pound symbol...
        if line.startswith("# ")[...]:
	        # We know that it is a section definition
	        [...]
```

It must be noted, however, that functions defined within a NoBash script must consist exclusively of letters, as having a function name start with „`#`“ would mean that the line defining the function would look like this: „`#, 12`“, causing the `12` to be interpreted as a function name (as it is a string of characters after the # separated by a space). 

Once we have found a line beginning with a pound symbol, we can then split this line into a list based on spaces. The expected list would look something like this: `[“#“, “[section name]“]`. We can take the second element of this list, which would be the section name, like so:
```Python
def splitSections(rawLines):
    [...]
    section = None
    for line in rawLines:
        if line.startswith("# ") [...]:
	        # The second item in the split line
	        # will be the section name
            section = line.split()[1]
```
We can then start reading every line and use the method described previously to detect a section definition and find the section name, which we then store in the variable `section`. In the dictionary storing all sections with their lines, we then use the section name as a key and have the corresponding value be an empty list. We then go through each subsequent line and add it to the list the current section name is pointing to:
```Python
def splitSections(rawLines):
    sections = {}
    section = None
    for line in rawLines:
        if line.startswith("# ") and len(line.split()) == 2:
            section = line.split()[1]
        # If the line is not a section and a
        # section was already defined
        elif section:
	        # Create an empty list in the sections
	        # dictionary if there is none already
            if section not in sections.keys():
                sections[section] = []
            # Add the line to the list of the section
            # that was defined last
            sections[section].append(line)
    return sections
```
This happens until either a new section is hit, in which case the process is repeated, or an EOF (end of file) is met. At this point, we add the last line to the current section and finally return the dictionary. The section dictionary now consists of all sections with the lines that belong to it. The compiler also added metadata to the instructions file. The interpreter has no need for these, so the interpreter deletes them if a metadata section is found:
```Python
def removeMetadata(sections):
	# If, for some reason, there is no metadata
	# in the file, we don't have to remove them
    if "Metadata" not in sections.keys():
        return
    # Otherwise, del(ete) the metadata section
    # and all lines associated with it
    del sections["Metadata"]
    return sections
```

## A„string replacement“ dictionary (Level 3)

A function call may look like this: `0, 0, put, "Hello, friend!"`. To us humans, it is clear that there is one argument, namely `"hello, world!"`. However, the interpreter might take the comma not as a part of the string but as a delimiter between two arguments, thus making the two arguments passed `"hello` and ` world!"`. We have previously faced this exact dilemma in the compiler. In this level, we want to fix this issue of special characters in strings messing with the parsing of the line. Here is an instruction before and after this level:
```Python
# Here is an instruction:
[0, 1, put, "Hello, friend!"]
# The comma between Hello and friend could be
# mistaken as a comma between two arguments

# Here is the same instruction with the string replaced with a reference to it:
[0, 1, put, str1]
# Crucially, the reference contains no commas
# which could be mistaken for anything else
```

Like with the compiler, we can do this by temporarily replacing all strings with placeholders until all the parsing is done. Continuing the above example, by replacing the string with "`replace-me!`" (which does not include any commas), the interpreter would correctly detect this to be one argument. It can then go on to perform any further parsing until we finally run the instructions, at which point we replace all instances of "`replace-me!`" with the same string again. This will be a multi-step process since we will have to reinsert the string later, which will take place in a future level. So, for level three, we will only create the means for replacing strings and storing them somewhere to be added in again later. 

  
As long as the reference does not include any special characters itself, all these issues would easily be avoided. We just need to find an algorithm to detect strings and replace them with a reference to them. Additionally, since we want to reintroduce the strings back into our program when they are needed, we need a safe and efficient way to store them until we want to work with them again.


In this level, we will create two functions, one to iterate through all lines and another to replace all string arguments. The only caveat of iterating through the lines now is that we must iterate both overall sections and then over all the lines contained within them. This will be done in the `removeStrings` function:
```Python
def removeStrings(sections, stringList):
	# Go through every section
    for section, lines in sections.items():
	    # And call stringRemover on every line
        lines = [stringRemover(stringList, line) for line in lines]
        # Finally, save the lines with the strings
        # now removed
        sections[section] = lines
    return sections
```

`removeStrings` will then call a new function, `stringRemover` on every line. It is the task of `stringRemover` to replace the strings with placeholders. Every string is replaced by a reference using the format "`STR[X]`", whereby `[X]` is a counter that keeps incrementing by one for each string that is replaced so that no two strings can ever be replaced by the same reference. Once their replacement has been made, we will have to identify all strings in the line. We first save their contents as we need to reinsert them later. Then, we can replace them in the line with their respective placeholders. We must also connect each placeholder with the string it represents. If we did not do so, we would have no way of knowing which placeholder is meant to replace which string.

As a first step, we must find out how many strings there are in a given line, which we do using the following code snippet: 
```Python
# // acts like a normal divide (/)
# However, if the result is a float, it gets
# rounded down into an integer
line.count('"')//2
```
It divides the number of quotes in the line by two, as every string must be composed of one quote to start the string and another one to end it. Since we want to remove all strings but can only replace one string at a time, we must repeat this replacement process for every string. Luckily, we have just found the number of strings in the line and, as such, the amount of times the replacement process must happen. 

First, we create the reference to be inserted later. The strings ID will be the number of strings already found plus one:
```Python
def stringRemover(stringList, line):
    string = None
    for _ in range(line.count('"')//2):
	    # To get the ID of the string, we run
	    # len(stringList)+1. When a string is found,
	    # it is added to stringList. We can therefore
	    # find out how many strings there have
	    # previously been by taking the length
	    # of that list. We can then add one to
	    # it to get the ID of the current string.
        stringEntry = f"str{len(stringList)+1}"
```
We can then use the `findStrings` function to find the start and end of the first string of the line. Note that each time the replacement process happens, the second string will become the first, as the previously first one was replaced:
```Python
def findStrings(line):
	# If there are not two quotes in the line,
	# we can return 0 as the index of the 
	# (nonexistent) opening and closing quotes.
    if line.count('"') >= 2:
	    # The index of the first quote can be
	    # determined by using the index method
        first = line.index('"')
        # We then return the index of the first
        # quote. We also return that of the closing
        # quote, but we must determine that first.
        return first, line[first+1:].index('"')+first+1

    return 0, 0
```
Let us look at `line[first+1:].index('"')+first+1` to understand why this gives us the location of the second quote in the line. To do this, we can take the following line as an example: `put("hello")`. First, we remove everything behind and including the opening quote from the line like so:
```Python
hello")
```
This means that the previously second quote has now become the first quote in the line. We can, therefore, also get its index using the `index` function:
```Python
hello")
#    5
# Index will tell us that the second quote is at
# index 5.
```
It should be noted that this was not possible earlier as `index` only returns the index of the first occurrence of the characters it is supposed to retrieve. This closing quote only has this index since we have removed everything before the opening quote earlier. We, therefore, must add the length of the characters we removed to this index in order to retrieve the index in the complete line:
```Python
# Our current index:
hello")
#    5 

# The total index:
put("hello")
#         10

# We must add the length of the characters
# we have removed to get the index of the quote
# in the total string:
put("
# This is 5 characters long
# and 5 (from 'put("' ) + 5 (the current index) = 10
```

Using the start and ending positions of the string, we can copy its contents by reading all characters in between them:
```Python
def stringRemover(stringList, line):
    string = None
    for _ in range(line.count('"')//2):
	    [...]
        start, stop = findStrings(line)
        # The string is located between the
        # opening and closing quotes
        string = line[start:stop]+'"'
```
At this point, we must replace the string with its placeholder. We can do this by taking everything to the left of the string and adding the reference to the end of that. We can then take everything to the right of the string and add that to the end. We can then set the line's content to be this new version:
```Python
def stringRemover(stringList, line):
    [...]
    for _ in range(line.count('"')//2):
        [...]
        # We add everything to the left of
        # the opening quote + the replacement
        # + everything to the left of the closing
        # quote
        line = line[:start]+ stringEntry + line[stop+1:]
```
Finally, we must save the string and store it with its reference. Without doing this, we could not insert the string back when it needs to be used during instruction execution. To do this, we can use the reference to the string as a key and the string as a value in the dictionary `stringList`. `stringList` will then hold these values until they can be reinserted back safely later:
```Python
def stringRemover(stringList, line):
    for _ in range(line.count('"')//2):
        [...]
        stringList[stringEntry] = string
    # Even though stringList is not returned,
    # because of the way that Python works,
    # the changes we made are still saved
    return line
```


## Separate into tokens (Level 4)

In this level, we want to take each line and separate it into its individual words or "tokens". More accurately, in this step, we will turn each line from one big string into a list that contains all of the "words" of the line in order. In doing so, we have our lines stored in a format that we can work with a lot better. Every token of an instruction is separated and stored in a fixed location. For example, the function to be called will always be the third token of an instruction. Thus, in future levels, when the interpreter needs the function name, it can access the third token of each line and know with certainty that it has the function name. If we did not do this and kept working with strings, the interpreter would have to determine which part of the line the function is each time it is needed. This is also the step that would be difficult to perform with strings in the arguments, so doing this will allow us to insert them back in the next step. 


Once again, we must only access every line individually and then separate all words into a list while still preserving the order of the words. When we replaced the strings in each line in the last level, we also got rid of all the commas they contained. This means that the only commas which are left in each line are meant to act as delimiters for the individual parts of each instruction (e.g: Instruction number **,** line number **,** function name **,** parameter1 **,** parameter2 **,** etc.). This comes in handy as we can now split up the line based on commas without worrying about accidentally cutting a string in half.
  

The function responsible for performing all actions in this level is `splitUp`. It first goes through all sections and stores the lines they contain in the `lines` variable:
```Python
def splitUp(sections):
    for section, lines in sections.items():
	    [...]
```
The function then goes through each line in `lines` and calls the `split` method on it. As a quick reminder: this method takes a string like `"1&2&3"` and cuts it up into a list based on a character or word of your choosing: 
```Python
"1&2&3".split("&")
# will become
["1", "2", "3"]
```
However, the list that is returned when we split up each line still has elements with trailing or leading whitespaces. When splitting the line: `0, 1, put, 1` we receive `["0", " 1", " put", " 1"]` instead of `["0", "1", "put", "1"]`. This could cause problems in the future (e.g: `"True" != " True"`), so we want to eliminate all of these unnecessary spaces. We can do this by iterating through each token and replacing it with a variant of itself that had the `.strip()` method called on it. This removes said spaces, leaving us with only the visible characters that we want:
```Python
def splitUp(sections):
    for section, lines in sections.items():
	    # This may look very confusing at first
	    # What you see here is a special
	    # way of writing for loops that is
	    # quicker to write for the programmer.
	    # In turn, it may be a bit more difficult
	    # to read. However, you should still be 
	    # able to spot the different steps described
	    # above, like the line.split()
        sections[section] = [[item.strip() for item in line.split(", ")] for line in lines]
    return sections
```
This new list of lines broken down into tokens is then saved to its section, replacing the old list of string-lines.

## Inserting strings (Level 5)

After having taken out strings to make the previous level easier on ourselves, we must now reinsert them into each instruction. This is important so that scripts output the intended strings rather than their placeholders. This step is essentially the reversal of level three of the interpreter. As we have already finished all operations that may be disrupted by certain characters in strings during the previous level, it is now safe to reintroduce them in a safe environment. We can also now safely turn any `&QUOTE` references back into quote characters. Here is a visualization of this level:
```Python
# Here is an instruction:
[0, 1, put, str1]
# Here is the same instruction with the string reinserted:
[0, 1, put, "Hello!"]
```
  

To insert the strings back in, we iterate over every word in a line and see if it matches a key in the string lookup dictionary. Because the keys in that dictionary are all a replacement for a string, we know a word such a key is a stand-in for a string. In that case, we can exchange the replacement with its original string value.

  
We must first create another function, `addStrings`, which iterates over all sections and all lines within them:
```Python
def addStrings(sections: dict, stringList: dict):
    # Go through every section and store its lines
    # in the 'lines' variable
    for section, lines in sections.items():
	    # Then, call 'stringAdder' and pass each line
	    # as an argument. stringAdder will return
	    # the line with its strings added back in.
	    # We can save this new list of lines
	    # back under the section they came from.
        sections[section] = [stringAdder(line, stringList) for line in lines]
    return sections
```
`addStrings` merely goes through each line and calls `stringAdder`; it is this latter function that actually inserts strings back into each line. It goes through each word in the line and checks whether it is contained in the keys of stringList. If it is, `stringAdder` can be sure that the word is a replacement for a string:
```Python
def stringAdder(line: str, stringList: dict):
	# for every word in the line
    for index, word in enumerate(line):
	    # check if it is contained in the keys
	    # of stringList
        if word in stringList.keys():
            [...]
    return line
```
If this is the case, we overwrite the word in the line list with the string it replaces. We also call the `replace` method on the string, replacing all instances of `&QUOTE` that we inserted during compilation with an actual quote character. This reverts "`He said: &QUOTE Hello! &QUOTE`" back to "`He said: "Hello!"`". Here is the full code for `stringAdder`, including this final bit of functionality:
```Python
def stringAdder(line: str, stringList: dict):
    for index, word in enumerate(line):
        if word in stringList.keys():
	        # The current word is a key for the
	        # string it replaces in stringList.
	        # This lets us retrieve the string
	        # from stringList like so:
	        string = stringList[word]
	        # We can then replace all instances of
	        # &QUOTE with an actual quote character
	        string = string.replace("&QUOTE", '"')
            # And finally we may save this string in
            # the instruction
            line[index] = string
    return line
```

  

  

## Turning the string tokens into actual token objects (Level 6)

As of right now, the words/"tokens" in each instruction are strings stored within a list. However, we will create our own "Token" class and have all strings become token objects. 

At this point, it may be useful to introduce what objects are in Python quickly. An object is like a "thing" that stores data and has actions you can perform on that data. For example, consider a "pet" object. The pet object can contain data like what type of animal and breed it is, along with other information like its color and how hungry it is. One object can, therefore, carry lots of data describing it, which can come in very handy. Additionally, this "pet" object can perform actions like "eat", which will decrease the hunger of the cat. We have already come across these "actions" before: methods. When we call `"Hello, friend!".split(",")`, we are calling the `split` method on a string object (`"Hello, friend!"`). 

This can also be applied to the tokens we are dealing with now. If a programmer writes `"hello" + 1`, this operation should not work, as you cannot add a string to an integer. Therefore, the `add` function must check whether the values being added have "compatible" types. If the values are objects, this can be as simple as comparing the following:
```Python
# If valueOne and valueTwo are both Token objects,
# we can find out their type by adding ".type" to
# to the end of them like so:
print(valueOne.type) # This will print 'string'
print(valueTwo.type) # This will print 'integer'

# This will also let us compare the types of the
# two tokens very easily:
if valueOne.type == valueTwo.type:
	# In the same way that '.type' gives us the
	# type of a token, '.value' will give us its
	# value. In this case, they would be "hello"
	# and 1 respectively.
	valueOne.value + valueTwo.value
```

The primary advantage that the token object gives us is full control over the type of different values as well as easy access to this information. Additionally, for certain special types like lists, dictionaries, or variables, our special Token type could store additional information, such as the value a variable is pointing to or the items that are stored in a list. As an example: While the programmer specifies that `"3.4"` is a string and not a float by wrapping the number with quotes, these quotes must be removed after the type has been determined. The reasoning for this can be explained by an example: Suppose a programmer wanted to create a script that requires the user to enter a password, which must be correct to continue the script. To do this, they would compare the password that the user typed in with the "correct" password that they specified, like `"password123"`. If the opening quotes were not removed, even if the user typed in `password123`, the passwords would not match. The "correct" password still has the quotes surrounding it to signify that it is a string. Quotes are used to signify that the enclosed sequence of characters is meant to be data, but they must not be treated as a part of said data. However, if you were to remove the quotes around the password, the interpreter could no longer differentiate it between a string and a variable, causing many bugs and errors. Because of this predicament, we must somehow specify the type of a string without referencing this in the actual string, as quotes do. This can most easily be done by converting our current tokens into "token objects" that have their type stored in them. This is what lets us use `token.type` instead of having to rely on quotes. Because the type is no longer stored in the value itself, we may remove the quotes from a string in favor of setting the `type` "attribute" to "string". When we retrieved the type of a token before using `valueOne.type`, we did so out of its `.type` "*attribute*". So, in short, in this level, we only want to define and construct a Token object that holds its value and type. We also want a method that automatically detects the type of a value and sets the type *attribute* to it. 


In order to tell Python what kind of data a token object should store in its *attributes*, we must define a token *class*. When a new token object is created, it will then use our code from the token class as a blueprint, basing itself on it. For example: If the token class has a `.type` *attribute*, so will the token object. Defining a token class with the two attributes `type` and `value` (which contains the actual value of the token, like `hello` or `1`) requires only a couple of lines of code. Because NoBash automatically detects the type of a value without the programmer needing to specify it implicitly, the difficulty of this level comes from the type-detection algorithm. In order for this algorithm to work, we need to find characteristics unique to the values of each type. For example, the way that NoBash will differentiate between a float and an int is the dot in the middle of the float (`1.4` vs `1`). We then need to iron out some quirks and define new standards for the language. For example, we must decide whether `4.0` is considered a float or an integer. We want `4.0` to be considered a float, so we must add this to the detection algorithm that NoBash uses. It must also be said that the detection algorithm may not work properly if it is run on values mid-execution. For example, the quotes of a string will be removed already, which would cause the string `"hello"` to become `hello` during execution, making it either a variable or function but not a string. 


In the `__init__` method of a class, it is usually defined what *attributes* the objects will have. The Tokens have the `__init__` method defined to take in a value and (optionally) a type as arguments. The attribute for the value is set equal to the passed value. If a type was passed, we can set the `type` *attribute* equal to that as well:
```Python
# Here is how one can create a new Token object:
t = Token("Hello!")
# The variable "t" now contains a Token object
# with 'Hello!' as its value. 
print(t) # This will output: Hello!


class Token():
	# The __init__ method is defined within the
	# Token class. Every function defined within
	# it will take an argument "self" which
	# you can ignore.
    def __init__(self, value, type=None ):
	    # When "Hello!" was passed as an argument
	    # above, it was stored in the value parameter.
	    # Now, we set the value attribute equal
	    # to the what the value parameter contains
        self.value = value
        self.type = None
```
If the type parameter is empty (`Token("Hi")` instead of `Token("Hi", "string")`, we must detect the type automatically by running our value through the detection algorithm. If a type was manually provided, we can set the type attribute equal to that:
```Python
class Token():
    def __init__(self, value: str, type=None ):
        if not type: # If the type was not defined:
            self.detect() # Run the detection algorithm
            # in self.detect()
        else: # If the type was passed as an argument
            self.type = type # Set the type
            # attribute equal to the type passed
```

The detection algorithm works as follows, running the following checks against the value in this order. First, the value is turned into a string, and all trailing and leading spaces are removed:
```Python
def detect(self):
	[...]
	value = str(self.value).strip()
```
1) If it only consists of numbers and one dot symbol (".") it is a float:
   ```Python
   def detect(self):
        [...]
        value = str(self.value).strip()
        # If the value contains only digits and
        # fullstops set its type to float
        if value and not any([lett for lett in value if lett not in string.digits+"."]):
            self.type = "float"
   ```
2) But if it only consists of numbers without the dot, it's an integer
   ```Python
   def detect(self):
        [...]
        value = str(self.value).strip()
        if [...]: # contains only digits and "."
            self.type = "float"
            # But if it does not contain a dot,
            # it must be an int because it can only
            # consists of digits then
            if "." not in value:
                self.value = int(self.value)
                self.type = "int"
                return
   ```
3) Values, both starting and ending with quotes, are strings. The quotes are then removed from the value
   ```Python
   def detect(self):
        [...]
        value = str(self.value).strip()
        if [...]: # Is float/int
            [...]
        # If the value starts and ends with quotes
        elif value.startswith('"') and value.endswith('"'):
	        # Remove the quotes from the string
            self.value = value.strip()[1:-1]
            # and set its type equal to string
            self.type = "string"
            [...]
            return
   ```
4) If the value is identical to the string "`None`", it's a nonetype:
   ```Python
   def detect(self):
        [...]
        value = str(self.value).strip()
        if [...]: # is int/float
            [...]
        elif value.startswith('"') and value.endswith('"'):
            [...]
        # If the value is literally "none"
        elif value == "none":
	        # the type is a nonetype
            self.type = "nonetype"
            return
   ```
5) If the value is either `true` or `false`, it is a boolean
   ```Python
   def detect(self):
        [...]
        value = str(self.value).strip()
        if [...]:
            [...]
        elif value.startswith('"') and value.endswith('"'):
            [...]
        elif value == "none":
            [...]
        # if the value is either "true" or "false"
        elif value in ["true", "false"]:
	        # set the type equal to "bool"
            self.type = "bool"
            return
   ```
6) If all checks fail, then it is either a function or a variable. However, in NoBash, functions count as variables, so their type is set accordingly:
   ```Python
   def detect(self):
        [...]
        value = str(self.value).strip()
        if [...]:
            [...]
        elif value.startswith('"') and value.endswith('"'):
            [...]
        elif value == "none":
            [...]
        elif value in ["true", "false"]:
            [...]
        # The function "varsAndFuncsNameCheck"
        # simply returns True, so this condition
        # will always pass. Previously it had
        # more complicated checks inside of it,
        # but these have been removed for a more
        # robust system
        elif varsAndFuncs.varsAndFuncsNameCheck(value):
	        # isVarOrFunc replies "variable" at
	        # all times for the same reason as above
            _type = varsAndFuncs.isVarOrFunc(value)
            # _type will always be "variable", so
            # the check whether _type contains
            # anything will always pass
            if _type:
	            # the type is set to "variable"
	            # if the detection algorithm
	            # has not detected any other
	            # type beforehand
                self.type = _type
                return
   ```

It should be noted that there are still other types, such as the `list` or `dict` type, but these can only be instantiated by calling a function rather than being written out in code like strings or integers. Additionally, their type must be implicitly stated when the token is created. For example, here is how to create a list in NoBash:
```Python
l = list(1, 2, 3)
```
The `list` function responsible for creating the list would use the following code to do so, declaring the "list" type in the second argument:
```Python
Token([1, 2, 3], "list")
```


## Finishing the list of tokens (Level 7)
We have now defined the token class in the previous level, but we still need to turn the individual strings that construct each line into these token objects. As such, this step just has us iterate over all the elements of a line and turn those into tokens, replacing the original string value with the new token object. When this step is completed, we should have all values loaded from the instructions into the interpreter in a "tokenized" form (or turned into a Token object). We must make sure that every value the interpreter works with is always in a tokenized form, as the syntax for working with token objects differs from that when working with normal strings. As such, when mixing up the two types, we might encounter malfunctions and, in the worst case, fatal errors that the programmer is not responsible for. There are two ways that values can be introduced to the interpreter: once when the instructions are first loaded into it and when functions are called which return new values, such as `input` or `add`. The first of these two options occurs now, as this is the point when we load new values into our interpreter. So, before we do this, we must „sanitize“ the soon-to-be input and make sure that everything the interpreter works with from now on is of the type `Token`.


This step, like many of the ones before it, is comprised mostly of iterating over all the items in a line and then setting the current item of the list to an altered version of itself. This time, we must tokenize the value and replace the item we are currently on with its tokenized version. 
  

We must first define a new function, `setTokens`, that takes the section dictionary in as an argument like so:
```Python
def setTokens(sections):
    [...] # Tokenise everything in a line
    return sections
```
We then iterate through each element of each line of each section. Assuming that the current element is saved in a variable called `element`, we then set the item at the current index of the line equal to `Token(element)`. This returns a tokenized version of the value of the element, which is then saved into the line:
```Python
def setTokens(sections: dict):
	# We first go through every section and store
	# its lines in the "lines" variable
    for section, lines in sections.items():
	    # We then go through every line in lines:
	    # [... for line in lines]
	    # Every line still consists of a list of
	    # values/words (but not token objects).
	    # We must go through the list of tokens
	    # and create a proper token object
	    # by passing the value it should contain
	    # as an argument: Token(value)
        lines = [[Token(value) for value in line] for line in lines]
    return sections
```
At the end, we make sure that the section dictionary with the modified lines is saved with its new tokenized values:
```Python
def setTokens(sections: dict):
    for section, values in sections.items():
        sections[section] = [...] # Tokenised lines
    return sections
```

  
  
## Function lookup table (Level 8)

In NoBash, functions may be written in two languages: NoBash and Python. At its core, because the NoBash interpreter is written in Python, all instructions must eventually call a Python function at some point. For example, let‘s invent a function `sayHello` that takes an argument `name`. The function works like this: The programmer passes their name to the function, and the string `“Hello, [name]“` is printed, whereby `[name]` is the value of the argument passed with the same name. In this function, there are most likely two instructions: one call of the function `add` and another to the `put` function. When two integers are added using the `add` function, their values are mathematically added together: 
`add(1, 2) == 3`
If, on the other hand, two strings are added together, they are concatenated, with the string to the right being *add*ed to the end of the one to the left:
`add("Hello, ", "Bob!") == "Hello, Bob!"`
The add function appends the value of the name argument to a string `“Hello, “`,  while the put function outputs the result of the previous call. However, both functions are simply calls to Python functions. `Put` can be considered a wrapper for the Python  `print` function. Even NoBash functions defined by the programmer are just collections of Python function calls when looked at closely. 

However, how do we connect the NoBash `put` function with the Python `print` function? We need a „function lookup table“. This table provides detailed information on every function, though the details provided vary depending on whether the function is written in NoBash or in Python. For example, we must specify the library that a Python function must be imported from and store data on how the interpreter can retrieve the function. For NoBash functions, we must only store the starting index of the function in the instructions. We do not need to store where the function ends as the `__funcReturn__` function call at the end of every NoBash function automatically handles returning back to the main script. Essentially, the FLT provides the means for the interpreter to correctly call the corresponding Python function or move to the correct instruction if we are jumping into a NoBash function. It also stores extra information, like the parameters of NoBash functions. 
  

In this step, we must first create a file containing the FLT. Programmers can manually add entries into the FLT file if they wish, though the data is automatically entered into it by NoBash as well. We must also make some functions that perform operations like:
- *loading* the FLT file into RAM 
- *looking up* functions within the FLT 
- *adding* new entries
The FLT file is stored on the computer in the "JSON" format. JSON files can easily be turned into a Python dictionary, which means that we can automatically turn the FLT file into a Python dictionary already populated with data. We will need a function that can retrieve information like what library a function is from, what language it is written in, what arguments a function takes in, and what instruction a NoBash function starts on. Finally, we must be able to add new functions to the FLT while the interpreter is running. 
  

Firstly, we must create a new file called “`functionTable.json`” and store it in a “`data`” directory. The `data` directory also contains files with other information, such as the version of NoBash installed on the system and a list of all errors that can occur. This folder will pop up again in the future. For example, we need one central location to store libraries the programmer has installed. We can’t spread these out over the system; otherwise, the interpreter would have to look through every file on the computer just to find one library. If all libraries are in one location, the scope of the search for the library is reduced drastically. We save them in the `pylibraries` directory, which, in turn, is located within the `data` directory. 

However, now that the FLT file is created, it currently only exists in the computer's storage with no way to read or write to it within the interpreter. Just as we had to read the instructions file in level one of the interpreter, we must now create a function that lets us load the FLT file's content into RAM. Additionally, it should be loaded into a format we can easily work with. We will use a dictionary to store the FLT as they make retrieving specific pieces of information simple. We can make use of the JSON library to work with the file easily. We effectively just read the contents of the file and have the JSON library turn it into a dictionary, which we then save to the `flt` variable:
```Python
def loadFLT() -> dict:
    try: 
	    # The flt is always stored in .nobash, which,
	    # in turn, is stored in the user's home
	    # directory. Because this directory
	    # changes from user to user, we can 
	    # use expanduser() to automatically
	    # give us the current user's home
	    # directory (e.g: "/home/alice" or 
	    # "/home/bob"). We then add ".nobash" to the 
	    # end of that to retrieve the full location
	    # of the FLT (e.g: "/home/alice/.nobash/functionTable.json")
		fltLocation = path.expanduser("~")+"/.nobash/functionTable.json"
		# we can then open the flt at that location
		# and save the file in the variable "file"
        with open(fileLocation, "r") as file:
            # Finally, we can run the json.load()
            # function on the file, automatically
            # turning the JSON file into a dictionary
            # for us. We can then return this.
            return json.load(file)
    # If something goes wrong, such as the
    # FLT not existing for some reason, 
    # we need to raise an error.
    except Exception:
        errors.error(41, "~/.nobash/functionTable.json"])

# Inside of the main program, we can 
# save the FLT in the "flt" variable
flt = loadFLT() 
```

As for the functions pertaining to getting data out of the FLT: We need two functions to store new NoBash and Python functions, respectively. These functions don‘t take in individual functions and add them to the FLT one by one. Instead, the variant responsible for NoBash functions takes in the entire function section of the instructions file. It will then load every function defined in there all at once. When you want to load a Python function called `foo()`, the interpreter instead loads every function contained in the library, which `foo()` is from. `foo()` will be one of these functions as well. You can only ever import entire Python libraries and can‘t pick and choose to only import certain functions from a library. As for NoBash, all functions must be known once the instruction file is created. Once we have added the functions from the function section to the FLT, we will never need to add more NoBash functions again, as you can‘t dynamically import NoBash functions on the fly during interpretation. For this reason, having the NoBash-related function only add functions that are stored in the functions section initially is enough. 

NoBash functions, which are written by the programmer, are added to the FLT as follows:
1) First, every function definition is iterated over in the section:
   ```Python
def addNbFunctions(functions):
	# Go through every function defined 
	# in the functions section
    for func in functions:
	    [...]
   ```
2) Its name is then added as a key to the FLT dictionary, with the corresponding value being a new dictionary. If we look at a NoBash function definition, we can tell that the function name is always the first value and its starting instruction the second: `name, instruction, arg1, arg2, ...`
   ```Python
def addNbFunctions(functions):
    for func in functions:
	    # Function definitions must contain
	    # the function name and starting instruction.
	    # A function definition not including 
	    # at least two values is therefore invalid
        if len(func) < 2:
            error(10031)
        # The function name is defined at the first
        # position of the function definition. 
        # When we tokenized all values, this included
        # the tokens in function definitions. The
        # name of the function was saved in the 
        # "value" attribute when it was tokenized
        funcName = func[0].value
        # We can now create a new entry in the FLT
        # using the function name. For now, we set
        # the value to be an empty dictionary.
        flt[funcName] = {}
   ```
3) This dictionary then stores all the details of the function. The starting instruction number and the language (this being "NoBash" here) the function was written are both stored here. Any potential arguments‘ names are also stored in a list:
   ```Python
def addNbFunctions(functions):
    for func in functions:
        if len(func) < 2:
            error(10031)
        funcName = func[0].value
        # We save the language of the function to
        # be nobash. The instruction which the 
        # function starts on is at the first index
        # of the line definition, so we can extract
        # it using func[1]. We can then save it
        # under the "line" key.
        flt[funcName] = {"language":"nobash", "line":func[1]}
        # If the function definition is longer than
        # two, the remaining values must be parameters
        # which the function expects. 
        if len(func) > 2:
        # We can add another key "arguments"
        # to the dictionary of the current function.
        # It holds a list which, in turn, 
        # contains all these parameters defined
        # after the instruction number
            flt[funcName]["arguments"] = [ parameter.value for parameter in func[2:]]
   ```
Python libraries and the functions they contain are added differently:
1) The function `importPyLib` imports the library so that we can access and run the functions it contains. Normally, libraries are imported in Python by writing "`import library`". We cannot do this here, as the library name will always change and is stored in a string. We will, therefore, need to use a different method to import libraries, which accepts the library's name in the form of a string.
  ```Python
  def importPyLib(libName, location):
    try:
	    # First, we add the home directory of
	    # the current user to where the libraries
	    # are stored (e.g: "/home/alice/.../libary.py")
        location = path.expanduser(location)
        [...]
        # The import_module function allows us
        # to import a library using its name 
        # as a string. The imported library
        # is returned as an object and stored
        # in the lib variable.
        lib = importlib.import_module(libName)
        [...]
    # If something goes wrong, we must raise an
    # error
    except Exception as e:
        error(74, [libName, e])
  ```
2) This library is then stored in an object. We must store this object so that we can call functions from it later. We will use the `pyLibs` dictionary to do this.
   ```Python
   def importPyLib(libName, location):
    try:
        location = path.expanduser(location)
        [...]
        lib = importlib.import_module(libName)
        # We then store the library in the pyLibs
        # dictionary. As a key, we use the libraries
        # name. The library object is stored as
        # the value.
        pyLibs[libName] = lib
    except Exception as e:
        error(74, [libName, e])
   ```
3) We can then go through every function defined in the imported library and add it to the FLT. As with the NoBash functions, we will use the function's name as a key and a new dictionary as the value. Inside the dictionary, we will store that the function was written in Python and the name of the library it originates from.
   ```Python
def addPyFuncs(libName):
	# libName contains the library's name
	# We, therefore, get the library object
	# out of the pyLibs dictionary and save
	# it in the "module" variable
	module = pyLibs[libName]
	# We then go through every function in the
	# library. We save the function's name in 
	# "name" and the function object in "obj"
    for name, obj in inspect.getmembers(module):
        # These two checks make sure that 
        # what we are adding to the FLT is
        # actually a function, as variables defined
        # in the library are also returned in
        # getmembers.
        if inspect.isfunction(obj) and inspect.getmodule(obj) == module:
	        # Finally, we add the Python
	        # function to the FLT. We store
	        # the name of the library it comes from
	        # under the "file" key.
            flt[name] = {"language":"Python", "file":libName}
   ```



## Iterating over instructions (Level 9)
At this point, we have concluded all preparations needed for executing the instructions and, thereby, running the actual script the programmer wrote. In order to do this, however, the interpreter needs to know which instructions to run in what order. This is not quite as simple as running one instruction after another all the time. Functions, conditions, and loops all change which instructions should be run next very frequently. In this level, we, therefore, need to construct a robust system that will not break easily but is still flexible enough to jump around to any other instruction when required to do so. 

The system NoBash uses was heavily inspired by the assembly "language". In assembly, the RIP (instruction pointer register) can be thought of as a "variable" used to point the program to the next instruction to be executed. As an example, we would typically execute one instruction after the other, so the RIP would keep incrementing to point to the next instruction in line. However, in special cases, such as jumping to and from functions, jumping back to previous instructions in a for-loop, or skipping over instructions when a condition is not met, we may want to have the RIP point to a very different location that is not just an increment over the last instructions location. We can use this same principle to do the same in NoBash, with some minor tweaks. For example, we do not use our RIP to point at a memory region where the next instruction is held, as the Python interpreter does this for us already. Instead, we will have it hold the instruction number of the instruction to be executed. When a NoBash function is called, we can then use the previously designed function-lookup-table to see what instruction number it starts at and set the RIP to this value, essentially jumping through the code. If we are simply running functions without needing to jump anywhere in the instructions, we can increment the RIP to the next instruction to progress in a linear manner. In this level, we will also need to create a system that iterates through instructions using the FLT and stores any necessary data for the current function in a variable.
  

This level, although very important, does not require a lot of code. We must create a "RIP" and a function that runs in an endless loop. Inside the loop, we first run whatever instruction the RIP is pointing at and subsequently increase the RIP to point at the next instruction. Executing functions and thus jumping to arbitrary locations is beyond the scope of this level, so we will only increment the RIP by one for now. Looping indefinitely, we grab the information stored in the FLT for the current instruction. If the instruction number is impossible, like being smaller than zero or is larger than the list of instructions, we must throw an error. 

Last but not least, there is one last complication we must fight with. Let us imagine a scenario in which a function is called, so we set the RIP to its starting location. Once we are done executing the function, we must jump back to the line the function is called from, but the old RIP containing this information has been overwritten by now. We can solve this issue by turning our RIP into a list and letting it carry several locations at once. When we want to jump into a function, we can add the new location to the end of the RIP list. The interpreter will check the last item of the RIP and move into this function. When we reach the end of the function indicated by a call to `__funcReturn__`, we may remove the last element of the RIP. This will put us right back to where the function was called. Here is an example of this:
```Python
# Instructions:
0, 1, add, 1, 2
1, 2, jumpToMe
2, 3, put, "Back to the main program!"
3, 4, __exit__ # Everything after __exit__ is the function
4, 5, put, "This is in the function"
5, 6, __funcReturn__

# We first run add(). After that, we increment the
# RIP from instruction 0 to 1.

# We arrive at jumpToMe:
1, 2, jumpToMe
# At this point, the RIP contains only "1" as we are
# at the instruction number one:
RIP = [1]
# jumpToMe starts at instruction 4, so we add 4
# to the end of the RIP:
RIP = [1, 4]
# The interpreter sees that the last item in the RIP
# is 4 and jumps to that location:
4, 5, put, "This is in the function"
# It will run the instruction and output:
"This is in the function"

# It will increase the last item of the RIP by one,
# bringing us to __funcReturn__:
RIP = [1, 5]
5, 6, __funcReturn__
# funcReturn must only remove the last item from the RIP:
RIP = [1]
# Additionally, it increments the currently last 
# item by one:
RIP = [2]
# This leads to the correct instruction after
# the function call:
2, 3, put, "Back to the main program!"
# The interpreter runs this and outputs:
"Back to the main program!"
```

If we need to change the RIP in any other case, even when we jump around during a loop or skip instructions if a condition is not met, we only change the value of the last RIP element. During each execution cycle, we take the last element of the RIP list and use that as the current instructions number.


The very first step here will be creating the RIP. We will store the multiple instruction numbers within a list, so we can initialize the RIP to be a list with a `0` inside of it, as we always want to start with the first instruction (which has an instruction number of zero). Circular imports might be a small issue that could arise. The entire NoBash project is not one big Python file but several files. One file, `A`, may contain code related to running functions, and another file, `B`, is dedicated to error handling. When something goes wrong during function execution, `A` requires the functionality stored within `B`. `A` will, therefore, import `B`, thereby getting access to its functions. This is typically no problem. When `A` imports `B` and `B` imports `A`, however, we have created a "circular import". File `A` needs file `B` to run and vice versa, creating a metaphorical gridlock. Multiple files require access to `RIP`, so in order to avoid circular imports, we must store the RIP in a file that does not import anything else. We will call this file `globalSGT.py`. 

We first create a new file and initialize the RIP in it:
```Python
RIP = [0]
```
Once this is done, we must create two functions that are key to having the RIP work correctly: `lastRIP` and `advanceRIP`. The first function simply checks to see if the RIP list is not empty and returns the last element or throws an error accordingly. This function will always be used to get the last instruction number from the RIP:
```Python
def lastRIP():
	# If the RIP is not empty...
    if len(RIP) >= 1:
	    # ...return the last item in the RIP
        return RIP[-1]
    # If the RIP is empty, we must error
    error(51)
```
The `__advanceRIP__` function takes in three arguments: the RIP before the current instruction was executed, the RIP after the instruction was executed, and the amount of all instructions. If a function was called, then the RIP would have changed from its previous value before the instruction was executed. In this case, the RIP was changed already to the start of the function, and the RIP does not have to be changed by `__advanceRIP__`. If, instead, the RIP remained the same, then no function was called, and we can increase the last value of the RIP by one to progress to the next instruction in order. As another error check, we also make sure that we don't try to set the last RIP value to an instruction that does not exist. This is to prevent us from jumping to the 20th instruction in a 10-instruction-long program:
```Python
# prevRIP = the RIP before the instruction was ran
# instructionsLen = how many instructions there are
# RIP = the current RIP after the instruction was ran
def advanceRIP(prevRIP, instructionsLen, RIP):
	# if the RIP remained unchanged...
    if prevRIP == RIP:
	    # increase the last RIP by one. No function
	    # was called and we can safely move to 
	    # the next element
        RIP[-1] += 1
    # If the last RIP is now greater than the length
    # of the instructions list, it points to an 
    # instruction that does not exist
    if RIP[-1] >= instructionsLen:
	    # In this case, we should throw an error.
        error(1010, RIP[-1])
```
Another two functions we will need are `extractSections` and `getInstruction`. The first function's job is to extract the `instructions` and the `functions` section and store them in individual variables for easier access:
```Python
def extractSections(sections):
	# If there are no instructions to run, like
	# when executing an empty script, we can
	# exit as the interpreter has nothing
	# to do.
    if "Instructions" not in sections.keys():
        sys.exit(0)
    functions, bracesInfo, ifChains = [], [], []
    if "Functions" in sections.keys():
        functions = sections["Functions"]
    if "BracesInfo" in sections.keys():
        bracesInfo = sections["BracesInfo"]
    if "IfChains" in sections.keys():
        ifChains = sections["IfChains"]
    # If each section exists, return it. Otherwise
    # return an empty list instead
    return sections["Instructions"], functions, bracesInfo, ifChains
```
The second function gets the last element from the RIP (so, the next instruction's number) and returns the instruction with that instruction number:
```Python
def getInstruction(instructions):
    if instructions:
	    # We get the last value in the RIP
	    # by calling lastRIP, which we defined earlier
        lastRip = lastRIP()
        # If the RIP points to a valid instruction...
        if lastRip < len(instructions):
	        # return that instruction
            return instructions[lastRip]
        # Otherwise, error
        error(1021, [len(instructions), lastRIP])
    # If there are no instructions, we must error
    error(52)
```

We now create a new function, `getDetails`, which formats the instructions more nicely. Currently, the arguments of an instruction are listed at the end like so:
`[0, 0, test, arg1, arg2]`
`getDetails` will take these arguments, put them into a list, and store that list at the end of the instruction like this:
`[0, 0, test, [arg1, arg2]]` 
This format will be easier to work with, as we can be sure that the fourth item in an instruction will always be a list of arguments. Previously, it was a bit more difficult to determine how many arguments (if any at all) an instruction contained. Here is the code of the function:
```Python
def getDetails(instruction):
	# If the instruction list does not contain at 
	# least three items, it is formatted wrong
    if len(instruction) < 3:
        error(63, [instruction[0], len(instruction)])
    # Save the first instruction number, line number
    # and function name in the details variable.
    details = [instruction[0], instruction[1], instruction[2]]
    # Some function names that NoBash uses are not
    # allowed by Python. replaceBuiltins exchanges
    # these "illegal" names for allowed ones. This
    # lets the programmer use the "illegal" names
    # in their script while Python only ever
    # deals with the allowed names.
    details[2] = replaceBuiltins(details[2])
    # If there are no extra arguments...
    if len(instruction) == 3:
	    # Set the arguments to an empty list
        arguments = []
    # Otherwise, set the arguments variable equal
    # to all items in an instruction after the 
    # third index. These items are all arguments.
    else:
        arguments = instruction[3:]
    # Add the (potentially empty) list of arguments
    # to the end of the new instruction.
    details.append( arguments)
    return details
```

Finally, we create an infinite loop to tie this all together. A script should not run indefinitely, which would normally be the case with an infinite loop. However, we also do not know how often we want to run instructions, as instructions may be repeated in the case of `while` or `for` loops. Instead, NoBash script files have a call to the "`__exit__`" function at the end of them. Once all instructions were run, the `__exit__` function will be run. The function shuts down the interpreter. While the interpreter is running, this while loop is essentially run forever. Inside this loop, we first store the current value of the RIP in a new variable in order to pass this on to the "`advanceRIP`" function, as explained earlier. We can then get the current instruction, get its details in a nice list, and finally increment the RIP by one (with the functionality for making the RIP work with functions already created but not used currently). In later levels, we will add function-execution here as well.
```Python
def runInstructions(sections: dict):
	# Save all the sections in separate variables
    instructions, functions, bracesInfo, ifChains = extractSections(sections)
    # Load the function lookup table
    globalSGT.init()
    # Repeat the instruction-execution cycle forever
    while True:
	    # copy the current RIP while no instruction
	    # has been ran yet
        prevRIP = RIP.copy()
        # get what instruction we have to run now
        instruction = getInstruction(instructions)
        # get all info about the current instruction
        # out of the function lookup table
        instNbr, lineNbr, funcName, parameters = getDetails(instruction)
        # Call advanceRIP to advance the RIP
        advanceRIP(prevRIP, len(instructions), RIP)
```

  
## Python function execution (Level 10)

NoBash does not perform any meaningful calculations itself. Things like input/output or math are instead calculated by the Python interpreter, which, as it is written in C, in turn has C complete these calculations. In the same way that Python passes off its code execution to C, NoBash passes that off to Python. In a previous level, we created a system that imports Python libraries and adds any functions defined within them to the FLT. This means that half of the work is already done for us in this level, as we now only have to check for the function to be executed in the FLT and call it from the library it was defined in, passing any parameters specified beforehand. The only caveat here is that we must first figure out whether the function to be run is written in NoBash or Python. 

  

As a first step, we will create a system that detects whether a function is written in Python or not, as this level is only meant to run Python code. Thanks to level 9, we already have the name and parameters of the function to run. We can retrieve the library object that the function is stored in, get the function object from within that library, and store this in a variable. We can then execute the function and finally save any values that the just-executed function returned back, though we will implement a proper system for returned variables in the next level. 

  

As a very first step, we will create a `isPyFunction` function, which tells us whether a function with a given name was written in Python or not. In this function, we first check whether or not a function with that name exists. If it does, we look it up in the FLT, which gives us a lot of information, including what language it was written in. Using a simple `if`
condition, we can then return `True` or `False`, depending on whether the language was Python or not:
```Python
def isPyFunction(functionName):
	# Only continue if the function is stored
	# in the FLT.
    if functionName.value in flt.keys():
        try:
	        # If the language of the function is
	        # Python...
            if flt[functionName.value]["language"] == "Python":
	            # ... return True.
                return True
            # if it was written in NoBash, return
            # False
            return False
        except Exception as e:
	        # If something went wrong while
	        # looking up the function in the 
	        # FLT, raise an error
            error(1001, [functionName, "language"])
    else:
	    # If the function is not stored in the FLT,
	    # throw an error
        error(72, functionName)
```

Once we have established that we are working with a Python function, we must retrieve the Python library's object from the `pyLibs` dictionary, which we have previously defined in level 8. The library's object is stored with its name as a key. The name of the library can be retrieved from the FLT. The interpreter can, therefore, look up the function in the FLT to get the library's name, which can then, in turn, be used to get the library object from the `pyLibs` dictionary:
```Python
def getFuncLibraryName(funcName):
    try:
	    # Get the data on a function from the FLT.
	    # From this data, get the name of the 
	    # library it was defined in. Store in the
	    # name in "libName"
        libName = flt[funcName.value]["file"].replace(".py", "")
    # If something went wrong, throw an error
    except Exception as e:
        error(1001, [funcName, "file"])
    # return the library's name
    return libName



def getFuncLibrary(funcName):
	# get the library's name from the function
	# we just defined above
    libName = getFuncLibraryName(funcName)
    # if the library is stored in pyLibs...
    if libName in pyLibs.keys():
	    # get its object out of pyLibs and return it
        return pyLibs[libName]
    # If the library was not found in pyLibs, throw
    # an error
    error(1002, libName)
```

Once we have the library, we can use the built-in function `getattr`, which retrieves the function object from a given library object and the function's name. We can store this function object in a variable "`func`" and call it using "`func()`" assuming that there are no arguments being passed. This can be visualized using the following example:
```Python
# In this Python code example, we first get the 
# function "hello" from a library and then execute it 
# on the next line. In this example, the variable 
# "lib" contains the library's object
func = getattr(lib, "hello")
func()
``` 


If we do end up passing arguments, we must watch out. Since we have all arguments stored in a list, it would not be too far-fetched to pass them to the function as follows:
```Python
# Problem:
func("argument one", "argument two")

# Wrong:
arguments = ["argument one", "argument two"]
# Here, we are not passing each value as an
# individual argument, but we are passing a list
# as one argument instead.
func(arguments)
``` 
However, instead of performing `func(a, b, c)`, we would actually call `func([a, b, c])`. This means that instead of passing three arguments, we instead pass a list with three items inside, which is not the same. We can solve this by "unpacking" the list of parameters. This can be done by prepending an asterisk ("\*") to the list. Unpacking allows you to assign each item of a list to multiple variables at once. Here is the previous example finished with the "correct" solution:
```Python
# Correct:
arguments = ["argument one", "argument two"]
func(*arguments)

# This is equivalent to:
argumentOne = arguments[0]
argumentTwo = arguments[1]
func(argumentOne, argumentTwo)
```

Because we are calling a Python function, we can return whatever the called function returned back to the `runInstructions` function. If a programmer does not specify a value a function should return, it returns `None` automatically. Because of this, functions always return something, so NoBash does not have to check whether or not a function returns anything. It can just pass on the return value, which will not cause any errors as there will always be one, either `None` or one specified by the programmer. Here is the `callPyFunction` function, which will tie everything we did in this level together:
```Python
def callPyFunction(functionName, arguments):
	# Get the libraries object first
    lib = getFuncLibrary(functionName)
    try:
	    # Try to get the function object out
	    # of the library as shown before
        func = getattr(lib, functionName.value)
    # If the function is not in the library,
    # we should throw an error.
    except Exception as e:
        error(73, [...])
    
    try:
	    # If there are no arguments in the instruction
        if not arguments:
	        # pass no arguments to the function
	        # definition
            retVals = func()
        # If there are parameters expected...
        else:
	        # Pass the arguments to the function
            retVals = func(*arguments)
        # Return what the function returns
        return retVals
	# If something went wrong while running
	# the function
    except Exception as e:
	    # If an incorrect amount of arguments was 
	    # passed, throw that error
        if len(arguments) != len(signature(func).parameters):
            error(81, [...])
        # But if something went wrong in the function
        # itself, we should save what Python says 
        # went wrong in the variable e. We can then
        # output variable e.
        error(8000, e)
```

  

## Returned values (Level 11)
In this step, we are essentially creating the basics of a variable system. A line in a normal NoBash script may look as follows: "`put(add(1, 2))`", where `add(1, 2)` returns 3, and this result is output to the screen. By breaking this statement up into instructions, we would have something like this:

```Python
0, 1, add, 1, 2
1, 1, put, RET0 
```

In this case, `RET0` stands for anything that is returned by the instruction number zero. This removes a lot of difficulties as we can now simply execute one instruction at a time without worrying about what function should be executed first and where the returned values should be passed on to. This is the system that NoBash uses, as limiting oneself to one function call per instruction is easier to denote syntactically and easier to work with on an interpreter level, at the cost of making the compiler slightly harder to create. What we still need are two things: 
- A system to store the returned values from a given instruction:
  ```Python
  # Instruction:
  0, 1, add, 1, 2
  
  # We need to store 3 in ret0 when add returns it:
  ret0 = add(1, 2)
  ```
- A system that replaces the reference to a return value with the actual value that was returned during execution. 
  ```Python
  0, 1, add, 1, 2
  1, 2, put, ret0 
  # Put should not literally output "ret0", but should
  # instead output what was returned in instruction
  # zero:
  1, 2, put, 3 # ret0 was exchanged with 3
  
  ```

It must first be made clear that this level applies to both NoBash and Python function executions. Additionally, NoBash *does* support unpacking (this would be valid and work as expected: `a, b, c = return123()` where `return123` returns `1, 2, 3`). However, this only works when explicitly declaring variables like shown above using an `=` character. A function `foo` that accepts two arguments can't only accept a function call to a function `fee` as a sole argument, even if that function returns two variables. 

```go
func foo(a, b) { // foo accepts two arguments
	[...]
}

func fee() {
	return 1, 2 // fee returns two values
}

// This would not work
foo(fee())

// This would work:
a, b = fee()
foo(a, b)

```

This would not work, because, under the hood, fee returns a list. This makes the call to `foo` be `foo([1, 2])` with parameter `b` being unaccounted for. However, following up with this example, this would work: `a, b = fee()` because the values returned by fee would be unpacked. This is comparable to writing `a, b = list(1, 2)`

  
To begin this level, we first create a new dictionary to store variables in, including the returned value variable (RVV):
```Python
vars = {}
```
The first function we must make is one that sets a value in this variables dictionary to the corresponding key. In this case, the key is the variable's name, and the value is the actual value of the variable. This lets us easily look up the value of a RVV:
```Python
def setVar(varName, varVal, [...]):
    [...]
    # Inside of the vars dictionary, we set save
    # the value under the variable name
    vars[varName] = varVal
```
As a quick reminder: RVVs are always set up as follows: `ret#`, where `#` is the number of the instruction that returned the value. We can now create a second function that handles creating the RVVs following this format:
```Python
def setRetVars(varVal):
	# If there is no value being passed, do
	# nothing
    if varVal == None:
        return
    # The RVV is composed of "ret" and the number
    # of the instruction which was executed. This
    # is stored in the last entry of RIP
    varName = "ret"+str(RIP[-1])
    # We can now create a new variable with the 
    # RVV as a name and the returned value as the
    # value
    setVar(varName, varVal, [...])
```
As previously described, multiple return values are automatically stored in a list. This list is then returned and stored as an RVV. As for replacing RVVs passed as arguments with their actual values, we must create a new function that takes in all arguments. It then checks whether an argument is actually variable, and, if so, replaces it with its actual value. Here is a visualization of the process:
```Python
# Instruction:
0, 1, add, 1, 2
1, 2, add, 3, ret0

# The arguments are passed to the function:
3, ret0

# The function now checks whether any argument
# is a variable (thereby also an RVV):
3, ret0
#  ^^^^  variable spotted

# The variable is then replaced with the proper value
3, 2

# The arguments are then sent back to the instruction:
1, 2, add, 3, 2
```
This is done by the `replaceVars` function, which is a bit more complicated than the other functions. First of all, it takes the list of arguments and the function's name as an argument. At the very beginning, we initialize a variable `newArgs` and set it equal to an empty dictionary. `newArgs` will contain all the new arguments, in which the variables were converted into the values they represent. The function then iterates through all arguments and checks whether their type is "`variable`". If so, we call the `getVar` function (that we will create next) and pass the variable as an argument. As its name suggests, the `getVar` function returns the value being represented by whatever variable was passed on to it. We then append the value of the variable or the original argument to `newArgs`. Additionally, we will run into problems when replacing the variables in the arguments of functions like `__setVariable__`. Here is an explanation of why this could cause issues:
```Python 
# ___setVariable__ is the function equivalent of =

x = 2
# is turned into
0, 1, __setVariable, x, 2

# We can't replace the first argument passed to 
# __setVariable__. The variable "x" does not exist, 
# but we are currently in the process of creating it.
# We must therefore not attempt to replace variables
# in arguments if the function in question is 
# responsible for setting the variable.
```
We can get around this problem by adding a `start` counter. If the arguments are being replaced for a function that is meant to set variables, we can tell `replaceVars` not to replace variables that may just be defined. `replaceVars` will only replace arguments past `start`. If the first argument might be a new variable, we can set `start` to two. This will force the interpreter to only replace arguments two and onward. Here is the code:
```Python
def replaceVars(arguments, funcName):
	# newArgs will contain the new arguments for now
    newArgs = []
    [...]
    # We set start to -1, effectively disabling it
    # for all functions by default
    start = -1
    # This list contains functions which require
    # start to be set to one, thereby skipping
    # the replacement of the first variable
    noReplaceList = ["__doFor__", [...], "__setDivVariable__"]
    if funcName.value in noReplaceList :
        start = 1
    # Because there may be several variables
    # to the left of a '=', we need to only
    # replace the last argument
    elif funcName.value == "__setVariable__":
        start = len(arguments) - 1
    # We then go through every argument to be passed
    for indx, arg in enumerate(arguments):
	    # If the argument is a variable and we
	    # are past potential new variables to
	    # be declared just now...
        if arg.type == "variable" and indx >= start:
	        # we can replace the argument with its
	        # value. getVar will be defined later.
            arg = getVar(arg)
        # If the argument was a variable, we add the
        # proper value to newArgs. Otherwise we can
        # add the argument as it was before
        newArgs.append(arg)
    return newArgs
```
We still need to implement `getVar`. It will be responsible for getting the respective value from a variable. As already mentioned, it accepts one argument, this being the variable as a token. We then check whether or not the name of the variable is stored in the `vars` dictionary as a key. If it was, we return the token that the variable's name was pointing to. If it was not, the programmer was attempting to use a variable that they had not declared before. In that case, we must throw an error:
```Python 
def hasVar(varName):
    # hasVar works slightly differently
    # to what is shown here. This will be further
    # described in the next level. For now, 
    # this level of hasVar will suffice
    [...]
    # We check whether the variable name is
    # a key in "vars", "proving" that it is a 
    # variable.
    if varName.value in vars.keys():
	    # If the check succeeds, we can
	    # return the variables value and
	    # True. The "True" indicates that
	    # a variable with the given name
	    # exists.
	    return vars[varName.value], True
	# If the variable is not in vars, it is
	# also not a variable defined already.
	# We must therefore return None and False.
	# The "False" indicates that the given value
	# is not a variable
    return None, False

def getVar(varName):
	# We first call hasVar to confirm that the
	# variable we must look up exists. It will
	# also give us the variables value.
    value, exists = hasVar(varName)
    # If the variable exists...
    if exists:
	    # We may safely return its value
        return value
    # If it does not exist, we must throw an error
    # as the programmer tried to use an undefined
    # variable
    error(101, varName)
```


## Nobash function execution (Level 12)
In level 11, we have established that Python function calls lie at the core of NoBash. However, we still need a way to execute functions in NoBash. This is the goal of the current level. Because we have already built the RIP system with functions in mind, a lot of the work for the current level is done already. However, there is a new concept that we will build into this level. Specifically, we will create"scoping". Let's take the following example:

```go
func foo() {
	x = 10
}

foo()
print(x)
```

Programming languages that feature scoping (such as Python) will crash upon attempting to execute the code above. When we created the variable `x` in function `foo`, `x` can only be accessed from within this function. In most interpreted languages, as soon as `foo()` finishes running, the variable will be deleted. This means that `print(x)` will fail, as the variable was limited (or "scoped") to `foo`. 

The last bit of added complexity is the following: variables are not only scoped to a function but to a specific instance of it, meaning that even if you call the same function, variables are scoped to the specific call of the function, not to the function as a whole. This is important, as when a function calls itself, we don't want the function to use the same value for a variable defined within it across different calls. Instead, we want it to have variables (even though they have the same name) to hold separate values independent of one another. 

So, our goal for this level is not only to implement a system that simply jumps to the right location within our instructions. Instead, we also want to have a scoping system that tells us both what function and what instance of the function we are currently in.


Similarly to level 11, our first step is to establish whether the function was actually written in NoBash or not. Because we have stored this data in the FLT in a previous level for this exact reason, we now don't have to write as much code. If we *are* dealing with a NoBash function, we first retrieve the number of the instruction it starts at. We can then append this to the RIP list to jump to this position during the next execution cycle. As a reminder, the interpreter will execute whatever instruction is listed at the end of the RIP. The next step would be to implement passing arguments to NoBash functions, but we need to first create the scoping system described earlier to enable this. Just like the RIP, we must create a scope list that we can add and remove functions from. Because the systems are so similar, we will call this list `funcNameRIP`. We also need a way to differentiate between the different instances of a function. We can now pass the scoped arguments to the NoBash function. First, we run some checks, like whether the function definition actually has parameters defined and whether the programmer has passed the correct amount of arguments. If all of these checks pass, we must now create the parameter as a variable. We can do this by creating a variable like usual. We can use the parameter for the variable's name. The value of the variable is the value of the argument being passed. We must also create a function that lets us return and automatically store returned values in an RVV.


We first create a function "`isNbFunction`", which takes the function's name as a parameter. If the function is found in the FLT and information on its language is stored, we can now run an `if` check on whether the function's language is equal to `"nobash"` and return the result as a boolean:
```Python
def isNbFunction(functionName):
	# Continue if the function is actually
	# stored in the FLT
    if functionName.value in flt.keys():
        try:
	        # If the language saved under the function
	        # is NoBash, we should return True
            if flt[functionName.value]["language"] == "nobash":
                return True
            # If the check did not pass, the function
            # was not written in NoBash. We should
            # return False in this case.
            return False
        # If something went wrong in the previous
        # three lines of code, we should raise
        # an error
        except Exception as e:
            error(1001, [functionName, "language"])
    # If the function is not in the FLT something went
    # wrong and an error should be reported
    else:
        error(72, functionName)
```
We then create a function called `callNbFunction`. If the previous check evaluated to `True`, we pass it the function's name and its parameters. We then look up the function's name in the FLT and store the instruction number at which the function starts. Now the instruction number is appended to the RIP and the functions name to the `funcNameRIP`. 
```Python
def getNbFuncLine(functionName):
	# Given a NoBash function's name, we look
	# up what instruction it starts at. This
	# info is saved in the FLT, making it trivial
	# to access
    return flt[functionName.value]["line"]

def callNbFunction(functionName, parameters):
	# We retrieve the instruction number
	# the function starts at
    line = getNbFuncLine(functionName)
    # Add the first instruction's number to
    # the end of the RIP
    RIP.append(line.value+1)
    # We will implement addToScope next. It will
    # be responsible for scoping variables correctly
    addToScope(functionName)
```

However, we are now still faced with the challenge of needing a way to differentiate between the instances of a function in the `funcNameRIP`. Consider the following example:
```go
func addOne(end) {
	if end == true {
		x += 1
	}
	x = 0
	addOne(true)
}

addOne(false)
``` 
When the function `addOne` is run for the first time, `end` is `false`. It will then create a new variable, `x`, and set it equal to `0`. The function then calls itself but sets the `end` argument to `true`. Now, in a programming language that does not consider "function instance scopes", `x` would be incremented by one. In this scenario, `x` was created when the function was called for the first time. Additionally, when the second function is called the second time, it can access the variable from when it was created in the first instance. This can potentially create bugs if the programmer is not aware that the language does not feature scoping (which could be seen as reasonable as many popular programming languages do have it). Additionally, bugs originating from this misunderstanding can become very tricky to debug. If the programming language does feature function instance scoping, this program will throw an error. When `x` was created, this was done in a different instance of the function, and therefore, the second instance has no knowledge of its existence. Even though this results in the program crashing, this is beneficial. The crash is caused by the variable being scoped to a different instance. In the other scenario, the program would not crash, but it would presumably not function properly. This malfunctioning would be harder to trace back to the scoping as the missing crash does not deliver valuable information about the problem. Having values "transcend" their instance into subsequent ones can be useful sometimes, but this can also be done by passing it as an argument.  

NoBash solves this problem by scanning the `funcNameRIP` for other calls to this same function and incrementing a number attached to the end of the name for every additional call to the same function. Calling a function `foo` twice would make the `funcNameRIP` look like this: `["main", "foo0", "foo1"]`. `main` is not a function. Instead, it represents the global scope, the part of the code outside of any functions. The current instance is always at the end of the list. This way, variables created in the second instance of `foo` would be saved in the `vars` dictionary under the `foo1` scope. Instead of saving variables to the vars dictionary directly (e.g: `{"x": 1, "y": 2}`), we now save them under their respective scope in the `vars` dictionary (e.g: `{"main": {"x": 1}, "foo": {"y": 2}}`). When we try to access variables in the future, we will try to look for the variable in the current scope. This is stored at the end of the list. If a variable is created in the first instance of the function `foo`, it will correspondingly also be saved under the scope `foo0`. When a second instance of the function is created (`foo1`) and the variable needs to be accessed, the interpreter will only search for it in the scope of `foo1`. The code responsible for dealing with scopes is the following:
```Python
# This function will create a new scope name to
# be added to funcNameRIP when a function is called
def newScopeName(funcName):
	# First, set the counter to the zero
    counter = 0
    # We then go through all scope names in the
    # funcNameRIP
    for oldFuncName in funcNameRIP:
	    # if the scope is for the same function
	    # as will be called now, we can increment 
	    # the counter by one. Counter therefore
	    # holds how many instances of the function
		# to be called already exist
        if oldFuncName.startswith(funcName.value):
            counter += 1
	# We can then create a new scope name. It consists
	# of the function's name and a unique ID at the end
	# This unique ID serves to discern the different
	# instances.
    return funcName.value+str(counter)

# This function will add a new instance of a 
# function to funcNameRIP, thereby creating a new
# scope
def addToScope(funcName):
    funcNameRIP.append(newScopeName(funcName))
```

Now, we check whether or not the programmer tried to pass any arguments. If they didn't, we check whether the function expected any arguments to begin with. This can be done by checking the list of parameters under the "arguments" key specified in the FLT. If the programmer tries to pass an incorrect number of arguments, we throw an error accordingly. If everything matches up, we call a new function called `passNbParameters` and pass the arguments and function name as arguments. It will be responsible for creating each argument's variable in the correct scope. We enumerate all arguments passed together with their index in the arguments list. We then create new variables for each argument and have them scoped to the last entry in `funcNameRIP` (as we have already set that to be the instance of the current function). For the variable's value, we take the argument passed. As for the name, we take the parameter at the same index in the parameters list. In other words, we use the \#th parameter as the name and the \#th argument as the value:
```go
func add(x, y) {
	[...]
}
add(1, 2)

arguments  = [1, 2]
parameters = [x, y]
//           #1  #2

// Argument #1 is saved under parameter #1
x = 1
// The same applies to argument and parameter #2:
y = 2
```
Here is the code responsible for this action:
```Python
# This function handles passing arguments to
# NoBash functions:
def passNbParameters(arguments, scope):
	# The scope argument carries the current
	# scope. In order to look up the functions
	# parameters in the FLT, we need to look
	# up the function name rather than the 
	# scope, which has extra numbers added to the
	# end. This function removes the excess numbers
	# and store the function name in "funcName"
    funcName = getBaseFunctionName(scope)
    # We make sure that the function expects
    # arguments
    if "arguments" in flt[funcName].keys():
	    # We can now extract the parameters list
	    # out of the flt.
        parameters = flt[funcName]["arguments"]
        # if the amount of arguments does not match
        # up with that of the paramters...
        if len(parameters) != len(arguments):
            [...] # ... raise an error
        # If all checks passed, go through all 
        # arguments passed
        for indx, arg in enumerate(arguments):
	        # Create a new variable for each
	        # argument. Each argument is stored
	        # in a variable with it's corresponding
	        # parameter as a name. Additionally,
	        # we pass the scope to setVar. This 
	        # ensures that the variables are saved
	        # in the correct scope.
            setVar(parameters[indx], arg, scope)
    # If the function does not expect arguments, we
    # must throw an error
    else:
        error(91, [len(arguments), 0])
```
If we don't try to pass any arguments, we also run these same checks but don't create any variables. We must make sure that the programmer only passes no arguments when the function in question also does not expect any:
```Python
def callNbFunction(functionName, arguments):
    [...]
    # If the programmer tries to pass arguments,
    # call the function we just defined.
    if arguments:
        passNbParameters(arguments, funcNameRIP[-1])
    # If the programmer does not try to pass
    # arguments, do the following:
    else:
	    # get the function's name
        functionName = functionName.value
        # If there is data on the function regarding
        # what parameters it expects...
        if "arguments" in flt[functionName].keys():
            # Find out what it wants. Perhaps
            # the list of parameters is empty
            reqArgs = flt[functionName]["arguments"]
            # If the function does not expect zero
            # arguments, we must throw an error. 
            # The programmer cannot omit arguments
            # for a function that expects them.
            if len(reqArgs) != 0:
                error(142, [functionName, len(parameters), len(reqArgs)])
```

Finally, we must also address returning out of the function. Several functions are already built into NoBash. One of these is "`__funcReturn__`". When we return multiple values, we store these in a list and return them. So, regardless of how many values the programmer wants to return, we will always only need to create one new RVV:
```go
// This function...
func returnMultipleValues() {
	return 1, 2, 3
}

// How do we store multiple values in one variable?
a = returnMultipleValues()

// Secretly does this:
func returnMultipleValues() {
	l = list(1, 2, 3)
	return l
}

// Now we can store the list in one variable!
a = returnMultipleValues()
put(a) // [1, 2, 3]

// If the programmer tries to store each value
// individually, this also works:
a, b, c = returnMultipleValues()
put(a) // 1
put(b) // 2
put(c) // 2
```
However, we must use the second last `RIP` value as an identifier for the RVV since that is where the function was called from. Similarly, we also don't set the instance of the current function as a scope but instead use the second last scope stored in `funcNameRIP`, since the goal of returning a value is to save it as an RVV of the instruction (in another scope) that called the function. Finally, we remove the last elements from the `RIP` and `funcNameRIP`, respectively, as we want to execute the instructions after the function call and return to the scope of these:
```Python
0, 1, hello        # Hello returns a value
1, 2, put, ret0    # We want ret0, not where the 
# return function was called
```
The code for `__funcReturn__` therefore looks like this:
```Python
def __funcReturn__(*values):
	# If one value is to be returned
    if len(values) == 1:
        try: 
	        # Store that one value in an RVV
	        # without a list. The RVV is composed
	        # of the second last RIP for the 
	        # reason explained above. The same
	        # principle counts for the scope.
            setVar("ret"+str(RIP[-2]), values[0], scope=funcNameRIP[-2])
        # Report an error if something went wrong
        except Exception as e:
            error(1041, RIP[-1])
    # If several values are returned...
    elif len(values) >= 2:
        try: 
	        # Store these variables in a list. Then,
	        # store that list in the RVV instead.
            setVar("ret"+str(RIP[-2]), Token(values, "list"), scope=funcNameRIP[-2])
        except Exception as e:
            error(1041, RIP[-1])
    # Remove the last RIP to jump back to where
    # the function was called
    RIP.pop()
    # Increment the last RIP by one to move to
    # the next instruction after the function call
    RIP[-1] = RIP[-1]+1
    # Then, remove the last scope as that function
    # instance has now been stopped. If that does
    # not work, we must throw an error.
    if len(funcNameRIP) > 1:
        funcNameRIP.pop()
    else:
        error(10051)
```

## Setting Variables (Level 13)

In levels 12 and 13, we have already implemented variables in the form of arguments. However, we still want the programmer to create variables anywhere in their script, outside of passing them as arguments or the RVV system that they can't control. Instead, we must give them a way to manually assign a value to a variable with a name of their choosing. We will accomplish this by creating a function that handles this that they can manually call themselves.
  

The already created the `setVar` function in level 12 has all the required functionality already, but it is not easily accessible outside of the inner workings of the interpreter. Because of this, the instructions file can't simply reference the `setVar` function, which it does not have access to. Instead, we can create a new `__setVariable__` function in `corefuncs.py`, which is always imported to every script. The `__setVariable__` function can act as a publicly accessible proxy and passes any parameters it receives on to the `setVar` function.
  

First, we must import the `setVar` function into `corefuncs.py`. We can then create a new function, `__setVariable__`, which takes in two parameters: The variable's name and the value that should be assigned to it. It then calls `setVar`, which takes the same two parameters and passes the arguments it has received on. If a list is passed into the function, we have to run some special checks. If the programmer wants to save the list in a single variable, we can do so as normal. If, however, the programmer wants to save each value in the list in a separate variable, we must handle that accordingly:
```Python
def __setVariable__(*varsAndValues):
	# Throw an error if we have not received
	# at least one variable name and value
    if len(varsAndValues) <= 1:
        error(249, [...])
    # The last argument passed will always be
    # the variables value. If the programmer
    # wants to save each of a list's items in a
    # separate variable, all arguments up to the 
    # value will be variable names.
    varNames, varValue = varsAndValues[:-1], varsAndValues[-1]
    # If we only have one variable name, save
    # the value under it
    if len(varNames) == 1:
        setVar(varNames[0].value, varValue)
        return
    # If we have several names but don't have a list
    # as a value, we must throw an error. You can
    # only "unwrap" lists in NoBash
    elif varValue.type != "list":
        error(345, [len(varNames), 1, RIP[-1]])
    # If there are not enough (or too many) variable
    # names for each list item, throw an error. Each
    # list item must have one variable name it is
    # stored under.
    elif len(varValue.value) != len(varNames):
        error(345, [...])
    # Finally, save each list item in the
    # corresponding variable name.
    for i, value in enumerate(varValue.value):
        setVar(varNames[i].value, value)
```


## The core functions and core utils (14)
The final puzzle piece missing are functions we can call. After all, what is the point of a programming language if it can't do anything? There will be two types of functions we will need to create. On the one hand, we need the "standard" functions every programming language should have. These include things like addition and subtraction, getting items out of a list, or printing things on the screen. The second type of functions we need are the "core utils". In order to replace Bash, the user must be able to interact with the system as easily as they can with Bash. They can first import the "coreutils" library into their NoBash script. From then on, they can use commands like "ls" or "cd" by calling their respective functions ("`ls()`" or "`cd()`"). In this level, we will create these functions.

Unfortunately, going through every function and discussing how it works would take too long. Instead, we should focus on how these functions work, generally speaking rather than individually. The standard functions typically take an input, transform it, and produce an output. Important to note here is that while the input and output of these functions are tokens, they are turned into traditional Python values to be worked with inside of the functions. After the result is calculated, we can turn that back into a token and return the tokenized value. This ensures that the interpreter only ever deals with tokens and not the standard Python types. The coreutils work by primarily using the functionality of the `shutil` library. This library has implemented a lot of the coreutils already. This means that the core util functions must analyze what the programmer wants to do and call the `shutil` functions accordingly.

Let's go through the creation process of one standard function and one core utility function. For the standard function, we will look at how the `add` function works. When two numbers are passed to the `add` function, we will want the result of a simple addition of the two. When two strings are passed, however, we want to add the latter to the end of the first. For example, `"Hello, "` and `"friend!"` added together would result in `"Hello, friend!"`. The `add` function represents the standard functions well, as we can see tokens being passed as arguments and returned out of the function. Inside of the function, we work with traditional Python values. Here is the code:
```Python
# Add takes two arguments: The value to the left
# of the "+" and the value to the right.
def add(x, y):
	# Numbers can only be of type "int" or "float"
    nums = ["int", "float"]
    # Both values can be integers or floats. NoBash,
    # like many other languages, allows the addition
    # of integers with floats. It is only important
    # that the programmer does not try to add a number
    # to a string.
    if x.type in nums and y.type in nums:
	    # We add the two numbers and return the value.
	    # Before we return it, however, we must
	    # turn it into a NoBash token.
        return Token(x.value + y.value, "float")
    # If both values are strings, we may add them
    # as well.
    elif x.type == y.type == "string":
	    # This time, the Token must be turned into
	    # a string. This is reflected in the last
	    # argument.
        return Token(x.value + y.value, "string")
    # If the values were neither numbers nor strings,
    # they can't be added. This must be reported as
    # an error.
    error(305, [x.type, y.type])
```
A very important core util is the `mv` command. It will accept two arguments, the first one being a file and the second a directory like so: `mv("test.txt", "Documents/")`. It will then move the file to the specified location. Let's look at the code behind the function:
```Python
def mv(source, destination):
	# First, we make sure that the source and 
	# desitination are both tokens. If they are, 
	# we then make sure that they are strings. 
    if isinstance(source, Token) and isinstance(destination, Token) and source.type == "string" and destination.type == "string":
        try:
	        # Using the aforementioned "shutil" 
	        # library, we move the file to
	        # the specified location
            shutil.move(source.value, destination.value)
            # If this succeeded, we can
            # return true. This can be used
            # to determine whether the 
            # movement happened 
            # successfully or not back in the
            # main script
            return Token("true", "bool")
        except Exception as e:
	        # If something went wrong, we 
	        # return false. 
            return Token("false", "bool")
    else:
	    # If either the source or destination
	    # arguments are not strings, we must
	    # throw an error.
        error(8100, "Both source and destination must be of type string")
```

# Reflection
## What went well
Although this is my first big programming project, I find the planning and development of NoBash to have been a success. Previously, I would write only small programs to see my work materialize into a tangible end-product fast. This time, over the course of months, I have managed to complete a much more impressive and complicated challenge than ever before. This was, however, only possible due to good planning. I must thank my Matura referent, Aaron Zeller, greatly for the advice he gave me in the infancy of my language. I had first started programming and planned on writing the chapters for each level afterward. What is not shown here is that I have restarted programming approximately eight times. Each time, I got further than the last attempt, but there was always a significant oversight, which I made at the beginning of each new try. This led to my program becoming increasingly better each time, but creating a product by making mistake after mistake would take too long. Instead, writing all the text, creating a blueprint, and constructing a plan detailing how all systems should work together achieved the same effect as trial and error. Crucially, it did so much faster while simultaneously creating the basis of this paper. 

Not only did planning help a lot, but structuring my code did, too. Although the order of this document would say otherwise, I started working on the interpreter before the compiler. I did this as I felt the compiler would be easier to write, meaning I would finish the hard part of the program first. The order in which I did things becomes apparent when one compares the structure of my code in the compiler with that of the interpreter. The interpreter's code is very messy, and while each level works independently of the others, this is not reflected in the files. Instead, one file may hold the code of multiple levels with the functions inside not being ordered either. Conversely, the compiler is structured very clearly, with nearly every level getting its own file. The `interpreter.py` and `compiler.py` files also differ in orderliness, though this was partially unavoidable. In the compiler's main file, each level is called, and the returned values are saved in a variable and are then passed on to be processed by the next level. This concept of breaking the programs down into levels and feeding the output of one level into another as input was also taught to me by my Matura referent, for which I must also thank him.

The end goal of NoBash was to be a language with a syntax as easy as that of Python but with the tight Linux integration that Bash has. The former condition was achieved as NoBash features a syntax very similar to that of Python, albeit with minor modifications. NoBash also works very well with Linux, as many of the coreutils can be used very easily, and common operations like reading or writing files are also trivial to do. This was possible due to my thorough planning before making the language. I defined what NoBash must do clearly so that I could focus on getting these criteria to work. One thing often overlooked in planning is deciding not only what features the end product should have but also which features are unnecessary. Doing so is very important, as one might otherwise add more and more features during development, delaying the release further and further since there will always be one more thing to add. According to the UNIX philosophy, a set of guidelines for writing good programs, the code should "do one thing and do it well". When more and more features are added to a program, you will pay less attention to the core capabilities it should have, leading to a product that can do many things but can't do any of them well. NoBash, for example, does not feature classes. This is because a simple script to perform tasks like sorting files in a folder does not require such advanced functionality. Instead, the time that would have gone toward creating the unnecessary feature went towards integrating all the important functions a NoBash script may require into NoBash. 

## What could have gone better

Not everything went smoothly. As said in the last chapter, the compilers and the interpreters are structured very differently. The interpreter works the same way as the compiler, though this is not easily seen in the code. While it takes the output of one level and uses it as input in the next, this can only be clearly spotted in the first couple of levels. The subsequent ones are primarily present in the `runner.py` and `varsAndFuncs.py` files. I also stated in the previous chapter that this is only partially my fault. While I could have potentially structured the code better and moved core parts from `runner.py` into `interpreter.py`, the nature of the interpreter differs from most other programs. While those mostly run linearly, the coder controls how the interpreter works in their NoBash script. The interpreter must, therefore, not step through levels one by one but instead use the functionality from any of them as requested by the programmer. In the end, I could have done this better, and the code clarity of the interpreter is not on par with that of the compiler. The upside is that I have already learned from the mistake, as seen in the compiler code. The lesson to be taken from this mistake is to use the aforementioned "levels" system and to break up every level into its own file. 

Retrospectively, another thing I would have done better is look up how other people have solved a problem I had. When I ran into a tricky part that I would have to code, such as level ten in the compiler, I would try to solve the problem entirely by myself with no outside help. While it is good to attempt a complex challenge by yourself first, there comes a point where it is better to look at how other people overcame the same challenge rather than struggle for hours with no result at the end. In fact, seeing various ways to solve a problem can benefit you more than just using your own method all the time. Doing so can broaden your horizons and give you insight into solutions better or more elegant than your own. This teaches you new approaches and mindsets to solving a challenge so that you can apply what you have learned from others in the future when you encounter a similar problem. Simply copying someone else's code is immoral and won't help you become a better programmer. However, reading through and trying to understand someone else's train of thought when tackling a challenge can give the aforementioned result. In the future, when I struggle to come up with my own way of solving something, I will read through other people's approaches to the same problem and try to understand what they are doing and why their method may be better than mine. 


## What could still be improved
If there is one part of NoBash that needs the most improvement, I would have to go with the error systems of both the interpreter and the compiler. Making error systems for any large-scale program is difficult, even more so when it relies heavily on user input. There are an infinite number of unique inputs a programmer could make, each one potentially causing NoBash to work unexpectedly. Finding all of them and creating an error system that deals with them accordingly and properly explains to the user what went wrong is a monumental task. There is a joke in the programming community that no matter how many special cases you prepare your program to handle, the user will always find one you missed. Another problem with handling errors in a script is that a mistake in the programmer's code may only reveal itself further down the line. For example, when an opening bracket is missing somewhere, the compiler can only tell that there is one closing bracket too much. The "error", therefore, is reported to be the extra closing bracket, whereas the coder actually forgot an opening bracket. While there are ways to determine the root causes of such problems rather than only detailing their effects (like an unmatched bracket), it is a lot more challenging to implement such solutions for seemingly endless possible slip-ups a programmer could make. In NoBash specifically, the error system could be improved as sometimes problems are misidentified in the interpreter. That of the compiler can be enhanced by adding more checks, as sometimes erroneous input is compiled without raising an error, with the interpreter then having to report it when coming across the mistake while running instead. In the future, it would be beneficial to integrate the error system into each level so that everything that can go wrong already has a dedicated error mechanism rather than testing the code afterward and finding new issues not addressed by the error-checker.

The speed of the interpreter could also be improved. That of the compiler is not that important as it is only run once. The interpreter, on the other hand, has a few more minor issues. The most glaring issue is that it is written in Python, a notoriously slow language. Python itself, like NoBash, is interpreted, which makes it a lot slower than compiled languages like Rust or C. By having an interpreted language interpret another language, this loss in speed is increased drastically. As stated before, I chose Python because I am most comfortable with it, and it is subjectively faster to do many things in Python than in other languages. If I could go back in time and choose what language the interpreter should be written in again, I would stick by my choice as it has accelerated my productivity tenfold compared to using a language I am only relatively familiar with, like Golang. Another example of inefficiency in NoBash is how it handles strings. The compiler removes strings and inserts them back into the instructions. The interpreter must then remove those same strings from the instructions again to parse them. This is wasteful, as the compiler could not reinsert the strings into the instructions and instead store them in a different section. The interpreter could then read the strings from there rather than perform the same work the compiler does a second time. I did this initially because when the strings are in the instructions rather than only references to them, if an error occurs relating to the strings while programming, it is a lot easier to tell what went wrong. The string is already there, and I would not have to mentally replace a reference to a string with its actual contents and then determine what went wrong. This was shortsighted thinking, which I regret. It is also something that I would undo. These problems can be avoided by thinking ahead and prioritizing having the program work better rather than making my development easier. 

Additionally, I wish I had spent more time testing my code and fixing any potential issues. Currently, there are a couple of problems in NoBash that are yet to be fixed. For example, the compiler will crash when the programmer writes a comment after an opening bracket. Such special cases should be tested from the very beginning and fixed immediately. This also lines up with creating a better error system, as the two are closely intertwined. Such "bugs" can be annoying to the programmer, though they are also to be expected in any and all programs. Even the best programmer in the world can't write bug-free code. They do try to fix them, though. In the future, I should assume that every line I wrote contains at least one bug and test my program accordingly.  

## What am I proud of
The two single most challenging levels I wrote were levels eight and ten in the compiler. Formatting a line in which the programmer can write and structure their code to their heart's content is not easy, as many special cases must be considered when parsing. In total, I spent around half a day working on both of these levels alone. In programming, there is a tool called "regular expressions" (regex), which are helpful for precisely this scenario, as they extract information from strings. Unfortunately, I underutilized them in both levels, using them once because I had never worked with them before. I have since gained some experience working with regex and now realize that I could have halved the development time by learning a little about them and implementing them into my code. Nevertheless, the fact that I have essentially implemented parsing, which is subjectively the most challenging part of making a programming language, all by myself nearly completely without using regex. 

While I am very proud of those two levels specifically, my greatest accomplishment was creating the language itself. It is widely regarded as a tough challenge for a programmer, albeit doable and rewarding. I am proud that due to sheer dedication and good planning, I was able to create one all by myself. It demonstrated that I could do more than my typical programming projects, simple programs that take me a couple of hours to write. I think of myself as a slightly chaotic person. I also have an undying passion for computers and programming, so while the technical feat was something special, I knew I would be able to program what I did from a practical standpoint. It was the dedication and organization I showed that specifically makes me proud. I like to program video games in my free time, only two of which I have ever finished. This project has been a monumental task, but one which I have managed to complete with good planning. It has shown me what I am capable of when setting definitive goals I want to reach and clearly structure my approach. Creating my own programming language has also been a dream of mine since I started programming when I was around 15, which is two years ago now. I am genuinely grateful for the opportunity to combine a goal of mine with the most important work of my school career. 


## What did I learn
The most important lessons I learned were planning ahead when programming and splitting my projects into levels, whereby each level serves as the foundation for the next. I have learned that being a good programmer does not depend on how many programming languages you know or how fast you can write code. Instead, it is dependent on how good you are at organizing your ideas and your code. It depends on your design philosophy and patterns, such as the aforementioned "levels". I also learned that it is good to look at other people's work and to learn from it, integrating other people's thought processes into your own and learning from it along the way. I also discovered that you should prioritize making a good product rather than making the process of creating it easier for yourself. You should test what you made for potential errors while working on it rather than waiting until you are done to catch any flaws before it's too late. Finally, I also learned that it is crucial not only to plan what you want your program to do but also what it should not do. By limiting the scope of your product, you can focus on making what really matters the best it can be rather than creating a million different systems, with none of them working very well. 


  

  

