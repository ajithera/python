try and except

Used to handle the error.

try - Executed the codes for error.
except -  This block will be executed when there is an error in try block.
else - this block executed when there is no error in try block
finally - executes regardless of try,except,else blocks

print(xyz) # it will throw error because xyz is not defined.

try:
    print(xyz)
except:
    print("xyz define pannuda venna") # this code will executed

There are many Exceptions available in python:

try:
    print(5/0)
except ZeroDivisionError:
    print("number can not be devided by zero")

