from inspect import stack

import util
from util import Stack, Queue, PriorityQueue, CUTOFF
from heuristics import nullHeuristic


# ----------------------------------------------------------------------
#                        Graph Search Problems
# ----------------------------------------------------------------------
def alwaysRightSearch(problem):
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
        if problem.isGoalState(state): # check wether the current state is the goal state or not yk we reach goal then return the actions we took to reach the goal state 
            return actions
        if state in explored: # Distinction between Graphs and Trees. Reason : Because of cyscle.
            continue
        if state not in explored:
            explored.add(state)
            for successor, action, _ in problem.getSuccessors(state):
                 # get the successors of the current state and push them to the stack if they are not already explored abdullah and also here unpacking is happening like successor is the next state, action is the action to reach that state and _ is the cost of reaching that state which we are not using here we will use it in uniform cost search and a* search
                if successor not in explored:
                    st.push((successor, actions + [action]))
    return None 


# ----------------------------------------------------------------------
#                         Breadth-First Search
# ----------------------------------------------------------------------
def breadthFirstSearch(problem):
    q = Queue()
    start = problem.getStartState()
    q.push((start, [])) #push the intial state and empty action list to the queue
    explored = set()
    while not q.isEmpty():
        state, actions = q.pop()
        if problem.isGoalState(state):
            return actions
        if state in explored:
            continue
        if state not in explored:
            explored.add(state)
            for  nextState , action, _ in problem.getSuccessors(state):
                if nextState not in explored:
                    q.push((nextState, actions + [action]))

        


# ----------------------------------------------------------------------
# Q3: Depth-Limited Search
# ----------------------------------------------------------------------
def depthLimitedSearch(problem, limit):
    cutoffOccurred = False

    def recurse(state, pathStates, depth):
        nonlocal cutoffOccurred  # Basically abdullah this is used to access the variable cutoffOccurred which is defined in the outer function depthLimitedSearch and we are using it in the inner function recurse so we need to use nonlocal keyword to access it otherwise it will give an error that cutoffOccurred is not defined in the inner function recurse or like it will look for current scope and it will not find it so it will give an error so we need to use nonlocal keyword to access the variable which is defined in the outer function depthLimitedSearch and we are using it in the inner function recurse

        if problem.isGoalState(state):
            return []

        if depth == limit:
            cutoffOccurred = True
            return None

        for successor, action, _ in problem.getSuccessors(state):
            if successor in pathStates:   # would loop back on this route
                continue
            result = recurse(successor, pathStates | {successor}, depth + 1)
            if result is not None:
                return [action] + result   # a goal was found below us

        return None

    start = problem.getStartState()
    result = recurse(start, {start}, 0)
    if result is not None:
        return result
    return CUTOFF if cutoffOccurred else None


# ----------------------------------------------------------------------
# Q4: Iterative Deepening Search
# ----------------------------------------------------------------------
def iterativeDeepeningSearch(problem, maxDepth=10000):
    for depth in range(maxDepth):
        result = depthLimitedSearch(problem, depth)
        if result != CUTOFF:
            return result
    return None


# ----------------------------------------------------------------------
# Q5: Uniform-Cost Search
# ----------------------------------------------------------------------
def uniformCostSearch(problem):
    """Search the node of least total path cost g(n) first (graph search)."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# ----------------------------------------------------------------------
# Q6: Greedy Best-First Search
# ----------------------------------------------------------------------
def greedyBestFirstSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that SEEMS closest to the goal first, i.e. the one with
    the lowest heuristic(state, problem) value (graph search).
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# ----------------------------------------------------------------------
# Q7: A* Search
# ----------------------------------------------------------------------
def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node with the lowest f(n) = g(n) + heuristic(n) first
    (graph search).
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()



# Abbreviations
always_right = alwaysRightSearch
dfs = depthFirstSearch
bfs = breadthFirstSearch
dls = depthLimitedSearch
ids = iterativeDeepeningSearch
ucs = uniformCostSearch
gbfs = greedyBestFirstSearch
astar = aStarSearch
