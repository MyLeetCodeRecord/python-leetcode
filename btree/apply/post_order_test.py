import unittest

from .post_order import TreeNode, Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_findDuplicateSubtrees(self):
        cases = (
            ([2, 1, 11, 11, None, 1], []),
        )

        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode.buildFromLevel(case[0])
                expect = case[1]
                actual = self.s.findDuplicateSubtrees(root)
                self.assertEqual(expect, actual)

    def test_longestUnivaluePath(self):
        cases = (
            ([5, 4, 5, 1, 1, 5], 2),
        )
        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode(
                    val=1,
                    right=TreeNode(1,
                                   left=TreeNode(1, left=TreeNode(1), right=TreeNode(1)),
                                   right=TreeNode(1, left=TreeNode(1))
                                   )
                )
                expect = case[1]
                actual = self.s.longestUnivaluePath(root)
                self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
