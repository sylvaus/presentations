"""
Exercise 1

Create a class called Counter with two methods:
  * increment -> increments an internal counter
  * print_counter -> print the counter value
"""


class Counter:
    def __init__(self):
        self._increment = 0

    def increment(self):
        self._increment += 1

    def print_counter(self):
        print(self._increment)


"""
Exercise 2

Create a class called MyList with a constructor taking the list name and two methods:
  * add_elt -> add an element to the internal list
  * clear -> clear the internal list
  * print_list -> print the name of the list followed by the elements of the list
"""


class MyList:
    def __init__(self):
        self._list = []

    def add_elt(self, elt):
        self._list.append(elt)

    def clear(self):
        self._list.clear()

    def print_list(self):
        print(self._list)
