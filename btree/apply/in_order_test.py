import unittest

from .in_order import TreeNode, Solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_isValidBST(self):
        cases = (
            ([2, 1, 3], True),
        )
        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode.buildFromLevel(case[0])
                expect = case[1]
                actual = self.s.isValidBST(root)
                self.assertEqual(expect, actual)

    def test_isValidBST2(self):
        cases = (
            ([2, 1, 3], True),
            ([-2147483648, ], True)
        )
        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode.buildFromLevel(case[0])
                expect = case[1]
                actual = self.s.isValidBST2(root)
                self.assertEqual(expect, actual)

    def test_findMode(self):
        cases = (
            ([1, None, 2, None, None, 2], [2, ]),
        )
        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode.buildFromLevel(case[0])
                expect = case[1]
                actual = self.s.findMode(root)
                self.assertEqual(expect, actual)

    def test_lowestCommonAncestor(self):
        cases = (
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], TreeNode(val=5), TreeNode(val=4),),
        )

        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode.buildFromLevel(case[0])
                expect = case[1]
                actual = self.s.findMode(root)
                self.assertEqual(expect, actual)

    def test_getNumber(self):
        cases = (
            ([3, 1, 4, None, 2, None, 5], [[1, 2, 4], [1, 1, 3], [0, 3, 5]], 2),
        )
        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode.buildFromLevel(case[0])
                expect = case[2]
                actual = self.s.getNumber(root, case[1])
                self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
