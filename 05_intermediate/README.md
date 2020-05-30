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


## 2D lists

We've learned how to work with Python lists in a previous lesson. We can create a 2-dimensional grid out of a list of lists.

```python
nums = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

```

Here we have a list called nums, which contains three other lists. We can access each row by index:

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


## Time, sleep

Timing is crucial for games and animation. We can import Python's `time` module to help us build our graphics display.

```python
import time

time.time() # The number of seconds since Jan 1, 1970
# 1590861260.771779
```

Let's wait a few seconds.

```python
time.time()
# 1590861311.3672168
```

Notice that the value of `time.time()` changed after some time had passed. We can also use the `time.sleep()` function to make Python pause for some amount of time.

```python
start_time = time.time()
# 1590861459.577342
time.sleep(5)
end_time = time.time()
# 1590861464.58429
print(f"Slept for {end_time - start_time} seconds.")
# Slept for 5.006947994232178 seconds.
```








* 2D arrays

* Nested Loops

* Time
  * Sleep

* Clear Screen
  * Google

  * Input
    * KBHit
    * Screen clearn


### Nested loops

You can nest lists, dictionaries, and values together as deep as you like.

```python
alice =  {'name': 'alice', 'age': 21, 'height': 61, 'friends': ['bob', 'dan']}
bob = {'name': 'bob', 'age': 20, 'height': 64, 'friends': ['alice', 'charlie']}
charlie =  {'name': 'charlie', 'age': 21, 'height': 63, 'friends': ['bob']}
dan =  {'name': 'dan', 'age': 22, 'height': 66, 'friends': ['alice', 'bob']}

people = {'alice': alice, 'bob': bob, 'charlie': charlie, 'dan': dan}
# {
# 'alice': {'name': 'alice', 'age': 21, 'height': 61, 'friends': ['bob', 'dan']},
# 'bob': {'name': 'bob', 'age': 20, 'height': 64, 'friends': ['alice', 'charlie']},
# 'charlie': {'name': 'charlie', 'age': 21, 'height': 63, 'friends': ['bob']},
# 'dan': {'name': 'dan', 'age': 22, 'height': 66, 'friends': ['alice', 'bob']}
# }
```

You can run nested loops as well.

```python
for person in people:
    print(f'{person} is friends with:')
    for friend in people[person]['friends']:
        print(f'  {friend}')
# alice is friends with:
#   bob
#   dan
# bob is friends with:
#   alice
#   charlie
# charlie is friends with:
#   bob
# dan is friends with:
#   alice
#   bob
```


