# Dictionaries

Like lists, dictionaries are used to store collections of items. Instead of storing those collections in order and accessing them by position, dictionaries let you store and access your data with any key you like. This makes them very flexible and efficient.

### Creating dictionaries

To create an empty dictionary, create a variable with empty curly brackets.

```python
d = {}
# {}
```

For each value you store in the dictionary, you need a key.

```python
d["key"] = "value"
# {'key': 'value'}
```

You can access the value with the key.

```python
d["key"]
'value'
```

You can only store one value per key. Assigning a new value to an existing key will overwrite the value.

```python
d["key"]
# 'value'
d["key"] = "new value"
d["key"]
# 'new value'
```

You can build the dictionary at the start if you know your keys and values.

```python
traits = {"name": "bob",
          "age": 16,
          "height": 64,
          "friends": ["alice", "charlie"]
         }
# {'name': 'bob', 'age': 16, 'height': 64, 'friends': ['alice', 'charlie']}
```

Note that values can be any valid type, including strings, numbers, lists and more.

### Length

Just like lists, you can get the number of key/value pairs with `len()`

```python
len(traits)
# 4
```


### Looping

Just like lists, you can loop through dictionaries with `for`.

```python
# {'name': 'bob', 'age': 16, 'height': 64, 'friends': ['alice', 'charlie']}
for key in traits:
    print(key)
# name
# age
# height
# friends
```

Note that this loops through the __keys__, NOT the __values__. You can loop through the values using your keys:

```python
# {'name': 'bob', 'age': 16, 'height': 64, 'friends': ['alice', 'charlie']}
for key in traits:
    print(traits[key])
# bob
# 16
# 64
# ['alice', 'charlie']
```

You can also do this using `values()`.

```python
for value in traits.values():
    print(value)
# bob
# 16
# 64
# ['alice', 'charlie']
```

Looping with the key is usually better because it lets you access both the keys and values.

```python
for key in traits:
    print(f"{key}: {traits[key]}")
# name: bob
# age: 16
# height: 64
# friends: ['alice', 'charlie']
```










