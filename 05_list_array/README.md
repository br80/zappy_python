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


Insert an item at a given index with `insert()`

```python
fruits.insert(1, "blueberry")  # Insert 'blueberry' at index 1
# ['apple', 'blueberry', 'banana', 'cherry', 'eggplant', 'fig', 'grape']
```

Pop out the item at the given index with `pop()`

```python
fruits.pop(2)  # Pop out the value at index 2
# 'banana'
# ['apple', 'blueberry', 'cherry', 'grape', 'eggplant', 'fig']
```


### Looping

Use `for` to loop through the list and perform an action on each item.

```python
for fruit in fruits:
    print(fruit)
# apple
# banana
# cherry
# eggplant
# fig
# grape
```


### Looping with an index

Use `range()` to get a range of indices starting from 0.

```python
# Get a range of 10 numbers starting from 0
range(10)
# range(0, 10)

# Get a range of all indexes in a list
range(len(fruits))
# range(0, 6)

# Print each index in a list
for i in range(len(fruits)):
    print(i)
# 0
# 1
# 2
# 3
# 4
# 5

# Print the index of each item in a list, and its value
for i in range(len(fruits)):
    print(f"{i} - {fruits[i]}")
# 0 - apple
# 1 - blueberry
# 2 - cherry
# 3 - eggplant
# 4 - fig
# 5 - grape
```



