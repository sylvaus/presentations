"""
Exercise 1:
Fill function exercise1 to count how many times each character appears in the text

Optional task 1: look at defaultdict and try to improve the code: https://docs.python.org/3/library/collections.html#collections.defaultdict
Optional task 2: look at counter and try to improve the code: https://docs.python.org/3/library/collections.html#collections.Counter
"""


def exercise1():
    text = "this will work great"
    letter_counters = {}
    for char in text:
        if char not in letter_counters:
            letter_counters[char] = 0

        letter_counters[char] += 1
        # equivalent to letter_counters[char] = letter_counters[char] + 1
    print("Exercise 1 Standard Dict Solution", letter_counters)

    # Default Dict solution
    from collections import defaultdict
    letter_counters = defaultdict(int)
    for char in text:
        letter_counters[char] += 1
    print("Exercise 1 Default Dict Solution", letter_counters)

    # Counter Solutions
    from collections import Counter
    letter_counters = Counter(text)
    print("Exercise 1 Counter Solution", letter_counters)


if __name__ == '__main__':
    exercise1()

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
    nb_categories = {}
    for nb in values:
        key = get_number_of_digits(nb)
        if key not in nb_categories:
            nb_categories[key] = []

        nb_categories[key].append(nb)
        # equivalent to letter_counters[char] = letter_counters[char] + 1
    print("Exercise 2 Standard Dict Solution", nb_categories)

    # Default Dict solution
    from collections import defaultdict
    nb_categories = defaultdict(list)
    for nb in values:
        key = get_number_of_digits(nb)
        nb_categories[key].append(nb)
    print("Exercise 2 Default Dict Solution", nb_categories)


if __name__ == '__main__':
    exercise2()
