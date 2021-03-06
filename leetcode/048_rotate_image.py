"""Rotate Image
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees(clockwise).

Note: You have to rotate the image in-place, which means you have to modify the input 2D matrix
directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

    Input:
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

    Output:
        [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]

Example 2:

    Input:
        [
            [ 5, 1, 9, 11],
            [ 2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ]

    Output:
        [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
        ]
"""

import copy
from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        length = len(matrix)
        matrix.reverse()

        for i in range(length):
            # 矩阵转置
            for j in range(i + 1, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    cases = [
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],

            [
                [7, 4, 1],
                [8, 5, 2],
                [9, 6, 3]
            ]
        ),
        (
            [
                [5, 1, 9, 11],
                [2, 4, 8, 10],
                [13, 3, 6, 7],
                [15, 14, 12, 16]
            ],
            [
                [15, 13, 2, 5],
                [14, 3, 4, 1],
                [12, 6, 8, 9],
                [16, 7, 10, 11]
            ]
        ),
    ]  # yapf: disable

    for case in cases:
        for S in [Solution]:
            item = copy.deepcopy(case[0])
            S().rotate(item)
            assert item == case[1]
