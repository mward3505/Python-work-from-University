#!/usr/bin/env python
# coding: utf-8

# In[4]:


class TreeNode:
    def __init__(self, val = None, par = None):
        self.left = None
        self.right = None
        self.value = val
        self.parent = par

    def left_child(self):
        return self.left
    
    def right_child(self):
        return self.right
    
    def set_value(self, val):
        self.value = val

    def get_value(self):
        return self.value
    
    def set_left(self, node):
        self.left = node
        node.parent = self
        return node
    
    def set_right(self, node):
        self.right = node
        self.parent = self
        return node
    
    def get_parent(self):
        return self.parent
    
    def level(self):
        result = 0
        temp = self
        while temp.parent is not None:
            temp = temp.parent
            result += 1
        return result

    def add(self, item):
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
        # Print ourselves
        result_list.append(self.value)
        # Recurse Left
        if self.left_child() is not None:
            self.left_child().pre_order(result_list)
        # Recurse Right
        if self.right_child() is not None:
            self.right_child().pre_order(result_list)

    def post_order(self, result_list):
        if self.left_child() is None:
            self.left_child().in_order(result_list)
        if self.right_child() is not None:
            self.right_child().in_order(result_list)
        return result_list.append(self.value)

    def in_order(self, result_list):
        if self.left_child() is None:
            self.left_child().in_order(result_list)
        result_list.append(self.value)
        if self.right_child() is not None:
            self.right_child().in_order(result_list)

    def find(self, item):
        if self.value == item:
            return self.value
        elif item < self.value:
            if self.left_child() is not None:
                return self.left_child().find(item)
            else:
                raise ValueError
        else:
            if self.right_child() is not None:
                return self.right_child().find(item)
            else:
                raise ValueError

    def pre_order_str(self):
        if self.left_child() is not None:
            self.left_child().pre_order_str()
        if self.right_child() is not None:
            self.right_child().pre_order_str()
        print("".ljust(self.level() * 2), self.value)

    def __str__(self):
        return str(self.value)


# In[43]:

