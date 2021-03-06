import unittest
from .pre_order import Solution, TreeNode


class MyTestCase(unittest.TestCase):
    def test_invertTree(self):
        cases = (
            ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        )

        s = Solution()

        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode.buildFromLevel(case[0])
                actual = s.invertTree(root)
                exepct = TreeNode.buildFromLevel(case[1])
                self.assertEqual(exepct, actual)

    def test_countNodes(self):
        cases = (
            ([1, 2, 3, 4, 5, 6], 6),
        )
        s = Solution()
        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode.buildFromLevel(case[0])
                expect = case[1]
                actual = s.countNodes(root)
                self.assertEqual(expect, actual)

    def test_binaryTreePaths(self):
        cases = (
            ([1, 2, 3, None, 5], ["1->2->5", "1->3"]),
        )
        s = Solution()
        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode.buildFromLevel(case[0])
                expect = case[1]
                actual = s.binaryTreePaths(root)
                self.assertEqual(expect, actual)

    def test_pathSum(self):
        cases = (
            ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1], 22, [[5, 4, 11, 2], [5, 8, 4, 5]]),
        )
        s = Solution()
        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode.buildFromLevel(case[0])
                expect = case[2]
                actual = s.pathSum(root, case[1])
                self.assertEqual(expect, actual)

    def test_isValidBST(self):
        cases = (
            ([5, 4, 6, None, None, 3, 7], False),
        )
        s = Solution()
        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode.buildFromLevel(case[0])
                expect = case[1]
                actual = s.isValidBST(root)
                self.assertEqual(expect, actual)

    def test_sumRootToLeaf(self):
        cases = (
            ([1, 0, 1, 0, 1, 0, 1], 22),
            ([1, 1], 3)
        )
        s = Solution()
        for (i, case) in enumerate(cases):
            with self.subTest(i=1):
                root = TreeNode.buildFromLevel(case[0])
                expect = case[1]
                actual = s.sumRootToLeaf(root)
                self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
