import unittest

from .ttypes import TreeNode


class TestTreeNode(unittest.TestCase):

    def test_build(self):
        cases = [
            ([], None),
            ([1, ], TreeNode(val=1)),
            ([1, 2, ], TreeNode(val=1, left=TreeNode(val=2))),
            ([1, 2, 3], TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))),
            ([1, 2, 3, 4], TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4)), right=TreeNode(val=3))),
            ([1,None, 3, None, None, 4], TreeNode(val=1, right=TreeNode(val=3, left=TreeNode(val=4)))),
        ]
        for (i, case) in enumerate(cases, start=1):
            with self.subTest(i=i):
                actual = TreeNode.buildFromLevel(case[0])
                expect = case[1]
                self.assertEqual(expect, actual)

    def test_eq(self):
        cases = [
            (None, TreeNode(val=0), False),
            (TreeNode(val=0), TreeNode(val=0), True),
            (TreeNode(val=0), TreeNode(val=1), False),
            (TreeNode(val=0), TreeNode(val=0, left=TreeNode(val=1)), False),
            (TreeNode(val=0), TreeNode(val=0, right=TreeNode(val=1)), False),
            (TreeNode(val=0, left=TreeNode(val=1)), TreeNode(val=0, left=TreeNode(val=1)), True),
            (TreeNode(val=0, right=TreeNode(val=1)), TreeNode(val=0, left=TreeNode(val=1)), False),
            (TreeNode(val=0, right=TreeNode(val=1)), TreeNode(val=0, right=TreeNode(val=1)), True),
        ]

        for (i, case) in enumerate(cases, start=1):
            with self.subTest(i=i):
                self.assertEqual(case[2], case[0] == case[1])


if __name__ == '__main__':
    unittest.main()
