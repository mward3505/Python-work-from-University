"""
Project: #5
Author: Matthew Ward
Course: CS 2420
Date: 03/25/2021

Description: This is to help me understand how binary trees work and preforming the necessary actions to implement it

Lessons Learned: Learned how to traverse through a binary tree, add, remove, and how to rebalance the tree.

"""
from pathlib import Path
from string import whitespace, punctuation
from bst import BST


class Pair:
    """ Encapsulate letter,count pair as a single entity.

    Realtional methods make this object comparable
    using built-in operators.
    """
    def __init__(self, letter, count=1):
        self.letter = letter
        self.count = count
    
    def __eq__(self, other):
        return self.letter == other.letter
    
    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'
    
    def __str__(self):
        return f'({self.letter}, {self.count})'


def make_tree():
    """ A helper function to build the tree.

    The test code depends on this function being available from main.
    :param: None
    :returns: A binary search tree
    """
    my_tree = BST()
    with open("G:\\development\\CS2420\\projectFive\\around-the-world-in-80-days-3.txt",
              "r") as f:
        while True:
            c = f.read(1)
            if not c:
                break
            if c.isalnum():
                try:
                    found = my_tree.find(Pair(c))
                    found.count += 1
                except ValueError:
                    my_tree.add(Pair(c))

    print(my_tree)
    return my_tree


def main():
    """ Program kicks off here.

    """
    pass


if __name__ == "__main__":
    main()
