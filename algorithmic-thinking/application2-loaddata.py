"""
Application #2 in Algorthimic Thinking.
Michael Connolly
"""

# general imports
import urllib2
import random
import time
import math
from collections import deque
import cPickle as pickle



# CodeSkulptor import
#import simpleplot
#import codeskulptor
#codeskulptor.set_timeout(60)

# Desktop imports
#import matplotlib.pyplot as plt


############################################
# Provided code

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    
def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order
    


##########################################################
# Code for loading computer network graph

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"
LOCAL_URL = "C:/dev/coursera/algorithmic-thinking/application2-data/alg_rf7.txt"


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


def load_graph_local(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    #graph_file = urllib2.urlopen(graph_url)
    graph_file = file(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
        
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    #print "Loaded graph with", len(answer_graph), "nodes and", count_edges(answer_graph), "edges"


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



def init_edges_complete_undirected(graph, probability):
    """
    internal function used to create all the edges necessary for a complete directed graph.
    """
    
    num_nodes = len(graph)

    for idx in range(num_nodes):
        for idy in (range(idx)):

            random_chance = random.random();
            if (random_chance < probability):
                graph[idx].add(idy)
                graph[idy].add(idx)
        
    return graph


def count_edges(graph):

    count = 0

    for node in graph.keys():
        count += len(graph[node])

    # Remember to divide by 2, since this is an undirected graph!
    return (count / 2)


def make_complete_graph_undirected(num_nodes, probability):
    """
    Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete
    directed graph with the specified number of nodes. A complete graph contains all possible
    edges subject to the restriction that self-loops are not allowed. The nodes of the graph
    should be numbered 0 to num_nodes - 1 when num_nodes is positive. Otherwise, the function
    returns a dictionary corresponding to the empty graph.
    """

    graph = init_graph(num_nodes)
    graph = init_edges_complete_undirected(graph, probability)

    #print "Loaded FOO graph with", len(graph), "nodes and", count_edges(graph), "edges"

    return graph


class UPATrial:
    """
    Simple class to encapsulate optimizated trials for the UPA algorithm
    
    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that each node number
        appears in correct ratio
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))

        #print self._node_numbers
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors


def create_UPA_graph2(final_num_nodes, num_edges_for_new_nodes):

    #graph = init_graph(num_edges_for_new_nodes)
    graph = make_complete_graph_undirected(num_edges_for_new_nodes, 1)
    num_nodes = len(graph)
    current_node_id = num_nodes
    upa_trial = UPATrial(num_edges_for_new_nodes)

     # how many "second wave" nodes do we have to create?
    num_new_nodes = final_num_nodes - num_edges_for_new_nodes

    # for the rest of the nodes, aka, n-m, create a new node,
    # create m amount of neighbors, and add to graph.
    for idx_new_nodes in range(num_new_nodes):

        # compute the neighbors for the newly-created node
        new_node_neighbors = upa_trial.run_trial(num_edges_for_new_nodes)
        #print "blah:", new_node_neighbors
        # actually append the node.
        graph[current_node_id] = new_node_neighbors

        # addition for undirected graphs:
        for node in new_node_neighbors:
            graph[node].add(current_node_id)

        current_node_id += 1

    return graph

        

def create_UPA_graph(final_num_nodes, num_edges_for_new_nodes):

    graph = init_graph(num_edges_for_new_nodes)
    #graph = make_complete_graph_undirected(num_edges_for_new_nodes, 1)
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

        # addition for undirected graphs:
        for node in new_node_neighbors:
            graph[node].add(current_node_id)

        current_node_id += 1
        
    return graph


def summarize_graph(label, graph):

      print "Loaded", label, "graph with", len(graph), "nodes and", count_edges(graph), "edges"


def random_order(graph):
    """
    Takes a graph and returns a list of the nodes in the graph in some random order.
    Then, for each of the three graphs (computer network, ER, UPA), compute a random
    attack order using random_order and use this attack order in compute_resilience
    to compute the resilience of the graph.
    """
    list_to_return = list([])
    
    for node in graph.keys():
        list_to_return.append(node)

    random.shuffle(list_to_return)

    return list_to_return



def bfs_visited(ugraph, start_node):
    """
    Takes the undirected graph ugraph and the node start_node and
    returns the set consisting of all nodes that are visited by a
    breadth-first search that starts at start_node.
    """

    visited = set([])

    #print "STARTING bfs_visited with:", start_node, ugraph

    # initialize Q to an empty queue
    que = deque()

    # initialize set_to_return to include the start_node,
    # and, add our start_node to the Q.
    visited.add(start_node)
    que.append(start_node)

    # lets loop through all our nodes!
    while len(que):

        #print "visited:", visited
        #print "q:", que

        # gimme the next item.
        current_node = que.popleft()
        #print "current_node:", current_node
        #print "ugraph:", ugraph
        #print "q after pop:", q

        # enumerate all neighbors and add them to the q.
        for neighbor in ugraph[current_node]:

            if (neighbor not in visited):

                visited.add(neighbor)
                que.append(neighbor)

    #print "ending bfs_visited with:", visited
    return visited



def cc_visited(ugraph):
    """
    Takes the undirected graph ugraph and returns a list of sets,
    where each set consists of all the nodes (and nothing else) in
    a connected component, and there is exactly one set in the
    list for each connected component in ugraph and nothing else.
    """

    remaining_nodes = ugraph.copy()
    list_of_sets = list([])

    while len(remaining_nodes):

        #print "remaining_nodes:", remaining_nodes
        
        idx = remaining_nodes.keys()[0]
        #print "i:", i

        #print "ABOUT to call bfs_visited with:", idx, ugraph
        visited_nodes = bfs_visited(ugraph, idx)
        #print "visited_nodes:" , visited_nodes
        if (visited_nodes not in list_of_sets):
            list_of_sets.append(visited_nodes)
        #print "list_of_sets:" , list_of_sets
        

        remaining_nodes.pop(idx)

    #print "about to return cc_visited:", list_of_sets
    return list_of_sets


def largest_cc_size(ugraph):
    """
    Takes the undirected graph ugraph and returns the size (an integer)
    of the largest connected component in ugraph.
    """

    #print "starting with graph:", ugraph
    size_to_return = 0

    set_of_cc = cc_visited(ugraph)

    for components in set_of_cc:
        #print "components:", components
        size_of_cc = len(components)
        
        if (size_of_cc > size_to_return):
            size_to_return = size_of_cc

    return size_to_return


def compute_resilience(ugraph, attack_order):
    """
    Takes the undirected graph ugraph, a list of nodes attack_order
    and iterates through the nodes in attack_order. For each node
    in the list, the function removes the given node and its edges
    from the graph and then computes the size of the largest
    connected component for the resulting graph.
    """

    list_of_cc_largest_sizes = list([])
    list_of_cc_largest_sizes.append(largest_cc_size(ugraph))

    hacked_graph = ugraph.copy()

    debug_counter = 0
    debug_counter_total = len(attack_order)
    
    for node_to_attack in attack_order:

        #print "graph start:", hacked_graph
        print "compute_resilience: starting", debug_counter, "of", debug_counter_total
        debug_counter += 1

        # Remove the node_to_attack, by ...
        # 1) removing the edges that connect to it    
        for node_key in hacked_graph.keys():
            #print "node_key:", node_key
            hacked_graph[node_key].difference_update(list([node_to_attack]))
        # 2) removing the node itself

        #print "node to attack:", node_to_attack
        hacked_graph.pop(node_to_attack)
        
        #print "graph end:", hacked_graph

        size_of_largest = largest_cc_size(hacked_graph)
        list_of_cc_largest_sizes.append(size_of_largest)

    return list_of_cc_largest_sizes
    



###
### START OF PROGRAM
###

# Logic for computer network graphs.
computer_network_graph = load_graph_local(LOCAL_URL)
summarize_graph("CN", computer_network_graph)

# Logic for ER graphs.
er_graph = make_complete_graph_undirected(1239, .004)
summarize_graph("ER", er_graph)

# Logic for UPA graphs.
initial_size = 3
target_size = 1239
#trial_count = target_size - initial_size
#upa_graph = create_UPA_graph(target_size, initial_size)
#summarize_graph("UPA", upa_graph)
#upa_trial = UPATrial(initial_size)
#upa_graph = upa_trial.run_trial(trial_count)
#print upa_graph
#summarize_upa_graph("UPA", upa_graph)
upa_graph = create_UPA_graph2(target_size, initial_size)
summarize_graph("UPA", upa_graph)

#test_upa_graph = create_UPA_graph(20, 5)
#print test_upa_graph
#random_nodes = random_order(test_upa_graph)
#print random_nodes

# Let's create a list of node for each graph in random order.
random_order_nodes_computer_network = random_order(computer_network_graph)
random_order_nodes_er = random_order(er_graph)
random_order_nodes_upa = random_order(upa_graph)

with open("random-CN.txt", 'wb') as f:
    pickle.dump(random_order_nodes_computer_network, f)
#foo = pickle.dumps(random_order_nodes_upa, "foo.txt")

if (True):
    # let's start calculating resilience
    #print "starting resiliency check for CN"
    resilience_computer_network = compute_resilience(computer_network_graph, random_order_nodes_computer_network)
    filename_res_CN = "resilience_CN.txt"
    with open(filename_res_CN, 'wb') as f:
        pickle.dump(resilience_computer_network, f)

    #print "starting resiliency check for ER"
    resilience_er = compute_resilience(er_graph, random_order_nodes_er)
    filename_res_ER = "resilience_ER.txt"
    with open(filename_res_ER, 'wb') as f:
        pickle.dump(resilience_er, f)

    #print "starting resiliency check for UPA"
    resilience_upa = compute_resilience(upa_graph, random_order_nodes_upa)
    filename_res_UPA = "resilience_UPA.txt"
    with open(filename_res_UPA, 'wb') as f:
        pickle.dump(resilience_upa, f)

# Let's do a 


