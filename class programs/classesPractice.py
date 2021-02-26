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

    def append(self, data_val):
        if self.first is None:
            self.first = Node(data_val)
        else:
            item = self.first
            while item.next is not None:
                item = item.next

            temp = Node(data_val)
            item.next = temp
            temp.prev = item

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


class ArrayList:
    def __init__(self):
        self.myArray = []
        self.lastIndex = 0
        self.maxSize = 0
        self.sizeExponent = 0

    def add(self, value):
        if self.lastIndex > self.maxSize - 1:
            self.__resize__()
        for i in range(self.lastIndex, 0, -1):
            self.myArray[i + 1] = self.myArray[i]
        self.myArray[0] = value

    def append(self, value):
        if self.lastIndex > self.maxSize - 1:
            self.__resize__()
        self.myArray[self.lastIndex] = value
        self.lastIndex += 1

    def __resize__(self):
        new_size = 2 ** self.sizeExponent
        new_array = [0] * new_size
        for i in range(self.maxSize):
            new_array[i] = self.myArray[i]
        self.maxSize = new_size
        self.myArray = new_array
        self.sizeExponent += 1

    def __getitem__(self, index):
        if index > self.lastIndex:
            raise LookupError("Index out of bounds")
        return self.myArray[index]


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


    my_list.append(1)
    my_list.append(5)
    my_list.append(3)
    my_list.append(2)
    my_list.append(4)
    my_list.append(6)

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
