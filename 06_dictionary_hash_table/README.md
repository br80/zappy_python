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
d = {"key1": "value1", "key2": "value2", "key3": "value3"}
# {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
```

### Length

Just like lists, you can get the number of key/value pairs with `len()`

```python
len(d)
# 3
```


### Looping

Just like lists, you can loop through dictionaries with `for`.

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


