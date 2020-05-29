# Python

```
Code is read more often than it is written.
Code should always be written in a way that promotes readability.

    - Guido Van Rossum, creator of Python
```

Clean and simple, it is an ideal beginning programming language. Powerful and flexible, it is the primary tool of choice for millions of expert researchers, data scientists, web developers, hackers and more.

In this video series, we will be covering all the basics you need to get started with Python code. By the end, you'll be able to read and write the code to build a simple graphical adventure game:

![Python Game](/00_intro/img/PythonRogue.gif)

## Is this series for you?

Are you a fast learner, new to programming and looking for the shortest path to making cool games? This series is for you.

Are you studying programming in school but bored building todo lists and calculators? This series is for you.

Are you experienced in another programming language but curious about the power, flexibility and fun of Python? This series is for you.

## Installation and Setup

Python is very easy to install and set up. In order to write and run code though, you will need a text editor and terminal.

### Text Editor and Terminal

For text editors, I recommend [Sublime Text](https://www.sublimetext.com/) for Mac and Linux, and [VSCode](https://code.visualstudio.com/) for Windows.

You'll also want to start getting used to your computer's Command Line Interface. Mac and Linux come bundled with the Terminal program by default while VSCode comes with a built-in command line.


### Installing Python

You'll need to have Python 3 installed for this series.

#### Mac

1. Open a Terminal window on your Mac.

2. Install `brew` via the instructions on the [Homebrew website](https://brew.sh/).

3. Install Python via brew by typing `brew install python` in your Terminal.

4. Test your Python install by typing `python3 --version` in your Terminal. It should return version 3.6 or greater.

#### Windows

1. Download the latest Python from the [Python website](https://www.python.org/downloads/windows/).

2. Check `[ ] Add to PATH` when prompted by the installer.

3. Open VSCode and click `New Terminal` from the toolbar.

4. Type `python --version` in the Terminal. It should return version 3.6 or greater.

#### Linux

This can vary by distribution. Check the docs! You may already have Python installed.

## Python Basics

Let's go over a few basics.

### Running .py files

Python files end with .py and can be executed by opening a Terminal and navigating to the directory containing the file, then typing `python file.py` (`python3` on Mac)

You can open the terminal in the directory itself using VSCode (Windows) or CTRL+Clicking a folder and selecting "New Terminal at Folder" (Mac), or navigate on the command line. Here are some quick commands to help you navigate:

* `pwd` - Show the path to the current directory
* `ls`  - List everything in the current directory
* `cd [NAME]` - Change to the directory called [NAME]
* `cd ..` - Change to the previous directory
* `cd ~` - Change to the home directory

Try downloading the `hello.py` file and running it from the Terminal. It should return "Hello, world!"

### Interpreter

Python comes with a tool for testing out code, called the Interpreter. Activate it from any terminal by typing `python` (`python3` on Mac)

Here you can test out any Python code as if it were being run from a file. This is a great tool for development and I'll be using it a lot for demonstration purposes.

### Variables

You can store values in variables using `=`. Try typing this into your interpreter and hit ENTER:

```python
answer = 3 + 4
```

Now type `answer` again:

```python
answer
# 7
```

You can store every and anything in a variable.

### Printing

You can print things out using `print()`. This happens automatically in the interpreter (sometimes) but is necessary to see output from .py files.

Try to print out the variable `answer` from the previous section.

```python
print(answer)
```

### Strings

Strings are another word for text. You can represent this with either single or double quotes: it doesn't make a difference.

Try typing this into your interpreter:

```python
message_0 = "Hello,"
message_1 = ' world!'
```

```python
message_0 + message_1
# 'Hello, world!'
print(message_0 + message_1)
# Hello, world!
```

### f-strings

F-strings allow you to format strings exactly how you want. They are more of an intermediate topic, but they are so useful I have to tell you about them now.

To create one, put an `f` in front of the string you're creating to let Python know you want to format it. Now, everything inside that string surrounded by curly brackets will be interpreted as if they were code. For example:

```python
num1 = 5
num2 = 6
math_string = f"{num1} + {num2} = {num1+num2}"
print(math_string)
# 5 + 6 = 11
```


### Comments

You might be wondering about those `#` marks. Those are comments. Anytime you want to leave a note in your code, put a `#` in front of it and it will be ignored.

```python
# This is a comment and is ignored.
```

### Math

Computers are great at simple math! Try it out:

```python
2 + 3  # Addition
# 5

5 - 1  # Subtraction
# 4

4 * 2  # Multiplication
# 8

8 / 5  # Division
# 1.6

8 // 5 # Division rounded to the nearest integer
# 1

8 % 5  # Modulo, or remainder after division
# 3

i = 2
i += 3 # Increment i by 3
i
# 5
```

### Logic

Computers are also great at simple logic. Try these out:

```python
5 > 3  # 5 is greater than 3
# True

5 < 3  # 5 is less than 3
# False

"apple" == "apple"  # apple equals apple
# True

"orange" != "orange" # orange does not equal orange
# False

5 >= 5  # 5 is greater than or equal to 5
# True

6 <= 5  # 6 is less than or equal to 5
# False

3 > 4 or 2 < 5 # 3 is greater than 4 or 2 is less than 5
# True

not True
# False
```

### Conditionals

Like most programming languages, Python can use logical operators for conditional branching using `if/elif/else` for single conditionals and `while` which executes code as long as the condition is `True`.

The code within each block must contain the same indentation to run correctly. This is one of the trickiest parts of Python.

```python
x = 3
# If x is less than 5 and greater than or equal to 0
if x < 5 and x >= 0:
    print("Between 5 and 0")
else:
    print("Not between 5 and 0")
print("Between 5 and 0")


size = 4
if size < 2: # If size is less than 2
    print("Small")
elif size < 5: # Else, if size is less than 5
    print("Medium")
elif size < 8: # Else, if size is less than 8
    print("Large")
else: # Otherwise
    print("X-Large")
# Medium

i = 0
while i < 5:
    print(i)
    i += 1
# 0
# 1
# 2
# 3
# 4
```


### Functions

You can define functions to encapsulate blocks of code. You can pass variables to the function with an argument.

```python
def odd_or_even(num):
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

odd_or_even(5)
# 5 is odd.
odd_or_even(8)
# 8 is even.
```

Notice the following syntax contains `def` to show that it's a function, `odd_or_even` which is the function's name, `num` which is an argument that gets passed in, and a `:` to mark a that the function is beginning. All code inside the function must be indented.

The `if/else` block is also indented to show that it's encapsulated within the function.

We've combined the remainder/modulo operator (`%`) with `==` equality to test if the `num` argument is even or odd, and using an f-string to print the result.

Even though we are combining many concepts, the code itself is very clean and understandable, perhaps even if you've never seen Python before in your life.


### Dir

Curious what functions are available from a given object? Try the `dir()` method: It will give you a directory of all methods and attributes available on that object.

```python
dir(string)
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

This will give you all the functions you can use from a string.

(Ignore the items surrounded by underscores. Those are for internal use.)

### Help

Curious what a function does? Type `help()` to find out.

```python
help("string".isdigit)
# isdigit() method of builtins.str instance
#     Return True if the string is a digit string, False otherwise.

#     A string is a digit string if all characters in the string are digits and there is at least one character in the string.
```

Exit this page by hitting `q`.


### Import

If you're looking for more than basic functionality, Python's got a great default library. You can access this using `import`.

Say you want to generate some random numbers. Import the `random` module to do so.

```python
import random

random.randint(0, 100)
# 91

random.randint(0, 100)
# 71

random.randint(0, 100)
# 38

random.randint(0, 100)
# 62

random.randint(0, 100)
# 24

random.randint(0, 100)
# 9

random.randint(0, 100)
# 88
```

Read more about the standard Python library [here](https://docs.python.org/3/library/).
