# i am dumb

import collections

class Queue:
    #implemenets the FIFO quqe
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0 
    
    def put(self,x):
        pass        

class SimpleGraph:
    def __init__(self):
        # declares edges as a dictionary
        self.connection = {}
    def neighbors(self,id):
        return self.edges[id]

class Node:
    def __init__(self):

        # color can be a string idc if it's slow
        # "white", "grey", "black"
        self.color = "white" 

        # im gonna use -1 to represent infint
        self.d = -1

        # this is the backtrace indicator
        self.pi = None

    def makeNodes(self):
        # this function reads in a dictionary of the form key: connections and makes the nodes with that connection 
        

if __name__ == "__main__":

    # this is the real part that i dont understand.  how do i 
    # what i really want is a node object with certain attributes,
    # and the node gets added tot he graph object 

    #declare the nodes
    A = Node() 
    print(A.color)

    # i want a function tha reads in the graph.connection dict, and then places those as a node




    # basically all i gotta do is instead of a string the node object goes in there.
    example_graph = SimpleGraph()
    example_graph.connection= {
        'A' : ['B'],
        'B' : ['A', 'B', 'D'],
        'C' : ['A'],
        'D' : ['E','A'],
        'E' : ['B']
    }

 
