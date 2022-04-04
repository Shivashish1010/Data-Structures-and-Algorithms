class Stack:
    def __init__(self):
        self.stack = []
    
    #push an element to the stack
    def push(self, val):
        self.stack.append(val)

    #pop the top most element and return it
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "Stack is Empty"

    #return true if the stack is empty otherwise false
    def is_empty(self):
        return not len(self.stack) >= 1

    #returns the top most element
    def peek(self):
        if self.stack:
            return self.stack[-1]
        return "Stack is Empty"

    #overwriting repr dunder to print the stack
    def __repr__(self):
        return str(self.stack)