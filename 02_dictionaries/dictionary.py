

d = {}
d["key"] = "value"
d["key2"] = "value2"



d = {"key1": "value1", "key2": "value2", "key3": "value3"}

for key in d:
    print(f"KEY: {key}, VALUE: {d[key]}")

for value in d.values():
    print(value)


"key1" in d

"value1" in d

"value1" in d.values()


bear = {}
bear["species"] = "bear"
bear["color"] = "brown"
bear["size"] = "big"
bear["diet"] = []

bear["diet"].append("berries")
bear["diet"].append("birds")
bear["diet"].append("bugs")


print(bear)


animals = {}

animals["ant"] = {"species": "ant", "color": "black", "size": "tiny"}
animals["bear"] = {"species": "bear", "color": "brown", "size": "big"}
animals["cat"] = {"species": "cat", "color": "grey", "size": "small"}


animals["bear"]["diet"] = ["berries", "bugs", "birds"]





# Objects and Dictionaries

class Animal:
    def __init__(self, species, color, name, size, diet):
        self.species = species
        self.color = color
        self.name = name
        self.size = size
        self.diet = diet

bear = Animal("bear", "brown", "Bob", "big")

bear.name



# Create an empty dictionary
animals = []

bear = {"species": "bear",
        "name": "Bob",
        "color": "brow",
        "size": "big"
        "diet": ["berries", "bugs", "birds"]}

animals.append(bear)

bear["name"]
