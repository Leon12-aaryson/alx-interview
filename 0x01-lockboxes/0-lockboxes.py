#!/usr/bin/python3
""" Lockboxes task """


def canUnlockAll(boxes):
    """ Initialize a set to keep track of visited boxes """
    visited = set()

    """ Define a DFS function to explore boxes """
    def dfs(box):
        """ Mark the current box as visited """
        visited.add(box)

        """ Explore keys in the current box """
        for key in boxes[box]:
            """ If the key opens an unvisited box, recursively explores it """
            if key not in visited:
                dfs(key)

    dfs(0)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)
