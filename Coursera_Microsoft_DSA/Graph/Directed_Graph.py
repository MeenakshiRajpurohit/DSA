class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.graph and to_vertex in self.graph:
            self.graph[from_vertex].append(to_vertex)
        else:
            print("one or both vertices not found")

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

g = DirectedGraph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")

g.print_graph()
