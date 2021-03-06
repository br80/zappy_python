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
    def speak(self):
        print("...")


class Ant(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "ant", "tiny", "omni")


class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "bear", "large", "omni")
    def speak(self):
        print("ROAR!")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "cat", "small", "carni")
    def speak(self):
        print("meow")


class Deer(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "deer", "medium", "herbi")


class Elephant(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "elephant", "x-large", "herbi")
    def speak(self):
        print("BAROOOG!")





antoine = Ant("Antoine", 1)
antoine.get_size()
# 'tiny'

anthony = Ant("Anthony", 2)
anthony.speak()
# '...'


cathy = Cat("Cathy", 5)
cathy.get_size()
# 'small'
cathy.get_size()
# 'meow'
print(cathy)
# Cathy: cat, age 5, small carnivore
