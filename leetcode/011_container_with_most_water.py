"""
Given n non-negative integers a1, a2, ..., an, where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
froms a container, such that the container contans the most water.

Note: You may not slant the container and n is at least 2.

Refer: https://leetcode.com/problems/container-with-most-water/
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        max_area = 0

        i = 0
        j = len(height) - 1

        while i < j:
            max_area = max(max_area, min(height[i], height[j])*(j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area


if __name__ == '__main__':
    testcases = [
        ([4, 2, 7, 6], 12)
    ]

    s = Solution()
    for case in testcases:
        assert s.maxArea(case[0]) == case[1]
