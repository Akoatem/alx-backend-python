#!/usr/bin/env python3

import math

"""Write a type-annotated function floor which takes
a float n as argument and returns the floor of the float.
"""
#method 1
def floor(n: float) -> float:
    return math.floor(n)

# method 2 returning float into an int

"""
def floor(n: float) ->int:
    return int(n)
"""
