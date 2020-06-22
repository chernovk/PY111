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
    if priority in range(PRIORITY_NUMBER):
        priority_queue[priority].append(elem)
    else:
        raise IndexError('No such priority in existing queue')
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
    if priority in range(PRIORITY_NUMBER):
        if ind in range(len(priority_queue[priority])+1):
            return priority_queue[priority][ind]
        else:
            raise IndexError('No element of such index in queue with such priority')
    else:
        raise IndexError('No such priority in existing queue')



def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global priority_queue
    priority_queue = {i: [] for i in range(PRIORITY_NUMBER)}
    return None
