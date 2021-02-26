from time import perf_counter


class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data_val)

    def recursive_append(self, data_val):
        if self.next is None:
            self.next = Node(data_val)
        else:
            self.next.recursive_append(data_val)


class MyList:
    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0

    def recursive_append(self, data_val):
        if self.first is None:
            self.first = Node(data_val)
        else:
            self.first.recursive_append(data_val)

    def add(self, data_val):
        if self.first is None:
            self.first = Node(data_val)
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
        if index == 0:
            temp = self.first.next
            self.first = temp
        elif index > 0:
            one_before = self.get(index - 1)
            temp = one_before.next
            one_before.next = one_before.next.next
            temp.next = None

    def append(self, node):
        if self.first is None:
            self.first = self.last = node
        elif self.last.data_val < node:
            self.last = self.__set_links(self.last, node, None)
        elif self.first.data_val >= node:
            self.first = self.__set_links(None, Node(node), self.first)
        else:
            current = self.first
            while current.course_number < node:
                current = current.next
            self.__set_links(current.prev, node, current)
        self.count += 1

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
        last = self.get(self.length() - 1)
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

    def __remove_item(self, current):
        if current == self.first:
            self.first = current.next
        if current == self.last:
            pass

    def __set_links(self, before, item, after):
        if item is None:
            if before is not None:
                before.next = after
            if after is not None:
                after.prev = before
        else:
            if before is not None:
                before.next = item
            if after is not None:
                after.prev = item
            item.prev = before
            item.next = after

        return item


def main():
    # start = perf_counter()
    my_list = MyList()
    # elapsed = perf_counter() - start
    # print("Linked creation took", elapsed)
    #
    # print(my_list)
    #
    # start = perf_counter()
    # second_list = ArrayList()
    # elapsed = perf_counter() - start
    # print("Built in creation took", elapsed)


    my_list.append(Node(1))
    my_list.append(Node(5))
    my_list.append(Node(3))
    my_list.append(Node(2))
    my_list.append(Node(4))
    my_list.append(Node(6))

    # start = perf_counter()
    # for i in range(10000):
    #     my_list.append(i)
    # elapsed = perf_counter() - start
    # print("Linked append took", elapsed)
    #
    # start = perf_counter()
    # for i in range(10000):
    #     second_list.append(i)
    # elapsed = perf_counter() - start
    # print("Built in append took", elapsed)

    # print(my_list)
    # my_list.remove(4)
    # print(my_list)
    # my_list.pop()
    # print(my_list)

    # a_list = MyList()
    #
    # a_list.recursive_append(1)
    # a_list.recursive_append(5)
    # a_list.recursive_append(9)
    # a_list.recursive_append(65)
    # a_list.recursive_append(12)

    print(my_list)


if __name__ == "__main__":
    main()
