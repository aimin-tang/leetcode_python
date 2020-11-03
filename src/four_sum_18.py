from typing import List


class Solution:
    def get_last_two(self, nums: List[int], target: int, pos1: int, pos2: int) -> List[List[int]]:
        """
        If pos1 and pos2 are known for the first two numbers, find all solutions
        """
        l = pos2 + 1
        r = len(nums) - 1
        result = []

        while l < r:
            if nums[pos1] + nums[pos2] + nums[l] + nums[r] < target:
                l += 1
            elif nums[pos1] + nums[pos2] + nums[l] + nums[r] > target:
                r -= 1
            else:
                one_answer = [nums[pos1], nums[pos2], nums[l], nums[r]]
                one_answer.sort()
                result.append(one_answer)
                l += 1
                r -= 1

        return result


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        if len(nums) < 4:
            return []

        result = []
        for pos1 in range(len(nums) - 3):
            for pos2 in range(pos1+1, len(nums) - 2):
                result.extend(self.get_last_two(nums, target, pos1, pos2))

        result2 = []
        for r in result:
            if r not in result2:
                result2.append(r)
        return result2
