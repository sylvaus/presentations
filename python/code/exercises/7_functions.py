"""
Functions are a great way to divide your code in manageable part
Moreover, when you divide your code into functions, it encourages reusability and improves the readability

The syntax of writing a simple function is straightforward:
def function_name(param1, param2, param3):
    function_code

Example: function that prints lower case
def print_lower(text):
    lower_text = text.lower()
    print(lower_text)

print_lower("Bonjour") # will print: bonjour
# lower_text is not available here

Another advantage of using functions is that the variables declared in the function will not be available outside
the function, allowing you to reuse the same name in different functions without any risk of the variable being already
used

This is nice but functions that gives no value in return when they are called have limited usage.
To return a value (or several), you must use the return keyword
The return keyword ends the functions and returns the given variables to the caller

Syntax:
def function_name(param1, param2, param3):
    function_code
    return var1, var2

Example 1 : function that returns the square of the value

def square(val):
    val_square = val * val
    return val_square

result = square(4) # Result will be 16

Example 2 (multiple return values): function that returns the min and max of a list

def get_min_max(nb_list):
    min_elt = min(nb_list)
    max_elt = max(nb_list)
    return min_elt, max_elt

min_val, max_val = get_min_max([0,1,3,4,1,47,-6,79]) # This will return -6 and 79

Another nice feature when defining a function in python is default value.
By defining a default value for a parameter you show to the user the standard way to use the function
but still allow the operator to use the options if they want to use it
Syntax:
def function_name(param1, param_default=default_val):
    function code

Example:
def print_val(text, add_end_period=True):
    if add_end_period:
        print(text + ".")
    else:
        print(text)

print_val("Hello") # will print: Hello.
print_val("Hello", False) # will print: Hello # the period was not added

"""

"""
Exercise 1
Create a function that return the given string if the len of the string is below 10 and "Too long to display" otherwise
Then use this function on all the elements of str_list in exercise1 function

Optional 1: Have a look at the map function and try to use to apply your function to all the element of the list: 
    Doc: 
        * https://docs.python.org/3/library/functions.html#map
        * http://book.pythontips.com/en/latest/map_filter.html
"""


def exercise1():
    str_list = ["bonjour", "hello", "saluti", "comment ca va", "how are you doing", "come stai"]
