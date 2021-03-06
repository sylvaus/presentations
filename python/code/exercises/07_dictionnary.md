A dictionary is a collection of pair: key and value (sometimes called map in other programming language)           
Another way to see a dictionary, is to view dictionaries as list that can use any type (not only int) as indexes

Python doc: https://docs.python.org/3/library/stdtypes.html#dict

Advantages:
* A dictionary is great structure to organize elements in group using indexes that are not continuous and not integer
* For example: given a list of books, it is easy to quickly retrieve book given its title by
* creating a dictionary where the key is the title and the value is the book

Disadvantages:
* You cannot add an element to the dictionary without a key
* And if there is already an element associated to the key, the element will be replaced
* Accessing elements is slower than a list

Syntax:
```python
# Creation:
my_dict = dict() # Empty
# or
my_dict = {} # Empty
# or
my_dict = {"key 1": "value1", "key 10": "value10", "key 4": "value4", "key 12": "value12"}

# Adding:
my_dict[key] = value

# Check if element is a key:
if element in my_dict:
    code

# Accessing:
# All values
for element in my_dict.values():
    code

# All keys
for element in my_dict.keys():
    code

# All pairs: key, value
for element in my_dict.items():
    code

# One element
element = my_dict["key 1"] # may throw an exception if the key does not exist
element = my_dict.get("key 1", "default") # return the value if the key exists otherwise default

# Removing element:
del my_dict[42]
# or
value = my_dict.pop(42) # remove and returns the value
```