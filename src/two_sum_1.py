from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(list)

        for idx, num in enumerate(nums):
            d[num].append(idx)

        for idx, num in enumerate(nums):
            diff = target - num
            if diff == num:
                if len(d[num]) > 1:
                    return [d[num][0], d[num][1]]
            else:
                if len(d[diff]) > 0:
                    return [idx, d[diff][0]]

        return [-1, -1]

