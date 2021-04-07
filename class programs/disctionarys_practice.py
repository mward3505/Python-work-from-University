class Dictionary:
    def __init__(self):
        self.size = 30
        self.array = [None] * self.size

    def is_full(self):
        for i in range(self.size):
            if self.array[i] is None:
                return False
        return True

    def get_hash(self, value):
        result = 0
        if isinstance(value, str):
            n = 1
            for c in value:
                result += ord(c) * n
                n += 1
        if isinstance(value, int):
            print("SquaredValue is ", value ** 2)
            result = int(str(value ** 2)[1:3])
            print("Mid-SquaredValue is ", result)
        return result % self.size

    # def add(self, key, value):
    #     index = self.get_hash(key)
    #     if self.array[index] is not None and self.array[index][0] != key:
    #         for i in range(index, index + self.size):
    #             actual_index = i % self.size
    #             if self.array[actual_index] is None:
    #                 self.array[actual_index] = (key, value)
    #                 return
    #         raise KeyError("There is no room")
    #     else:
    #         self.array[index] = (key, value)

    def add(self, key, value):
        index = hash(key) % self.size
        if self.is_full():
            self.size = self.size * 2
            temp = self.array
            self.array = [None] * self.size
            for item in temp:
                self.add(item[0], item[1])
        if self.array[index] is None:
            self.array[index] = []
            self.array[index].append((key, value))
        else:
            for key_value_pair in self.array[index]:
                if key_value_pair[0] == key:
                    key_value_pair[0] = value
                    return
            self.array[index].append((key, value))

    # def get(self, key):
    #     index = self.get_hash(key)
    #     if self.array[index][1] == key:
    #         return self.array[index]
    #
    #     for i in range(index, index + self.size):
    #         actual_index = i % self.size
    #         if self.array[actual_index][0] == key:
    #             return self.array[actual_index][1]
    #     raise KeyError("Key not found")

    def get(self, key):
        index = hash(key) % self.size
        if self.array[index] is None:
            raise KeyError("Key not found")
        for key_value_pair in self.array[index]:
            if key_value_pair[0] == key:
                return key_value_pair[1]
        raise KeyError("Key not found")


diction = Dictionary()
diction.add("One", 1)
diction.add("Two", 2)
diction.add("Three", 3)
diction.add("Four", 4)
diction.add("Five", 5)
diction.add("Six", 6)
diction.add("Seven", 7)
diction.add("Eight", 8)
diction.add("Nine", 9)

print(diction.array)

print(diction.get("One"))
print(diction.get("Two"))
print(diction.get("Three"))
print(diction.get("Four"))
print(diction.get("Five"))
print(diction.get("Six"))
print(diction.get("Seven"))
print(diction.get("Eight"))
print(diction.get("Nine"))
