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
            while len(stack) > 0 and stack[len(stack)-1].val == postorder[j]:
                stack.pop()
                j += 1
            if stack[len(stack)-1].left is None:
                stack[len(stack)-1].left = node
            else:
                stack[len(stack)-1].right = node
            stack.append(node)
        # 如果再这里再补一份出栈, 最终stack为空
        return stack[0]
