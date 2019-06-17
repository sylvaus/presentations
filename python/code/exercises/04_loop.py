"""
Exercise 1:
Fill exercise1 function to print all the element in the list of elements parameter element_list
"""


def exercise1(element_list):
    # Put your code here
    pass


"""
Exercise 2:
Fill exercise2 function to print all the elements inferior to 10 in the given sorted list sorted_list
"""


def exercise2(sorted_list):
    # Put your code here
    pass


if __name__ == '__main__':
    print("Exercise 1")
    exercise1(list(range(0, 10, 3)))
    print("Exercise 2")
    exercise2(list(range(0, 40, 2)))


def solution1(elements):
    for element in elements:
        print(element)


def solution2(elements):
    index = 0
    while elements[index] < 10:
        print(elements[index])
        index += 1
