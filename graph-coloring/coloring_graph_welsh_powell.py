import networkx as nx
import matplotlib.pyplot as plt


# implementation of welsh_powell algorithm for coloring the graph
def coloring_algo_welsh_powell(graph):
    # sorting the nodes in descending degree
    nodes_list = sorted(graph.nodes(), key=lambda x: len(graph[x]), reverse=True)
    # dictionary to store the colors assigned to each node and  assign the first color to the first node
    color_values = {nodes_list[0]: 0}
    # Assign colors to remaining N-1 nodes
    for node in nodes_list[1:]:
        available = [True] * len(graph.nodes())

        # iterates through all the adjacent nodes and marks it's color as unavailable,if it's color has been set already
        for adj_node in graph.neighbors(node):
            if adj_node in color_values.keys():
                color = color_values[adj_node]
                available[color] = False
        clr = 0
        for clr in range(len(available)):
            if available[clr]:
                color_values[node] = clr
                break

    print("color values: ", color_values)
    return color_values


# takes input from the file and creates a undirected graph of the given data in form of nodes
def create_graph():
    g = nx.Graph()
    # read the data from the given file
    file = open('sample-input.txt')
    # file = open('facebook_combined.txt')
    for line in file:
        graph_edge_list = line.split()
        g.add_edge(graph_edge_list[0], graph_edge_list[1])
    file.close()

    return g


# draws the graph and display the colored graph
def draw_graph(g, col_val):
    pos = nx.spring_layout(g)
    values = [col_val.get(node, 'blue') for node in g.nodes()]
    nx.draw(g, pos, with_labels=True, node_color=values, edge_color='black', width=1,
            alpha=0.9)  # with_labels=true is to show the node number in the output graph


# main function
if __name__ == "__main__":
    # called the defined functions here
    created_graph = create_graph()
    color_values = coloring_algo_welsh_powell(created_graph)
    # nx.draw(G)
    draw_graph(created_graph, color_values)
    plt.show()