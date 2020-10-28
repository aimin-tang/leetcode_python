from typing import List, Tuple

class Solution:
    def find_the_other_two(self, nums: List[int], i: int, result: List[List[int]]) -> List[Tuple[int]]:
        """
        In sorted list nums, for nums[i], find all j, k so that nums[i] + \
        nums[j] + nums[k] is 0.
        :return list of lists, such as: [[-1, -1, 2], [-1, 0, 1]]
        """
        if nums[i] > 0 or i > len(nums) - 3:
            return []

        l = i + 1
        r = len(nums) - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            elif nums[i] + nums[l] + nums[r] < 0:
                l += 1
            else:
                result.append((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1

        return result


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for start in range(len(nums) - 2):
            self.find_the_other_two(nums, start, result)

        result = set(result)
        return [[n1, n2, n3] for n1, n2, n3 in result]
