""" Text Justification

Given an array of words and a width maxWidth, format the text such that each line has exactly
maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in
each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces
on a line do not divide evenly between words, the empty slots on the left will be assigned more
spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


Example 1:

    Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
    Output:
    [
       "This    is    an",
       "example  of text",
       "justification.  "
    ]

Example 2:

    Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
    Output:
    [
      "What   must   be",
      "acknowledgment  ",
      "shall be        "
    ]
    Explanation: Note that the last line is "shall be    " instead of "shall     be",
    because the last line must be left-justified instead of fully-justified.
    Note that the second line is also left-justified becase it contains only one word.

Example 3:

    Input: words = ["Science","is","what","we","understand","well","enough","to",
                    "explain","to","a","computer.","Art","is","everything","else","we","do"],
           maxWidth = 20
    Output:
    [
      "Science  is  what we",
      "understand      well",
      "enough to explain to",
      "a  computer.  Art is",
      "everything  else  we",
      "do                  "
    ]


Constraints:

* 1 <= words.length <= 300
* 1 <= words[i].length <= 20
* words[i] consists of only English letters and symbols.
* 1 <= maxWidth <= 100
* words[i].length <= maxWidth
"""


class Solution(object):

    def full_justify(self, words, max_width):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        line = []
        length = 0
        res = []
        for i, v in enumerate(words):
            if len(line) - 1 + length + len(v) >= max_width:
                self.format(line, length, max_width, res)
                line = []
                length = 0
            length += len(v)
            line.append(v)
        if len(line) > 0:
            self.format(line, length, max_width, res)

        last = res.pop(-1)
        last_char = None
        formats = ''
        for i in last:
            if last_char == ' ' and i == ' ':
                continue
            formats += i
            last_char = i
        formats += ' ' * (max_width - len(formats))
        res.append(formats)
        return res

    def format(self, line, length, max_width, res):
        diff = max_width - length
        remainder = 0
        if (len(line) - 1) > 1:
            interval = diff // (len(line) - 1)
            remainder = diff % (len(line) - 1)
        else:
            interval = diff
        w = ''
        for inx, val in enumerate(line):
            w += val
            if inx != len(line) - 1 or len(line) == 1:
                if remainder > 0:
                    w += ' ' * (interval + 1)
                    remainder -= 1
                else:
                    w += ' ' * (interval)
        res.append(w)


if __name__ == '__main__':
    cases = [(["This", "is", "an", "example", "of", "text",
               "justification."], 16, ["This    is    an", "example  of text", "justification.  "]),
             (["What", "must", "be", "acknowledgment", "shall",
               "be"], 16, ["What   must   be", "acknowledgment  ", "shall be        "]),
             ([
                 "Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
                 "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"
             ], 20, [
                 "Science  is  what we", "understand      well", "enough to explain to",
                 "a  computer.  Art is", "everything  else  we", "do                  "
             ])]

    for case in cases:
        assert Solution().full_justify(case[0], case[1]) == case[2]
