# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.dfs(1,n) if n>=1 else []
    
    def dfs(self,start,end):
        if start>end:
            return [None]
        ans = []
        for i in range(start,end+1):
            Left = self.dfs(start,i-1)
            Right = self.dfs(i+1,end)
            for l in Left:
                for r in Right:
                    root = TreeNode(i)
                    root.left,root.right = l,r
                    ans.append(root)
        return ans
    
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1) 
        dp[0] = 1
        for i in range(n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.dfs(root,ans)
        return ans
    
    def dfs(self,root,ans):
        if not root:
            return 
        self.dfs(root.left,ans)
        ans.append(root.val)
        self.dfs(root.right,ans)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.judge(root,-float('inf'),float('inf'))
    
    def judge(self,root,minv,maxv):
        if not root:
            return True
        if root.val <= minv or root.val >= maxv:
            return False
        return self.judge(root.left,minv,root.val) and self.judge(root.right,root.val,maxv)
