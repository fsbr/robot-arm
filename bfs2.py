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
    
    def pop(self):
        return self.elements.popleft()

class Node:
    def __init__(self):
        # set to the CLRS defaults
        self.name = "untitled"
        self.color = "white" # grey is on deck, black is done
        self.d = np.inf
        self.pi = None
        self.neighbors =[] 

        # get the location of the node in the grid
        self.x = 0
        self.y = 0
        self.location = (self.x,self.y)
    def printNeighbors(self):
        neighborsList = []
        for n in self.neighbors:
            neighborsList.append(n.name) 
        print("my neighbors are", neighborsList)

# i'm thinking we may delete this object
#class SimpleGraph:
#    def __init__(self,edgeList):
#        # declares the nodes and their connections as a dictionary
#        self.edges = {}
#
#        for f in edgeList:
#            Node.name = f
#            print(Node.name)
#            Node.neighbors = edgeList[f]

    def neighbors(self,id):
        return self.edges[id]
    

def bfs(graph, start, end):
    # inputs: 
    # graph: a collection of points
    # start: a starting node within 'graph'

    # performs the BFS search for path planning as close as possible to CLRS
    # lines 1-7 of CLRS are done in the NODE object by default

    start.color = "grey"
    start.d = 0
    # start.pi = None already

    q = Queue()
    q.put(start)
    while not q.empty():
        u = q.pop()
        for v in u.neighbors:
            if v.color == "white":
                v.color = "grey"
                v.d = u.d + 1
                v.pi = u
                q.put(v)
                print("visiting",v.name)
                print("dist",v.d)
                print("pi",v.pi.name)
            if v.name == end:
                # print allt he predecessor nodes until you get to the starting node
                # haaaaa
                currentNode = v
                backTrace = []
                while currentNode != start:
                    backTrace.append(currentNode.pi.name)
                    currentNode = currentNode.pi
                print("backTrace",backTrace)
            
        u.color = "black"
if __name__ == "__main__":

    # basic use case of a queue
    a = [1,2,3,4,5]    
    q = Queue()
    for s in a:
        print("putting s",s)
        q.put(s)
        print(q.elements) 

    for s in range(0,len(a)): 
        A = q.pop()
        print("just popped",A)
        print(q.empty())

    # lets make a graph i literally dont care how scrubby this is
    # we'll get there eventually
    A = Node()
    B = Node()
    C = Node()
    D = Node()
    E = Node()

    # name each one
    A.name = "A"
    B.name = "B"
    C.name = "C"
    D.name = "D"
    E.name = "E"

    #insert neighbors
    A.neighbors = [B]
    B.neighbors = [A,C,D]
    C.neighbors = [A]
    D.neighbors = [A,E]
    E.neighbors = [B] 

    graph = [A,B,C,D,E]
    # for node in graph:
        # node.printNeighbors()

    
    # the golden GOOSE
    bfs(graph,A,"E")
