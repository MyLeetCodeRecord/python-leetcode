from typing import  Optional
from collections import  deque

from btree import TreeNode

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """
        513. 找树左下角的值
        https://leetcode-cn.com/problems/find-bottom-left-tree-value/
        """
        if root is None:
            return 0
        result = 0

        deq = deque()
        deq.append(root)

        while len(deq) > 0:
            size = len(deq)
            for i in range(size):
                node = deq.popleft()
                if i == 0:
                    result = node.val
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
        return result



