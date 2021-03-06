from typing import List, Optional

from btree import TreeNode
import bisect


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        98. 验证二叉搜索树
        https://leetcode-cn.com/problems/validate-binary-search-tree/

        1. 不能单纯的比较左节点小于中间节点，右节点大于中间节点就完事了
           见测试用例1
        """
        # if root is None:
        #     return False
        #
        # self.result = True
        #
        # def traversal(node):
        #     if node is None:
        #         return
        #     nodeVal = node.val
        #     if node.left:
        #         leftVal = node.left.val
        #         if nodeVal <= leftVal:
        #             self.result = False
        #             return
        #         traversal(node.left)
        #     if node.right:
        #         rightVal = node.right.val
        #         if nodeVal >= rightVal:
        #             self.result = False
        #             return
        #         traversal(node.right)
        #
        # traversal(root)
        # return self.result

        self.store = []

        def traversal(node):
            if node is None:
                return
            traversal(node.left)
            self.store.append(node.val)
            traversal(node.right)

        def isSorted(lll):
            pre, post = 0, 1
            while post < len(lll):
                if lll[pre] >= lll[post]:
                    return False
                pre += 1
                post += 1
            return True

        traversal(root)
        if len(self.store) == 0:
            return False
        return isSorted(self.store)

    def isValidBST2(self, root: TreeNode) -> bool:
        """
        98. 验证二叉搜索树
        https://leetcode-cn.com/problems/validate-binary-search-tree/

        递归实现
        """
        self.max = - (2 ** 32)

        def traversal(node):
            if node is None:
                return True
            left = traversal(node.left)
            if not left:
                return False
            elif node.val > self.max:
                self.max = node.val
            else:
                return False
            right = traversal(node.right)
            return right

        return traversal(root)

    def getMinimumDifference(self, root: TreeNode) -> int:
        """
        530. 二叉搜索树的最小绝对差
        https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
        """

        ser = []

        def traversal(node):
            if node is None:
                return
            traversal(node.left)
            ser.append(node.val)
            traversal(node.right)

        traversal(root)

        minDiff = 10 ** 5
        pre, post = 0, 1
        while post < len(ser):
            minDiff = min(minDiff, abs(ser[post] - ser[pre]))
            post += 1
            pre += 1

        return minDiff

    def getMinimumDifference2(self, root: TreeNode) -> int:
        """
        530. 二叉搜索树的最小绝对差
        https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
        """

        self.minDiff = 10 ** 5
        self.pre = None

        def traversal(node):
            if node is None:
                return
            traversal(node.left)
            if self.pre is not None:
                self.minDiff = min(self.minDiff, node.val - self.pre.val)  # 为啥不需要abs?
            self.pre = node
            traversal(node.right)

        traversal(root)

        return self.minDiff

    def findMode(self, root: TreeNode) -> List[int]:
        """
        501. 二叉搜索树中的众数
        https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/
        """

        self.store = []
        self.cnt, self.maxCnt = 0, 0
        self.pre = None

        def traversal(node):
            if node is None:
                return
            traversal(node.left)

            if self.pre is not None and self.pre.val == node.val:
                self.cnt += 1
            else:
                self.cnt = 1

            self.pre = node
            if self.cnt == self.maxCnt:
                self.store.append(node.val)
            elif self.cnt > self.maxCnt:
                self.maxCnt = self.cnt
                self.store.clear()
                self.store.append(node.val)
            traversal(node.right)

        traversal(root)

        return self.store

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        235. 二叉搜索树的最近公共祖先
        https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
        """
        if root is None:
            return None
        if root.val > p.val and root.val > q.val:
            left = self.lowestCommonAncestor(root.left, p, q)
            if left:
                return left
        if root.val < p.val and root.val < q.val:
            right = self.lowestCommonAncestor(root.right, p, q)
            if right:
                return right
        return root

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        235. 二叉搜索树的最近公共祖先
        https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
        """
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                break
        return root

    def lowestCommonAncestor3(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        236. 二叉树的最近公共祖先
        https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

        区别于二叉搜索树, 没有大小性质可以利用, 只能全遍历
        """
        if root is None:
            return root
        if root == p or root == q:
            return root





    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        538. 把二叉搜索树转换为累加树
        https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
        """
        if root is None:
            return None

        self.pre = TreeNode()

        def traversal(node):
            if node is None:
                return
            traversal(node.right)
            node.val += self.pre.val
            self.pre = node

            traversal(node.left)

        traversal(root)
        return root

    def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
        ser = []

        def traversal(node):
            if node is None:
                return
            traversal(node.left)
            ser.append(node.val)
            traversal(node.right)
        traversal(root)

        mark = [1] * len(ser)
        for op in ops:
            code, x, y = op
            left = bisect.bisect_left(ser, x)
            right = bisect.bisect_right(ser, y)
            if code == 1:
                mark[left] += 1
                if right < len(mark):
                    mark[right] += -1
            else:
                mark[left] += -1
                if right < len(mark):
                    mark[right] += 1
        flag = mark[0]
        for i in range(1,len(mark)):
            mark[i] = flag + mark[i-1]
            flag = mark[i]

        cnt = 0
        for m in mark:
            if m > 0:
                cnt += 1

        return cnt

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        """
        面试题 04.06. 后继者
        https://leetcode.cn/problems/successor-lcci/

        先利用二叉搜索树性质, 找到目标节点
        有右子树的, 用由子树的最左边节点
        没有右子树, 用"父节点"
            父节点不一定大于自己, 因此需要存下链路
        没有父节点, 返回None
        """

        parents = []
        curr = root
        while curr is not None:
            if curr.val == p.val:
                break;
            elif curr.val > p.val:
                parents.append(curr)
                curr = curr.left
            else:
                parents.append(curr)
                curr = curr.right
        if curr is None:
            return None
        if curr.right is None:
            while len(parents) > 0:
                parent = parents.pop()
                if parent.val > curr.val:
                    return parent
            return None
        curr = curr.right
        while curr.left is not None:
            curr = curr.left
        return curr

    def inorderSuccessor_1(self, root: TreeNode, p: TreeNode) -> TreeNode:
        """
        面试题 04.06. 后继者
        https://leetcode.cn/problems/successor-lcci/

        也可以不用完整的存链路, 只要节点比p的值大, 就更新
        存下最底层的那个即可
        """
        if p.right:
            curr = p.right
            while curr.left:
                curr = curr.left
            return curr
        curr = root
        successor = None
        while curr:
            if curr.val > p.val:
                successor = curr
                curr = curr.left
            else:
                curr = curr.right
        return successor

