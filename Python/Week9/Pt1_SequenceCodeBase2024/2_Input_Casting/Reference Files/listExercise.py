# https://www.w3docs.com/learn-python/python-lists.html
"""You can think of list methods as special functions that are applied to lists. 
To call a list method, you need to use dot notation (as in the examples that follow).  """

"Objectives"
"Create list"  # A dynamic data structure that holds items under one name. The items can be of varying data types.
"Traverse"  # Move through a sequence.
"Custom built function"  # A function that you have created yourself and imported into other programs that you have created.
"Method"  # A function that belongs to an object.
    #  Use list methods to:"
    #  list.append(item)"   # add item at end of list
    #  list.insert(index,item)"  # add item at index
    #  list.pop(index)"  # remove item at index
    #  list.remove(item)"  # remove item
    #  list.index(item)"  # search for index of item
    #  list.count(item)"  # get occurrences of item
    #  list.reverse()"  # reverse list
    #  list.sort()"  # sort list

"Predict, then Run, and then Investigate"
emptyList = []  # declare emptyList variable and assign it a list datatype
print(type(emptyList))
print(emptyList)

# declare list2 variable and assign it a list datatype with two items
listOfModules = ["SDLC","HTML"] 
print(type(listOfModules))
print(listOfModules)

"List is a mutable data structure as items can be added or modify after the list has been created"

# String methods used to perform operations on strings
" Use the link below to investigate python lists and complete the tasks where appilcable"
# https://www.w3docs.com/learn-python/python-lists.html

#Access list items by their index position
# index    0        1       2     3  4   5     6
listOfElements = ["Paul", "Kane", "Anna", "Luke", "Abdul", "Tim", "Zak", "Waqas", "Narayan", "Christian", "Richie"]
print(listOfElements[1])

"To Do: Task 1a: Accessing list items" 
# print Anna from list3 using the index position/value
# print Kane from list3 using the negative index position/value
items = [1, 2]

for i in items:
    if i < len(listOfElements):
        print(f"Trainer {i}: {listOfElements[i]}")
    else:
        print(f"Index {i} is out of range for the string.")


"Modify:"
"To Do: Task 1b: modifying list items" 
#Complete the code below to add your name(replace kane with your name) to the list using the '=' assignment operator
listOfElements[1] = "Pritesh"

# List operations
"Appending items to list" 

listOfModules.append("CSS")  # use append method to add item("CSS") to the list, listOfModules.
print(listOfModules)

"Make"
"To Do:Task 2a:"
"Add 'NoSQL Database' to the listOfModules using the append method and print the list"
listOfModules.append("NoSQL Database")
print(listOfModules)

"Inserting items to list" 
listOfModules.insert(3,"JS")  # use insert method to insert JS in listOfModules(requires item position and item) 
print(listOfModules)

"Make"
"To Do:Task 2b: "
"Insert 'MySQL Database' to the listOfModules using the insert method at index position 4 and print the list"
"Return the length of the list"
listOfModules.insert(4, "MySQL Database")
print(listOfModules)

"To Do:Task 3a: "
#Complete the code below to return the length of the list using the len function
print("The length of the list is:", len(listOfElements))

"Slicing a list"
print(listOfElements[1:6])  # list[start:end]

"Remove list items as per index position"
countries = ["Scotland", "Ireland", "England", "Wales", "Brazil", "Argentina"]
print(type(countries))
print(countries)
del(countries[1])
print(countries)

"Modify:"
"To Do:Task 3b: "
# Complete the code below to remove item in index position 3 using del statement and print the list 
del(listOfElements[3])  # use del statement to delete by index position                 
print(listOfElements)

"To Do: What item did you remove at index position 3 b"
#Luke

"Modify:"
# Complete the code below to remove items in index position 3 and index position 5 print the list 
del(listOfElements[3], listOfElements[5])
print(listOfElements)

"Remove list items as per item value"
countries.remove("Brazil")
print(countries)

listOfElements.remove("Anna")  # use remove method to delete by item value
print(listOfElements)

"Modify:"
"To Do: Task 3c: "
"Remove the last country from the list of countries using the remove method"
del(countries[-1])
print(countries)

"Predict, then Run, and then Investigate"
"Exercise: Run the code below to understand the respective methods and/or functions"
# max and min function
listOfNums  = [1, 2, 4, 5, 6, 34.7, -8, 34, 67, 19, 23]
list4 = listOfNums
# returns the minimum item from the list
print(min(list4))
# returns the maximum item from the list
print(max(list4))
# sort list items
# sort list in ascending order
list4.sort()  
print(list4)
# sort list in descending order
list4.sort(reverse=True)
print(list4)
# clear list
# clear/ remove all list items
list4.clear()
print(list4)

"Make"
"To Do: Extension: Make: List of colours"

# create a list of 6 different colours
listOfColours = ["red", "blue", "green", "yellow", "white", "black"]
print(listOfColours)
# insert a new item(colour) in postion 3
listOfColours.insert(3, "orange")
print(listOfColours)
# add another another item(colour) to the list
listOfColours.insert(4, "navy")
print(listOfColours)
# remove an item(colour) by value
listOfColours.remove("navy")
print(listOfColours)
# remove the item(colour) at index position 3
del(listOfColours[3])
print(listOfColours)
# for every list operation performed print the list
