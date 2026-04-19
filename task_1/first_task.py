"""Binary Tree Traversal"""

class TreeNode:
    """node tree initialization"""
    def __init__(self, left = None, right = None, data = 0):
        self.left = left
        self.right = right
        self.data = data

# Pre-order traversal
def pre_order(node):
    """realization of preorder binary tree traversal"""
    all_list = []

    def dfs(node):
        if node is not None:
            all_list.append(node.data)
            dfs(node.left)
            dfs(node.right)
    dfs(node)
    return all_list

# In-order traversal
def in_order(node):
    """realization of in order binary tree traversal"""
    res_list = []

    def recurse(node):
        if node is not None:
            recurse(node.left)
            res_list.append(node.data)
            recurse(node.right)

    recurse(node)
    return res_list


# Post-order traversal
def post_order(node):
    """realization of post order binary tree traversal"""
    current = node
    stack = []
    visited = set()
    res_list = []

    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek_node = stack[-1]
            if peek_node.right and peek_node.right not in visited:
                current = peek_node.right
            else:
                res_list.append(peek_node.data)
                visited.add(peek_node)
                stack.pop()
    return res_list
