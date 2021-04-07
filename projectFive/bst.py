"""
This file is to help a construct a binary tree
"""


class TreeNode:
    """
    This creates tree nodes to help create the binary tree
    """
    def __init__(self, val=None, par=None):
        """Constructs the node with default values"""
        self.left = None
        self.right = None
        self.value = val
        self.parent = par

    def left_child(self):
        """Returns the left child"""
        return self.left

    def right_child(self):
        """Returns the right child"""
        return self.right

    def set_value(self, val):
        """Sets the nodes value"""
        self.value = val

    def get_value(self):
        """Returns the nodes value"""
        return self.value

    def set_left(self, node):
        """Sets the left child for the node"""
        self.left = node
        if node is not None:
            node.parent = self
        return node

    def set_right(self, node):
        """Sets the right child for the node"""
        self.right = node
        if node is not None:
            node.parent = self
        return node

    def get_parent(self):
        """Returns the parent for the node"""
        return self.parent

    def level(self):
        """Helps determine how deep we are into the tree"""
        result = 0
        temp = self
        while temp.parent is not None:
            temp = temp.parent
            result += 1
        return result

    def add(self, item):
        """Adds an node to the tree"""
        if item < self.get_value():
            if self.left_child() is None:
                self.set_left(TreeNode(item))
            else:
                self.left_child().add(item)
        else:
            if self.right_child() is None:
                self.set_right(TreeNode(item))
            else:
                self.right_child().add(item)

    def pre_order(self, result_list):
        """Helps order the tree with checking the node first and then it's children"""
        result_list.append(self.value)
        if self.left_child() is not None:
            self.left_child().pre_order(result_list)
        if self.right_child() is not None:
            self.right_child().pre_order(result_list)

    def in_order(self, result_list):
        """Helps order the tree with checking the left child first and then the node and then the right child"""
        if self.left_child() is not None:
            self.left_child().in_order(result_list)
        result_list.append(self.value)
        if self.right_child() is not None:
            self.right_child().in_order(result_list)

    def post_order(self, result_list):
        """Helps order the tree with checking the children first and then the node"""
        if self.left_child() is not None:
            self.left_child().post_order(result_list)
        if self.right_child() is not None:
            self.right_child().post_order(result_list)
        result_list.append(self.value)

    def find(self, item):
        """Finds the current item that is passed in the tree"""
        if self.value == item:
            return self.value
        elif item < self.value:
            if self.left_child() is not None:
                return self.left_child().find(item)
            else:
                raise ValueError()
        else:
            if self.right_child() is not None:
                return self.right_child().find(item)
            else:
                raise ValueError()

    def pre_orderStr(self):
        """Helps print the tree using pre_order"""
        if self.left_child() is not None:
            self.left_child().pre_orderStr()
        if self.right_child() is not None:
            self.right_child().pre_orderStr()
        print("".ljust(self.level() * 2), str(self.value))

    def __str__(self):
        """Prints the node"""
        return str(self.value)


class BST:
    """Helps build a tree using the TreeNode class"""
    def __init__(self):
        """Helps start the tree"""
        self.root = None

    def is_empty(self):
        """Checks the tree to see if it's empy"""
        return self.root is None

    def size(self):
        """Returns the size of the tree"""
        return self.__size(self.root)

    def __size(self, node):
        """Helps the size method"""
        if node is None:
            return 0
        result = 1
        result += self.__size(node.left)
        result += self.__size(node.right)
        return result

    def add(self, item):
        """Adds the values to the tree using TreeNode's add method"""
        if self.root is None:
            self.root = TreeNode(item)
        else:
            self.root.add(item)
        return self.root

    def find(self, item):
        """Finds the item in the tree"""
        if self.root is not None:
            return self.root.find(item)
        raise ValueError()

    def remove(self, item):
        """Removes the desired node from the tree"""
        return self.__remove(self.root, item)

    def __remove(self, node, item):
        """Helps the remove method"""
        if node is None:
            return node

        if item < node.get_value():
            node.set_left(self.__remove(node.left_child(), item))
        elif item > node.get_value():
            node.set_right(self.__remove(node.right_child(), item))
        else:
            if node.left_child() is None:
                temp = node.right_child()
                if temp is not None:
                    temp.parent = node.parent
                node = None
                return temp
            elif node.right_child() is None:
                temp = node.left_child()
                if temp is not None:
                    temp.parent = node.parent
                node = None
                return temp
            else:
                minNode = self.__minValueNode(node.right_child())

                node.set_value(minNode.get_value())

                node.set_right(self.__remove(node.right_child(), minNode.get_value()))

        return node

    def __minValueNode(self, node):
        """Determines the minimum node needed for remove"""
        current = node
        while current.left_child() is not None:
            current = current.left_child()
        return current

    def inorder(self):
        """Orders the tree using TreeNode's in_order method"""
        result = []
        if self.root is not None:
            self.root.in_order(result)
        return result

    def preorder(self):
        """Orders the tree using TreeNode's pre_order method"""
        result = []
        if self.root is not None:
            self.root.pre_order(result)
        return result

    def postorder(self):
        """Orders the tree using TreeNode's post_order method"""
        result = []
        if self.root is not None:
            self.root.post_order(result)
        return result

    def rebalance(self):
        """Balance the tree in the proper structure"""
        ordered_list = self.inorder()
        self.root = None
        self.__rebalance(ordered_list, 0, len(ordered_list) - 1)

    def __rebalance(self, ordered_list, low, high):
        """Helps the rebalance method"""
        if low <= high:
            mid = (high - low) // 2 + low
            self.add(ordered_list[mid])
            self.__rebalance(ordered_list, low, mid - 1)
            self.__rebalance(ordered_list, mid + 1, high)

    def height(self):
        """Returns how deep we are into the tree"""
        return self.__recursiveHeight(self.root, 0)

    def __recursiveHeight(self, node, current):
        """Helps the height method to recurse through the tree"""
        if current == 0:
            current = current + 1
        left_value = current
        rightValue = current
        if node.left_child() is not None:
            left_value = self.__recursiveHeight(node.left, current + 1)
        if node.right_child() is not None:
            rightValue = self.__recursiveHeight(node.right, current + 1)

        return max(left_value, rightValue)

    def __strInsert(self, value, position, char):
        """Prints the tree"""
        return str(value[:position] + char + value[position + 1:])

    def __str__(self):
        """Helps print the tree"""
        if self.root is not None:
            self.root.pre_orderStr()
        return ""
