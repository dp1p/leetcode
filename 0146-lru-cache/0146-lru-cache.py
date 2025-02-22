class LRUCache:
    # all operations must run o(1)
    # hashmaps or hashsets
    def __init__(self, capacity: int):
        # intializes the positive size capacity (the size of the hashmap)
        self.capacity = capacity
        self.hashmap = {}
        self.tracker = []

        #use array
        #depending on the order, we pop
        # we want to shift that arr

    def get(self, key: int) -> int:
        # simply search if the key exists
        # use a tracker to keep track of what has been recently used
        # print(f'getting')
        if key in self.hashmap:
            #replace the order, and move that key to the beginning
            #shift arr

            self.tracker.pop(self.tracker.index(key))
            self.tracker.insert(0, key)

            # print(self.tracker)
            return self.hashmap[key]
        # print(f'{key} was not found')
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # print('updating')
            self.hashmap[key] = value
            self.tracker.pop(self.tracker.index(key))
            self.tracker.insert(0, key)

        elif len(self.hashmap) != self.capacity:
            # print('inserting')
            self.tracker.insert(0, key)
            self.hashmap[key] = value
            # print(self.tracker)
            # print(self.hashmap)
        else:
            
            # in the tracker, determine what has been used the least
            
            #insertion takes precedence
            #we should implement a lastest insertion tracker 
            key_to_delete = self.tracker.pop() # o(1)
            del self.hashmap[key_to_delete]
            # print(f'deleting {key_to_delete}')
            # print(self.tracker)
            self.hashmap[key] = value
            self.tracker.insert(0, key)



        # pair key value
        # if the key exists, update value
        # if number keys exceeds capacity, evict the least recently used key
        # counter how many tiems each one has been called
        # we can determine the least recently used key by comparing values
        # sort by key value pairs #lambda function


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)