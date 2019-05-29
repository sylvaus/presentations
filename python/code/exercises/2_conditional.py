"""
Python offers three conditions keyword: if elif and else
Syntax:
if condition:
    code
elif condition:
    code
else:
    condition

Example:
if nb > 10000:
    print("big number")
elif nb > 100:
    print("medium number")
else:
    print("small number")

Exercise 1:
Write a function that takes one integer parameter and print "even" if the number is even or odd otherwise
"""


def exercise1(nb):
    # Put your solution here
    pass


"""
Exercise 2:
Write a function that takes one integer parameter representing the age of the operator
and print a comment on the age
"""


def exercise2(age):
    # Put your solution here
    pass


if __name__ == '__main__':
    print("Input number is 14")
    exercise1(14)
    print("Input number is 25")
    exercise1(25)

    print("Peter is 54")
    exercise2(54)
    print("Laura is 24")
    exercise2(24)
    print("george is 17")
    exercise2(17)


def solution1(nb):
    if (nb % 2) == 0:
        print("even")
    else:
        print("odd")


def solution2(age):
    if age > 50:
        print("This pretty old")
    elif age > 20:
        print("This is middle aged")
    else:
        print("This is young")
