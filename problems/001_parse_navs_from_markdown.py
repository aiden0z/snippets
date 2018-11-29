"""从 Markdown 文本中解析出目录信息

现在有格式如下的文档:

```markdown

* [目录 1](chapter1/1.md)
  * [目录 1.1](chapter1/1-1.md)
    * [目录 1.1.1](chapter1/1-1-1.md)
* [目录 2](chapter2/1.md)
```

要求写一个解析器，解析返回所有目录信息，并包含层级关系。返回的示例数据如下。

```python
[
    {
        'name': '目录 1',
        'path': 'chaper1/1.md',
        'chapters': [
            {
                'name': '目录 1.1',
                'path': 'chapter1/1-1.md',
                'chapters': [
                    {'name': '目录 1.1.1', 'path': 'chapter1/1-1-1.md'}
                ]
            }
        ]},
    {'name': '目录 2', 'path': 'chapter2/1.md'}
]
```
"""

import re
import pprint


class Solution:

    def parse_navs(self, content):
        stack = [({'name': 'dummy', 'path': 'dummy', 'children': []}, -1)]
        for line in content.splitlines():
            # 有效行判断
            meta = re.match(r'.*\[(.+)\]\((.+)\)', line)
            if meta is None:
                continue

            # 缩进匹配
            result = re.match(r'^\s+', line)
            if result is None:
                indent = 0
            else:
                indent = result.span()[1]
            name, path = meta.groups()

            item = {'name': name, 'path': path, 'children': []}
            pre_indent = stack[-1][1]

            if indent == pre_indent:
                stack.pop()
                parent = stack[-1][0]
            elif indent > pre_indent:
                parent = stack[-1][0]
            else:
                while indent != stack.pop()[1]:
                    pass
                parent = stack[-1][0]
            stack.append((item, indent))
            parent['children'].append(item)
        return stack[0][0]['children']
            

if __name__ == '__main__':
    summary = """
* [a](content/preface/preface-chinese.md)
    * [b](content/chapter1/1.1-chinese.md)
    * [c](content/chapter1/1.1-chinese.md)
        * [d](content/chapter2/2.1-chinese.md)
"""

    solutions = [Solution]
    for s in solutions:
        result = s().parse_navs(summary)
        pprint.pprint(result, indent=4)
        assert result[0]['children'][1]['children'][0]['name'] == 'd'

