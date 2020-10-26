from typing import List


class Solution:
    def findArea(self, height: List[int], i: int, j: int) -> int:
        "Given two indices, i and j, find the area."
        base = j - i
        height = min(height[i], height[j])
        return base * height

    def find_bigger_container(self, height, biggest, i, j):
        "See if i and j form a bigger container than current biggest"
        new_area  = self.findArea(height, i, j)
        if new_area > biggest:
            return new_area
        else:
            return 0

    def maxArea(self, height: List[int]) -> int:
        if len(height) in [0, 1]:
            return 0
        biggest = self.findArea(height, 0, len(height)-1)

        for i in range(0, len(height) - 1):
            for j in range(i+1, len(height)):
                new_area = self.find_bigger_container(height, biggest, i, j)
                if new_area:
                    biggest = new_area

        return biggest

