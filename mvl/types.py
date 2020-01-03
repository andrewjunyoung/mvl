# Imports from third party packages.
from typing import Union, SupportsFloat

Floatable = Union[SupportsFloat, str, bytes, bytearray]
""" A type defining all objects o for which float(o) is defined.
"""
