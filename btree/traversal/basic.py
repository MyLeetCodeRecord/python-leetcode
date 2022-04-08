from typing import List, Optional
from collections import deque

from btree import TreeNode


class Solution:
    """
    深度优先: 先序/后序/中序遍历
    广度优先: 层序遍历

    先序/后序/中序可以使用递归, 统一表述形式, 写法很简单.
    层序可以借助队列, bfs
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        144. 二叉树的前序遍历
        https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
        """
        if root is None:
            return []
        ret = list()

        def traversal(node: TreeNode):
            if node is None:
                return
            ret.append(node.val)
            traversal(node.left)
            traversal(node.right)

        traversal(root)
        return ret

    def preorder(self, root: 'Node') -> List[int]:
        """
        589. N 叉树的前序遍历
        https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
        """
        ret = []

        def traversal(node):
            if node is None:
                return
            ret.append(node.val)

            if not node.children:
                return
            for child in node.children:
                traversal(child)

        traversal(root)
        return ret

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        94. 二叉树的中序遍历
        https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
        """
        if root is None:
            return []
        ret = list()

        def traversal(node: TreeNode):
            if node is None:
                return
            traversal(node.left)
            ret.append(node.val)
            traversal(node.right)

        traversal(root)
        return ret

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        145. 二叉树的后序遍历
        https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
        """
        if root is None:
            return []
        ret = list()

        def traversal(node: TreeNode):
            if node is None:
                return
            traversal(node.left)
            traversal(node.right)
            ret.append(node.val)

        traversal(root)
        return ret

    def postorder(self, root: 'Node') -> List[int]:
        """
        590. N 叉树的后序遍历
        https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/
        """
        ret = []

        def traversal(node):
            if node is None:
                return
            while 1:
                if not node.children:
                    break
                for child in node.children:
                    traversal(child)
                break
            ret.append(node.val)

        traversal(root)
        return ret


    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        102. 二叉树的层序遍历
        https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
        """
        if root is None:
            return []
        deq = deque()
        deq.append((root, 1))

        ret = []

        curr_lvl = 0
        while len(deq) > 0:
            node, lvl = deq.popleft()
            if lvl != curr_lvl:
                ret.append([])
                curr_lvl = lvl
            ret[len(ret)-1].append(node.val)
            if node.left is not None:
                deq.append((node.left, lvl+1))
            if node.right is not None:
                deq.append((node.right, lvl+1))

        return ret
