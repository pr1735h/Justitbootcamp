"""
Session objectives
●	Write to text files
●	Read data from a text file
●	Append to text files
●   Use context manager to handle resource usage
Key vocabulary
Data files, text files

"""
"Spend 3 minutes to read the comments in green"
# In order to read the data stored in a text file, you must open it first. ​

# Just like a book. You can’t read what is inside if you don’t open it first.​

# There are four modes for opening a file:​

# r for only reading files​

# w for only writing to files​ and creating the file if it does not exists but overwrites existing file contents

# a for adding to an existing file​

# r+ for reading and writing files

"""
Key file-handling techniques are:Open, Read ,Close, Write
The text file must be saved in the same location as your Python file for the program to work. 
"""

"1_FileHandling_ReadWrite/myfile.txt","w"
"Syntax :  varName = openMethod('pathtofolder/parthtofile/fileName.txt', 'w')"
filePath1 = open("Week10/OneDrive_1_29-01-2024/Pt7_FilesDictsCodeBase2024/file1.txt", "w") # folder/folder/filename
# write to file
filePath1.write("Python Programming")
# close the filepath and file/ releasing the resource
filePath1.close()

"To Do: Refer to the example code above to create a file called yourName.txt and Write your name to the file"
# Using "a" to appends content to the file, allowing you to add, rather than override which "w" will do.
filePath2 = open("Week10/OneDrive_1_29-01-2024/Pt7_FilesDictsCodeBase2024/yourname.txt", "a")
for i in range(15):
    filePath2.write("Pritesh\nHirani\nDeleteThis\nMusic\nGames\nFood\n")
filePath2.close()

# Code to delete lines from files:
with open("Week10/OneDrive_1_29-01-2024/Pt7_FilesDictsCodeBase2024/yourname.txt", "r") as f:
    lines = f.readlines()

with open("Week10/OneDrive_1_29-01-2024/Pt7_FilesDictsCodeBase2024/yourname.txt", "w") as f:
    for line in lines:
        if "DeleteThis" not in line:
            f.write(line)
# If stuck refer to the example above

# Read from file:
filePath3 = open("Week10/OneDrive_1_29-01-2024/Pt7_FilesDictsCodeBase2024/yourName.txt")
print(filePath3.read())
filePath3.close()
# Or:
with open("Week10/OneDrive_1_29-01-2024/Pt7_FilesDictsCodeBase2024/yourName.txt", "r") as filePath1:
    readContent = filePath1.readlines()
    print(readContent)

# To create a file:
with open("Week10/OneDrive_1_29-01-2024/Pt7_FilesDictsCodeBase2024/newFile.txt", "w+") as f:
    f.write("This text file was created using Python\nThis text file was created using Python\nThis text file was created using Python\nThis text file was created using Python\n")
    f.seek(0)
    print(f.read())

"Further reading"
# https://www.w3docs.com/snippets/python/how-to-read-a-text-file-into-a-list-or-an-array-with-python.html