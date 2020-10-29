from typing import List


class Solution:
    def three_sum_closest_on_n1(self, nums: List[int], num1_pos: int, target: int) -> int:
        """
        If num1 is fixed at num1_pos, which two numbers after it can we get
        to be close to target.
        """
        # num1_pos is at least 2 positions before end. so there is always an answer.
        l = num1_pos + 1
        r = len(nums) - 1
        result = nums[num1_pos] + nums[l] + nums[r]
        min_diff = abs(result - target)

        while l < r:
            tmp_result = nums[num1_pos] + nums[l] + nums[r]
            tmp_diff = abs(tmp_result - target)
            if tmp_result > target:
                r -= 1
                if tmp_diff < min_diff:
                    result = tmp_result
                    min_diff = tmp_diff
            elif tmp_result < target:
                l += 1
                if tmp_diff < min_diff:
                    result = tmp_result
                    min_diff = tmp_diff
            else:
                return target

        return result


    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        last_best = self.three_sum_closest_on_n1(nums=nums, num1_pos=0, target=target)
        if len(nums) == 3:
            return last_best

        for start in range(1, len(nums) - 2):
            curr_best = self.three_sum_closest_on_n1(nums, start, target)
            if abs(curr_best - target) < abs(last_best - target):
                last_best = curr_best
                if last_best == target:
                    return last_best

        return last_best


