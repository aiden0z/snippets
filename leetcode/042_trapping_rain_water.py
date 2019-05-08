"""Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after rainning.


![](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

The above elevation map is represented by array [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1].
In this case, 6 units of rain water (blue section) are being trapped.


Example:

                          *
                  *       * *   *
              *   * *   * * * * * *
            0 1 2 3 4 5 6 7 8 9 0 1
    Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6

"""

from typing import List, Tuple


class Solution:

    def trap(self, height: List[int]) -> int:

        return self.calculate(height, 0)

    def calculate(self, height: List[int], total: int) -> None:

        start, end = self.fix(height)

        if start >= end or end - start == 1:
            return total

        filled = 0
        for i in range(start + 1, end + 1):
            filled += height[i]
            if height[i] >= height[start]:
                total += ((i - start - 1) * height[start] - (filled - height[i]))
                return self.calculate(height[i:], total)

        # 翻转重新计算，比如 [4, 2, 3] -> [3, 2, 4]
        return total + self.calculate(height[::-1], 0)

    # 每次计算桶的左边界和右边界
    def fix(self, height: List[int]) -> Tuple:

        def _fix(height: List[int], start: int) -> int:
            if len(height) <= 2:
                return start

            maxmium = max(height)

            if maxmium == height[0]:
                second_maxmium = max(height[1:])
                if second_maxmium == height[1]:
                    return _fix(height[1:], start + 1)

            inner = 0
            for i in range(1, len(height)):
                if height[i] >= height[i - 1]:
                    if i - inner == 1:
                        inner = i
                    else:
                        break
                else:
                    break
            return start + inner

        start = _fix(height, 0)
        end = len(height) - _fix(height[::-1], 0) - 1
        return start, end


class SolutionB:

    def trap(self, height: List[int]) -> int:
        right_index = len(height) - 1
        left_index = 0
        max_left_height, max_right_height = 0, 0
        count = 0
        while right_index > left_index:
            if height[left_index] < height[right_index]:
                if height[left_index] >= max_left_height:
                    max_left_height = height[left_index]
                count += (max_left_height - height[left_index])
                left_index += 1
            else:
                if height[right_index] >= max_right_height:
                    max_right_height = height[right_index]
                count += (max_right_height - height[right_index])
                right_index -= 1
        return count


class SolutionDP:

    def trap(self, height: List[int]) -> int:
        count = 0
        maxmium = 0

        # 寻找 i 左边最大值
        dp = []
        for i in range(len(height)):
            dp.append(maxmium)
            maxmium = max([maxmium, height[i]])

        maxmium = 0
        for i in range(len(height) - 1, -1, -1):
            dp[i] = min(dp[i], maxmium)
            maxmium = max([maxmium, height[i]])
            if dp[i] - height[i] > 0:
                count += dp[i] - height[i]
        return count


class SolutionStack:

    def trap(self, height: List[int]) -> int:
        stack = []

        count = 0
        i = 0

        while i < len(height):
            if len(stack) == 0 or height[i] <= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                target = stack.pop()
                if len(stack) == 0:
                    continue
                width = i - stack[-1] - 1
                count += (min([height[i], height[stack[-1]]]) - height[target]) * width
        return count


if __name__ == '__main__':

    cases = [([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6), ([4, 2, 3], 1),
             ([6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3], 83)]
    # print(Solution().fix([3, 2, 1, 2, 1]))
    # print(Solution().fix([4, 2, 3]))
    # print(Solution().fix([1, 2, 1, 2, 3]))
    # print(Solution().fix([2, 1, 1]))
    # print(Solution().fix([2, 2, 5, 2, 2]))
    # print(Solution().fix([2, 0, 0, 2]))

    for case in cases:
        for S in [Solution, SolutionB, SolutionDP, SolutionStack]:
            s = SolutionStack()
            # print(s.trap(case[0]))
            assert s.trap(case[0]) == case[1]
