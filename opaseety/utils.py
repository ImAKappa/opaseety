"""utils

Module for utility functions
"""

from itertools import groupby
from typing import Iterable

def all_equal(iterable: Iterable) -> bool:
    """https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-equal"""
    g = groupby(iterable)
    return next(g, True) and not next(g, False)