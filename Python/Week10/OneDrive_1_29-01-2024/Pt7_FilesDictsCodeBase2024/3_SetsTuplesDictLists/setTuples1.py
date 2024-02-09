"""
 Tuple is a sequence of items that are in order
 and it is not possible to modify the tuples. Therefore,
 tuples are faster than list and the primary use of tuples
 is to create write protect data 
 items can be accessed based on their index position
"""


"To Do: Predict, then Run, and then Investigate"

# declare a tuple and assign different data type
tpl1 = ("a", "b", "c", 1, 12, "a", "b", "c", "z", 10.4, -5, 12, 10.4, -5)
tpl2 = ("Anna",) # a single tuple item must have a comma after it
print(type(tpl1))
print(type(tpl2))

print(tpl1)
print(f"The item found is : {tpl1[1]}")
print(
    f"The index position {tpl1.index('b')} : and the value in this position is: {tpl1[1]}"
)
print(f"The number of items is : {tpl1.count('b'), 'b'}")
print(f"The number of {tpl1[8]} is {tpl1.count('z')}")


"""set  is a collection of unique items that are not in order,
it is an unorder data type. Duplicates are eliminated in a set.
set items can not be accessed by index
"""
print("This is a set\n")
set1 = {
    "a",
    "b",
    "c",
    1,
    12,
    "a",
    "b",
    "c",
    10.4,
    -5,
    12,
    10.4,
    -5,
    "Anna",
    "Paul",
    "Joe",
    "Jane",
    "Anna",
    "Paul",
    "Joe",
    "Jane",
}
print(type(set1))
print(set1)

# add items to a set
set1.update(["Em", "Jay", 103, 200])  # add items to the set
print(set1)
set1.remove("Em")
print(set1)
set1.remove(1)
print(set1)
set1.clear()
print(set1)



# frozen set
"once a set is frozen it the items in the set cannot be modify/change"
set1 = {
    "a",
    "b",
    "c",
    1,
    12,
    "a",
    "b",
    "c",
    10.4,
    -5,
    12,
    10.4,
    -5,
    "Anna",
    "Paul",
    "Joe",
    "Jane",
    "Anna",
    "Paul",
    "Joe",
    "Jane",
}
fset = frozenset(set1)
print(f"This set is frozen {fset}")
# fset.update(["Emma", "Jayne", 1003, 2000])
print(fset)

"To Do: Task1: Add comments to the code above to demonstrate understanding of what the code is doing"