import unittest

from .level import Solution, TreeNode


class MyTestCase(unittest.TestCase):
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

    def test_levelOrderBottom(self):
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
                expect.reverse()
                actual = s.levelOrderBottom(root)
                self.assertEqual(expect, actual)

    def test_rightSideView(self):
        cases = [
            ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
            ([1, None, 3], [1, 3]),
            ([1, ], [1, ]),
            ([], [])
        ]
        s = Solution()

        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode.buildFromLevel(case[0])
                expect = case[1]
                actual = s.rightSideView(root)
                self.assertEqual(expect, actual)

    def test_averageOfLevels(self):
        cases = [
            ([3, 9, 20, None, None, 15, 7], [3.00000, 14.50000, 11.00000]),
            ([3, 9, 20, 15, 7], [3.00000, 14.50000, 11.00000]),
            ([1, ], [1.0, ]),
            ([], [])
        ]
        s = Solution()

        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode.buildFromLevel(case[0])
                expect = case[1]
                actual = s.averageOfLevels(root)
                self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
