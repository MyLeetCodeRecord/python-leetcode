from typing import List, Optional
from collections import deque

from btree import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        102. 二叉树的层序遍历
        https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
        """
        if root is None:
            return []
        ret = []
        deq = deque()
        deq.append(root)
        while len(deq) > 0:
            size = len(deq)  # 必须固定大小, 这样保证取出的都是一层的
            part = []
            for _ in range(0, size):
                node = deq.popleft()
                part.append(node.val)
                if node.left is not None:
                    deq.append(node.left)
                if node.right is not None:
                    deq.append(node.right)
            ret.append(part)
        return ret

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        107. 二叉树的层序遍历 II
        https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/
        """
        top = self.levelOrder(root)
        top.reverse()
        return top

    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        199. 二叉树的右视图
        https://leetcode-cn.com/problems/binary-tree-right-side-view/
        """
        # lvlOrder = self.levelOrder(root)
        # ret = [part[-1] for part in lvlOrder]
        # return ret
        if root is None:
            return []
        ret = []
        deq = deque()
        deq.append(root)
        while len(deq) > 0:
            size = len(deq)  # 必须固定大小, 这样保证取出的都是一层的
            for i in range(0, size):
                node = deq.popleft()
                if i == size - 1:
                    ret.append(node.val)
                if node.left is not None:
                    deq.append(node.left)
                if node.right is not None:
                    deq.append(node.right)
        return ret

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        637. 二叉树的层平均值
        https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/
        """

        if root is None:
            return []
        ret = []
        deq = deque()
        deq.append(root)
        while len(deq) > 0:
            size = len(deq)
            curr_sum = 0.0
            for _ in range(0, size):
                node = deq.popleft()
                curr_sum += node.val
                if node.left is not None:
                    deq.append(node.left)
                if node.right is not None:
                    deq.append(node.right)
            ret.append(curr_sum / size)
        return ret

    # class Node:
    #     def __init__(self, val=None, children=None):
    #         self.val = val
    #         self.children = children
    def levelOrderN(self, root: 'Node') -> List[List[int]]:
        """
        429. N 叉树的层序遍历
        https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
        """
        if root is None:
            return []
        ret = []
        deq = deque()
        deq.append(root)
        while len(deq) > 0:
            size = len(deq)
            part = []
            for _ in range(0, size):
                node = deq.popleft()
                part.append(node.val)
                for child in node.children:
                    deq.append(child)
            ret.append(part)
        return ret

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        515. 在每个树行中找最大值
        https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/
        """
        if root is None:
            return []

        ret = []

        deq = deque()
        deq.append(root)

        while len(deq) > 0:
            size = len(deq)
            _max = deq[0].val
            for _ in range(0, size):
                node = deq.popleft()
                if node.val > _max:
                    _max = node.val
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            ret.append(_max)

        return ret

    # class Node:
    #     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    #         self.next = next
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        116. 填充每个节点的下一个右侧节点指针
        https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
        """
        if root is None:
            return None
        # 可以用层序的方式, 取出每一层的, 然后链接next
        # deq = deque()
        # deq.append(root)
        # while len(deq) >0:
        #     size = len(deq)
        #     for i in range(0, size):
        #         node = deq.popleft()
        #         if i < size - 1:
        #             node.next = deq[0]
        #         if node.left:
        #             deq.append(node.left)
        #         if node.right:
        #             deq.append(node.right)
        # return root

        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next  #
            leftmost = leftmost.left

        return root

    def connect2(self, root: 'Node') -> 'Node':
        """
        117. 填充每个节点的下一个右侧节点指针 II
        https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/

        区别于116, 树不再是完美二叉树
        """
        if root is None:
            return
        deq = deque()
        deq.append(root)
        while len(deq) > 0:
            size = len(deq)
            for i in range(0, size):
                node = deq.popleft()
                if i < size - 1:
                    node.next = deq[0]
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
        return root

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        104. 二叉树的最大深度
        https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
        """
        if root is None:
            return 0
        _max = 0
        deq = deque()
        deq.append((root, 1))
        while len(deq) > 0:
            node, lvl = deq.popleft()
            if lvl > _max:
                _max = lvl
            if node.left:
                deq.append((node.left, lvl+1))
            if node.right:
                deq.append((node.right, lvl+1))
        return _max

    def minDepth(self, root: TreeNode) -> int:
        """
        111. 二叉树的最小深度
        https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
        """
        if root is None:
            return 0
        _min = 100000
        deq = deque()
        deq.append((root, 1))
        while len(deq) >0:
            node, lvl = deq.popleft()
            if node.left is None and node.right is None:
                if lvl < _min:
                    _min = lvl
            if node.left:
                deq.append((node.left, lvl+1))
            if node.right:
                deq.append((node.right, lvl+1))
        return _min
