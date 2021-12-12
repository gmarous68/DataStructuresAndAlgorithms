class HashTable(object):
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash__(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
            return my_hash

    def set_item(self, key, value):
        idx = self.__hash__(key)
        if self.data_map[idx] is None:
            self.data_map[idx] = []
        self.data_map[idx].append([key, value])

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def get_item(self, key):
        idx = self.__hash__(key)
        if self.data_map[idx] is not None:
            for i in range(len(self.data_map[idx])):
                if self.data_map[idx][i][0] == key:
                    print(self.data_map[idx][i][0], ":", self.data_map[idx][i][1])

    def get_keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for k in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][k][0])
        return all_keys
