from Graph import Graph

my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)
my_graph.add_vertex(5)
my_graph.print_graph()
print('*' * 20)

my_graph.add_edge(1, 2)
my_graph.add_edge(3, 2)
my_graph.add_edge(5, 2)
my_graph.add_edge(1, 4)
my_graph.add_edge(4, 2)
my_graph.add_edge(3, 1)
my_graph.print_graph()
print('*' * 20)

my_graph.remove_vertex(2)
my_graph.print_graph()
print('*' * 20)

my_graph.remove_edge(1, 4)
my_graph.print_graph()
print('*' * 20)