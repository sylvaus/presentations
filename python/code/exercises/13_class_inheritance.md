Class inheritance is the concept of reusing a class methods/attributes in other classes without having to rewrite them.
A class that inherits from one or several classes is called a derived class or child class or subclass.  
A class which is inherited is called a  super class or base class.

The syntax to inherit from a Base class in python is fairly easy:
```python

class Base:
    def __init__(self):
        self.value = 10

    def print(self):
        print("Called Base print function")
        
    def print2(self):
        print("Called Base print2 function")
        
class Derived(Base):
    def print2(self):
        print("Called Derived print2 function")
        
    def print3(self):
        print("Called Derived print3 function")
    
derived = Derived()

print(derived.value)     # print 10 coming from the base class implementation
print(derived.print())   # print "Called Base print function" coming from the base class implementation
print(derived.print2())  # print "Called Derived print2 function" coming from the derived class implementation since we Derived has one implementation
print(derived.print3())  # print "Called Derived print3 function" coming from the derived class implementation

```

The print2 method is implemented in Base and Derived, in this case we say that this method has been
__overriden__, and thus an instance of the Derived class will use the definition in Derived instead of the one in the Base class

Sometimes, you may want to reuse the function of the base class in the methods of the derived class.
This can be achieved by using the super keyword.
This is especially useful when overriding the `__init__` method to reuse the base class constructor
Syntax:
```python
class AffineFunction: 
    """
    Affine function defined as y = a * x + b where a is the slope and b is the intercept 
    """
    def __init__(self, slope, intercept):
        self._slope = slope
        self._intercept = intercept
        
    def calculate_y(self, x):
        return self._slope * x + self._intercept
         
class LinearFunction(AffineFunction): 
    """
    Linear function defined as y = a * x where a is the slope 
    """
    def __init__(self, slope):
        super().__init__(slope, 0) # the intercept function is always 0 for linear function
        
    def calculate_y(self, x):
        return self._slope * x + self._intercept
```

A complete example of inheritance would be the Monster class discussed in 10_class_init.md, 
this class can be used as the base class for all the monsters of a game 

```python
class Monster:
    def __init__(self, name, atk, df, hp, max_hp):
        self._name = name
        self._atk = atk
        self._df = df
        self._hp = hp
        self._max_hp = max_hp
        
    @property
    def name(self):
        return self._name
        
    @property
    def hp(self):
        return self._hp  

    def attack(self, other):
        other.defend(self._atk)

    def defend(self, attack):
        damage = max(attack - self._df, 0)
        self._hp = max(self._hp - damage, 0)

    def rest(self):
        recovered_hp = self._max_hp // 5
        self._hp = min(self._hp + recovered_hp, self._max_hp)

class Gobelin(Monster):
    def __init__(self):
        super().__init__("Gobelin", 10, 7, 12, 12)
        
class Boss(Monster):
    def __init__(self):
        super().__init__("Boss", 30, 20, 50, 50)
        
    def attack(self, other): # special behavior for Boss attack
        # if the boss hp is below 10% its attack is multiplied by 1.5
        if self._hp < (self._max_hp * 0.1): 
            other.defend(self._atk * 1.5)
        else:
            other.defend(self._atk)
```
