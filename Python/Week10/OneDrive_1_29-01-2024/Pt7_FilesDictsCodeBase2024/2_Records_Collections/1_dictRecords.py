"""
Read data structures and record for 2 minutes
Data structures are used to store data in an organised and accessible way.
A list is a data structure.  Another example of a data structure is a record.
You might have heard of the word record if you have ever created a database before.
A record allows you to store a collection of attributes for a single entity.
Data structure: record: An entity can be any object, place, person, or thing.
Attributes are properties or characteristics of that entity.
Attributes are sometimes referred to as fields.
"""
"To Do: Predict, then Run, and then Investigate"
# Create a dictionary 
dict1 = {"fname":"Pritesh Hirani", "address":"123 Street Road, Townville, Cityon", "interest":"Coding", "age":30}
print(dict1)
print(dict1["age"])
print(dict1["fname"],",", dict1["age"])

"Using dictionary methods"

# D.items() -> a set-like object providing a view on D's items
dItems = dict1.items()
print(dItems)
 
# D.keys() -> a set-like object providing a view on D's keys
dKeys = dict1.keys()
print(dKeys)
 
# D.values() -> an object providing a view on D's values
dVals = dict1.values()
print(dVals)
# Loop through the keys and/values
print("\nLoop through the keys")
for aKey in dKeys:
    print(aKey)
 
print("\nLoop through the values")
for aValue in dVals:
    print(aValue) 
 
print("\nLoop through the keys and values")
for aKey,aValue in dItems:
    print(f"Key: {aKey} and Value : {aValue}")

"To Do: Task 1: Refer to the example code above to create your own dictionary with key value pairs and explain the differences between the items(), keys() and values() dictionary methods"
dict2 = {
    "song1": {
        "title": "Bohemian Rhapsody",
        "artist": "Queen",
        "album": "A Night at the Opera",
        "year": 1975,
        "genre": "Rock",
        "duration": 354
    },
    "song2": {
        "title": "Stairway to Heaven",
        "artist": "Led Zeppelin",
        "album": "Led Zeppelin IV",
        "year": 1971,
        "genre": "Rock",
        "duration": 482
    },
    "song3": {
        "title": "Smells Like Teen Spirit",
        "artist": "Nirvana",
        "album": "Nevermind",
        "year": 1991,
        "genre": "Grunge",
        "duration": 301
    }
}

"To Do: Task 2: Modify"
# Modify: The for loop block above to loop through your own the values
dItems2 = dict2.items()
dKeys2 = dict2.keys()
dVals2 = dict2.values()

print("\nLoop through the keys")
for aKey in dKeys2:
    print(aKey)

print("\nLoop through the values")
for aValue in dVals2:
    print(aValue)

"To Do: Extension: Can you use the for loop with the items method to loop through the keys and values simultaneously"
# Modify: The for loop block above to loop through the keys and the values and format your output
 
print("\nLoop through the keys and values")
for aKey,aValue in dItems2:
    print(f"Key: {aKey} and Value : {aValue}")

# create a dictionary 
dict3 = {2:"Python", 3:"HTML", 4:"CSS"}
print(f"Dictionary 2 {dict3}")


# Use of the Update method to merge two dictionaries
dict1.update(dict3)
print(f"Updated dictionary 1\n{dict1}")

"To Do: Task 2: Research: Look up Pop vs popItem explaind comment the code below to explain the difference"
# The pop() method removes items from Python dictionaries. The argument can be left blank to remove and return the last value.
# Add comment here to explain the function of the pop() method.
dict2.pop(3) # In this example the pop() method will remove the 3rd item from dict2.
print(dict2)

# Add comment here to explain the function of th popItem() method.
dict1.popitem() # popitem() is used to remove and return a value but it is returned with it's key and item values.
print(dict1)

"Delete key-value pair from dictionary:"
# We can delete a key-value pair from a dictionary using the del keyword followed by the key value to be deleted enclosed in [].
del dict1[2]

# update dictionary value using the key
dict1[1] = "Emma Smith"
user={"interests" :"coding"}

print(user)
user["interests"] = "Football"

print(dict1)
print(user)