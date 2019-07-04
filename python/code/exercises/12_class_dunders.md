Dunders in python are all the methods/variables whose name start and end by double underscore.   
They are most of the time special operation/values:
 * `__file__` contains the path to the current python file
 * `__init__` in a class is the function called when constructing a class 
 
A first usage of defining dunders for a class is to implement the + - * / == operations.   
The simplest example is a 2D vector (x number, y number), you want to be able to add/subtract vectors elementwise:

The implementation could be:
```python
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other): # + operation
        return Vector2D(self.x + other.x, self.y + other.y)
     
    def __sub__(self, other): # - operation
        return Vector2D(self.x + other.x, self.y + other.y)
        
    def __eq__(self, other): # == operation
        if type(other) != Vector2D:
            return False
        return (self.x == other.x) and (self.y == other.y)
        
vec = Vector2D(1, 2)
vec2 = Vector2D(3, 2)

vec_sum = vec + vec2
print("Are equal :", vec_sum == Vector2D(4, 4))

```

Another simple usage is improve the simplicity of debugging 
by making the string representation of the class instance more explicit.
When asking the for the string representation of an instance, the function `__str__` is called
if it exists otherwise `__repr__` is called if exists otherwise the default string representation 
for object is used.

Example with the Vector 2D
```python
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "x:{}, y:{}".format(self.x, self.y)


    def __repr__(self):
        return "Vector 2D x:{}, y:{}".format(self.x, self.y)

vec = Vector2D(1, 2)
print(vec)
print(str(vec))
print(repr(vec))
print("{}".format(vec))

```

If you have to choose between implementing `__str__` or `__repr__`, implement `__repr__` since the call 
to str on the object will fallback on `__repr__` if `__str__` does not exits.

If you implement the two, `__repr__` should contain more information than `__str__`: [complete reason](https://docs.python.org/3/reference/datamodel.html#object.__repr__)

A full list of the dunders (or magic methods): [Python Documentation](https://docs.python.org/3/reference/datamodel.html)