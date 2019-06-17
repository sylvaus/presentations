A set is a structure that store unique values without any particular order
Python doc: https://docs.python.org/3/library/stdtypes.html#set

Advantages:
* A set is great structure to extract all the unique elements of a collection of elements
* Moreover, looking if an element is in a set is a lot faster than looking if an element is an list.

Disadvantages:
* Elements of the set cannot be accessed in any particular order

Syntax:
```python
# Creation:
my_set = set() # Empty
# or
my_set = {0, 1, 4, 5, 6}
# or
my_set = set([0, 4, 4, 6, 6]) # Creation from list, returns {0, 4, 6}

# Adding:
my_set.add(42)

# Check if element belong to set:
if element in my_set:
    # code

# Accessing:
# All elements
for element in my_set:
    # code

# One element
element = my_set.pop() # remove and return one element

# Removing element:
my_set.remove(42)
```
