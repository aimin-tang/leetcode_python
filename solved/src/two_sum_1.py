from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in nums:
                idx2 = nums.index(diff)
                if idx != idx2:
                    return sorted([idx, nums.index(diff)])