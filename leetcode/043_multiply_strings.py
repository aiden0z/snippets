"""Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of
num1 and num2, also represented as a string.

Example 1:

    Input: num1 = "2", num2 = "3"
    Output: "6"

Example 2:

    Input: num1 = "123", num2 = "456"
    Output: "56088"

Note:

    1. The length of both num1 and num2 is < 110.
    2. Both num1 and num2 contain only digits 0-9;
    3. Both num1 and num2 do not contain any leading zero, except the number 0 itself.
    4. You must not use any built-in BigInteger library or convert the inputs to integer
       directly.
"""


class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]

        arr = [0] * (len(num1) + len(num2))
        # arr = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i + j] += int(num1[i]) * int(num2[j])

        ans = []
        for i in range(len(arr)):
            digit = arr[i] % 10
            carry = arr[i] // 10
            if i < len(arr) - 1:
                arr[i + 1] += carry
            ans.insert(0, str(digit))

        while ans[0] == '0' and len(ans) > 1:
            del ans[0]
        return ''.join(ans)


class SolutionB:

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        ans = 0
        for i, n1 in enumerate(num2[::-1]):
            pre = 0
            curr = 0
            for j, n2 in enumerate(num1[::-1]):
                multi = (ord(n1) - ord('0')) * (ord(n2) - ord('0'))
                first, second = multi // 10, multi % 10
                curr += (second + pre) * (10**j)
                pre = first
            curr += pre * (10**len(num1))
            ans += curr * (10**i)
        return str(ans)


if __name__ == '__main__':
    cases = [(('2', '3'), '6'), (('123', '456'), '56088')]

    for case in cases:
        for S in [Solution, SolutionB]:
            assert S().multiply(*case[0]) == case[1]
