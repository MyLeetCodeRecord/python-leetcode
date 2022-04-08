import unittest

from .ext import Solution, TreeNode


class MyTestCase(unittest.TestCase):
    def test_preorderTraversal(self):
        cases = [
            ([1, None, 2, None, None, 3], [1, 2, 3]),
            ([1, 2], [1, 2]),
            ([1, ], [1, ]),
            ([1, None, 2], [1, 2]),
            ([], [])
        ]
        s = Solution()

        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode.buildFromLevel(case[0])
                expect = case[1]
                actual = s.preorderTraversal(root)
                self.assertEqual(expect, actual)

    def test_postorderTraversal(self):
        cases = [
            ([1, None, 2, None, None, 3], [3, 2, 1]),
            ([1, 2], [2, 1]),
            ([1, ], [1, ]),
            ([1, None, 2], [2, 1]),
            ([], [])
        ]
        s = Solution()

        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode.buildFromLevel(case[0])
                expect = case[1]
                actual = s.postorderTraversal(root)
                self.assertEqual(expect, actual)

    def test_inorderTraversal(self):
        cases = [
            ([1, None, 2, None, None, 3], [1, 3, 2]),
            ([1, 2], [2, 1]),
            ([1, ], [1, ]),
            ([1, None, 2], [1, 2]),
            ([], [])
        ]
        s = Solution()

        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode.buildFromLevel(case[0])
                expect = case[1]
                actual = s.inorderTraversal(root)
                self.assertEqual(expect, actual)

    def test_levelOrder(self):
        cases = [
            ([1, None, 2, None, None, 3], [[1], [2], [3]]),
            ([1, 2], [[1], [2]]),
            ([1, ], [[1], ]),
            ([1, None, 2], [[1], [2]]),
            ([], [])
        ]
        s = Solution()

        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode.buildFromLevel(case[0])
                expect = case[1]
                actual = s.levelOrder(root)
                self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
