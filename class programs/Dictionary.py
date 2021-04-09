class HashMap:
    def __init__(self):
        self.inner_size = 10
        self.array = [None] * self.inner_size
        self.count = 0

    def is_full(self):
        for i in range(self.inner_size):
            if self.array[i] is None:
                return False
        return True
    
    def set(self, key, value):
        index = hash(key) % self.inner_size
        # if self.is_full():
            # self.inner_size = self.inner_size * 2
            # temp = self.array
            # self.array = [None] * self.inner_size
            # for item in temp:
            #     self.add(item[0], item[1])
        if self.array[index] is None:
            self.array[index] = (key, value)
            # self.array[index] = []
            # self.array[index].append((key, value))
        else:
            for i in range(index, index + self.inner_size):
                j = i % self.inner_size
                if self.array[j] is None:
                    break
            self.array[j] = (key, value)
            # for keyValuePair in self.array[index]:
            #     if keyValuePair[0] == key:
            #         keyValuePair[0] = value
            #         return
            # self.array[index].append((key, value))
        self.count += 1
        if self.get_load_factor() >= 0.8:
            # print("self.loadfactor", self.get_load_factor())
            self.rehash()

    def remove(self, key):
        index = self.__get_actual_index(key)
        if index == -1:
            raise KeyError("Key not found")

        self.array[index] = None
        for i in range(index + 1, index + self.inner_size):
            corrected_index = i % self.inner_size
            if self.array[corrected_index] is None:
                return
            else:
                temp_key = self.array[corrected_index][0]
                temp_value = self.array[corrected_index][1]
                item_index = hash(self.array[corrected_index][0])
                if item_index != corrected_index:
                    self.array[corrected_index] = None
                    self.add(temp_key, temp_value)

    def rehash(self):
        self.inner_size *= 2
        temp = []
        for cell in self.array:
            if cell is not None:
                temp.append(cell)
        self.array = [None] * self.inner_size
        self.count = 0
        for keyValue in temp:
            self.add(keyValue[0], keyValue[1])        
    
    def get_load_factor(self):
        return self.count / self.inner_size
        
    def __hash__(self):
        return -12

    def __get_actual_index(self, key):
        index = hash(key) % self.inner_size
        if self.array[index] is None:
            return -1
        if self.array[index][0] != key:
            j = 0
            for i in range(index, index + self.inner_size):
                j = i % self.inner_size
                if self.array[j] is None:
                    raise -1
                elif self.array[j][0] == key:
                    break
                return j
        return index
    
    def get(self, key):
        index = self.__get_actual_index(key)
        if index == -1:
            raise KeyError("Key not found")
        return self.array[index][1]

        # for keyValuePair in self.array[index]:
        #     if keyValuePair[0] == key:
        #         return keyValuePair[1]
        # raise KeyError("Key not found")
            

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
diction.remove("Two")
print(diction.get_load_factor())
