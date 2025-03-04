class Node:
    def __init__(self, key, value):
    #reason why we place a key value is to delete the node when capacity is reached
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1) 
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        next_node = node.next 
        prev_node = node.prev 
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        #H <-> N2 <-> N1 <-> N2 <-> T
        #H <-> N  
        #H <-> N2 <-> N1 <-> T
        node.prev = self.head #to point to our dummy head
        node.next = self.head.next #to point whatever our head was pointing
        self.head.next.prev = node #have next of head
        self.head.next = node


    def get(self, key: int) -> int:
        if key in self.node_map:
            node = self.node_map[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            self._remove(self.node_map[key]) #move the key 
        
        node = Node(key, value)
        self.node_map[key] = node
        self._add_to_front(node)

        if len(self.node_map) > self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.node_map[lru_node.key] 
        



        #if key is in hashmap
        #   update key value pair
        #   update it so it is the most recently used
        #   we update it by removing the node, and readding it, then updating the dictionary
        #if capacity has been reached
        #   delete least recently used key
    
    #add and remove function for the linkedlist
    #this function will add a linkedlist 
    #_add(self, node)
    # pointing our node to the head
    #node.next = self.head.prev (want our node to where the head is, but it is head.next because our head is a dummy node)
    #node.prev = self.head #to point to our dummy node
    #insert our node into our doubly linkedlist
    #self.head.next.prev = node #head is a dummy node
    #self.head.next = node
    

    #h <-> 1 <----> 3

    #_remove(self, node):
    # prev_node = node.prev
    # next_node = node.next
    # prev_node.next = next_node 
    # next_node.prev = prev_node






# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)