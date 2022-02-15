from tree_library import *

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(9)
i = Node(15)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
e.left = h
e.right = i

#      1
#      /\
#     2  3
#    /\  /\
#   4  5 6 7
#     /\
#    9  15

print(bfs(a)) # [1, 2, 3, 4, 5, 6, 7, 9, 15]
print(dfs_iterative(a)) # [1, 2, 4, 5, 9, 15, 3, 6, 7]
print(dfs_recursive(a)) # [1, 2, 4, 5, 9, 15, 3, 6, 7]
print(count_nodes(a)) # 9
print(is_present(a,15)) # True
print(tree_sum(a)) # 52
print(tree_min_value(a)) # 1
print(max_root_to_leaf(a)) # 23
print(max_depth(a)) # 4
print(inorder(a)) # [4, 2, 9, 5, 15, 1, 6, 3, 7]
print(preorder(a)) # [1, 2, 4, 5, 9, 15, 3, 6, 7]
print(postorder(a)) # [4, 9, 15, 5, 2, 6, 7, 3, 1]