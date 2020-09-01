""" Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters
' ', return the length of last word (last word means the last apperaring word if
we loop from left to right) in the string.

if the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters
only.

Example:

    Input: "Hello World"
    Output: 5

"""


class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])


if __name__ == '__main__':
    cases = [
        ("", 0),
        ("a ", 1),
        ("Hello World", 5),
        ("Today is a nice day", 3),
    ]  # yapf: disable

    for case in cases:
        for S in [Solution]:
            assert S().lengthOfLastWord(case[0]) == case[1]
