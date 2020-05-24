

#######
# Lists
#######

# Create an empty list
fruits = []
# []

fruits.append("apple")
# ['apple']

fruits.append("cherry")
# ['apple', 'cherry']

# Create a full list
fruits = ["apple", "banana", "cherry", "eggplant", "fig", "grape"]



# Get the number of items in the list
len(fruits)
# 6

# Access items by index
# ['apple', 'banana', 'cherry', 'eggplant', 'fig', 'grape']
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


# Insert 'blueberry' at index 1
fruits.insert(1, "blueberry")
# ['apple', 'blueberry', 'banana', 'cherry', 'eggplant', 'fig', 'grape']

# Pop out the value at index 2 ('banana')
fruits.pop(2)
# ['apple', 'blueberry', 'cherry', 'eggplant', 'fig', 'grape']


# Print each item in the list
for fruit in fruits:
    print(fruit)
# apple
# blueberry
# cherry
# grape
# eggplant
# fig


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



#######
# Number lists
#######

# Create a list with numbers in it
numbers = [2, 4, 6, 8, 10]

# Access the item at index 0 (first item)
numbers[0]
# 2

# Access the item at index 2 (third item)
numbers[2]
# 6

# Get the minimum value
min(numbers)
# 2

# Get the maximum value
min(numbers)
# 10

# Add up all the numbers
sum(numbers)
# 30

