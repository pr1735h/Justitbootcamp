def user(paraUser):  # define the subroutine user with a parameter paraUser
    # return f"My name is {paraUser}"
    return paraUser
 
print(user("Johnny Bravo"))
print(f"Welcome {user('Johnny Bravo')}")
# or
userData = user("Lucy Smith")
print(userData)
 
print(f"You are {userData}")

# define the subroutine userName
def userName(paraFname, paraInterest, paraAddress):
    return paraFname, paraInterest, paraAddress
 
 
user1data = userName("AA","BB","CC")
print(user1data[0])
print(user1data[1])
print(user1data[2])
 
 
argFname = input("Enter your full name: ")
argInterest = input("Enter your interest: ")
argAddress = input("Enter your address: ")
 
user2data = userName(argFname,argAddress,argInterest)
print(user2data[0])
print(user2data[1])
print(user2data[2])