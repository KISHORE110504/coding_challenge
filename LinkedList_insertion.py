class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None              # O(1)
        self.tail = None              # O(1)
        self.length = 0               # O(1)

    def __str__(self):
        temp_node = self.head
        result = ' '
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "->"
            temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)      # O(1)
        if self.head is None:      # O(1)
            self.head = new_node      # O(1)
            self.tail = new_node      # O(1)
        else:
            self.tail.next = new_node      # O(1)
            self.tail = new_node      # O(1)
        self.length += 1      # O(1)
    
        
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
print(new_linked_list)