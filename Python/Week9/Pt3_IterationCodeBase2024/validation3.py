def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)

def remove_numbers(input_string):
    return ''.join(char for char in input_string if not char.isdigit())

name = input("Please type your name: ")
name_without_numbers = remove_numbers(name)
name1 = name_without_numbers.title()

if name1.istitle() and not has_numbers(name):
    print(f"Welcome {name1}")
else:
    print(f"Your name, {name}, should start with capital letters and not contain numbers!\nLike this: {name1}")