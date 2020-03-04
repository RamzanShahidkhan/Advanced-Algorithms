import networkx as nx
import matplotlib.pyplot as plt


# implementation of welsh_powell algorithm
def coloring_algorithm(G):
    # sorting  nodes in order of decreasing degree
    node_list = sorted(G.nodes(), key=lambda x: list(G.neighbors(x)), reverse=True)
    col_val = {}  # dictionary to store the colors assigned to each node
    col_val[node_list[0]] = 0  # assign the first color to the first node

    # Assign colors to remaining N-1 nodes
    for node in node_list[1:]:
        available_colors = [True] * len(
            node_list)  # boolean list[i] contains false if the node color 'i' is not available

        # iterates through all the adjacent nodes and marks it's color as unavailable, if it's color has been set already
        for neighbour in G[node]:
            if neighbour in col_val:
                col = col_val[neighbour]
                available_colors[col] = False
        for color, available in enumerate(available_colors):
            if available == True:
                break
        col_val[node] = color
    print(col_val)
    return col_val


# takes input from the file and creates a undirected graph
def ceate_graph_from_data(f):
    G = nx.Graph()
    line = f.readline().split()
    while (line != ""):
        graph_edge_list = line
        G.add_edge(graph_edge_list[0], graph_edge_list[1])
        line = f.readline().split()
        # print(line)
        # check if line is not empty
        if not line:
            break

    return G


# draws the graph and displays the weights on the edges
def drawing_graph(G, col_val):
    pos = nx.spring_layout(G)
    values = [col_val.get(node, 'yellow') for node in G.nodes()]

    nx.draw_networkx(G, pos, with_labels=True, node_color=values, edge_color='r', width=1,
            alpha=0.7)  # with_labels=true is to show the node number in the output graph


# main function
if __name__ == "__main__":
    f = open('sample-input.txt')
    #f = open('facebook_combined.txt')
    G = ceate_graph_from_data(f)
    col_val = coloring_algorithm(G)
    drawing_graph(G, col_val)
    plt.show()