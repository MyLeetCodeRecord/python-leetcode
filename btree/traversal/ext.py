from typing import List, Optional
from collections import deque

from btree import TreeNode


class Solution:
    """
    区别于basic里面的常规实现方式,
    这里 先序/后序/中序遍历 不用递归 用迭代
    层序遍历 不用bfs 用dfs
    """

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        144. 二叉树的前序遍历
        https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
        """
        if root is None:
            return []
        ret = list()

        stack = list()
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            ret.append(node.val)  # 先记录root
            # 先入栈, 后出栈, 因此先处理右节点
            # 出栈时就变为了 root -> left -> right
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return ret

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        94. 二叉树的中序遍历
        https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
        """
        if root is None:
            return []
        ret = list()

        stack = list()
        curr = root

        while curr is not None or len(stack) > 0:
            if curr is not None:
                # 优先推进左边
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                ret.append(node.val)  # root
                if node.right is not None:
                    # 切到右子树, 重复推进左边
                    curr = node.right

        return ret

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        145. 二叉树的后序遍历
        https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
        """
        if root is None:
            return []
        ret = list()

        stack = list()
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            ret.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        ret.reverse()  # root -> right -> left 的反转
        return ret

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        102. 二叉树的层序遍历
        https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
        """
        if root is None:
            return []
        ret = []

        def dfs(node, lvl):
            if node is None:
                return
            if lvl >= len(ret):
                ret.append([])
            if node.left is not None:
                dfs(node.left, lvl+1)
            ret[lvl-1].append(node.val)
            if node.right is not None:
                dfs(node.right, lvl+1)

        dfs(root, 1)
        if len(ret[len(ret)-1]) == 0:
            ret.pop()

        return ret
