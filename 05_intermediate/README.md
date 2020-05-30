# Display

Let's review what we've learned so far:

* Variables
* Printing
* Strings
* Comments
* Arithmetic/Logic
* Conditionals
* Functions
* Imports
* Lists
* Loops
* Dictionaries
* CSVs

Not bad! We can do a lot with this. Let's put these together to make a very simple graphics display which we will turn into an adventure game next lesson.

To do that, we will implement the following:

1. Create a grid of pixels
2. Print the pixel grid to the terminal
3. Process keyboard inputs to update the grid
4. Update the pixel grid with changes
5. Clear the screen between updates


## More list techniques

Let's build on our knowledge of lists with some more techniques.

### 2D lists

We've learned how to work with Python lists in a previous lesson. We can create a 2-dimensional grid out of a list of lists.

```python
nums = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
```

Here we have a list called `nums`, which contains three other lists. We can access each row by index:

```python
nums[0] # First row
# [1, 2, 3]

nums[1] # Second row
# [4, 5, 6]

nums[2] # Third row
# [7, 8, 9]
```

We can access the columns in each row with a second set of square brackets like so:

```python
nums[0][1] # First row, second column
# 2

nums[1][2] # Second row, third column
# 6

nums[2][0] # Third row, first column
# 7
```

We can print out each item in the grid with a nested for loop:

```python
for row in nums:
    for val in row:
        print(val)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```

### Initializing lists with `*`

You can create large lists using the multiplication (`*`) operator.

```python
['x'] * 10  # Creates a list with 10 x's
# ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
```

You can use this to create a 2D grid.

```python
rows = 5
cols = 10

# Create a grid with 5 rows and 10 columns
grid = []
for i in range(rows):
    grid.append(['x'] * cols)

# [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
#  ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
#  ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
#  ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
#  ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

```


### List comprehensions

List comprehensions are a handy way to filter and formatting to every item in a list. For example, let's take a list of numbers, filter out everything that's less than 12, then turn it into a string.

```python
nums = [0, 5, 10, 15, 20]

# Stringify each number in the nums list if that number is greater than or equal to 12.
[str(num) for num in nums if num >= 12]
# ['15', '20']
```

We can break these up into 3 parts:

1. **Formatting:** `str(num)`
2. **Collection:** `for num in nums`
3. **Filter:**     `if num >= 12`

It may help to read the comprehension like, "Stringify each number in the nums list if that number is greater than or equal to 12."


### Join

We can join all the elements of a list with the `join()` function.

```python
names = ["Alice", "Bob", "Charlie", "Dan", "Eve"]

" - ".join(names)
# 'Alice - Bob - Charlie - Dan - Eve'

".".join(names)
# 'Alice.Bob.Charlie.Dan.Eve'
```

The string at the front of the expression is what's inserted between each element in the list. Note that this doesn't work for non strings, but we can change each element to a string with a list comprehension.

```python
nums = [1, 2, 3, 4, 5]

", ".join(nums)  # Can only join strings, not integers
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: sequence item 0: expected str instance, int found

", ".join([str(num) for num in nums])  # Comprehension turns ints into strings
# '1, 2, 3, 4, 5'
```



## Print grid

We can combine our 2D list with the `print()` function to print out a 2D list.

```python
rows = 5
cols = 10

grid = []
for i in range(rows):
    grid.append(['x'] * cols)

for row in grid:
    print(row)
# ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
# ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
# ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
# ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
# ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
```

We can make it look nicer with `join()`

```python
for row in grid:
    print(" ".join(row))
# x x x x x x x x x x
# x x x x x x x x x x
# x x x x x x x x x x
# x x x x x x x x x x
# x x x x x x x x x x
```



## Clear screen

Clearing all text on the screen in Windows is done using the `os` module by calling `os.system('cls')` and on every other operating system using `os.system('clear')`. We can make this work on every OS with the following code.

```python
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
```

'nt' is Python's identifier for Windows OS.


## Keyboard input

Python has a built-in function to capture input:

```python
name = input("Type your name: ")
```

This will wait for the user to type a name and hit ENTER, then set the 'name' variable to whatever the user typed. If we want to capture input without waiting for ENTER, we'll need to implement some new functionality. Fortunately, the Python community is very helpful and we can find a solution to this with a quick search online. We will be using the [kbhit module](./kbhit.py), written by [Simon D. Levy](https://simondlevy.academic.wlu.edu/files/software/kbhit.py).

Every coder borrows code online and is usually highly encouraged. Be sure to check the licenses and give credit when you do!

```python
# test.py
import kbhit
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

kb = kbhit.KBHit()

last_c = "NONE"

clear_screen()

while True:
    if kb.kbhit():
        c = kb.getch()
        if c == "q":  # Hit `q` to break out of the loop
            break
        last_c = c
    clear_screen()
    print(last_c)
```

Check out this code in `test.py` which will clear the screen and print out the last character typed. Try it out!

You may notice some flickering because the screen is being cleared and printed so frequently. You can fix this by printing only when there is an update by indenting `clear_screen()` and `print(last_c)` into the `if` block.

```python
while True:
    if kb.kbhit():
        c = kb.getch()
        if c == "q":  # Hit `q` to break out of the loop
            break
        last_c = c
        clear_screen()
        print(last_c)
```

## Rendering objects

First let's create an object to render:

```python
class Object:
    def __init__(self, character, row, col, display):
        self.display_char = character
        self.row = row
        self.col = col

        self.display = display
        self.display.grid[row][col] = self

    def __str__(self):
        # This is what's displayed when rendered in the grid
        return self.display_char
```

Let's create a class to represent our grid display.

```python
import os
import kbhit

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Display:

    def __init__(self):
        self.rows = 5
        self.cols = 10

        self.grid = []
        for i in range(self.rows):
          self.grid.append(["."] * self.cols)

        self.obj = Object("o", 3, 3, d)

    def print_screen(self):
        # First, clear the screen
        clear_screen()
        # Then print each row in the grid
        for row in self.grid:
            char_row = [str(c) for c in row]
            print(' '.join(char_row))

    def run(self):
        self.print_screen()

```

Now let's create and run the display.

```python
d = Display()
d.run()

# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . o . . . . . .
# . . . . . . . . . .
```

## Moving objects on the grid

Finally, let's use our `kbhit` module to move the object with WASD keys. Add this to your Display class:

```python
def process_command(self, c):
    directions = {"w": "north", "a": "west", "s": "south", "d": "east"}
    if c in directions:
          self.obj.move(directions[c])
```

With "WASD" commands, 'w' is north, 'a' is west, 's' is south and 'd' is east. This dictionary provides a handy mapping for these commands.

The last step is to implement the `move()` command in the object.

```python
def move(self, direction):
    # Set the current position to empty
    self.display.grid[self.row][self.col] = "."
    # If we're not in the top row, move up one row
    if direction == "north" and self.row > 0:
        row -= 1
    # If we're not in the last row, move down one row
    elif direction == "south" and self.row < self.display.rows - 1:
        row += 1
    # If we're not in the far-left column, move left one column
    elif direction == "west" and self.col > 0:
        col -= 1
    # If we're not in the far-right column, move right one column
    elif direction == "east" and self.col < self.display.cols - 1:
        col += 1
    # Put ourself in the updated grid position
    self.display.grid[self.row][self.col] = self
```

Now try running `display.py` to move your object around the grid!

