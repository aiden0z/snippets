""" Merge Intervals

Given a collection of intervals, merge all overlapping intervals:

Example 1:

    Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6]
    Output: [[1, 6], [8, 10], [15, 18]]
    Explanation: Since intervals [1, 3] and [2, 6] overlaps, merge them into [1, 6].

Example 2:

    Input: intervals = [[1, 4], [4, 5]]
    Output: [[1, 5]]
    Explanation: Intervals [1, 4] and [4, 5] are considered overlapping.

Constraints:

    intervals[i][0] <= intervals[i][1]

"""

from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) in (0, 1):
            return intervals

        intervals.sort(key=min)

        result = [intervals[0]]
        i = 0
        for j in range(1, len(intervals)):
            if result[i][1] >= intervals[j][0]:
                result[i] = [min(result[i] + intervals[j]), max(result[i] + intervals[j])]
            else:
                result.append(intervals[j])
                i += 1
        return result


if __name__ == '__main__':
    cases = [
        ([[1, 4], [0, 0]], [[0, 0], [1, 4]]),
        ([[1, 4], [0, 1]], [[0, 4]]),
        ([[1, 4], [0, 4]], [[0, 4]]),
        ([[0, 4], [1, 4]], [[0, 4]]),
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
    ]  # yapf: disable

    for case in cases:
        for S in [Solution]:
            assert S().merge(case[0]) == case[1]
