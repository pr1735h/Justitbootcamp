def details(name, age):
    print(f"Hello, {name} your age is {age}")

# Call sub:
details(age = 30, name = "Pritesh Hirani") # The order of arguments does not matter as they are specified by name

def welcome(name, greet="Welcome"): # Assign a default value for the variable "greet".
    print(f"{greet}, {name}!")

welcome("Gordo") # Uses the default value for the variable "greet".
welcome("Anna", greet="Goodbye")