"""Creates a hashmap to organize data"""


def hash_tuple(tuple_value):
    """helps hash tuples"""
    if tuple_value is tuple:
        return tuple_value[0] ** tuple_value[1]
    return hash(tuple_value)


class HashMap:
    """Class to create the hashmap"""
    def __init__(self):
        """Constructs default data for hashmap"""
        self.inner_size = 7
        self.array = [None] * self.inner_size
        self.count = 0

    def is_full(self):
        """Helps check to see if the hashmap is almost full"""
        for i in range(self.inner_size):
            if self.array[i] is None:
                return False
        return True

    def size(self):
        """Returns the count of the current values in the hashmap"""
        return self.count

    def set(self, key, value):
        """Sets the hashmap up with values"""
        index = hash_tuple(key) % self.inner_size

        if self.is_full():
            self.inner_size = self.inner_size * 2
            temp = self.array
            self.array = [None] * self.inner_size
            # for i in temp:
            #     self.set(i[0], i[1])
        if self.array[index] is None:
            self.array[index] = []
            self.array[index].append((key, value))
        else:
            for key_value_pair in self.array[index]:
                if key_value_pair[0] == key:
                    if key_value_pair[1] != value:
                        temp = (key, value)
                        self.remove(temp[0])
                        self.set(temp[0], value)
                        return
                    key_value_pair[1] = value
                    return
            self.array[index].append((key, value))
        self.count += 1
        if self.get_load_factor() >= 0.80:
            self.rehash()

    def remove(self, key):
        """Removes the key from the hashmap if found. Returns keyValue error if not found"""
        index = self.__get_actual_index(key)
        if index is None:
            raise KeyError("Key not found")

        self.array[index] = None
        for i in range(index + 1, index + self.inner_size):
            corrected_index = i % self.inner_size
            if self.array[corrected_index] is None:
                return
            else:
                temp_key = self.array[corrected_index][0]
                temp_value = self.array[corrected_index][0]
                item_index = hash(self.array[corrected_index][0])
                if item_index != corrected_index:
                    self.array[corrected_index] = None
                    self.set(temp_key, temp_value)

    def __get_actual_index(self, key):
        """Gets the actual index for the key being searched for"""
        index = hash(key) % self.inner_size
        if self.array[index] is None:
            return -1
        if self.array[index][0] != key:
            j = 0
            for i in range(index, index + self.inner_size):
                j = i % self.inner_size
                if self.array[j] is None:
                    raise self.array[j]
                elif self.array[j][0][0] == key:
                    break
                return j
        return index

    def clear(self):
        """Clears the hashmap"""
        self.inner_size = 7
        self.array = [None] * self.inner_size
        self.count = 0

    def capacity(self):
        """Returns the size of the hashmap"""
        return self.inner_size

    def keys(self):
        """Returns the keys for the hashmap"""
        result = []
        for i in range(self.inner_size):
            if self.array[i] is not None:
                for item in self.array[i]:
                    result.append(item[0])
        return result

    def rehash(self):
        """Rehashes the hashmap to reorganize it"""
        self.inner_size = self.inner_size * 2 - 1
        temp = []
        for cell in self.array:
            if cell is not None:
                for key_value in cell:
                    temp.append(key_value)
        self.array = [None] * self.inner_size
        self.count = 0
        for key_value in temp:
            self.set(key_value[0], key_value[1])

    def get_load_factor(self):
        """Returns how much the hashmap should increase"""
        return self.count / self.inner_size

    def __hash__(self):

        return -12

    def get(self, key):
        """Returns the value for the key passed"""
        index = hash(key) % self.inner_size
        if self.array[index] is None:
            raise KeyError("Key not found")
        for key_value_pair in self.array[index]:
            if key_value_pair[0] == key:
                return key_value_pair[1]
        raise KeyError("Key not found")