class Pair:
    ''' Encapsulate letter,count pair as a single entity.

    Realtional methods make this object comparable
    using built-in operators.
    '''

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


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def is_empty(self):
        return self.root is None
    
    def size(self):
        return self.__size(self.root)
    
    def __size(self, node):
        if node is None:
            return 0
        result = 1
        result += self.__size(node.left)
        result += self.__size(node.right)
        return result
    
    def add(self, item):
        if self.root is None:
            self.root = TreeNode(item)
        else:
            self.root.add(item)
        return self.root

    def find(self, item):
        if self.root is not None:
            return self.root.find(item)
        return False
    
    def remove(self, item):
        return self.__remove(self.root, item)
        
    def __remove(self, node, item):
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
        current = node
        while (current.left_child() is not None):
            current = current.left_child()
        return current
        
    def in_order(self):
        result = []
        if self.root is not None:
            self.root.in_order(result)
        return result

    def pre_order(self):
        result = []
        if self.root is not None:
            self.root.pre_order(result)
        return result

    def post_order(self):
        result = []
        if self.root is not None:
            self.root.post_order(result)
        return result

    def __in_orderValues(self, resultList, node):
        if node is None:
            return
        self.__in_orderValues(resultList, node.left_child())
        resultList.append(node.get_value())
        self.__in_orderValues(resultList, node.right_child())
    
    def rebalance(self):
        orderedList = self.in_order()
        self.root = None
        self.__rebalance(orderedList, 0, len(orderedList) - 1)
        
    def __rebalance(self, orderedList, low, high):
        if (low <= high):
            mid = (high - low) // 2 + low
            self.add(orderedList[mid])
            self.__rebalance(orderedList, low, mid - 1)
            self.__rebalance(orderedList, mid + 1, high)
    
    def height(self):
        return self.__recursiveHeight(self.root, 0)
    
    def __recursiveHeight(self, node, current):
        leftValue = current
        rightValue = current
        if node.left_child() is not None:
            leftValue = self.__recursiveHeight(node.left, current + 1)
        if node.right_child() is not None:
            rightValue = self.__recursiveHeight(node.right, current + 1)
        
        return max(leftValue, rightValue)
   
    def __strInsert(self, value, position, char):
        return str(value[:position] + char + value[position + 1:])
           
    def __str__(self):
        if self.root is not None:
            self.root.pre_order_str()
    #     totalLayers = self.height() + 1
    #     totalWidth = (2 ** totalLayers) * 2
    #     nodePosition = [None] * (totalLayers)
    #     for i in range(totalLayers):
    #         nodePosition[i] = [None] * (2 ** i)
    #         for j in range(2 ** i):
    #             nodePosition[i][j] = [0] * 3
    #
    #     lastLayer = nodePosition[totalLayers - 1]
    #     gap = totalWidth // len(lastLayer)
    #     for i in range(len(lastLayer)):
    #         lastLayer[i][0] = i * gap
    #         lastLayer[i][1] = lastLayer[i][0]
    #         lastLayer[i][2] = lastLayer[i][0]
    #
    #     for i in reversed(range(totalLayers - 1)):
    #         for j in range(len(nodePosition[i])):
    #             first = nodePosition[i + 1][j * 2][0]
    #             second = nodePosition[i + 1][j * 2 + 1][0]
    #             nodePosition[i][j][1] = first + 1
    #             nodePosition[i][j][2] = second - 1
    #             nodePosition[i][j][0] = ((second - first) // 2) + first
    #
    #     result = [""] * (totalLayers * 2)
    #     for i in range(1, len(result), 2):
    #         for j in range(totalWidth):
    #             result[i] += " "
    #
    #     self.__nodePrettyPrint(result, self.root, [0] * (totalLayers), nodePosition, ' ')
    #     return "\n".join(result)
    
    # def __nodePrettyPrint(self, result, node, nodeList, nodePosition, char):
    #     level = node.level()
    #     startLine = nodePosition[level][nodeList[level]][1]
    #     endLine = nodePosition[level][nodeList[level]][2]
    #     position = nodePosition[level][nodeList[level]][0]
    #     resultLevel = level * 2
    #     nodeList[level] += 1
    #     currentLen = len(result[resultLevel])
    #
    #     for i in range(currentLen - 1, startLine):
    #         result[resultLevel] += " "
    #
    #     for i in range(startLine, position):
    #         result[resultLevel] += "_"
    #
    #     result[resultLevel] += str(node.get_value())
    #
    #     for i in range(position + len(str(node.get_value())), endLine):
    #         result[resultLevel] += "_"
    #
    #     result[resultLevel + 1] = self.__strInsert(result[resultLevel + 1], startLine, '/')
    #     if (endLine == startLine):
    #         endLine += len(str(node.get_value()))
    #     result[resultLevel + 1] = self.__strInsert(result[resultLevel + 1], endLine + 1, '\\')
    #
    #     if (node.left_child() is not None):
    #         self.__nodePrettyPrint(result, node.left_child(), nodeList, nodePosition, '/')
    #     elif (level + 1) < len(nodeList):
    #         nextLevel = level + 1
    #         capacity = 1
    #         while nextLevel < len(nodeList):
    #             nodeList[nextLevel] += capacity
    #             capacity *= 2
    #             nextLevel += 1
    #
    #     if (node.right_child() is not None):
    #         self.__nodePrettyPrint(result, node.right_child(), nodeList, nodePosition, '\\')
    #     elif (level + 1) < len(nodeList):
    #         nextLevel = level + 1
    #         capacity = 1
    #         while nextLevel < len(nodeList):
    #             nodeList[nextLevel] += capacity
    #             capacity *= 2
    #             nextLevel += 1


# In[45]:


myTree = BinarySearchTree()

myTree.add(12)

myTree.add(7)

myTree.add(20)

myTree.add(99)

myTree.add(32)

myTree.add(46)

myTree.rebalance()

myTree.rebalance()
myTree.pre_order()

print(myTree.find(12))
print(myTree.find(20))
print(myTree.find(99))

# In[ ]:


# def main():
#     my_tree = BinarySearchTree()
#     with open()


