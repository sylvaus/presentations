"""
List and tuple are simples structure and are used everywhere in python

A list as its name indicates is a list of elements.
There are various ways to create a list:
# Empty list
my_list = list() using the list constructor
my_list = []

# With initial values
my_list = [1, 34, 64, "str"]

# Access element
var = my_list[2] # The list is zero indexed and thus 64 would be returned
# Negative index can be used to index element from the end
var = my_list[-1] # This return the last element

Elements can be added or remove from the list
# Add one element
my_list.append("new element")

# Add another list
my_list.extend(other_list)

# Remove one element by value
my_list.remove("str")

# Remove one element by index
delete my_list[2] # Remove the third element (The list is zero indexed)
var = my_list.pop(2) # Remove the third element and returns it

# Remove all elements
my_list.clear()

# Slicing: this refers to taking sub-section of the list
# The syntax is:
sub_list = my_list[start_index:end_index]
or
sub_list = my_list[start_index:end_index:step]
# The start_index is the index of the first element to include in the sub_list
# The end_index is the index of the first element to NOT include in the sub_list
# The step is the number to add to the previous index to know which is the next index to add

# if start_index is not given, its value will be 0
# if end_index is not given, its value will be len(my_str)
# if step is not given, its value will be 1

A tuple has the same property as a list except for that a tuple cannot be modified: no value can be added or removed

"""

"""
Exercise 1

Given the my_list, print the sum of the first element and the last element of my-list
"""


def exercise1():
    my_list = [4878, 874566, 97, 6476, 797, 64, 7, 94, 789, 78, 489, 77, 468, 79, 7, 7, 98, 874, 979, 97468]


"""
Exercise 2

Given the my_list listing the 100 (0-99) first integers, 
print the list of the 50 first even numbers and 
print the list of the 50 first odd numbers
"""


def exercise2():
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,]



