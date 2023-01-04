from math import floor
from typing import List

from numpy.random import normal

def harvest_tree(num_apples:int) -> List[int]:
    """Function to generate masses of apples from a hypothetical tree

    :param num_apples: _description_
    :type num_apples: int
    :return: _description_
    :rtype: List[int]
    """
    return [floor(i) for i in normal(loc=200, scale=50/3, size=num_apples)]