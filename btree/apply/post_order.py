from collections import defaultdict, deque
from typing import List, Optional

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
        while len(deq) > 0:
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
            return 1 + right
        if root.right is None:
            return 1 + left
        return 1 + min(left, right)

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

            if abs(leftDepth - rightDepth) > 1:
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

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        236. 二叉树的最近公共祖先
        https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
        """
        if root is None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is not None and right is not None:
            return root
        elif left is not None:
            return left
        elif right is not None:
            return right
        return None

    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        669. 修剪二叉搜索树
        https://leetcode-cn.com/problems/trim-a-binary-search-tree/
        """
        if root is None:
            return None
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        if root.val < low or root.val > high:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            cur = root.right
            while cur.left:
                cur = cur.left
            cur.left = root.left
            return root.right
        return root

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        """
        508. 出现次数最多的子树元素和
        https://leetcode.cn/problems/most-frequent-subtree-sum/
        """
        cnt_map = defaultdict(int)

        def traval(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                cnt_map[node.val] = cnt_map[node.val] + 1
                return node.val
            left = traval(node.left)
            right = traval(node.right)
            s = left + right + node.val
            cnt_map[s] = cnt_map[s] + 1
            return s

        traval(root)
        curr_cnt = 0
        for _, cnt in cnt_map.items():
            if cnt > curr_cnt:
                curr_cnt = cnt

        ret = []
        for s, cnt in cnt_map.items():
            if cnt == curr_cnt:
                ret.append(s)

        return ret
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        """
        687. 最长同值路径
        https://leetcode.cn/problems/longest-univalue-path/
        """        
        self.max = 0
        def post_travel(node):
            if node is None:
                return 0
            left, right = post_travel(node.left), post_travel(node.right)

            left1 = left + 1 if node.left and node.left.val == node.val else 0
            right1 = right + 1 if node.right and node.right.val == node.val else 0

            self.max = max(self.max, left1+right1)
            return max(left1, right1)
        post_travel(root)
        return self.max
                
