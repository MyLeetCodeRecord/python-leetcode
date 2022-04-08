import unittest

from .mirror import TreeNode, Solution


class MyTestCase(unittest.TestCase):
    def test_isSymmetric(self):
        cases = (
            ([1, 2, 2, 3, 4, 4, 3], True),
            ([1, 2, 2, None, 3, None, 3], False),
        )
        s = Solution()
        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                root = TreeNode.buildFromLevel(case[0])
                expect = case[1]
                actual = s.isSymmetric(root)
                self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
