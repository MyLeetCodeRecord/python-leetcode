from typing import List, Optional
from collections import deque
from copy import deepcopy

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
        leftHeight, rightHeight = 1, 1  # 初始值为1,
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

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        404. 左叶子之和
        https://leetcode-cn.com/problems/sum-of-left-leaves/
        """

        def traversal(node, isLeft):
            if node is None:
                return
            if node.left is None and node.right is None:
                if isLeft:
                    self.sum += node.val
                return
            traversal(node.left, True)
            traversal(node.right, False)

        self.sum = 0
        traversal(root, False)
        return self.sum

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        112. 路径总和
        https://leetcode-cn.com/problems/path-sum/
        """
        if root is None:
            return False

        self.sum = 0
        self.found = False

        def traversal(node):
            if node is None:
                return
            self.sum += node.val
            if self.sum == targetSum and not node.left and not node.right:
                self.found = True
            if self.found:
                return
            traversal(node.left)
            traversal(node.right)
            self.sum -= node.val

        traversal(root)
        return self.found

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        113. 路径总和 II
        https://leetcode-cn.com/problems/path-sum-ii/
        """
        if root is None:
            return []

        self.sum = 0
        self.path = []
        self.result = []

        def traversal(node):
            if node is None:
                return
            self.sum += node.val
            self.path.append(node.val)

            if self.sum == targetSum and not node.left and not node.right:
                self.result.append(deepcopy(self.path))
            else:  # 这个地方和hasPathSum的短路效果不同, 不能直接返回, 需要能pop和减去
                traversal(node.left)
                traversal(node.right)

            self.path.pop()
            self.sum -= node.val

        traversal(root)
        return self.result

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """
        617. 合并二叉树
        https://leetcode-cn.com/problems/merge-two-binary-trees/
        """
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        root = root1
        root.val = root.val + root2.val

        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)

        return root

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        700. 二叉搜索树中的搜索
        https://leetcode-cn.com/problems/search-in-a-binary-search-tree/
        """

        self.result = None

        def traversal(node):
            if node is None:
                return
            if node.val == val:
                self.result = node
                return
            traversal(node.left)
            traversal(node.right)

        traversal(root)
        return self.result

    def searchBST2(self, root: TreeNode, val: int) -> TreeNode:
        """
        700. 二叉搜索树中的搜索
        https://leetcode-cn.com/problems/search-in-a-binary-search-tree/
        """

        self.result = None

        def traversal(node):
            if node is None:
                return
            if node.val == val:
                self.result = node
                return
            elif node.val > val:
                traversal(node.left)
            else:
                traversal(node.right)

        traversal(root)
        return self.result


    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        701. 二叉搜索树中的插入操作
        https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/
        """
        if root is None:
            return TreeNode(val=val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        450. 删除二叉搜索树中的节点
        https://leetcode-cn.com/problems/delete-node-in-a-bst/
        """
        if root is None:
            return None
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            curr = root.right
            while curr.left:  # 右支的最小值, 但大于left
                curr = curr.left
            curr.left = root.left
            return root.right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        669. 修剪二叉搜索树
        https://leetcode-cn.com/problems/trim-a-binary-search-tree/
        """
        if root is None:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        108. 将有序数组转换为二叉搜索树
        https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
        """
        if len(nums) == 0:
            return None
        length = len(nums)
        mid = length // 2  # 0, 1, 2 => 2; 0, 1 => 1
        root = TreeNode(val=nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

