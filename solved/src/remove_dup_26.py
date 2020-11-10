from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        for i in reversed(range(len(nums))):
            if nums.count(nums[i]) > 1:
                del nums[i]

        return len(nums)

