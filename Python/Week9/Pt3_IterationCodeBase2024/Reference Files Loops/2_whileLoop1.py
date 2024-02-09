"""use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program"""

num = 1

"To Do: Explain what is += 1  ?"
# start from num(1), keep counting until the value of num is 20
while num <=20:
    print(f"The number is: {num}")
    num +=1 # num = num + 1

"Modify/Make"
"To Do: Task 2: Modify the whileloop above to count down from 20 to 1 and comment your code"
num = 20 # Start from num(20)
while num >=1: # Whilst num is greater than or equal to 1:
    print(f"The number is: {num}") # Print the current number,
    num -=1 # num = num - 1