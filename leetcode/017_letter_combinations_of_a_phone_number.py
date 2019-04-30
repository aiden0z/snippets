"""Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that
the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

2 -> ['a', 'b', 'c']
3 -> ['d', 'e', 'f']
4 -> ['g', 'h', 'i']
5 -> ['j', 'k', 'l']
6 -> ['m', 'n', 'o']
7 -> ['p', 'q', 'r', 's']
8 -> ['t', 'u', 'v']
9 -> ['w', 'x', 'y', 'z']

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

Seen this question in a real interview before?  

Refer https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""


class Solution:

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        result = []
        if len(digits) == 0:
            return result

        pools = []
        for digit in digits:
            if digit in letters:
                pools.append(letters[digit])

        import itertools
        for item in itertools.product(*pools):
            result.append(''.join(item))

        return result


class SolutionB:

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        additional = mapping[digits[-1]]
        return [s + c for s in prev for c in additional]


if __name__ == '__main__':
    cases = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ]

    s = Solution()
    for case in cases:
        result = s.letterCombinations(case[0])
        for item in result:
            if item not in case[1]:
                print(item, result, case[1])
                assert False
