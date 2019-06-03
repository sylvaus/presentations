"""
Exception is a nice tool to handle events that should not happen in the normal flow of the program but should still
be taken into consideration.

For example, while parsing some text the function int(), that takes a string and returns an int, will raise an exception
if the given string cannot be converted into an int, e.g, int("a") will raise an Exception

When an exception is raised all code is ignored until a catch is reached.
This can be really helpful when the handling of the error is done really far from where the exception is raised
and not have to return the error from every value

To raise an exception, the code syntax is:
raise Exception(text)
# Exception could be replaced by any class that inherit from Exception (inheritance will be presented later)

The syntax to catch an exception is:
# Catch any Exception
try:
    code that may throw
except Exception as e: # the exception raise will be in variable e
    code to handle exception

# Catch a specific Exception: MyException
try:
    code that may throw
except MyException as e: # the exception raise will be in variable e
    code to handle exception

# Catch multiple Exceptions:
try:
    code that may throw
except MyException1 as e:
    code to handle exception
except MyException2 as e:
    code to handle exception
except MyException3 as e:
    code to handle exception

An interesting construct is the try-catch-else which canbe useful if code should ne executed
only if no exception was thrown
try:
    code that may throw
except MyException as e:
    code to handle exception
else:
    code that should be executed if no exception is raised

"""

"""
Exercise 1
Write a code that asks the operator for its name and throws an exception if the string is longer than 20 characters

"""

"""
Exercise 2
Write a code that asks the operator for its age and tries to convert it to int
Use the int(string) function: https://docs.python.org/2/library/functions.html#int
This function will throw an ValueError if it cannot be converted, use the try-catch-else construct to inform 
the user if the age given was correct or not

"""
