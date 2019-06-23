"""
Exercise 1
Create a function that return the given string if the len of the string is below 10 and "Too long to display" otherwise
Then use this function on all the elements of str_list in exercise1 function

Optional 1: Have a look at the map function and try to use to apply your function to all the element of the list: 
    Doc: 
        * https://docs.python.org/3/library/functions.html#map
        * http://book.pythontips.com/en/latest/map_filter.html
"""


def func(string):
    if string < 10:
        return string
    else:
        return "too long to display"


def exercise1():
    str_list = ["bonjour", "hello", "saluti", "comment ca va", "how are you doing", "come stai"]
    for element in str_list:
        print(element)


exercise1()
