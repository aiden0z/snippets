# -*- coding:utf-8 -*-

"""
convert dict
{u'detail.province': u'www11', u'mobile': u'4561', u'detail.city': u'qqq11', u'email': u'1231'}

to

{u'mobile': u'4561', u'detail': {u'province': u'www11', u'city': {u'number': u'qqq11'}}, u'email': u'1231'}

"""


def convert(doc):
    new_doc = {}
    for field in doc:
        dots = field.split('.')
        curr_doc = doc[field]
        if len(dots) == 1:
            new_doc[field] = curr_doc
        else:
            edit_doc = new_doc
            for part in dots[:-1]:
                edit_doc = edit_doc.setdefault(part, {})
            edit_doc[dots[-1]] = curr_doc

    return new_doc


if __name__ == '__main__':
    src = {u'detail.province': u'www11', u'mobile': u'4561', u'detail.city.number': u'qqq11', u'email': u'1231'}
    print(convert(src))
