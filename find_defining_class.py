'''
takes object and method name (as a string) and returns
the class that provides the definition of this method
'''

def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty
