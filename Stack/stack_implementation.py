from list_as_stack import Stack

stack = Stack()
stack.push(5)
print(stack) # [5]
stack.push(1) 
stack.push(3)
print(stack) # [5,1,3]
print(stack.peek()) # 3
print(stack.pop()) # 3
print(stack) # [5,1]
print(stack.is_empty()) # False
print(stack.pop()) # 1
print(stack.pop()) # 5
print(stack) # []
print(stack.is_empty()) # True