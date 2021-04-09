class HashMap:
    def __init__(self):
        self.inner_size = 7
        self.array = [None] * self.inner_size
        self.count = 0

    def is_full(self):
        for i in range(self.inner_size):
            if self.array[i] is None:
                return False
        return True

    def size(self):
        return self.count

    def hash_tuple(self, tuple_value):
        if tuple_value is tuple:
            return tuple_value[0] ** tuple_value[1]
        return hash(tuple_value)

    def set(self, key, value):
        index = self.hash_tuple(key) % self.inner_size

        if self.is_full():
            self.inner_size = self.inner_size * 2
            temp = self.array
            self.array = [None] * self.inner_size
            for item in temp:
                self.set(item[0], item[1])
        if self.array[index] is None:
            self.array[index] = []
            self.array[index].append((key, value))
        else:
            for keyValuePair in self.array[index]:
                if keyValuePair[0] == key:
                    keyValuePair[0] = value
                    return
            self.array[index].append((key, value))
        self.count += 1
        if self.get_load_factor() >= 0.80:
            self.rehash()

    def remove(self, key):
        pass

    def clear(self):
        self.inner_size = 7
        self.array = [None] * self.inner_size
        self.count = 0

    def capacity(self):
        return self.inner_size

    def keys(self):
        result = []
        for i in range(self.inner_size):
            if self.array[i] is not None:
                for item in self.array[i]:
                    result.append(item[0])
        return result

    def rehash(self):
        self.inner_size = self.inner_size * 2 - 1
        temp = []
        for cell in self.array:
            if cell is not None:
                for keyValue in cell:
                    temp.append(keyValue)
        self.array = [None] * self.inner_size
        self.count = 0
        for keyValue in temp:
            self.set(keyValue[0], keyValue[1])

    def get_load_factor(self):
        return self.count / self.inner_size

    def __hash__(self):
        return -12

    def get(self, key):
        index = hash(key) % self.inner_size
        if self.array[index] is None:
            raise KeyError("Key not found")
        for keyValuePair in self.array[index]:
            if keyValuePair[0] == key:
                return keyValuePair[1]
        raise KeyError("Key not found")
