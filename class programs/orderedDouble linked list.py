from time import perf_counter


class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data_val)


class OrderedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0

    def add(self, data_val):
        if self.is_empty():
            self.first = Node(data_val)
            self.last = self.first
        elif self.first.data_val > data_val:
            new_node = Node(data_val)
            new_node.next = self.first
            self.first.prev = new_node.next
            self.first = new_node
        else:
            # Find where item is > than data_val
            # Find where next is None
            current = self.first

            # Check location for new node
            while current.next is not None and current.next.data_val < data_val:
                current = current.next

            # Assign the current nodes next and the new nodes next
            new_node = Node(data_val)
            new_node.next = current.next
            current.next = new_node

            # Update New Nodes previous pointer
            new_node.prev = current
            if new_node.next is not None:
                new_node.next.prev = new_node
            else:
                self.last = new_node

        self.count += 1

    def index(self, item):
        pass

    def remove(self, item):
        pass

    def search(self, item):
        pass

    def get(self, index):
        if index < 0 or index >= self.count:
            return None
        if self.is_empty():
            return None
        else:
            current_index = 0
            current = self.first
            while current_index < index:
                current = current.next
                current_index += 1
        return current

    def __len__(self):
        pass

    def is_empty(self):
        return self.first is None

    def length(self):
        return self.count

    def pop(self):
        pass

    def pop(self, pos):
        pass

    def __str__(self):
        result = ""
        current = self.first
        while current.next is not None:
            result += str(current)
            result += " "
            current = current.next
            result += str(current)

        return result


my_list = OrderedList()
my_list.add(12)
my_list.add(4)
my_list.add(8)
my_list.add(3)
my_list.add(1)
my_list.add(247)
my_list.add(11)

print(str(my_list))

print(my_list.get(1))
print(my_list.get(3))
print(my_list.get(6))
print(my_list.get(8))
print(my_list.get(-1))
