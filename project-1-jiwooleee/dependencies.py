import fileinput
from collections import defaultdict

class Graph:
    def __init__(self):
        # adjacency list using dictionary
        # reversed graph
        # key == vertex, values == incoming edges
        self.g = defaultdict(list)
        # list of all vertices
        # key == file name, value == marked or unmarked
        self.V = defaultdict()
        # to detect cycle
        # key == file name, value == marked or unmarked
        self.Cycle = defaultdict()
        self.Cyclestart = None

    # append new edge to adjacency list
    def appendE(self, v, u):
        self.g[v].append(u)

    # append new vertex to list of vertices
    def appendV(self, v):
        # default: unmarked
        self.V[v] = False
        # default: unmarked
        self.Cycle[v] = False

    # auxiliary fuction for topological_sort
    def PostProcessDAGDFS(self, S, Vertices, v):
        # mark the vertex
        self.V[v] = True
        # mark to detect cycles
        self.Cycle[v] = True
        # for every u dependent on v
        for u in self.g[v]:
            if self.V[u] == False:
                # u is unmarked
                if self.PostProcessDAGDFS(S, Vertices, u) == True:
                    # u is contained in a cycle
                    print(u)
                    return True
            elif self.Cycle[u] == True:
                # detected a cycle
                print("Cyclic dependency: ")
                print(u)
                return True

        # put it in order
        S.append(v)
        # unmark the vertex, it is not contained in a cycle
        self.Cycle[v] = False
        return False

    # topological sort
    def topological_sort(self):
        # stack to store the ordering
        S = []
        # Vertices = list of file names
        Vertices = (self.V).keys()

        for v in Vertices:
            if  self.V[v] == False:
                # if the vertex is unmarked
                # PostProcessDAGDFS
                if self.PostProcessDAGDFS(S, Vertices, v) == True:
                    return

        while len(S) > 0:
            print(S.pop())



# Read dependency data from standard input, and return a graph.
def read_graph():
    g = Graph()
    # Process each line in standard input.
    for line in fileinput.input():

        # Split the current line into tokens, and remove the trailing newline.
        tokens = line.rstrip().split(',')

        if len(tokens) == 1:
            # vertices
            g.appendV(tokens[0])
        else:
            i = 0
            while i < len(tokens) - 1:
                # save a reversed graph
                # (u, v) -> (v, u): u is dependent on v
                g.appendE(tokens[i+1], tokens[i])
                i += 2
    return g

# Compute & print either
# (1) a topological sort of the given graph, or
# (2) a cycle of dependencies.

def main():
    graph = read_graph()
    graph.topological_sort()

main()
