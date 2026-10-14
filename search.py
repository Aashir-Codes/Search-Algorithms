"""
search.py
---------
THE MAZE RUNNER — Mini Project 1: Classical Search

This is where you implement the search algorithms (Questions 1–7).

Every algorithm receives a SearchProblem (see problems.py) and must retu    rn a
LIST OF ACTIONS that leads from the start state to a goal state, e.g.
['South', 'South', 'East']. Return [] if the start state is already a goal.

Conventions the grader relies on (please read — they matter!):

  * Use the fringe containers from util.py (Stack, Queue, PriorityQueue).
  * Calling problem.getSuccessors(state) counts as EXPANDING that state.
    Call it exactly once per expanded state, and never for a state you only
    generated.
  * Goal test when a state is POPPED from the fringe (just before you would
    expand it), not when it is pushed. (For BFS the grader also accepts
    the "early" goal test done when a state is generated.)
  * Push successors in the order getSuccessors returns them.
  * Q1, Q2, Q5, Q6, Q7 are GRAPH searches: keep a set of already-expanded
    states and never expand the same state twice.
"""

from inspect import stack

import util
from util import Stack, Queue, PriorityQueue, CUTOFF
from heuristics import nullHeuristic


# ----------------------------------------------------------------------
# Q0 (worked example, not graded): always go right
# ----------------------------------------------------------------------
def alwaysRightSearch(problem):
    """
    Not a real search: the runner keeps stepping right ('East') until he
    reaches the goal. If a wall blocks the way east, he is stuck and gives up
    (returns None). It shows you how to use the problem's methods. Try it:
        python runner.py -l maze_tiny -a right     (escapes)
        python runner.py -l maze_small -a right       (walks into a wall)
    """
    state = problem.getStartState()
    actions = []
    while not problem.isGoalState(state):
        successors = problem.getSuccessors(state)   # list of (next, action, cost)
        east = [s for s in successors if s[1] == 'East']
        if not east:
            return None   # a wall straight ahead: the doors close with him inside
        nextState, action, stepCost = east[0]
        actions.append(action)
        state = nextState
    return actions


# ----------------------------------------------------------------------
#                    Depth-First Search
# ----------------------------------------------------------------------
def depthFirstSearch(problem):
    st = Stack()
    start_state = problem.getStartState() # this will the intial location of the runner like 0,0 type stuff 
    st.push((start_state, [])) 
    explored = set()
    while not st.isEmpty():
        state, actions = st.pop()
        if problem.isGoalState(state):
            return actions
        if state in explored:
            continue
        if state not in explored:
            explored.add(state)
            for successor, action, _ in problem.getSuccessors(state):
                if successor not in explored:
                    st.push((successor, actions + [action]))
    return None 


# ----------------------------------------------------------------------
# Q2: Breadth-First Search
# ----------------------------------------------------------------------
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first (graph search)."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# ----------------------------------------------------------------------
# Q3: Depth-Limited Search
# ----------------------------------------------------------------------
def depthLimitedSearch(problem, limit):
    """
    Depth-first search that never goes deeper than 'limit' actions.

    Return value:
      * a list of at most 'limit' actions that reaches a goal, or
      * CUTOFF (from util) if no goal was found but the search was stopped
        by the depth limit somewhere, so a deeper solution may exist, or
      * None if no goal was found and the limit was never reached, which
        proves there is no solution at all.

    The start state is at depth 0. A state at depth == limit may be goal
    tested but must not be expanded.

    Do NOT use a global explored set here (think about why that can make the
    search miss a solution that fits within the limit). Instead, avoid cycles
    by not revisiting a state that is already on the current path.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# ----------------------------------------------------------------------
# Q4: Iterative Deepening Search
# ----------------------------------------------------------------------
def iterativeDeepeningSearch(problem, maxDepth=10000):
    """
    Run depthLimitedSearch with limit = 0, 1, 2, ... until it finds a
    solution. Return that solution, or None if the problem has no solution
    (or none within maxDepth).
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# ----------------------------------------------------------------------
# Q5: Uniform-Cost Search
# ----------------------------------------------------------------------
def uniformCostSearch(problem):
    """Search the node of least total path cost g(n) first (graph search)."""
    priority_queue = PriorityQueue()
    explored = set()
    
    start_state = problem.getStartState()
    start_cost = 0
    priority_queue.push(
        (start_state, [], start_cost), start_cost
    )
    
    while not priority_queue.isEmpty():
        current_state, actions, current_cost = priority_queue.pop()
        
        # goal test when state is popped
        if problem.isGoalState(current_state):
            return actions
        
        # not expanding the same state twice
        if current_state in explored:
            continue
        
        explored.add(current_state)
        
        # expanded current state
        for next_state, action, step_cost in problem.getSuccessors(current_state):
            if next_state not in explored:
                next_cost = current_cost + step_cost
                
                priority_queue.push(
                    (next_state, actions + [action], next_cost), next_cost
                )
                
    return None


# ----------------------------------------------------------------------
# Q6: Greedy Best-First Search
# ----------------------------------------------------------------------
def greedyBestFirstSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that SEEMS closest to the goal first, i.e. the one with
    the lowest heuristic(state, problem) value (graph search).
    """
    priority_queue = PriorityQueue()
    explored = set()
    start_state = problem.getStartState()
    
    priority_queue.push(
        (start_state, []), heuristic(start_state, problem)
        )
    
    while not priority_queue.isEmpty():
        current_state, actions = priority_queue.pop()
        
        # goal test when state is popped
        if problem.isGoalState(current_state):
            return actions
        
        # not expanding a state twice
        if current_state in explored:
            continue
        
        explored.add(current_state)
        
        #expand state
        for next_state, action, step_cost in problem.getSuccessors(current_state):
            if next_state not in explored:
                next_h = heuristic(next_state, problem)
                priority_queue.push(
                    (next_state, actions + [action]), next_h
                 )
                
    return None
    

# ----------------------------------------------------------------------
# Q7: A* Search
# ----------------------------------------------------------------------
def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node with the lowest f(n) = g(n) + heuristic(n) first
    (graph search).
    """
    priority_queue = PriorityQueue()
    explored = set()
    start_state = problem.getStartState()
    start_g = 0
    start_h = heuristic(start_state, problem)
    start_f = start_g + start_h
    
    priority_queue.push(
        (start_state, [], start_g), start_f
    )
    
    while not priority_queue.isEmpty():
        current_state, actions, current_g = priority_queue.pop()
        
        #goal test when state is popped
        if problem.isGoalState(current_state):
            return actions
        
        #not expanding the same state twice
        if current_state in explored:
            continue
        
        explored.add(current_state)
        
        #expanded current state
        for next_state, action, step_cost in problem.getSuccessors(current_state):
            if next_state not in explored:
                next_g = current_g + step_cost
                next_h = heuristic(next_state, problem)
                next_f = next_g  + next_h
                
                priority_queue.push(
                    (next_state, actions + [action], next_g), next_f
                )
    return None


# Abbreviations
always_right = alwaysRightSearch
dfs = depthFirstSearch
bfs = breadthFirstSearch
dls = depthLimitedSearch
ids = iterativeDeepeningSearch
ucs = uniformCostSearch
gbfs = greedyBestFirstSearch
astar = aStarSearch
