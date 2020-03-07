"""
prints  attribute name and its values
"""

def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))
