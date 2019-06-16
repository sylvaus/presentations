List and tuple are simples structure and are used everywhere in python

A list as its name indicates is a list of elements.
There are various ways to create a list:
Empty list
```python
my_list = list() # using the list constructor
my_list = []
```
With initial values
```python
my_list = [1, 34, 64, "str"]
```
Access element
```python
var = my_list[2] # The list is zero indexed and thus 64 would be returned
# Negative index can be used to index element from the end
var = my_list[-1] # This return the last element
```

You need to be careful while accessing an element with an indexing an exception will occur if the list 
is shorter than the index asked.
The length of a list can be obtained using the len keyword
```python
length = len(my_list)
```

Elements can be added or remove from the list
Add one element
```python
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
```

Slicing: this refers to taking sub-section of the list
The syntax is:
sub_list = my_list[start_index:end_index]
or
sub_list = my_list[start_index:end_index:step]
The start_index is the index of the first element to include in the sub_list
The end_index is the index of the first element to NOT include in the sub_list
The step is the number to add to the previous index to know which is the next index to add

if start_index is not given, its value will be 0, e.g., my_list[:end:step] or my_list[:end]
if end_index is not given, its value will be len(my_str), e.g., my_list[start::step] or my_list[start:]
if step is not given, its value will be 1, e.g., my_list[start:end]

A tuple has the same property as a list except for that a tuple cannot be modified: no value can be added or removed