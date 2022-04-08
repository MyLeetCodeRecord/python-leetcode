from typing import List, Optional
from collections import deque

from btree import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        226. 翻转二叉树
        https://leetcode-cn.com/problems/invert-binary-tree/
        """
        if root is None:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def countNodes(self, root: TreeNode) -> int:
        """
        222. 完全二叉树的节点个数
        https://leetcode-cn.com/problems/count-complete-tree-nodes/

        完全二叉树:
        部分必然为满二叉树, 即节点数量等于2**高度-1

        并且, 只有一个节点 有一个子节点, 其他的要么没有, 要么两个子节点
        """
        if root is None:
            return 0

        left, right = root.left, root.right
        leftHeight, rightHeight = 1, 1 # 初始值为1,
        # leftHeight, rightHeight = 0, 0
        while left:
            left = left.left
            leftHeight += 1
        while right:
            right = right.right
            rightHeight += 1
        if leftHeight == rightHeight:
            # 两边高度相等, 满二叉树
            return 2 ** leftHeight - 1
            # return (2 << leftHeight) - 1 # 对应初始高度为0
            # 注意 指数和左移还不一样
        # 两边高度不相等, 不能直接计算, 递归统计
        leftCnt = self.countNodes(root.left)
        rightCnt = self.countNodes(root.right)

        return leftCnt + rightCnt + 1

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        257. 二叉树的所有路径
        https://leetcode-cn.com/problems/binary-tree-paths/
        """

        def traversal(node):
            if node is None:
                self.store.append("->".join(self.s_part))
                return
            self.s_part.append(str(node.val))
            if node.left is not None:
                traversal(node.left)
            if node.right is not None:
                traversal(node.right)
            if node.left is None and node.right is None:
                traversal(None)  # 需要处理
            self.s_part.pop()


        self.s_part = []
        self.store = []
        traversal(root)

        return self.store
