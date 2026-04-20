"""delete node in a BST"""

# Definition for a binary tree node.
class TreeNode:
    """initializing tree node"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root, key):
        """deleting given node"""
        if not root:
            return

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = root.right
            while temp.left:
                temp = temp.left

            root.val = temp.val
            root.right = self.deleteNode( root.right, temp.val)

        return root
