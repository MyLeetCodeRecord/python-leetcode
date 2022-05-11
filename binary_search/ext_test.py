import unittest

from .ext import Solution


class MyTestCase(unittest.TestCase):
    def test_maximumCandies(self):
        cases = (
            ([5, 8, 6], 3, 5),
            ([2, 5], 11, 0),
            ([1, 2, 6, 8, 6, 7, 3, 5, 2, 5], 3, 6)
        )
        s = Solution()
        for (i, case) in enumerate(cases):
            with self.subTest(i=i):
                expect = case[2]
                actual = s.maximumCandies(case[0], case[1])
                self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
