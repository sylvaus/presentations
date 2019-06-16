"""
Exercise 1:
Fill exercise1 function to print all the element in the list of elements parameter element_list
"""


def exercise1(element_list):
    for element in element_list:
        print(element)


"""
Exercise 2:
Fill exercise2 function to print all the elements inferior to 10 in the given sorted list sorted_list
"""


def exercise2(sorted_list):
    index = 0
    # For solution
    for elt in sorted_list:
        # If an element is bigger than 10, we can exist the loop since the list is sorted
        if elt >= 10:
            break
        print(elt)

    # While solution
    while index < len(sorted_list):
        # If an element is bigger than 10, we can exist the loop since the list is sorted
        if sorted_list[index] >= 10:
            break
        print(sorted_list[index])
        index += 1


if __name__ == '__main__':
    print("Exercise 1")
    exercise1(list(range(0, 10, 3)))
    print("Exercise 2")
    exercise2(list(range(0, 40, 2)))
