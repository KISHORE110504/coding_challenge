class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
    def __str__(self):
        return str(self.value)
        
class CircularDoublyLinkedList:       
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 
        
    def __str__(self):
        curr_node = self.head
        result = ' '

        while curr_node:
            result += str(curr_node.value)
            curr_node = curr_node.next
            if curr_node == self.head : break
            result += " <-> "
        return result
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node
        self.length += 1
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
            if current == self.head: break
            
    def reverse_traverse(self):
        current = self.tail
        while current:
            print(current.value)
            current = current.prev
            if current == self.tail: break
            
    def search(self, target):
        current_node = self.head
        while current_node:
            if current_node.value == target:
                return True
            current_node = current_node.next
            if current_node == self.head: break
        return False
    
    def get(self, index):
        current_node = None
        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev
        return current_node
    
    def set_value(self, index, value):
        if new_node := self.get(index):
            new_node.value = value
            return True
        return False
    
    def insert(self, index, value):  # sourcery skip: extract-method
        new_node = Node(value)
        if index < 0 or index > self.length:
            print("Index out of range")
            return
        if index == 0:
            self.prepend(value)
            return 
        elif index == self.length:
            self.append(value)
            return
        else:
            prev_node = self.get(index-1)
            new_node.next = prev_node.next
            new_node.prev = prev_node
            prev_node.next.prev = new_node
            prev_node.next = new_node
            self.length += 1
            

    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.prev = None
            popped_node.next = None
            self.head.prev = self.tail
            self.tail.next = self.head
            self.length -= 1
        return popped_node
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            popped_node.next = None
            popped_node.prev = None
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        popped_node = self.get(index)
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        popped_node.next = None
        popped_node.prev = None
        self.length -= 1
        return popped_node
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
                
    
    
    
dcll = CircularDoublyLinkedList()

dcll.append(10)
dcll.append(20)
dcll.append(30)
dcll.prepend(40)
dcll.pop()
print(dcll)
