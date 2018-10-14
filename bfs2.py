# try two.
# two major data structures
# first one is a node
# second one is a graph.  

# the graph is just a collection of nodes

# imports
import numpy as np
import collections
class Queue:
    # implements the First in first out queue struct.
    def __init__(self):

        # this is basically a list but fast
        self.elements = collections.deque()

    def empty(self):
        # why do this in a function like this and not like 
        # a variable declaration?
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()

class Node:
    def __init__(self):
        # set to the CLRS defaults
        self.name = "untitled"
        self.color = "white" # grey is on deck, black is done
        self.d = np.inf
        self.pi = None
        self.Neighbors = {}

        # get the location of the node in the grid
        self.x = 0
        self.y = 0
        self.location = (self.x,self.y)

class SimpleGraph:
    def __init__(self,edgeList):
        # declares the nodes and their connections as a dictionary
        self.edges = {}

        for f in edgeList:
            Node.name = f
            print(Node.name)
            Node.neighbors = edgeList[f]

    def neighbors(self,id):
        return self.edges[id]
    

def BFS(graph, start):
    # inputs: 
    # graph: a collection of points
    # start: a starting node within 'graph'

    # performs the BFS search for path planning as close as possible to CLRS
    pass

if __name__ == "__main__":


    # basically instead of ints, im gonna have "nodes"


    # basic use case of a queue
    a = [1,2,3,4,5]    
    q = Queue()
    for s in a:
        print("putting s",s)
        q.put(s)
        print(q.elements) 

    for s in range(0,len(a)): 
        A = q.get()
        print("just popped",A)
        print("total queue",q.elements)
