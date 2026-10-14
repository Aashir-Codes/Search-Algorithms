"""
heuristics.py
-------------
Heuristics for the basic maze problem (Question 6).

A heuristic is a function heuristic(state, problem) that returns an estimate
of the cost of the cheapest path from 'state' to a goal. For a MazeProblem,
'state' is a (row, col) tuple and the goal position is 'problem.goal'.
"""

import math

import util


def nullHeuristic(state, problem=None):
    """The trivial heuristic: it knows nothing, so it always says 0."""
    return 0


def manhattanHeuristic(state, problem):
    """
    Q6: the Manhattan distance from 'state' to problem.goal:
        |row1 - row2| + |col1 - col2|
    """
    goal = problem.goal
    
    row_difference = abs(state[0] - goal[0])
    col_difference = abs(state[1] - goal[1])
    
    return row_difference + col_difference


def euclideanHeuristic(state, problem):
    """
    Q6: the straight-line (Euclidean) distance from 'state' to problem.goal.
    """
    goal = problem.goal
    
    row_difference = state[0] - goal[0]
    col_difference = state[1] - goal[1]
    
    return math.sqrt( row_difference ** 2 + col_difference ** 2)
