"""
Classes are a powerful tool to:
    * group together data and  actions that can be applied on the data
    * hide away the data that should not access directly

The syntax for defining a class with only attributes is the following:
class MyClass:
    class_attr = "class attr"
    def __init__(self, attribute):
        self.obj_attr = attribute

You can then use it this way
obj = MyClass("My object attribute")
print(obj.obj_attr) # It will print: My first attribute My second attribute
print(obj.class_attr, MyClass.class_attr) # It will print: class attr class attr

You may be wondering about the two new keywords __init__ and self and the difference between class_attr and obj_attr

The __init__ is the function being called when the object is constructed (e.g. when doing MyClass("a1"))
and thus it is used to set the object attribute initial values

The self keyword is referring to the object that is being created.
In the previous example, self would refer to obj and thus,
when doing "self.obj_attr = attribute" we set the attribute obj_attr of obj

Now onto the difference between the attributes class_attr and obj_attr,
as their name indicate one is a class attribute and one is an object attribute

An object attribute is only attached to a single object which means
that every time you call MyClass(attribute), will have its own independent attribute

It is the opposite for class attributes, they are shared between the different object of the same class

To experiment this you can try the following code using the previously defined MyClass:
obj = MyClass("Object 1 attribute")
obj2 = MyClass("Object 2 attribute")

print(obj.obj_attr, obj.class_attr) # will print: Object 1 attribute class attr
print(obj2.obj_attr, obj2.class_attr) # will print: Object 2 attribute class attr

# Modify obj1 attribute
obj.obj_attr = "Object 1 was modified"

print(obj.obj_attr, obj2.obj_attr) # will print: Object 1 was modified Object 2 attribute -> Only obj was modified

# Modifying class Attribute
MyClass.class_attr = "Modified class attribute"

print(obj.class_attr, obj2.class_attr) # will print: Modified class attribute Modified class attribute -> The two objects were modified


An example of a useful usage of a class would a monster in a video game
A monster data would be:
    * attack power (atk)
    * defense (df)
    * health point (hp)
    * max health point (max_hp)
A monster methods would be:
    * attack(other) attack other creature
    * defend(attack_force) receive an attack from another creature
    * rest() restore 1/5 of max hp

The python code for the monster class would be
"""


class Monster:
    def __init__(self, atk, df, hp, max_hp):
        self._atk = atk
        self._df = df
        self._hp = hp
        self._max_hp = max_hp

    def attack(self, other):
        other.defend(self._atk)

    def defend(self, attack):
        # Damage is the attack minus the defense of the monster
        # and take the max with 0 to ensure the damage is a positive number
        damage = max(attack - self._df, 0)
        # The new health point value is current health point minus damage
        # and like the damage, the health point value cannot be negative so we can take the max value with zero
        self._hp = max(self._hp - damage, 0)

    def rest(self):
        # The // means integer division to ensure recovered_hp is an integer
        recovered_hp = self._max_hp // 5
        # Min with max_hp is used since the monster cannot recover more than its max_hp
        self._hp = min(self._hp + recovered_hp, self._max_hp)

