""" Permutation Sequence

The set [1, 2, 3, ...., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the
following sequence for n = 3:

    1. "123"
    2. "132"
    3. "213"
    4. "231"
    5. "312"
    6. "321"

Given n and k, return the k(th) permutation sequence.

Note:

    * Given n will be between 1 and 9 inclusive.
    * Given k will be between 1 and n! inclusive.

Example 1:

    Input: n = 3, k = 3
    Output: "213"

Example 2:

    Input: n = 4, k = 9
    Output: "2314"
"""


class Solution:

    def getPermutation(self, n: int, k: int) -> str:
        ans = ''
        fact = [1] * n
        num = [str(i) for i in range(1, 10)]
        for i in range(1, n):
            fact[i] = fact[i - 1] * i
        k -= 1
        for i in range(n, 0, -1):
            first = k // fact[i - 1]
            k %= fact[i - 1]
            ans += num[first]
            num.pop(first)
        return ans


class SolutionB:
    """ Soltion will exceed time limit"""

    def getPermutation(self, n: int, k: int) -> str:
        i = 1
        for result in self.permutations(range(1, n + 1)):
            if i == k:
                break
            i += 1
        return ''.join(map(str, result))

    def permutations(self, iterable):
        # reference https://docs.python.org/3/library/itertools.html#itertools.permutations
        pool = tuple(iterable)
        n = len(pool)
        for indices in self.product(range(n)):
            if len(set(indices)) == n:
                yield tuple(pool[i] for i in indices)

    def product(self, iterable):
        # reference https://docs.python.org/3/library/itertools.html#itertools.product
        pools = [tuple(iterable)] * len(iterable)
        result = [[]]
        for pool in pools:
            result = [x + [y] for x in result for y in pool]
        for prod in result:
            yield tuple(prod)


if __name__ == '__main__':
    cases = [
        ((3, 3), "213"),
        ((4, 9), "2314"),
    ]  # yapf: disable

    for case in cases:
        for S in [Solution]:
            assert S().getPermutation(*case[0]) == case[1]
            # print(S().getPermutation(*case[0]))
