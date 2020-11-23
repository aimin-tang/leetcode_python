from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0

        result = 0
        for idx, num in enumerate(nums):
            if num < target:
                result = idx + 1
            else:
                return result
        else:
            return result
