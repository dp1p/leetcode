class RandomizedSet:

    def __init__(self):
        #intialize both a hashmap and a hashset
        self.hashmap = {}
        self.arr = []
    def insert(self, val: int) -> bool:
        #insert into hashmap / hashset o(1)
        #appending to an arr o(1)
        if val in self.hashmap:
            return False
        self.arr.append(val)
        self.hashmap[val] = len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        #insert into hashmap / hashset o(1)
        #removing an idx using index() is o(n)
        #poping is o(1)
        # swap the current value to the last value of the list
        # in order to swap, we'll need
        # the idx of the value
        # current val
        # 2
        if val in self.hashmap:
            last_element = self.arr[-1] # 2
            indice_of_val = self.hashmap[val] # 0
            self.hashmap[last_element] = indice_of_val #2 : 0
            self.arr[indice_of_val] = last_element 
            self.arr.pop()
            del self.hashmap[val]
            return True
        return False

    def getRandom(self) -> int:
        #cannot get a random number in a hashset
        #if we convert the hashset into an arr, thats o(n)
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()