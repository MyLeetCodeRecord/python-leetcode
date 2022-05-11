import unittest

from .build import TreeNode, Solution
from .build import Codec


class MyTestCase(unittest.TestCase):
    def test_constructFromPrePost(self):
        cases = [
            ([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1], [1, 2, 3, 4, 5, 6, 7]),
            ([1, ], [1, ], [1, ])
        ]

        s = Solution()

        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                actual = s.constructFromPrePost(case[0], case[1])
                expect = TreeNode.buildFromLevel(case[2])
                self.assertEqual(expect, actual)

    def test_Codec(self):
        cases = [
            [2, 1, 3],
            [],
        ]
        codec = Codec()
        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                tree = TreeNode.buildFromLevel(case)
                ser = codec.serialize(tree)
                deser = codec.deserialize(ser)
                self.assertEqual(tree, deser)


if __name__ == '__main__':
    unittest.main()
