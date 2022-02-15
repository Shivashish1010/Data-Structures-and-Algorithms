from linked_list_library import *

l1 = linkedList()
l1.append_left(10) # 10
l1.append_left(20) # 20 -> 10
l1.append(30) # 20 -> 10 -> 30
l1.append(40) # 20 -> 10 -> 30 -> 40
l1.append(5) # 20 -> 10 -> 30 -> 40 -> 5
l1.pop(2) # 20 -> 30 -> 40 -> 5
l1.reverse() # 5 -> 40 -> 30 -> 20
l1.insert(20,5) # 5 -> 40 -> 30 -> 20 -> 20
l1.insert(250,4) # 5 -> 40 -> 30 -> 20 -> 250 -> 20
l1.remove(20) # 5 -> 40 -> 30 -> 250
print(l1)