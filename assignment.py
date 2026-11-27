# You can remove 'pass' if you written code in the function
# Every exercise must use exception handling: try / except


# Exercise 1
def ReadFile(FileName):
    try:
        file = open(FileName, "r")
        text = file.read()
        file.close()
        return text

    except:
        print("File not found")
        return ""

# Exercise 2
def ReadNumber(FileName):
    # Write your code here
    pass


# Exercise 3
def SaveMessage(FileName, Message):
    # Write your code here
    pass


# Exercise 4
def TotalOfFile(FileName):
    # Write your code here
    pass
