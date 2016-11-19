import sys
import os
from math import isinf
from collections import defaultdict

class Graph(object):
    def __init__(self, edges):
        # expect list of edges
        if not isinstance(edges, list):
            print("Graph edges must be specified in a list. "
                "Aborting.")
            sys.exit(-1)
        # create a dictionary, and for each node record all adjacent nodes
        self.edges = defaultdict(list)
        for i, row in enumerate(edges):
            if len(row) == 2:
                self.edges[row[0]].append(row[1])
                self.edges[row[1]].append(row[0])
        self.nodes = set(self.edges.keys())
    
    def shortest_paths(self, root):
        # create a dictionary and record shortest path from root to each node
        # distance to non-connected nodes = infinity
        distances = dict.fromkeys(self.nodes, float('inf'))
        distances[root] = 0      
        edges = self.edges
        # mantain a queue of nodes
        q = []
        q.append(root)       
        while q:
            # get and remove the first node in the queue
            current = q.pop(0)
            # iterate over all neighbour nodes, 
            # record distance to neighbour if not already visited 
            neighbours = edges[current]       
            for node in neighbours:
                if isinf(distances[node]):
                    # distance is one more than distance to current node
                    distances[node] = distances[current] + 1
                    q.append(node) 
        return distances       
    
    def farness(self, root):           
        distances =  self.shortest_paths(root)  
        return sum(distances.values())        
    
    def closeness(self, root): 
        farness = self.farness(root)
        if farness == 0:
             print("Farness equals 0 for node %s. Cannot compute closeness. "
                "Aborting." % (root))
             sys.exit(-1)   
        return 1 / float(farness)
                
def load_edges(edges_file):
    # check file exists
    if not os.path.exists(edges_file):
        print("Cannot find edges file '%s'. "
            "Aborting." % (edges_file))
        sys.exit(-1)     
    edges = []
    with open(edges_file) as f:
        for line in f:
            # expect two vertex names separated by a single space
            parts = line.rstrip('\n').split(' ')  
            if len(parts) == 2: 
                edges.append(parts)             
    return edges      
        
def rank_closeness(graph):
    if not isinstance(graph, Graph):
        print("%s is not a Graph. Cannot rank vertex closeness. "
            "Aborting." % (graph))
        sys.exit(-1)    
    # compute and rank closeness for each node in graph
    closeness = [[node, graph.closeness(node)] for node in graph.nodes]
    closeness = sorted(closeness, key=lambda tup: tup[1], reverse=True)
    return closeness
                                   
if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 1:
        edges_file = args[0]
    else:
        edges_file = "edges.dat"   
    edges = load_edges(edges_file)
    graph = Graph(edges)
    closeness = rank_closeness(graph)
    print("vertex, closeness")
    print("\n".join(", ".join(map(str,row)) for row in closeness))


    




