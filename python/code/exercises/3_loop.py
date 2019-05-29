"""
Python offers two keywords for looping
while and for

Syntax:
for element in elements:
    code

while condition:
    code

Exercise 1:
Write a function that prints all the element in the elements parameter

Exercise 2:
Write a function that print all the elements inferior to 10 in the given sorted list
"""


def exercise1(elements):
    # Put your code here
    pass


def exercise2(elements):
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
