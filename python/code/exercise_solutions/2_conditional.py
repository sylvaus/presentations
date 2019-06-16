"""
Exercise 1:
Write a function that takes one integer parameter and print "even" if the number is even or odd otherwise

Hint: the remainder of a division is obtained by using the module operator %. Example 5 % 3 will be 2
"""


def exercise1(nb):
    if (nb % 2) == 0:
        print("even")
    else:
        print("odd")


"""
Exercise 2:
Fill the exercise2 function with code which prints a comment based on the parameter age (this parameter will be an int)
, e.g. if the age given is smaller than yours you can print "You're young" 
if it is the same "We're the same age so cool" 
and older : "You must be wise". 
"""


def exercise2(age):
    if age > 50:
        print("This pretty old")
    elif age > 20:
        print("This is middle aged")
    else:
        print("This is young")


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
