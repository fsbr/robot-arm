# this code will hopefully implement a graph in a grid format
import collections

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

class SimpleGraph:
    def __init__(self):
        #declares edges as a dict.
        self.edges = {}
    def neighbors(self,id):
        return self.edges[id]

class SquareGrid:
    #make a rectangular grid ya
    pass

def breadth_first_search_1(graph,start):
    # print out what we find
    frontier = Queue()

    # put is just a fancy name for append
    frontier.put(start)

    # these are like the grey nodes
    visited = {}
    visited[start] = True

    # this is why its a function so you can call it like this   
    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r" % current)
        for next in graph.neighbors(current):

            # so sick you can just do 'not in'
            if next not in visited:
                frontier.put(next)
                visited[next] = True 
#all_nodes = []
#for x in range(20):
#    for y in range(10):
#        all_nodes.append([x,y])

# basically prints the coordinates of the nodes
#print(all_nodes)

# make the neighbors
def neighbors(node):
    # takes a node as the input and appends neighbors to
    # a ``result" list. 
    
     
    # define the N S, E W direction
    # tron called this connectivity 4
    dirs = [[1,0], [0,1],[-1,0],[0,-1]]

    # result is a list which contains all the neighbor nodes
    result = []

    # look at a node and append the E, W, S etc direction
    # there's probably a way cleaner way to write this but
    # i dont want to think about it.
    for dir in dirs:
        if neighbor in all_nodes:
            result.append([node[0] +dir[0], node[1] + dir[1]])
    return result

if __name__ == "__main__":
    example_graph = SimpleGraph()
    example_graph.edges = {
        'A' : ['B'],
        'B' : ['A','C','D'],
        'C' : ['A'],
        'D' : ['E', 'A'],
        'E' : ['B']
    }

    breadth_first_search_1(example_graph,'A')

