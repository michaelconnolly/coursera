"""
Application #1 in Algorthimic Thinking.
Michael Connolly
"""

# general imports
import urllib2
import matplotlib.pyplot as plt
import numpy as np
import math
import random


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


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
            #if digraph[key_to_check].has_key(key_to_look_for):
                dictionary_to_return[key_to_look_for] += 1
                
    return dictionary_to_return


def compute_out_degrees(digraph):
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
        dictionary_to_return[key] = len(digraph[key])
                
    return dictionary_to_return


def compute_average_out_degree(digraph):

    # initialize the dictionary we want to return with the right keys.
    dictionary_to_return = dict()
    num_nodes = len(digraph)
    num_out_degrees = 0
    
    for key in digraph.keys():
        #dictionary_to_return[key] = len(digraph[key])
        num_out_degrees += len(digraph[key])
                
    return (num_out_degrees / num_nodes)
    


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

        #if (in_count not in dictionary_to_return.keys()):
        if (not (dictionary_to_return.has_key(in_count))):
            dictionary_to_return[in_count] = 1
        else:
            dictionary_to_return[in_count] += 1
    
    return dictionary_to_return


def out_degree_distribution(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the unnormalized
    distribution of the in-degrees of the graph. The function should return a dictionary whose
    keys correspond to in-degrees of nodes in the graph. The value associated with each particular
    in-degree is the number of nodes with that in-degree. In-degrees with no corresponding nodes
    in the graph are not included in the dictionary.
    """

    count_digraph = compute_out_degrees(digraph)
    #num_nodes = len(in_count_digraph)
    dictionary_to_return = dict()

    for key in count_digraph.keys():

        count = count_digraph[key]

        #if (in_count not in dictionary_to_return.keys()):
        if (not (dictionary_to_return.has_key(count))):
            dictionary_to_return[count] = 1
        else:
            dictionary_to_return[count] += 1
    
    return dictionary_to_return


def normalize_distribution(graph):
    """
    yeah!
    """
    total = 0

    for key in graph.keys():
        total += graph[key]

    print total

    dict_to_return = dict()

    for key in graph.keys():
        new_value = float(float(graph[key]) / float(total))
        dict_to_return[key] = new_value

    return dict_to_return


def log_log_it(dict_input):
    """
    yeah!
    """

    dict_to_return = dict()

    for key in dict_input.keys():
        #print key
        if (key != 0):
            new_key = math.log(key)
        else:
            new_key = 0
        #print dict_input[key]
        value = dict_input[key]
        new_value = math.log(value)

        new_value = value

        dict_to_return[new_key] = new_value
        print key, new_key
        print value, new_value
        
    return dict_to_return



def create_ER_graph(num_nodes, edge_probability):

    graph = init_graph(num_nodes)
    
    for idx in range(num_nodes):
        for idy in (range(idx)):
            random_one = random.random()
            random_two = random.random()
            #print edge_probability, random_one, random_two
            if (edge_probability > random_one):
                graph[idx].add(idy)
            if (edge_probability > random_two):
                graph[idy].add(idx)
        
    return graph


def create_DPA_graph(final_num_nodes, num_edges_for_new_nodes):

    graph = init_graph(num_edges_for_new_nodes)
    num_nodes = len(graph)
    current_node_id = num_nodes
    node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]

    # create a full graph for the starter "m" set of nodes.
    for idx in range(num_edges_for_new_nodes):
        for idy in (range(idx)):
            graph[idx].add(idy)
            graph[idy].add(idx)

    # how many "second wave" nodes do we have to create?
    num_new_nodes = final_num_nodes - num_edges_for_new_nodes

    # for the rest of the nodes, aka, n-m, create a new node,
    # create m amount of neighbors, and add to graph.
    for idx_new_nodes in range(num_new_nodes):
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_edges_for_new_nodes):
            new_node_neighbors.add(random.choice(node_numbers))

        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        node_numbers.append(current_node_id)
        node_numbers.extend(list(new_node_neighbors))

        # actually append the node.
        graph[current_node_id] = new_node_neighbors

        current_node_id += 1
        
    return graph

    


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

if False:

    graph = EX_GRAPH2
    print graph
    
    # Create the in-degree distribution.
    print "starting in_degrees distribution"
    in_degrees_dist = in_degree_distribution(graph)
    print "ending in_degrees distribution"

    # Testing!
    #keys3 = in_degrees_dist.keys()
    #print keys3[0]
    #print in_degrees_dist[keys3[0]]
    print in_degrees_dist

    # Normalize the distribution.
    print "starting the normalization."
    normalized = normalize_distribution(in_degrees_dist)
    print "ending the normalization."
    print normalized

    # Log/Log it.
    print "starting loglog"
    loglog = log_log_it(normalized)
    print "ending loglog"
    print loglog

    #print citation_graph
    print "done!"

    if False:
        x = np.linspace(0, 2, 100)

        plt.plot(x, x, label='linear')
        plt.plot(x, x**2, label='quadratic')
        plt.plot(x, x**3, label='cubic')

        plt.xlabel('x label')
        plt.ylabel('y label')

        plt.title("Simple Plot")

        plt.legend()

        plt.show()

    elif True:

        plt.plot(loglog.keys(), loglog.values(), 'ro', label="in_degrees")
        plt.xlabel('in_degrees level')
        plt.ylabel('in_degrees occurence')
        
        plt.title("Simple Plot")
        plt.legend()
        plt.show()
        
    #fig = plt.figure()  # an empty figure with no axes
    #fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
    #fig.show()
    
    
    #fig, ax = plt.subplots(1, 1)
    #ax.plot(data1, data2, **param_dict)
    #plt.show()



    

if True:
    
    # Load graph.   
    print "starting graph init"
    #graph = load_graph(CITATION_URL)
    #graph = create_ER_graph(1000, 0.05)
    graph = create_DPA_graph(28000, 12)
    print "ending graph init"

    # Testing!
    #print graph
    #keys = graph.keys()
    #print keys[0]
    #print graph[keys[0]]

    # Calculate the in-degree of each node..
    #print "starting in_degrees calc"
    #in_degrees = compute_in_degrees(citation_graph)
    #print "ending in_degrees calc"

    # Testing!
    #keys2 = in_degrees.keys()
    #print keys2[0]
    #print in_degrees[keys2[0]]

    # Create the in-degree distribution.
    if (True):
        print "starting in_degrees distribution"
        in_degrees_dist = in_degree_distribution(graph)
        print "ending in_degrees distribution"

        # Normalize the distribution.
        print "starting the normalization."
        normalized = normalize_distribution(in_degrees_dist)
        print "ending the normalization."
        #print normalized

    # Testing!
    #keys3 = in_degrees_dist.keys()
    #print keys3[0]
    #print in_degrees_dist[keys3[0]]

    

    if (False):
        # Create the out-degree distribution.
        print "starting out_degrees distribution"
        out_degrees_dist = out_degree_distribution(graph)
        print "ending out_degrees distribution"
        print out_degrees_dist
        average_out_degree = compute_average_out_degree(graph)
        print "average out_degree:", average_out_degree

        # Normalize the distribution.
        print "starting the normalization for out_degrees."
        normalized_out = normalize_distribution(out_degrees_dist)
        print "ending the normalization for out_degrees."
        #print normalized

    # Log/Log it.
    #print "starting loglog"
    #loglog = log_log_it(normalized)
    #print "ending loglog"
    #print loglog
    
    #print citation_graph
    #print "done!"

    if True:
        plt.plot(normalized.keys(), normalized.values(), 'ro', label="normalized")
        plt.xlabel('in_degrees occurence')
        plt.ylabel('in_degrees level')
        plt.yscale('log')
        plt.xscale('log')

    else:
        plt.plot(out_degrees_dist.keys(), out_degrees_dist.values(), 'ro', label="normalized")
        plt.xlabel('out_degrees occurence')
        plt.ylabel('out_degrees level')
        #plt.yscale('log')
        #plt.xscale('log')
        
    plt.title("Log/Log Plot of In-Degrees Distribution")
    #plt.legend()
    plt.show()


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

