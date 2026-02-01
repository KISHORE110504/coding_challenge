class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)            # O(1)
        self.head = new_node              # O(1)
        self.tail = new_node              # O(1)
        self.length = 1                   # O(1)
        
new_linked_list = LinkedList(10)
print(new_linked_list.head.value)
        