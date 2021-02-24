""" Add Binary
Given two binary strings a and b, return their sum as a binary string.

Example 1:

    Input: a = "11", b = "1"
    Output: "100"

Example 2:

    Input: a = "1010", b = "1011"
    Output: "10101"

Constraints:

* 1 <= a.length, b.length <= 104
* a and b consist only of '0' or '1' characters.
* Each string does not contain leading zeros except for the zero itself.1:
"""


class Solution:

    def add_binary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            much = a
            less = b
        else:
            much = b
            less = a

        r = []

        carry = 0
        for i in range(len(much) - 1, -1, -1):
            lessi = i - (len(much) - len(less))
            if lessi >= 0:
                x = int(less[lessi])
            else:
                x = 0
            y = int(much[i])
            z = carry + x + y

            if z == 3:
                carry = 1
                r.insert(0, "1")
            if z == 2:
                carry = 1
                r.insert(0, "0")
            elif z == 1:
                carry = 0
                r.insert(0, "1")
            elif z == 0:
                r.insert(0, "0")
                carry = 0
        if carry == 1:
            r.insert(0, "1")
        print("".join(r))
        return "".join(r)


if __name__ == '__main__':
    cases = [(["11", "1"], "100"), (["1010", "1011"], "10101"), (["0", "11"], "11")]

    for case in cases:
        assert Solution().add_binary(*case[0]) == case[1]
        # Solution().add_binary(*case[0])