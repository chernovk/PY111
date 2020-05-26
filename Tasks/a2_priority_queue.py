"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any

PRIORITY_NUMBER = 11
priority_queue = {i: [] for i in range(PRIORITY_NUMBER)}

def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global priority_queue
    priority_queue[priority].append(elem)
    return None

def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    global priority_queue
    for i in priority_queue:
        if priority_queue[i]:
            return priority_queue[i].pop(0)
    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global priority_queue
    return priority_queue[priority][ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global priority_queue
    priority_queue = {i: [] for i in range(PRIORITY_NUMBER)}
    return None
