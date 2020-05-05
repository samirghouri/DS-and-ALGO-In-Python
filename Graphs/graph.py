# implementation of the adjacency list in python


class Vertex:
    # we use a dictionary to keep track of the vertices to which it is connected
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, nbr, weight=0):
        # for adding the neighbor of the vertex
        self.connected_to[nbr] = weight

    def __str__(self):
        # get the string of ids connected to
        return str(self.id) + "connectTO: "+str([x.id for x in self.connected_to])

    def getConnections(self):
        # get the connections
        return self.connected_to.keys()

    def getId(self):
        # get the id of the vertex
        return self.id

    def getWeight(self, nbr):
        # get the weight of the vertex and the connected neightbor
        return self.connected_to[nbr]


class Graph:
    def __init__(self):
        self.vertex_list = {}
        self.num_of_vertices = 0

    def add_vertex(self, key):
        self.num_of_vertices = self.num_of_vertices + 1
        new_vertex = Vertex(key)
        self.vertex_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        if key in self.vertex_list:
            return self.vertex_list[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertex_list

    def add_edge(self, from_key, to_key, weight=0):
        if from_key not in self.vertex_list:
            new_vertex = self.add_vertex(from_key)
        if to_key not in self.vertex_list:
            new_vertex = self.add_vertex(to_key)
        self.vertex_list[from_key].add_neighbor(
            self.vertex_list[to_key], weight)

    def getVertices(self):
        return self.vertex_list.keys()


g = Graph()
for i in range(6):
    g.add_vertex(i)
# print(g.vertex_list)

g.add_edge(0, 1)
g.add_edge(0, 5)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 0)
g.add_edge(5, 4)
g.add_edge(5, 2)
print(g.getVertices())
