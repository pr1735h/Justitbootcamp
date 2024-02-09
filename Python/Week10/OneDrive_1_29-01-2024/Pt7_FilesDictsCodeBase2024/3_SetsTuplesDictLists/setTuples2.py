"To Do: Predict, then Run, and then Investigate"
student = {"name": "John Smith", "grades": [88, 76, 92, 85, 69]}

user1 = {"name": "Jane Smith", "Interests": ["Coding", "Gaming", "Swimming"]}
user2 = {"name": "Jane Smith", "Interests": ["Coding", "Gaming"]}
user3 = {"name": "Jane Smith"}
shopping = {"items": ["Eggs", "AA", "BBB", "CC"], "days": ["S", "M"]}
print(student.get("grades", []))
print(student.get("grades"))
print(user1.get("Interests"))

# Access array values by index
print(student["grades"][0])
print(user1["Interests"][1])
print(student["grades"][3])
student["grades"][3] = 98  # update an array/list value in index position 3
print(student["grades"][3])


d = {
    "a": (1, 1),  # tuple in dictionary
    "b": (1, 2),
    "c": (2, 1),
    "d": (2, 3, 4),
    "2": ["A", "C", "A", "F", "A"],  # list in dictionary
    "setA": {"JS", "Python", "HTML", "CSS"},
}

print(d["a"])
# Access tuple values by index
print(d["b"][1])  #
print(d["d"][2])  #

# Accessing set inside a dictionary
print(d["setA"])
# TypeError: 'set' object is not subscriptable, will result in error
# print(d["setA"]["Python"])
"Set is an unordered list and cannot be accessed by index"
# print(d["setA"][2])

# Key/value pairs are not allowed within a set
'set1 = {"A", "B", "C", "D", "E", "F":[1,2]}'
# Key/value pairs are not allowed within a tuple
'trainer = ("A", "B", "C", "D", "E", "F" :[1,2])'


# Sets
setC = {1, 2, 3, 4, 5}
setD = {3, 4, 5, 6, 7}

# Combine setC and setD
print(setC.union(setD))  # {1, 2, 3, 4, 5, 6, 7}

# Find common elements in setC and setD
print(setC.intersection(setD))  # {3, 4, 5}

# Find elements in setC which are not in setD
print(setC.difference(setD))  # {1, 2}

"Same result as above but using shorthand notation(special set operators)"
setC = {1, 2, 3, 4, 5}
setD = {3, 4, 5, 6, 7}

# Combine setC and setD
print(setC | setD)  # {1, 2, 3, 4, 5, 6, 7}

# Find common elements in setC and setD
print(setC & setD)  # {3, 4, 5}

# Find elements in setC which are not in setD
print(setC - setD)  # {1, 2}


"Chaining the operations together, for example to find the union of three sets:"
print("Chaining the operations together, for example to find the union of three sets:")
setC = {1, 2, 3, 4, 5}
setD = {3, 4, 5, 6, 7}
setE = {5, 6, 7, 8, 9}

# Combine setC and setD and setE
print(setC | setD | setE)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}


listOfTuples = [
    ("Em", "Jay"),
    ("The Matrix", 2006),
    ("Burna Boy", "Naugty By Nature"),
    "A",
    "B",
]
print(listOfTuples[0])
print(listOfTuples[1])
print(listOfTuples[3])


numList = [88, 76, 92, 85, 69]
print(numList)
print(sum(numList))  # returns the sum of the list items
print(min(numList))  # returns the min item in the list
print(max(numList))  # returns the max item in the list
print(numList[-1])  # returns the last list item
print(numList[::-1])  # returns the list in reverse order


# dictionary store data in key value pairs
"                  key: value"
dictionary1 = {1: "Jane Smith", "course": "Python"}
print(type(dictionary1))
print(dictionary1["course"])
print(dictionary1[1])

print(f"Prints every key and value held in the dictionary\n {dictionary1} ")
print(dictionary1)

# Nested dictionary
myFamily = {
    "firstChild": {"name": "Alice", "age": 24},
    "secondChild": {"name": "Paul", "age": 19},
}
print(myFamily)

print(myFamily.values())
print(myFamily.get("firstChild"))
print(myFamily.get("firstChild").values())
print(myFamily.get("firstChild").keys())
print(myFamily.get("firstChild").items())
print(myFamily.get("firstChild")["name"])
print(myFamily.get("firstChild")["age"])

# ..................
print(myFamily.get("secondChild"))
print(myFamily.get("secondChild").values())
print(myFamily.get("secondChild").keys())
print(myFamily.get("secondChild").items())
print(myFamily.get("secondChild")["name"])
print(myFamily.get("secondChild")["age"])

# The fromkeys() method returns a dictionary with the specified keys and the specified value.
# keys	Required. An iterable specifying the keys of the new dictionary
# value	Optional. The value for all keys. Default value is None
x = ("key1", "key2", "key3")
y = 0

thisdict = dict.fromkeys(x, y)


print(thisdict)


for aList, items in enumerate(myFamily):
    print(f"\nThis is child {aList} and list items: {items}")
    for indexPos, anItem in enumerate(items):
        print(f"This is index {indexPos} : item: {anItem}")


# ####################
for aList, items in enumerate(myFamily.items()):
    print(f"\nThis is child {aList} and list items: {items}")
    for indexPos, anItem in enumerate(items):
        print(f"This is index {indexPos} : item: {anItem}")


for aList, items in enumerate(myFamily.get("firstChild")["name"]):
    print(f"\nThis is child {aList} and list items: {items}")
    # for indexPos, anItem in enumerate(items):
    #     print(f"This is index {indexPos} : item: {anItem}")


for items in enumerate(myFamily.get("firstChild")["name"]):
    print(f"\nThis is child {aList} and list items: {items}")



"To Do: Task1: Add comments to the code above where possible to demonstrate understanding of what the code is doing"