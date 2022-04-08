from typing import List, Optional
from collections import deque

from btree import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        101. 对称二叉树
        https://leetcode-cn.com/problems/symmetric-tree/
        """
        return self.isSymmetricIter2(root)

    def isSymmetricRecursion(self, root: Optional[TreeNode]) -> bool:
        def recursion(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is not None and node2 is not None:
                if node1.val != node2.val:
                    return False
                if not recursion(node1.left, node2.right):  # 外层
                    return False
                if not recursion(node1.right, node2.left):  # 内层
                    return False
                return True
            return False

        if root is None:
            return True
        return recursion(root.left, root.right)

    def isSymmetricIter1(self, root: Optional[TreeNode]) -> bool:
        """
        层序加判断每一层是否是回文数组时, 不能丢掉空节点, 否则bug, 基础测试用例即可
        或者也可以不用存这么多数据, 只需要从外向内, 两个一组的入队出队
        """
        if root is None:
            return True
        deq = deque()
        deq.append(root.left)
        deq.append(root.right)

        while len(deq) > 0:
            size = len(deq)
            part = []
            for _ in range(0, size):
                node = deq.popleft()
                if node is not None:
                    part.append(node.val)
                    deq.append(node.left)
                    deq.append(node.right)
                else:
                    part.append(None)  # 需要占位
                    # deq.append(None)  # 不用占位
                    # deq.append(None)  #
            # if all([p is None for p in part]):
            #     return True
            left, right = 0, len(part) - 1
            while left < right:
                if part[left] != part[right]:
                    return False
                left += 1
                right -= 1
        return True

    def isSymmetricIter2(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        deq = deque()
        deq.append(root.left)
        deq.append(root.right)
        while len(deq) > 0:
            node1 = deq.popleft()
            node2 = deq.popleft()
            if node1 is None and node2 is None:
                pass
            elif node1 is not None and node2 is not None:
                if node1.val != node2.val:
                    return False
                deq.append(node1.left)
                deq.append(node2.right)
                deq.append(node1.right)
                deq.append(node2.left)
            else:
                return False
        return True

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        116. 填充每个节点的下一个右侧节点指针
        https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
        """
        if root is None:
            return None

        def connectRecursion(node1, node2):
            if node1 is None or node2 is None:
                return
            node1.next = node2
            connectRecursion(node1.left, node1.right)
            connectRecursion(node2.left, node2.right)
            connectRecursion(node1.right, node2.left)

        connectRecursion(root.left, root.right)
        return root

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        100. 相同的树
        https://leetcode-cn.com/problems/same-tree/
        """
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            if p.val != q.val:
                return False
            if not self.isSameTree(p.left, q.left):
                return False
            if not self.isSameTree(p.right, q.right):
                return False
            return True
        return False

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        """
        572. 另一棵树的子树
        https://leetcode-cn.com/problems/subtree-of-another-tree/

        TODO: 扩展其他方法
        """
        if root is None and subRoot is None:
            return True
        elif root is not None and subRoot is not None:
            if root.val == subRoot.val:
                if self.isSameTree(root, subRoot):
                    return True
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False


