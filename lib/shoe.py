#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Internal storage for size
        self.size = size  # Use the property setter to validate
        self.condition = None  # Condition attribute, initially None

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"  # After repair, set condition to "New"
