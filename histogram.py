import random

class Dictogram(dict):
    def __init__(self, iterable=None):
        super().__init__()
        self.types = 0 #the number of distinct item types in this histogram
        self.tokens = 0 # the total count of all item tokens in this histogram

        if iterable:
            self.update(iterable)

    def update(self, iterable):

        for item in iterable:
            if item in self:
                self[item] += 1
                self.tokens += 1
            else:
                self[item] = 1
                self.types += 1
                self.tokens += 1

    def count(self, item):
        if item in self:
            return self[item]
        return 0

    def return_random_word(self):
        random_key = random.sample(list(self), 1)
        return random_key[0]

    def return_weighted_random_word(self):

        random_int = random.randint(0, self.tokens-1)
        index = 0

        list_of_keys = list(self)
        
        for i in range(0, self.types):
            index += self[list_of_keys[i]]
            
            if index >= random_int:
                return list_of_keys[i]

        return list_of_keys[-1]
