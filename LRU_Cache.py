class Node:
    def __init__(self, key, val):
        
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        
        # init head and tail to null nodes
        
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        
        # connect head and tail to represent doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.hashmap = {}
        

    def get(self, key: int) -> int:
        
        # check if key exists in map -- if not return -1
        
        if not key in self.hashmap:
            return -1
        
        else:
            # retrieve the key value from map -- which is in the format of a 'node'
            node = self.hashmap[key]
            
            # Next, since this is recently accessed, push to head
                # 1. First remove node --- This rewires the prev node and next node of node we are removing
                # 2. Then add node to head
                
            self.removeNode(node)
            self.addToHead(node)
            
            return node.val

    def put(self, key: int, value: int) -> None:
        
        # check if key is already there
            # 1. update its value in map
            # 2. delete node and move up to front
            
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.hashmap[key] = node
            
            self.removeNode(node)
            self.addToHead(node)
            
        else:
            # we need to insert new key
                # 1. check if capacity already met ( check hashmap size)
                    # if yes, delete last node in linked list with tail ref
                    # remove it from map
                    # remove from linked list and add to front
                    
            if self.capacity == len(self.hashmap):
                tail_node = self.tail.prev # since self.tail points to Null node
                del self.hashmap[tail_node.key] # reference to delete the node since it has a key within node attribute
                self.removeNode(tail_node)
                
            # whether capacity was met or not met, add new key
                # 1.create a node of the value 
                # 2. add to map
                # 3. add to linkedlist head
                
            new_node = Node(key, value)
            self.hashmap[key] = new_node
            self.addToHead(new_node)
                
        
    # rewires connection of node's prev and next when removing node 
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    
    def addToHead(self, node):
        
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
