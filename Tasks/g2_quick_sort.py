from typing import List
import random


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    fi = 0
    la = len(container) - 1

    def borders_(first, last):
        if first >= last:
            return None
        lb = first
        rb = last
        m = random.choice(container[lb: rb])
        while lb <= rb:
            while container[lb] < m:
                lb += 1
            while container[rb] > m:
                rb -= 1
            if lb <= rb:
                container[lb], container[rb] = container[rb], container[lb]
                lb += 1
                rb -= 1
        borders_(first, rb)
        borders_(lb, last)

    borders_(fi, la)
    return container
