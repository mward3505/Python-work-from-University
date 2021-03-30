"""Stack class that adds items to a list and returns them in reverse order"""


class Stack:
    """Constructs a stack so that it can be used"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Checks to see if the stack is empty"""
        return self.items == []

    def push(self, item):
        """Adds an item to the stack"""
        self.items.append(item)

    def pop(self):
        """Pops an item off the stack if there are values else raises an error"""
        if not self.items:
            raise IndexError

        return self.items.pop()

    def top(self):
        """Returns the top item of the stack"""
        if not self.items:
            raise IndexError

        return self.items[-1]

    def size(self):
        """Returns the size of the stack"""
        return len(self.items)

    def clear(self):
        """Clears the stack"""
        self.items = []
