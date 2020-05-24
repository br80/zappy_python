# Lists

Lists, are used to store collections of items. They are extremely useful.

### Creating lists

To create an empty list, create a variable with empty brackets.

```python
fruits = []
# []
```

Add items to the end of the list with `append()`

```python
fruits.append("apple")  # Add 'apple' to the end of the list
# ['apple']

fruits.append("cherry") # Add 'cherry' to the end of the list
# ['apple', 'cherry']

fruits.append("apple") # Add 'apple' to the end of the list
# ['apple', 'cherry', 'apple']
```

You can remove items with `remove()`. If there are duplicates, it will remove the first occurence.
```python
fruits.remove('apple')
# ['cherry', 'apple']
```

If you know the items ahead of time, you can put them in the list at the start.

```python
fruits = ["apple", "banana", "cherry", "eggplant", "fig", "grape"]
# ['apple', 'banana', 'cherry', 'eggplant', 'fig', 'grape']
```

### Length

Get the length of the list with `len()`
```python
len(fruits)
# 6
```


### Indexes

Each item in a list can be accessed by its index. The index of an item is it's position, starting from 0.

```python
fruits
# ['apple', 'banana', 'cherry', 'eggplant", 'fig', 'grape']

fruits[0]  # The first item, index 0
# 'apple'

fruits[1]  # The second item, index 1
# 'banana'

fruits[2]  # The third item, index 2
# 'cherry'

fruits[3]  # The fourth item, index 3
# 'eggplant'

fruits[4]  # The fifth item, index 4
# 'fig'

fruits[5]  # The sixth item, index 5
# 'grape'
```

You can reassign an item with its index too.
```python
fruits[0] = "apricot"
# ['apricot', 'banana', 'cherry', 'eggplant', 'fig', 'grape']
```


Insert an item at a given index with `insert()`

```python
fruits.insert(1, "blueberry")  # Insert 'blueberry' at index 1
# ['apricot', 'blueberry', 'banana', 'cherry', 'eggplant', 'fig', 'grape']
```

Pop out the item at the given index with `pop()`

```python
fruits.pop(2)  # Pop out the value at index 2
# 'banana'
# ['apricot', 'blueberry', 'cherry', 'grape', 'eggplant', 'fig']
```


### Looping

Use `for` to loop through the list and perform an action on each item.

```python
for fruit in fruits:
    print(fruit)
# apricot
# blueberry
# cherry
# eggplant
# fig
# grape
```


### Looping with an index

The `range()` is helpful for looping through lists with indexes.

```python
# Get a range of 10 numbers starting from 0
range(10)
# range(0, 10)
```

Use it to get a range of all indexes in a list.

```python
range(len(fruits))
# range(0, 6)
```

You can use `for` to loop through each index.
```python
# Print each index in a list
for i in range(len(fruits)):
    print(i)
# 0
# 1
# 2
# 3
# 4
# 5
```

You can use this to access the list items by index.
```python
# Print the index of each item in a list, and its value
for i in range(len(fruits)):
    print(f"{i} - {fruits[i]}")
# 0 - apricot
# 1 - blueberry
# 2 - cherry
# 3 - eggplant
# 4 - fig
# 5 - grape
```


Let's capitalize every other item in our list by combining `range()`, the `%` operator, index assignment and the `captialize()` function.
```python
# Print the index of each item in a list, and its value
for i in range(len(fruits)):
    if i % 2 == 0:
        fruits[i] = fruits[i].capitalize()
    print(f"{i} - {fruits[i]}")
# 0 - apricot
# 1 - blueberry
# 2 - cherry
# 3 - eggplant
# 4 - fig
# 5 - grape
```

### Number lists

If your list only consists of numbers, Python lets you run some special functions.

```python
numbers = [2, 4, 6, 8, 10]
```

Find the smallest value with `min()`

```python
min(numbers)
# 2
```

Find the largest value with `max()`

```python
min(numbers)
# 10
```

Add up all the numbers with `sum()`

```python
# Add up all the numbers
sum(numbers)
# 30
```
