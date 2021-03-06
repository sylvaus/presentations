"""
Exercise 1

Given the my_list, print the sum of the first element and the last element of my-list
"""


def exercise1():
    my_list = [4878, 874566, 97, 6476, 797, 64, 7, 94, 789, 78, 489, 77, 468, 79, 7, 7, 98, 874, 979, 97468]
    # Best solution
    print(my_list[0] - my_list[-1])
    # Also works
    print(my_list[0] + my_list[len(my_list) - 1])


"""
Exercise 2

Given the my_list listing the 100 (0-99) first integers, 
print the list of the 50 first even numbers and 
print the list of the 50 first odd numbers

Hint: use slicing
"""


def exercise2():
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
               29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
               55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
               81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, ]
    print("Even values:", my_list[0::2])
    print("Odd values:", my_list[1::2])
