# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#My solution  80.99% runtime & 69.60 memory
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        result = [root.val]
        temp = [root]
        hold = []
        while True:
            while temp:
                out = temp.pop()
                if out.left: hold.append(out.left)
                if out.right: hold.append(out.right)
            if not (hold):
                return result
            Max = hold[0].val
            for i in hold:
                Max = max(Max, i.val)
            result.append(Max)
            temp = hold
            hold = []
