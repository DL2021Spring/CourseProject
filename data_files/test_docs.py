"Test harness for doctests."



__metaclass__ = type
__all__ = [
    'additional_tests',
    ]

import atexit
import doctest
import os


import unittest

DOCTEST_FLAGS = (
    doctest.ELLIPSIS |
    doctest.NORMALIZE_WHITESPACE |
    doctest.REPORT_NDIFF)
















