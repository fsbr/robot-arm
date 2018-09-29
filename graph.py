""" A python class
A simple python graph class demonstrating the essential 
facts and functions of graphs
"""

class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            if no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ if the vertex 'vertex' is not in self.__graph_dict, a key 'vertex' with
        and empty list value is added to the dictionary
        basically prevents duplicates
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """
        assumes that edge of type set, tuple or list
        between two vertices can be multiple edges! 
        (didn't know that
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """
        A static method generating the edges of hte graph
        'graph'.  Edges are respresented as sets with one
        (a loop back to the vertex), or two vertices
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbor in self.__graph_dict[vertex]:
                if {neighbor, vertex} not in edges:
                    edges.append({vertex, neighbor})
        return edges

    def __str__(self):
        res = "vertices: " 
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

if __name__ == "__main__":
    g = {   "a" : ["d"], 
            "b" : ["c"],
            "c" : ["b", "c", "d", "e"],
            "d" : ["a", "c"],
            "e" : ["c"],
            "f" : []
        }

    graph = Graph(g)
    
    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

        
