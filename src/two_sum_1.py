from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            diff = target - num
            if diff != num:
                if diff in nums:
                    return [idx, nums.index(diff)]
            else:
                # diff is num
                l1 = [idx for idx, n in enumerate(nums) if n == num]
                if len(l1) > 1:
                    return [l1[0], l1[1]]

        return [-1, -1]

