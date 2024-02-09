fname    = input("Enter your full name: ")
address   = input("Enter your address: ")
interest = input("Enter your interest: ")
age      =    int(input("Enter your age: "))

"Make"
"To Do: Task 1: Use the code above to ask for user input and then save it to a file called userDetails.txt"
filename = "userDetails.txt"
with open(filename, "a") as f:
    f.write(f"Full Name: {fname}\n")
    f.write(f"Address: {address}\n")
    f.write(f"Interest: {interest}\n")
    f.write(f"Age: {age}\n")

with open("userDetails2.txt", "a") as f:
    f.write(f"First Name: {input("Enter your first name: ")}\n")
    f.write(f"Last Name: {input("Enter your last name: ")}\n")
    f.write(f"Address: {input("Enter your address: ")}\n")
    f.write(f"Age: {input("Enter your age: ")}\n")

readFile = open("userDetails2.txt")
print(readFile.read())
readFile.close()

with open("userDetails3.txt", "a") as data:
    "method 1"
    user_info = f"\n {fname}\n {address} \n{interest} \n {age}"
    data.write(user_info)
 
    "method 2"
    # data.write("\n" +fname+ "\n" +address+ "\n" + interest+ "\n" + str(age) )
 
    "method 3"

"Further reading"
# https://www.w3schools.com/python/python_file_handling.asp