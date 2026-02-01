class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0

    def __str__(self):
        if self.isEmpty():
            return "Stack is empty"
        
        values = [str(x) for x in reversed(self.items)]
        return '\n'.join(values)

    def push(self, element):
        self.items.append(element)
        
    def pop(self):
        return "Stack is empty." if self.isEmpty() else self.items.pop()

    def peek(self):
        return "Stack is empty." if self.isEmpty() else self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def delete_all(self):
        self.items = []
        
my_stack = Stack()
print(my_stack.items)