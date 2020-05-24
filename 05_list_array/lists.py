

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


# Access the item at index 0 (first item)
fruits[0]
# 'apple'

# Access the item at index 2 (third item)
fruits[2]
# 'cherry'


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

# Insert 'blueberry' at index 1
fruits.pop(2)  # Pop out the value at index 2 ('banana')
# ['apple', 'blueberry', 'cherry', 'eggplant', 'fig', 'grape']


# Print each item in the list
for fruit in fruits:
    print(fruit)
# apple
# banana
# cherry
# eggplant
# fig
# grape


# Get a range of 10 numbers starting from 0
range(10)
# range(0, 10)



# Get a range of all indexes in a list
range(len(fruits))
# range(0, 8)


# Print the index of each item in a list, and its value
for i in range(len(fruits)):
    print(f"{i} - {fruits[i]}")
# 0 - apple
# 1 - banana
# 2 - fig
# 3 - date
# 4 - eggplant
# 5 - cherry
# 6 - grape
# 7 - honeydew


# Put the list in order
fruits.sort()
# ['apple', 'banana', 'cherry', 'date', 'eggplant', 'fig', 'grape', 'honeydew']



# You can add duplicates to lists
fruits.append("cherry")      # Add to the end
# ['apple', 'banana', 'cherry', 'date', 'eggplant', 'fig', 'grape', 'honeydew', 'cherry']
fruits.insert(4, "cherry")   # Insert before the 4th index
# ['apple', 'banana', 'cherry', 'date', 'cherry', 'eggplant', 'fig', 'grape', 'honeydew', 'cherry']



# Remove the first occurence of an item
fruits.remove("cherry")
# ['apple', 'banana', 'date', 'cherry', 'eggplant', 'fig', 'grape', 'honeydew', 'cherry']
fruits.remove("cherry")
# ['apple', 'banana', 'date', 'eggplant', 'fig', 'grape', 'honeydew', 'cherry']





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

