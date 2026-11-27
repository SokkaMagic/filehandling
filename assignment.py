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
    try:
        file = open(FileName, "r")
        num = file.readline().strip()
        num = int(num)
        file.close()
        return num
    except FileNotFoundError:
        print("File not found")
        return -1

    except ValueError:
        print("Not a number")
        return -1


# Exercise 3
def SaveMessage(FileName, Message):
    try:
        file = open(FileName, "w")
        file.write(Message)
        return True
    except:
        print("Cannot save")
        return False
# Exercise 4
def TotalOfFile(FileName):
    # Write your code here
    pass
