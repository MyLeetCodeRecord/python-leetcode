from typing import List, Optional
from collections import  deque

from btree import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        104. 二叉树的最大深度
        https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
        """
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        _max = max(left, right) + 1

        return _max

    def maxDepthN(self, root: 'Node') -> int:
        """
        559. N 叉树的最大深度
        https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/
        """
        if root is None:
            return 0
        deq = deque()
        deq.append(root)
        depth = 0
        while len(deq)>0:
            size = len(deq)
            depth += 1
            for _ in range(size):
                node = deq.popleft()
                if not node.children:
                    continue
                for child in node.children:
                    deq.append(child)
        return depth

    def minDepth(self, root: TreeNode) -> int:
        """
        111. 二叉树的最小深度
        https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
        """
        if root is None:
            return 0;
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if root.left is None:
            return 1+right
        if root.right is None:
            return 1+left
        return 1+min(left, right)

    def isBalanced(self, root: TreeNode) -> bool:
        """
        110. 平衡二叉树
        https://leetcode-cn.com/problems/balanced-binary-tree/

        很明显和 104. 二叉树的最大深度 相似
        但是如何将高度和判定结果同时返回呢?

        python 支持多返回, 因此可以将高度和子树判定结果一并返回
        其他不支持多返回的语言, 可以用 高度-1 表示子树非平衡树
        """
        if root is None:
            return True

        def getDepth(node):
            if node is None:
                return 0, True
            leftDepth, leftResult = getDepth(node.left)
            if not leftResult:
                return 0, False
            rightDepth, rightResult = getDepth(node.right)
            if not rightResult:
                return 0, False

            if abs(leftDepth-rightDepth) > 1:
                return 0, False
            return 1 + max(leftDepth, rightDepth), True

        _, result = getDepth(root)
        return result

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        652. 寻找重复的子树
        https://leetcode-cn.com/problems/find-duplicate-subtrees/


        """
        if root is None:
            return []

        import collections

        self.result = []
        self.count = collections.Counter()

        def lookup(node):
            if node is None:
                return "201"
            left = lookup(node.left)
            right = lookup(node.right)
            _id = str(node.val) + "," + left + "," + right  # 序列化, 耗时不可忽略其实
            self.count[_id] += 1
            if self.count[_id] >= 2:
                self.result.append(node)
            return _id

        lookup(root)
        return self.result



