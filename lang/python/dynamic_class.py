# -*- coding:utf-8 -*-


class CanDoSomething(object):

    message = "You don't have permission"

    def has_permission(self, request, view):
        return True


class CanDoSomethingOrReadOnly(CanDoSomething):

    def has_permission(self, request, view):
        return False


class HasPermissionToDo(object):

    p_class = CanDoSomething
    name = "HasPermissionToDo%s"

    def __init__(self, permission_code, *args, **kwargs):
        pass

    def __new__(cls, permission_code, *args, **kwargs):
        code = permission_code.split('.')[1]
        name = ''.join(x.title() for x in code.split('_'))
        cls.p_class.message= "hello world"
        cls.p_class.__name__ = cls.name % name
        return cls.p_class


class HasPermissionToDoOrReadOnly(HasPermissionToDo):
    p_class = CanDoSomethingOrReadOnly
    name = "HasPermissionToDo%sOrReadOnly"
