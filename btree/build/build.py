from typing import List

from btree import TreeNode


class Solution:
    """
    1. 只用 前序+后序 不能确定唯一树 ?
        如果树是满二叉树, 是可以确定的.
    2. 前序是刚进入节点时, 就做记录
        后序是准备离开节点时做记录
    """

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        """
        889. 根据前序和后序遍历构造二叉树
        https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

        结合前序后序的性质 + 元素不重复.
        因此一旦发现前序的值等于后序的值时, 即表示这个节点(以及它的子节点)已经构造完毕, 开始准备退出了.

        因此, 将前缀的构造节点压栈, 如果栈顶元素和后序值相等, 则出栈表示其构造结束.
        同时后序的光标后移一位.
        """
        stack = list()
        stack.append(TreeNode(val=preorder[0]))

        j = 0
        for i in range(1, len(preorder)):
            node = TreeNode(val=preorder[i])
            # 由于是在压栈之前做判断, 因此会遗漏最后一轮的后序退出
            # 最终stack中会有剩余数据, 其中stack[0]为root
            while len(stack) > 0 and stack[len(stack) - 1].val == postorder[j]:
                stack.pop()
                j += 1
            if stack[len(stack) - 1].left is None:
                stack[len(stack) - 1].left = node
            else:
                stack[len(stack) - 1].right = node
            stack.append(node)
        # 如果再这里再补一份出栈, 最终stack为空
        return stack[0]

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        106. 从中序与后序遍历序列构造二叉树
        https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

        inorder 和 postorder 都由 不同 的值组成
        """
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        root = TreeNode(val=postorder[-1])
        midIdx = inorder.index(root.val)

        leftInOrder = inorder[:midIdx]
        leftPostOrder = postorder[0:len(leftInOrder)]
        root.left = self.buildTree(leftInOrder, leftPostOrder)

        rightInOrder = inorder[midIdx + 1:]
        rightPostOrder = postorder[len(leftInOrder):len(leftInOrder) + len(rightInOrder)]
        root.right = self.buildTree(rightInOrder, rightPostOrder)

        return root

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        105. 从前序与中序遍历序列构造二叉树
        https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
        """
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root = TreeNode(val=preorder[0])
        midIdx = inorder.index(root.val)

        leftInOrder = inorder[:midIdx]
        leftPreOrder = preorder[1:1 + len(leftInOrder)]
        root.left = self.buildTree2(leftPreOrder, leftInOrder)

        rightInOrder = inorder[midIdx + 1:]
        rightPreOrder = preorder[1 + len(leftInOrder):]
        root.right = self.buildTree2(rightPreOrder, rightInOrder)

        return root

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        """
        654. 最大二叉树
        https://leetcode-cn.com/problems/maximum-binary-tree/
        """
        if len(nums) == 0:
            return None

        idx = 0
        _max = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > _max:
                _max = nums[i]
                idx = i

        root = TreeNode(val=_max)
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx + 1:])

        return root


class Codec:
    """
    449. 序列化和反序列化二叉搜索树
    https://leetcode.cn/problems/serialize-and-deserialize-bst/

    由于是 二叉搜索树, 自带排序属性.
    因此可以直接推断出中序遍历.
    构建树, 可以 前+中 或者 后+中, 因此序列化只需要关注 前 或 后.
    """

    def serialize(self, root: TreeNode) -> str:
        arr = []

        def postOrder(root: TreeNode) -> None:
            if root is None:
                return
            postOrder(root.left)
            postOrder(root.right)
            arr.append(root.val)

        postOrder(root)
        return ' '.join(map(str, arr))  # 左 右 中

    def deserialize(self, data: str) -> TreeNode:
        arr = list(map(int, data.split()))

        def construct(lower: int, upper: int) -> TreeNode:
            if arr == [] or arr[-1] < lower or arr[-1] > upper:
                return None
            val = arr.pop()  # 后续遍历, 序列的最后一个一定是(子)树的root,
            root = TreeNode(val)
            root.right = construct(val, upper)  # 必须先右后左, 序列化结果的反向; 同时限定好最小值边界.
            root.left = construct(lower, val)  # 执行最大值边界, 保证左子树的最大值 不超过根节点.
            return root

        return construct(-1, 10001)
