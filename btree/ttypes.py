from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other) -> bool:
        if other is None or not isinstance(other, TreeNode):
            return False
        if self.val != other.val:
            return False
        if not self.left == other.left:
            return False
        if not self.right == other.right:
            return False
        return True

    @staticmethod
    def buildFromLevel(vals: List[int]):
        if len(vals) == 0:
            return
        nodes = []
        for val in vals:
            if val is not None:
                nodes.append(TreeNode(val=val))
            else:
                nodes.append(None)

        for (i, node) in enumerate(nodes, start=1):
            if node is None:
                continue
            if 2 * i <= len(nodes):
                node.left = nodes[2 * i - 1]
            if 2 * i + 1 <= len(nodes):
                node.right = nodes[2 * i]
        return nodes[0]
