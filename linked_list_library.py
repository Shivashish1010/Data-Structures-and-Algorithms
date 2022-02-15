class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    #overwriting str dunder to pretty print the linked list
    def __str__(self):
        node = self.head
        res = ""
        while node:
            res += str(node.value)
            if node.next:
                res += "->"
            node = node.next
        return res

    #insert element at the start of the linked list 
    def append_left(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
    
    #insert element at the end of the linked list 
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            prev_node = self.head
            while prev_node.next:
                prev_node = prev_node.next
            
            prev_node.next = new_node

    #insert element at a desired location 
    def insert(self, value, pos):
        new_node = Node(value)
        if not self.head:
            self.head = new_node

        elif pos < 1:
            print("Invalid position")
            return

        elif pos == 1:
            new_node.next = self.head
            self.head = new_node

        else:  
            prev = None
            curr = self.head
            while pos>1:
                if curr is not None:
                    prev = curr
                    curr = curr.next
                    pos-=1
                else:
                    print("Position out of range")
                    return

            prev.next = new_node
            new_node.next = curr

    #reverse the linked list
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        
        self.head = prev
        return self.__str__()

    #pop by index
    def pop(self, pos=1):
        prev = None
        curr = self.head

        if pos == 1:
            self.head=self.head.next
        else:
            for _ in range(pos-1):
                prev = curr
                if curr:
                    curr = curr.next
                else:
                    print("Position doesn't exist")
                    return
            if curr:
                prev.next = curr.next
            else:
                print("Position doesn't exist")
                return

    #remove all occurrences of an element 
    def remove(self, element):
        temp_head = self.head

        while temp_head.value == element:
            temp_head = temp_head.next

        self.head = temp_head

        prev = None
        curr = self.head
        while curr:
            if curr.value == element:
                    curr = curr.next
                    prev.next = curr
            else:
                prev = curr
                curr = curr.next