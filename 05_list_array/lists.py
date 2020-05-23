# Create a list
fruits = ["apple", "banana", "cherry", "eggplant", "fig", "grape"]

# Get the number of items in the list
len(fruits)
# 6

# Print the list
print(fruits)
# ['apple', 'banana', 'cherry', 'eggplant', 'fig', 'grape']


# Add an item to the end of the list
fruits.append("honeydew")
# ['apple', 'banana', 'cherry', 'eggplant', 'fig', 'grape', 'honeydew']

# Insert an item at the 3rd index (starting from 0)
fruits.insert(3, "date")
# ['apple', 'banana', 'cherry', 'date', 'eggplant', 'fig', 'grape', 'honeydew']


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



# Switch the item at index 2 with the item at index 5
fruits[2], fruits[5] = fruits[5], fruits[2]
# ['apple', 'banana', 'fig', 'date', 'eggplant', 'cherry', 'grape', 'honeydew']


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





#####
# Number Lists
#####

numbers = [0, 1, 2, 3, 4]

# Get the minimum value
min(numbers)
# 0

# Get the maximum value
min(numbers)
# 4

# Add up all the numbers
sum(numbers)
# 10

