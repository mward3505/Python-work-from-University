from time import perf_counter


class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data_val)


class MyList:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, data_val):
        if self.first is None:
            self.first = Node(data_val)
            self.last = self.first
        else:
            temp = Node(data_val)
            temp.next = self.first
            self.first = temp

    def index(self, item):
        index = 0
        while index < self.length():
            if self.get(index).data_val == item:
                return index
            item += 1
        return -1

    def remove(self, item):
        index = self.index(item)

        if self.last == self.first:
            self.last = None
            self.first = None
        elif index == 0:
            temp = self.first.next
            self.first = temp
        elif index > 0:
            one_before = self.get(index - 1)
            temp = one_before.next
            if self.last == temp:
                self.last = one_before
            one_before.next = one_before.next.next
            temp.next = None

    def append(self, data_val):
        if self.first is None:
            self.first = Node(data_val)
            self.last = self.first
        else:
            new_item = Node(data_val)
            self.last.next = new_item
            new_item.prev = self.last
            self.last = new_item
            new_item.next = None

    def get(self, index):
        current = 0
        if index >= self.length():
            return None
        if index < 0:
            return None

        item = self.first
        while current < index:
            item = item.next
            current += 1
        return item

    def __len__(self):
        return self.length()

    def is_empty(self):
        return self.first is None

    def length(self):
        result = 0
        if self.first is None:
            return result

        item = self.first
        result += 1
        while item.next is not None:
            item = item.next
            result += 1
        return result

    def pop(self):
        last = self.last
        self.remove(last.data_val)
        return last

    def __str__(self):
        if self.first is None:
            return "empty"

        result = self.first.__str__()
        item = self.first
        while item.next is not None:
            item = item.next
            result = str(result) + "," + str(item.__str__())
        return result
