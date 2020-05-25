

# Create an empty dictionary
d = {}
# {}

# Add key/value pairs to the dictionary
d["key"] = "value"
# {'key': 'value'}

d["key2"] = "value2"
# {'key': 'value', 'key2': 'value2'}

# Create a dictionary with existing values
traits = {'name': 'bob',
          'age': 20,
          'height': 64,
          'friends': ['alice', 'charlie']
         }
# {'name': 'bob', 'age': 20, 'height': 64, 'friends': ['alice', 'charlie']}


# Search to see if the dictionary contains a given key
'age' in traits
# True
'weight' in traits
# False


# Search to see if the dictionary contains a given value
'bob' in traits.values()
# True
'dan' in traits.values()
# False


# Get the number of key/value pairs in the dictionary
len(traits)
# 4



# Loop through the keys of a dictionary
for key in traits:
    print(key)
# name
# age
# height
# friends


# Loop through values in a dictionary
for key in traits:
    print(traits[key])
# bob
# 20
# 64
# ['alice', 'charlie']

# Another way to loop through the values
for value in traits.values():
    print(value)
# bob
# 20
# 64
# ['alice', 'charlie']


# Using the key, you can loop through both keys and values
for key in traits:
    print(f'{key}: {traits[key]}')
# name: bob
# age: 20
# height: 64
# friends: ['alice', 'charlie']


"key1" in d

"value1" in d

"value1" in d.values()

