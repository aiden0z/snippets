"""Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

Refer https://leetcode.com/problems/median-of-two-sorted-arrays/
"""


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        O(m + n)
        """
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        mid = int((nums1_len + nums2_len) / 2) + 1
        even = True
        if (nums1_len + nums2_len) % 2 == 1:
            even = False
        result = []
        i, j, = 0, 0
        while True:
            if i < nums1_len and j < nums2_len and nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            elif i < nums1_len and j < nums2_len and nums1[i] > nums2[j]:
                result.append(nums2[j])
                j += 1
            elif i < nums1_len and j >= nums2_len:
                result.append(nums1[i])
                i += 1
            elif i >= nums1_len and j < nums2_len:
                result.append(nums2[j])
                j += 1
            if len(result) == mid:
                break

        if even:
            return (result[-1] + result[-2]) / 2.0
        return result[-1] * 1.0


class SolutionB(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        O(lg(m+n))
        """

        def search(l1, l2, k):
            if len(l1) == 0:
                return l2[k]
            if len(l2) == 0:
                return l1[k]
            if k == 0:
                return min(l1[k], l2[k])
            mid1 = len(l1) >> 1
            mid2 = len(l2) >> 1
            if mid1 + mid2 < k:
                if l1[mid1] > l2[mid2]:
                    return search(l1, l2[mid2 + 1:], k - mid2 - 1)
                return search(l1[mid1 + 1:], l2, k - mid1 - 1)
            else:
                if l1[mid1] > l2[mid2]:
                    return search(l1[:mid1], l2, k)
                return search(l1, l2[:mid2], k)

        leng = len(nums1) + len(nums2)
        if leng % 2 == 0:
            return (search(nums1, nums2, leng >> 1) + search(nums1, nums2, (leng >> 1) - 1)) / 2.0
        return search(nums1, nums2, leng >> 1)


class SolutionC(object):

    def findMedianSortedArrays(self, a, b):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        c = a + b
        c.sort()
        m = len(c) / 2
        mm = len(c) % 2
        if mm > 0:
            return c[m]
        return (c[m - 1] + c[m]) / 2.0


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 3, 4, 5]
    nums2 = [2]
    print(s.findMedianSortedArrays(nums1, nums2))

    nums1 = [1, 2, 4, 5, 6, 7]
    nums2 = [3, 4, 5, 6]
    print(s.findMedianSortedArrays(nums1, nums2))
