"""
Taylor series
"""
from typing import Union
import math

def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    accuracy = 0.000000001
    ex_ = 0
    i = 0
    while True:
        elem_ = x ** i / math.factorial(i)
        ex_ += elem_
        i += 1
        if elem_ < accuracy:
            break
    return ex_


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    accuracy = 0.0001
    sinx_ = 0
    i = 0
    while True:
        elem_ = ((-1) ** i * x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        sinx_ += elem_
        i += 1
        if abs(elem_) < accuracy:
            break
    return sinx_


