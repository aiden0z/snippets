"""Group Anagrams
Given an array of strings, group anagrams together.

Example:

    Input:

        ["eat", "tea", "tan", "ate", "nat", "bat"]

    Output:

        [
            ["ate","eat","tea"],
            ["nat","tan"],
            ["bat"]
        ]

Note:
    All inputs will be in lowercase.
    The order of your output does not matter.

"""

from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}

        for item in strs:
            key = ''.join(sorted(item))
            if key in store:
                store[key].append(item)
            else:
                store[key] = [item]

        return store.values()


if __name__ == '__main__':
    cases = [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [
                ["ate", "eat", "tea"],
                ["nat", "tan"],
                ["bat"]
            ]
        ),
    ]  # yapf: disable

    for case in cases:
        for S in [Solution]:
            result = S().groupAnagrams(case[0])
            for l in case[1]:
                for item in l:
                    found = False
                    for ll in result:
                        if item in ll:
                            found = True
                    assert found
