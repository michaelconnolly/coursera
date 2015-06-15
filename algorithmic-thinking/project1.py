"""
Project #1 in Algorthimic Thinking.
Michael Connolly
"""


def init_graph(num_nodes):
    """
    internal function used to create a graph with the inputed amount of nodes.
    """

    # Init graph structure.
    graph = dict()

    # Handle the error case case num_nodes is bogus.
    if (num_nodes > 0):
    
        # Add nodes to graph.
        for idx in range(num_nodes):
            graph[idx] = set([])

    return graph



def init_edges_complete_directed(graph):
    """
    internal function used to create all the edges necessary for a complete directed graph.
    """
    
    num_nodes = len(graph)

    for idx in range(num_nodes):
        for idy in (range(idx)):
            graph[idx].add(idy)
            graph[idy].add(idx)
        
    return graph



def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete
    directed graph with the specified number of nodes. A complete graph contains all possible
    edges subject to the restriction that self-loops are not allowed. The nodes of the graph
    should be numbered 0 to num_nodes - 1 when num_nodes is positive. Otherwise, the function
    returns a dictionary corresponding to the empty graph.
    """

    graph = init_graph(num_nodes)
    graph = init_edges_complete_directed(graph)

    return graph



def compute_in_degrees(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the in-degrees
    for the nodes in the graph. The function should return a dictionary with the same set of
    keys (nodes) as digraph whose corresponding values are the number of edges whose head
    matches a particular node.
    """

    #num_nodes = len(digraph)

    # initialize the dictionary we want to return with the right keys.
    dictionary_to_return = dict()
    for key in digraph.keys():
        dictionary_to_return[key] = 0

    # for every node we already have ...
    for key_to_look_for in digraph.keys():

        # for every node we already have ...
        for key_to_check in digraph.keys():

            # see if key_to_look_for is listed as an out_edge.
            if (key_to_look_for in digraph[key_to_check]):
                dictionary_to_return[key_to_look_for] += 1
                
    return dictionary_to_return



def in_degree_distribution(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the unnormalized
    distribution of the in-degrees of the graph. The function should return a dictionary whose
    keys correspond to in-degrees of nodes in the graph. The value associated with each particular
    in-degree is the number of nodes with that in-degree. In-degrees with no corresponding nodes
    in the graph are not included in the dictionary.
    """

    in_count_digraph = compute_in_degrees(digraph)
    #num_nodes = len(in_count_digraph)
    dictionary_to_return = dict()

    for key in in_count_digraph.keys():

        in_count = in_count_digraph[key]

        if (in_count not in dictionary_to_return.keys()):
            dictionary_to_return[in_count] = 1
        else:
            dictionary_to_return[in_count] += 1
    
    return dictionary_to_return



def print_graph(graph):
    """
    Test method to help during development.
    """
    
    print "graph:", graph
    return



# initialize our constants.
EX_GRAPH0 = dict()
EX_GRAPH1 = dict()
EX_GRAPH2 = dict()

# create the graphs and nodes.
EX_GRAPH0 = init_graph(3)
EX_GRAPH1 = init_graph(7)
EX_GRAPH2 = init_graph(10)

# Add edges to EX_GRAPH0.
EX_GRAPH0[0].add(1)
EX_GRAPH0[0].add(2)

# Add edges to EX_GRAPH1.
EX_GRAPH1[0].add(1)
EX_GRAPH1[1].add(2)
EX_GRAPH1[2].add(3)
EX_GRAPH1[3].add(0)
EX_GRAPH1[0].add(4)
EX_GRAPH1[4].add(1)
EX_GRAPH1[0].add(5)
EX_GRAPH1[5].add(2)
EX_GRAPH1[1].add(6)
    
# Add edges to EX_GRAPH2.
EX_GRAPH2[0].add(1)
EX_GRAPH2[1].add(2)
EX_GRAPH2[2].add(3)
EX_GRAPH2[8].add(1)
EX_GRAPH2[8].add(2)
EX_GRAPH2[0].add(4)
EX_GRAPH2[4].add(1)
EX_GRAPH2[0].add(5)
EX_GRAPH2[5].add(2)
EX_GRAPH2[1].add(6)
EX_GRAPH2[2].add(7)
EX_GRAPH2[7].add(3)
EX_GRAPH2[3].add(7)
EX_GRAPH2[9].add(4)
EX_GRAPH2[9].add(5)
EX_GRAPH2[9].add(6)
EX_GRAPH2[9].add(7)
EX_GRAPH2[9].add(0)
EX_GRAPH2[9].add(3)



# Actual program.
#init(EX_GRAPH0, EX_GRAPH1, EX_GRAPH2)
#init()
##print "EX_GRAPH0:", print_graph(EX_GRAPH0)
##print "EX_GRAPH1:", print_graph(EX_GRAPH1)
##print "EX_GRAPH2:", print_graph(EX_GRAPH2)
##
##graph1 = make_complete_graph(5)
##print "test #1:", print_graph(graph1)
##
##in_graph0 = compute_in_degrees(EX_GRAPH0)
##in_graph1 = compute_in_degrees(EX_GRAPH1)
##in_graph2 = compute_in_degrees(EX_GRAPH2)
##print_graph(in_graph0)
##print_graph(in_graph1)
##print_graph(in_graph2)
##
##dist_graph0 = in_degree_distribution(EX_GRAPH0)
##dist_graph1 = in_degree_distribution(EX_GRAPH1)
##dist_graph2 = in_degree_distribution(EX_GRAPH2)
##print_graph(dist_graph0)
##print_graph(dist_graph1)
##print_graph(dist_graph2)

