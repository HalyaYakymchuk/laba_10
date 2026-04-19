"""sort binary tree by levels"""

class Node:
    """node initialization"""
    def __init__(self, left = None, right = None, value = 0):
        self.left = left
        self.right = right
        self.value = value

def tree_by_levels(node):
    """adding children by levels"""
    final_list = []
    queue = [node]

    if not node:
        return []

    while queue:
        current = queue.pop(0)
        final_list.append(current.value)

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return final_list
