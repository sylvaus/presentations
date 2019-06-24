In the previous exercise, we've seen that classes are an elegant way to hide data to the user of the class.  
However, sometimes we may want to give the user access to part of our object, maybe for reading, maybe for writing 
and maybe in a controlled way.

We could achieve this by writing a setter for writing the data and/or a getter for writing the data.
For example, if we want to access the health point of the Monster class previously presented, 
the new class could look something like this:

```python
class Monster:
    def __init__(self, atk, df, hp, max_hp):
        self._atk = atk
        self._df = df
        self._hp = hp
        self._max_hp = max_hp

    def set_hp(self, val):
        if val > self._max_hp:
            self._hp = self._max_hp
        elif val < 0:
            self._hp = 0
            
    def get_hp(self):
        return self._hp
        
    # Rest of the the class implementation
```

This implementation is fine but python give us a tool to make this a lot more intuitive for the user.
It would seem a lot better if could get the health point of my monster by typing `monster.hp` instead of `monster.get_hp()`

You could do that by making `_hp` public but then the user could change it without protection.
The real solution is to use the property decorators:
 * @property              for the getter
 * @PROPERTY_NAME.setter  for the setter
 
The syntax to use then is pretty straightforward:
```python
class MyClass:
    @property
    def prop_name(self):
        pass # code that returns the property value (that may have to be computed)
    
    @prop_name.setter
    def prop_name(self, value):
        pass # code that set the internal data and may perform check before doing so 
```
CAREFUL: you can only create a setter if you have getter (but you can write a getter without a setter)

with this, we can rewrite the Monster class in a more intuitive way and add a property to easily check if it is alive:
```python
class Monster:
    def __init__(self, atk, df, hp, max_hp):
        self._atk = atk
        self._df = df
        self._hp = hp
        self._max_hp = max_hp

    @property 
    def hp(self):
        return self._hp
        
    @hp.setter
    def hp(self, val):
        if val > self._max_hp:
            self._hp = self._max_hp
        elif val < 0:
            self._hp = 0
        
    # Rest of the the class implementation
    
    @property
    def alive(self):
        if self._hp > 0:
            return True
        return False
```

