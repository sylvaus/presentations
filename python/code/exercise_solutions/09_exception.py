"""
Exercise 1
Write a code that asks the operator for its name and throws an exception if the string is longer than 20 characters

"""

def exercise1():
    name = input("what is your name")
    if len(name) > 20:
        raise Exception("too long")


exercise1()

"""
Exercise 2
Write a code that asks the operator for its age and tries to convert it to int
Use the int(string) function: https://docs.python.org/3/library/functions.html#int
This function will throw an ValueError if it cannot be converted, use the try-catch-else construct to inform 
the user if the age given was correct or not

"""


def exercise2():
    age = input("what is your name")
    try:
        age = int(age)
    except ValueError:
        print("Invalid Format")
    else:
        print("Whoa, you're", age)

exercise2()
