#!/usr/bin/python3
"""
A method that determines if all the boxes can be opened.
"""
from collections import deque


def canUnlockAll(boxes):
    """Lockboxes logic"""
    numOfBoxes = len(boxes)
    unlockedBoxes = {0}
    toExplore = deque([0])
    
    while toExplore:
        current_box = toExplore.popleft()
        keys = boxes[current_box]
        
        for key in keys:
            if key not in unlockedBoxes and key < numOfBoxes:
                unlockedBoxes.add(key)
                toExplore.append(key)

    return len(unlockedBoxes) == numOfBoxes
