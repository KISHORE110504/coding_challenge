class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = None              
        self.tail = None             
        self.length = 0  
        
    def __str__(self):
        temp_node = self.head
        result = ' '
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "->"
            temp_node.next
        return result
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
            
    def search(self, target):
        current = self.head
        while current != None:
            if current == target:
                return True
            current = current.next
            index += 1
        return False
	
    def get(self, index):
        if index == -1:
            return self.tail.value
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value        
    
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node.value
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp 
            temp.next = None
        self.length -= 1
        return popped_node.value
    
    def remove(self, index):
        if index >= self.length or index < 0:
            return Node
        if index == 0:
            return pop_first()
        if index == self.length - 1 or index == -1:
            return pop()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1 
        return popped_node
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def reverse(self):
        prev_node = None
        curr_node = self.head
        
        while curr_node is not None:
            next_temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_temp
        return prev_node