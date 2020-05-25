# Objects

A well-organized codebase needs structure and objects are a great way to give structure to your data with classifications and attributes.

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


### Printing objects

Let's try print our "ant" object.

```python
print(animals["ant"])
# <__main__.Animal object at 0x101035250>
```

Yikes, not too useful. We can fix that by defining a `__str__()` method, which returns a human-readable string.

```python
class Animal:
    def __init__(self, species, size, diet):
        self.species = species
        self.size = size
        self.diet = diet
    def __str__(self):
        return f"{self.species}: {self.size} {self.diet}vore"


animals["ant"] = Animal("ant", "tiny", "omni")

print(animals["ant"])
# ant: tiny omnivore
```

That's much better.

### Class methods

To define an action, add a method within the class and include `self` as the first argument.


```python
class Animal:
    def __init__(self, species, size, diet):
        self.species = species
        self.size = size
        self.diet = diet
    def __str__(self):
        return f"{self.species}: {self.size} {self.diet}vore"
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
    def __init__(self, name, age, species, size, diet):
        self.name = name
        self.age = age
        self.species = species
        self.size = size
        self.diet = diet
    def __str__(self):
        return f"{self.name}: {self.species}, age {self.age}, {self.size} {self.diet}vore"
    def get_size(self):
        return self.size

class Ant(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "ant", "tiny", "omni")

ant = Ant("Anthony", 1)
ant2 = Ant("Antoine", 2)

print(ant)
# Anthony: ant, age 1, tiny omnivore
print(ant2)
# Antoine: ant, age 2, tiny omnivore
```

Since ants are animals, we can __inherit__ all animal properties and behavior from the `Animal` class with this line:

```python
class Ant(Animal):
```

`Ant` is a sub-class of `Animal` (sometimes called child class) and `Animal` is the super-class of `Ant` (sometimes called parent class).

Notice that since all ants are tiny omnivores, the `Ant` class fills those in automatically, only requiring us to fill in the name and age. The rest is handled like a normal animal by calling the super-class constructor, `super().__init__()`.

You'll also notice that the `Ant` class inherits the `get_size()` method from `Animal` even though we don't explicitly declare it.

```python
ant.get_size()
# 'tiny'
```

