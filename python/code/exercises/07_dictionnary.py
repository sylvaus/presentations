"""
Exercise 1:
Fill function exercise1 to count how many times each character appears in the text 

Optional task 1: look at defaultdict and try to improve the code: https://docs.python.org/3/library/collections.html#collections.defaultdict
Optional task 2: look at counter and try to improve the code: https://docs.python.org/3/library/collections.html#collections.Counter
"""


def exercise1():
    text = "this will work great"
    # Your code


"""
Exercise 2:
Fill function exercise1 to split the given list of numbers based on the number of digits of the number.
To get the number of digit of a number, use the given function: get_number_of_digits
For example:
    for 11, the key would be 2
    for 25, the key would be 2
    for 250, the key would be 3
So, if the input was [11, 25, 250]
The result would be
 * key:2, value: [11, 25]
 * key:3, value: [250]

Optional task 1: look at defaultdict and try to improve the code: https://docs.python.org/3/library/collections.html#collections.defaultdict
"""

from math import log10, floor


def get_number_of_digits(number):
    return floor(log10(number)) + 1


def exercise2():
    values = [100214545, 45421, 4578, 1, 787, 47878, 789, 12, 78, 7847, 454, 787, 13358, 789, 12, 7, 774]
