class RandomizedSet:

    def __init__(self):
        #"intialize a hashmap"
        #intialize a list
        self.hashmap = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        #when we insert in our hashmap, we make val the key, val the idx
            #hashmap[val] == len(nums) - 1
            #insert to list
            #returns True
        #else return False
        if val in self.hashmap:
            return False
        self.arr.append(val)
        self.hashmap[val] = len(self.arr) - 1

        return True

    def remove(self, val: int) -> bool:
        #if val in hashmap:
        """
        [1, 2, 3]
        we can get last index o(1)
        
        idx_to_remove = hashmap[val] #2
        last_val = arr[-1] #3
        now we just swap them
        idx_to_remove = last_val
        arr.pop()
        """
        if val not in self.hashmap:
            return False
        #instantiate the variables we going to need when swapping
        idx_to_remove = self.hashmap[val] #0
        last_val = self.arr[-1] #2

        #before we remove, we need too update the new idx
        self.hashmap[last_val] = idx_to_remove

        #now we remove and delete
        self.arr[idx_to_remove] = last_val
        self.arr.pop()
        del self.hashmap[val]
        return True

    def getRandom(self) -> int:
        #"returns a random probability" o(1), so we need a list
        return random.choice(self.arr)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()