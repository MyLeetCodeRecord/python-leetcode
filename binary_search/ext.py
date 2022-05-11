from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """
        2226. 每个小孩最多能分到多少糖果
        https://leetcode-cn.com/problems/maximum-candies-allocated-to-k-children/
        """
        _sum = sum(candies)
        if _sum < k:
            return 0
        left, right = 1, 10**7
        while left <= right:
            size = (left+right) // 2
            _k = sum([can//size for can in candies])
            #  每组太多了, 分组不够
            if _k < k:
                right = size - 1
            else:
                left = size + 1
        # if sum([can // left for can in candies]) >= k:
        #     return left
        return left - 1


