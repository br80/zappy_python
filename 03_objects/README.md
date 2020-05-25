# Objects

A well-organized codebase needs structure and objects are a great way to give structure to your data.

### Creating objects

Say we are writing a program to stores a collection of animals. We could do so using lists and dictionaries:

```python
animals = {}

animals["ant"] = {"species": "ant", "size": "tiny", "diet": "omni"}
animals["bear"] = {"species": "bear", "size": "large", "diet": "omni"}
animals["cat"] = {"species": "cat", "size": "small", "diet": "carni"}
animals["deer"] = {"species": "deer", "size": "medium", "diet": "herbi"}
animals["elephant"] = {"species": "elephant", "sizz": "x-large", "diet": "herbi"}

def get_size(animal_type):
    return animals[animal_type]["size"]

get_size("cat")
# 'small'
```

This will work, but notice that there are a lot of manually typed labels and repetition which can lead to errors. For example:

```python
get_size("elephant")
# KeyError: 'size'
```

We can avoid this by using object-oriented programming, sometimes abbreviated as OOP.

# Classes and constructors

Classes are like the blueprints for our objects. They determine what attributes each object has and what actions they can do.


```python
class Animal:
    def __init__(self, species, size, diet):
        self.species = species
        self.size = size
        self.diet = diet

animals["ant"] = Animal("ant", "tiny", "omni")
animals["bear"] = Animal("bear", "large", "omni")
animals["cat"] = Animal("cat", "small", "carni")
animals["deer"] = Animal("deer", "medium", "herbi")
animals["elephant"] = Animal("elephant", "x-large", "herbi")

```

The `__init__()` function is called a constructor. This gives you a set of fields that must be set to create the object. If we try to create an animal without all of the required fields, we will get an error:

```python
Animal()
# TypeError: __init__() missing 3 required positional arguments: 'species', 'size', and 'diet'
```

Note that `self` is used to refer to the object itself and is required in the class definitions. It is included automatically when you construct an object.


### Class methods

To define an action, add a method within the class and include `self` as the first argument.


```python
class Animal:
    def __init__(self, species, size, diet):
        self.species = species
        self.size = size
        self.diet = diet
    def get_size(self):
        return self.size

animals["ant"] = Animal("ant", "tiny", "omni")
animals["bear"] = Animal("bear", "large", "omni")
animals["cat"] = Animal("cat", "small", "carni")
animals["deer"] = Animal("deer", "medium", "herbi")
animals["elephant"] = Animal("elephant", "x-large", "herbi")

animals["cat"].get_size()
# 'small'

animals["elephant"].get_size()
# 'x-large'
```

Here, we define an action called `get_size()` which returns the size of the animal. Since we are using a class that forces us to define the animal's size in the constructor, this is guaranteed to return successfully.



### Inheritance

Say we want to extend our program to store many instances of each animal, along with an age and name for each. We can avoid more repetition errors using class inheritance.


```python
class Animal:
    def __init__(self, species, size, diet):
        self.species = species
        self.size = size
        self.diet = diet
    def get_size(self):
        return self.size

class Ant(Animal):
    def __init__(self, name, age):
        super().__init__("ant", "tiny", "omni")
        self.name = name
        self.age = age

ant = Ant("Anthony", 1)
ant2 = Ant("Antoine", 2)


ant.name
# 'Anthony'
ant.age
# 1
ant.species
# 'ant'
ant.size
# 'tiny'
ant.get_size()
# 'tiny'
ant.diet
# 'omni'

ant2.name
# 'Antoine'
```


