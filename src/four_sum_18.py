from typing import List
from itertools import combinations


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        for c in combinations(nums, 4):
            c = sorted(list(c))
            if sum(c) == target and c not in result:
                result.append(c)

        return sorted(result)
