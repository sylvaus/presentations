"""
Exercise 1:
Fill function exercise1 to count how many unique characters are in the text and print the number

Help: a string can also be considered as a list of characters which means it can be used in a for loop like any other list

Optional task 1: write the code to ignore the case of the text (hint: look at the string function: https://docs.python.org/3/library/stdtypes.html#string-methods)
Optional task 2: add some code to have the user input the text
"""


def exercise1():
    text = "This will work great as it is"
    unique_letters = set(text)
    print("Number of unique case sensitive letters", len(unique_letters))

    unique_letters = set(text.casefold())  # set(text.lower()) for python 2.7
    print("Number of unique case insensitive letters", len(unique_letters))

    user_input = input("Enter some text:")
    unique_letters = set(user_input.casefold())  # set(text.lower()) for python 2.7
    print("Unique case insensitive letters", len(unique_letters))


if __name__ == '__main__':
    exercise1()
