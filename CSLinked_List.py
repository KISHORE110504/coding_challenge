class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)  #need to convert it into string
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += '->'
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
        
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node    
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1
    
    def insert(self, index, value):
        new_node = Node(value)
        if index > self.length or index < 0:
            raise Exception("Index out of Range")
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
    
    def traversal(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
            if current == self.head:
                break
            
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:   
            prev_node = self.get(index-1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
            self.length -= 1
            return popped_node
    
    def delete_all(self):
        if self.length == 0:
            return
        self.head = None
        self.tail.next = None
        self.tail = None
        self.length = 0
        
cslinkedlist = CSLinkedList()
cslinkedlist.append(10)
cslinkedlist.append(20)
cslinkedlist.append(30)
# print(cslinkedlist)
# cslinkedlist.prepend(100)
# cslinkedlist.insert(5,100)
# cslinkedlist.pop()
print(cslinkedlist)
cslinkedlist.delete_all()
print(cslinkedlist)