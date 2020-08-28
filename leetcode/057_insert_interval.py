""" Insert Interval

Given a set of non-verlapping intervals, insert a new interval into the
intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

    Input: intervals = [[1, 3], [6, 9]], newInterval = [2, 5]
    Output: [[1, 5], [6, 9]]

Example 2:

    Input: intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval = [4, 8]
    Output: [[1, 2], [3, 10], [12, 16]]
    Explanation: Because the new interval [4, 8] overlaps with [3, 5], [6, 7], [8, 10]
"""

from typing import List


class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if len(intervals) == 0:
            return [newInterval]

        result = []
        inserted = False
        for i in range(len(intervals)):
            if inserted:
                result.append(intervals[i])
            elif newInterval[0] < intervals[i][0]:
                result.append(newInterval)
                result.append(intervals[i])
                inserted = True
            else:
                result.append(intervals[i])

        if not inserted:
            result.append(newInterval)

        return self.merge(result)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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
        ([[1, 5]], [2, 7], [[1, 7]]),
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
    ]  # yapf: disable

    for case in cases:
        for S in [Solution]:
            assert S().insert(case[0], case[1]) == case[2]
