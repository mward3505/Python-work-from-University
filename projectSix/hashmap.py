class HashMap:
    def __init__(self):
        self.inner_size = 0
        self.array = [None] * self.inner_size
        self.count = 0

    def isfull(self):
        for i in range(self.inner_size):
            if self.array[i] is None:
                return False
        return True

    def size(self):
        return self.count

    def hashTuple(self, tupleValue):
        if tupleValue is tuple:
            return tupleValue[0] ** tupleValue[1]
        return hash(tupleValue)

    def set(self, key, value):
        index = self.hashTuple(key) % self.inner_size

        if self.isfull():
            self.inner_size = self.inner_size * 2
            temp = self.array
            self.array = [None] * self.inner_size
            for item in temp:
                self.add(item[0], item[1])
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
        if self.getLoadFactor() >= 0.80:
            self.rehash()

    def remove(self, key):
        pass

    def clear(self):
        self.inner_size = 0
        self.array = [None] * self.inner_size
        self.count = 0

    def capacity(self):
        return self.inner_size

    def keys(self):
        result = []
        for i in range(self.inner_size):
            if self.array[i] is not None:
                for item in self.array[i]:
                    result += item[0]
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

    def getLoadFactor(self):
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
