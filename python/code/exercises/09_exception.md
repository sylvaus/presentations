Exception is a nice tool to handle events that should not happen in the normal flow of the program but should still
be taken into consideration.

For example, while parsing some text the function int(), that takes a string and returns an int, will raise an exception
if the given string cannot be converted into an int, e.g, int("a") will raise an Exception

When an exception is raised all code is ignored until a catch is reached.
This can be really helpful when the handling of the error is done really far from where the exception is raised
and not have to return the error from every value

To raise an exception, the code syntax is:
```python
raise Exception(text)
# Exception could be replaced by any class that inherit from Exception (inheritance will be presented later)
```
The syntax to catch an exception is:
```python
# Catch any Exception
try:
    # code that may throw
except Exception as e: # the exception raise will be in variable e
    # code to handle exception

# Catch a specific Exception: MyException
try:
    # code that may throw
except MyException as e: # the exception raise will be in variable e
    # code to handle exception

# Catch multiple Exceptions:
try:
    # code that may throw
except MyException1 as e:
    # code to handle exception
except MyException2 as e:
    # code to handle exception
except MyException3 as e:
    # code to handle exception
```

An interesting construct is the try-catch-else which canbe useful if code should ne executed
only if no exception was thrown
```python
try:
    # code that may throw
except MyException as e:
    # code to handle exception
else:
    # code that should be executed if no exception is raised
```
