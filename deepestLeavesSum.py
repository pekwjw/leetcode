# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None  

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tree = {}

        def front_digui(root, level):
            if root == None:
                return

            if level not in tree:
                tree[level] = []
            tree[level].append(root.val)
            front_digui(root.left, level+1)
            front_digui(root.right, level+1)
        front_digui(root, 0)

        return sum(tree[max(tree.keys())])
