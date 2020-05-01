from itertools import combinations
import networkx as nx
from itertools import combinations
from nxviz import CircosPlot


def triangle_finding_strategies():
    ans = """
One way would be to take one node, and look at its neighbors.
If its neighbors are also connected to one another,
then we have found a triangle.

Another way would be to start at a given node,
and walk out two nodes.
If the starting node is the neighbor of the node two hops away,
then the path we traced traces out the nodes in a triangle.
"""
    print(ans)


def in_triangle(G, node):
    """
    Return whether a given node is present in a triangle relationship.
    """
    for nbr1, nbr2 in combinations(G.neighbors(node), 2):
        if G.has_edge(nbr1, nbr2):
            return True
    return False


def get_triangle_neighbors(G, node) -> set:
    neighbors1 = set(G.neighbors(node))
    triangle_nodes = set()
    for nbr1, nbr2 in combinations(neighbors1, 2):
        if G.has_edge(nbr1, nbr2):
            triangle_nodes.add(nbr1)
            triangle_nodes.add(nbr2)
    return triangle_nodes


def plot_triangle_relations(G, node):
    triangle_nbrs = get_triangle_neighbors(G, node)
    triangle_nbrs.add(node)
    nx.draw(G.subgraph(triangle_nbrs), with_labels=True)


def triadic_closure_algorithm():
    ans = """
I would suggest the following strategy:

1. Pick a node
1. For every pair of neighbors:
    1. If neighbors are not connected,
    then this is a potential triangle to close.

This strategy gives you potential triadic closures
given a "center" node `n`.

The other way is to trace out a path two degrees out
and ask whether the terminal node is a neighbor
of the starting node.
If not, then we have another triadic closure to make.
"""
    print(ans)


def get_open_triangles_neighbors(G, node) -> set:
    open_triangle_nodes = set()
    neighbors = list(G.neighbors(node))

    for n1, n2 in combinations(neighbors, 2):
        if not G.has_edge(n1, n2):
            open_triangle_nodes.add(n1)
            open_triangle_nodes.add(n2)

    return open_triangle_nodes


def plot_open_triangle_relations(G, node):
    open_triangle_nbrs = get_open_triangles_neighbors(G, node)
    open_triangle_nbrs.add(node)
    nx.draw(G.subgraph(open_triangle_nbrs), with_labels=True)


def simplest_clique():
    print("The simplest clique is an edge.")


def size_k_maximal_cliques(G, k):
    for clique in nx.find_cliques(G):
        if len(clique) == k:
            yield clique


def find_k_cliques(G, k):
    for clique in nx.find_cliques(G):
        if len(clique) >= k:
            for nodeset in combinations(clique, k):
                yield nodeset


def visual_insights():
    ans = """
We might hypothesize that there are 3,
maybe 4 different "communities" of nodes
that are completely disjoint with one another,
i.e. there is no path between them.
"""
    print(ans)


def label_connected_component_subgraphs(G):
    G = G.copy()
    for i, nodeset in enumerate(nx.connected_components(G)):
        for n in nodeset:
            G.nodes[n]["subgraph"] = i
    return G


def plot_cc_subgraph(G):
    c = CircosPlot(G, node_color="subgraph", node_order="subgraph")
    c.draw()
