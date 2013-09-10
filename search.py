# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
import searchAgents
from util import *
from game import Directions

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()
class Node:
    def __init__ (self, state, parent, action, stepCost):
        self.state = state
        self.parent = parent
        self.action = action
        if parent == None:
            self.cost = stepCost
        else:
            self.cost = stepCost + parent.cost
    def getParent(self):
        return self.parent
    def getState(self):
        return self.state
    def getAction(self):
        return self.action
    def getCost(self):
        return self.cost
    def pathToRoot(self):
        listOfActions =[]
        currentNode = self
        while currentNode.getAction() is not None:
            listOfActions.append(currentNode.getAction())
            currentNode = currentNode.getParent()
        listOfActions.reverse()
        return listOfActions


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())

    fringe = Stack()
    closedSet = set()
    fringe.push(Node(problem.getStartState(), None, None, 0))

    while (not fringe.isEmpty()):
        node = fringe.pop()
        if problem.isGoalState(node.getState()):
            return node.pathToRoot()
        if node.getState() not in closedSet:
            closedSet.add(node.getState())
            for childNode in problem.getSuccessors(node.getState()):
                fringe.push(Node(childNode[0], node, childNode[1], childNode[2]))
    return []


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    fringe = Queue()
    closedSet = set()
    fringe.push(Node(problem.getStartState(), None, None, 0))

    while (not fringe.isEmpty()):
        node = fringe.pop()
        if problem.isGoalState(node.getState()):
            return node.pathToRoot()
        if node.getState() not in closedSet:
            closedSet.add(node.getState())
            for childNode in problem.getSuccessors(node.getState()):
                fringe.push(Node(childNode[0], node, childNode[1], childNode[2]))
    return []

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    fringe = PriorityQueue()
    closedSet = set()
    fringe.push(Node(problem.getStartState(), None, None, 0), 0)

    while (not fringe.isEmpty()):
        node = fringe.pop()
        if problem.isGoalState(node.getState()):
            return node.pathToRoot()
        if node.getState() not in closedSet:
            closedSet.add(node.getState())
            for childNode in problem.getSuccessors(node.getState()):
                newNode = Node(childNode[0], node, childNode[1], childNode[2])
                fringe.push(newNode, newNode.getCost())
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"

    fringe = PriorityQueue()
    closedSet = set()
    fringe.push(Node(problem.getStartState(), None, None, 0), 0)

    while (not fringe.isEmpty()):
        node = fringe.pop()
        if problem.isGoalState(node.getState()):
            return node.pathToRoot()
        if node.getState() not in closedSet:
            closedSet.add(node.getState())
            for childNode in problem.getSuccessors(node.getState()):
                newNode = Node(childNode[0], node, childNode[1], childNode[2])
                fringe.push(newNode, newNode.getCost() + heuristic(newNode.getState(), problem))
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
