# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""MISTAKES"""
"""
-  not taking BST into account 
- 
"""
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q: # base case 
            return None 
        if max(p.val,q.val) < root.val :
            return self.lowestCommonAncestor(root.left,p,q)
        elif min(p.val,q.val) > root.val :
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root 

        # lowest common ancestor is esentially the closest ancestor node and we consider the node itself as an ancestor 
        """BRUTEFORCE:"""
        # one brute force is to find the distance between each ancestor node to that node 
        # #first find all the ancestor nodes 
        # # get the common nodes 
        # # compare the distances 


        # 3 -> 5 3
        # 4 -> 5 3 4

        # 3 -> 5=1 3= 0 3 < 5 
        # 4 -> 5=2 3 =1 3 < 5 
        # we take the lowest node 

     
    


