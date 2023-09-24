"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if not isinstance(item, str):
            item = str(item)
        frequencies[item] += 1
    return frequencies