from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) == 1:
        return [container[0], ]
    else:
        m = sort(container[0: len(container)//2])
        n = sort(container[len(container)//2:])
    container = []
    a = 0
    b = 0
    while True:
        if m[a] <= n[b]:
            container.append(m[a])
            a += 1
        else:
            container.append(n[b])
            b += 1
        if a > len(m) - 1:
            container.extend(n[b:])
            break
        elif b > len(n) - 1:
            container.extend(m[a:])
            break
    return container
