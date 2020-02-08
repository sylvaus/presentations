"""
Exercise 1

Implement a class Inventory that contains a collection of items.
Implement the + method to be able to add two inventories
Implement the representation method in a way that the items in the inventory will be printed
"""


class Inventory:
    def __init__(self, items: list = None):
        if items is None:
            items = []
        self._items = items

    def add_item(self, item):
        self._items.append(item)

    def __add__(self, other: "Inventory"):
        return Inventory(self._items + other._items)

    def __iadd__(self, other: "Inventory"):
        self._items.extend(other._items)
