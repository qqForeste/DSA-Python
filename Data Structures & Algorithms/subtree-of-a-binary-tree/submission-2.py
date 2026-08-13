# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def sameTree(self, p, t):
        if not p and not t:
            return True
        
        if not p or not t:
            return False
        
        if p.val == t.val:
            return (self.sameTree(p.left, t.left) and
                    self.sameTree(p.right, t.right))

        return False
                    
                
            