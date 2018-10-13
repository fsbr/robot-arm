# try two.
# two major data structures
# first one is a node
# second one is a graph.  

# the graph is just a collection of nodes

# imports
import numpy as np

class Queue:
    # implements the First in first out queue struct.
    def __init__(self):
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
        self.color = "white" # grey is on deck, black is done
        self.d = np.inf
        self.pi = None

        # get the location of the node in the grid
        self.x = 0
        self.y = 0
        self.location = (self.x,self.y)

class SimpleGraph:
    def __init__(self):
        # declares the nodes and their connections as a dictionary
        self.edges = {}

    def neighbors(self,id):
        return self.edges[id]

    def createNodes(self):
        # build the nodes in the graph
        for f in connection:
            Node.name = f
            Node.neighbors = connection[f]
    

def BFS(graph, start):
    # inputs: 
    # graph: a collection of points
    # start: a starting node within 'graph'

    # performs the BFS search for path planning as close as possible to CLRS
    pass

if __name__ == "__main__":
    example_graph = SimpleGraph()
    example_graph.edges = {
        'A' : ['B'],
        'B' : ['A','C','D'],
        'C' : ['A'],
        'D' : ['E', 'A'],
        'E' : ['B']
    }  

   
