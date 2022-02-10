class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#breadth first search
def bfs(node):
    visited = []
    if node:
        queue = [node]
        while queue:
            curr_node = queue.pop()
            visited.append(curr_node.val)
            if curr_node.left:
                queue.insert(0,curr_node.left)
            if curr_node.right:
                queue.insert(0,curr_node.right)
        
        return visited
    return []

#depth first search iterative
def dfs_iterative(node):
    visited = []
    if node:
        stack = [node]
        while stack:
            curr_node = stack.pop()
            visited.append(curr_node.val)
            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left:
                stack.append(curr_node.left)
        
        return visited
    return []

#depth first search recursive
def dfs_recursive(node):
    if node == None:
        return []
    else:
        return [node.val] + dfs_recursive(node.left) + dfs_recursive(node.right)

#count total nodes in the tree
def count_nodes(node):
    if node == None:
        return 0
    else:
        return 1 + count_nodes(node.left) + count_nodes(node.right)

#check if a value is present in the tree or not
def is_present(node,target):
    if node == None:
        return False
    if node.val == target:
        return True

    return is_present(node.left,target) or is_present(node.right,target)

#find the sum of all nodes of a tree
def tree_sum(node):
    if node == None:
        return 0
    else:
        return tree_sum(node.left) + node.val + tree_sum(node.right)

#find min value in the tree
def tree_min_value(node):
    if node == None:
        return float('inf')
    return min(node.val, tree_min_value(node.right), tree_min_value(node.left))

#find the path with maximum sum from root to leaf
def max_root_to_leaf(node):
    if node == None:
        return 0
    max_child_path = node.val + max(max_root_to_leaf(node.left), max_root_to_leaf(node.right))
    return max_child_path

#find the maximum depth of the tree
def max_depth(node):
    if node == None:
        return 0
    curr_max_depth = 1+max(max_depth(node.left),max_depth(node.right))
    return curr_max_depth

#inorder traversal
def inorder(root):
    res = []
    def dfs(node):
        nonlocal res
        if node:
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
    
    dfs(root)
    return res

#preorder traversal
def preorder(root):
    res = []
    def dfs(node):
        nonlocal res
        if node:
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
    
    dfs(root)
    return res

#postorder traversal
def postorder(root):
    res = []
    def dfs(node):
        nonlocal res
        if node:
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
    
    dfs(root)
    return res