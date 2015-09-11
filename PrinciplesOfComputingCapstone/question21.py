"""
Provided code for Question 25 on the Capstone Exam
"""

import urllib2

        
##########################################################
# Code for loading graphs


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



def run_example():
    """
    Generate example graphs
    """

    GRAPH1 = {1 : set([]), 2 : set([3, 7]), 3 : set([2, 4]), 4 : set([3, 5]),
              5 : set([4, 6]), 6 : set([5, 7]), 7 : set([2, 6])}
    GRAPH2 = {1 : set([2, 3, 4, 5, 6, 7]), 2 : set([1]), 3 : set([1]),
              4 : set([1]), 5 : set([1]), 6 : set([1]), 7 : set([1])}
    

    # Example graphs stored on Coursera (AWS) if using desktop Python
    GRAPH3_URL = "https://d396qusza40orc.cloudfront.net/foccapstone/exam_code/graph3.txt"
    GRAPH4_URL = "https://d396qusza40orc.cloudfront.net/foccapstone/exam_code/graph4.txt"
    GRAPH5_URL = "https://d396qusza40orc.cloudfront.net/foccapstone2/code/graph5_fall2015.txt"

    # Example graphs stored on Google (Storage) if using CodeSkulptor
    #GRAPH3_URL = "http://storage.googleapis.com/codeskulptor-assets/foc_assets/graph3.txt"
    #GRAPH4_URL = "http://storage.googleapis.com/codeskulptor-assets/foc_assets/graph4.txt"
    #GRAPH5_URL = "http://storage.googleapis.com/codeskulptor-assets/foc_assets/graph5_fall2015.txt"

    GRAPH3 = load_graph(GRAPH3_URL)
    GRAPH4 = load_graph(GRAPH4_URL)
    GRAPH5 = load_graph(GRAPH5_URL)
   

    # The number of nodes in the sets returned by Mystery for GRAPH3 and GRAPH4
    # are respectively, 6 and 9.

#run_example()
            
    
    



    
    
    









def create_subset2(graph, size_requested):

    if (len(graph) == 0):
        return list()

    if (size_requested == 0):
        #print "ERROR! size_requested == 0!"
        return list()

    if (size_requested == 1):
        return_list = list()
        for key in graph.keys():
            new_set = set()
            new_set.add(key)
            return_list.append(new_set)
        return return_list

    first_key = graph.keys()[0]
    rest_of_graph = graph.copy()
    rest_of_graph.pop(graph.keys()[0])
    #print "graph", graph
    #print "rest_of_graph", rest_of_graph

    #Give me the proper size where first_node is included.
    list_of_subsets = create_subset2(rest_of_graph, size_requested - 1)
    for subset in list_of_subsets:
        subset.add(first_key)

    #Give me the proper size from the rest_of_graph when first node is not included.
    list_of_subsets2 = create_subset2(rest_of_graph, size_requested)
    list_of_subsets.extend(list_of_subsets2)

    return list_of_subsets

        
        





##
##def create_subset(graph, size_requested):
##
##    returned_list_of_sets = list()
##    length_of_graph = len(graph)
##    print "---"
##    print "starting graph", graph, "size_requested", size_requested
##    
##    if (length_of_graph == 0 or size_requested == 0):
##        return returned_list_of_sets
##
##    elif (length_of_graph == size_requested):
##        returned_list_of_sets.append(graph.keys())
##        return returned_list_of_sets
##
##    elif (length_of_graph < size_requested):
##        print "error!!!!!!"
##        return returned_list_of_sets
##
##    elif (length_of_graph == 1):
##        returned_set.add(graph.keys()[0]) 
##        return returned_list_of_sets
##
##    else:
##
##        smaller_graph = dict(graph)
##        
##        for key in graph.keys():
##
##            print "starting with key", key
##            
##            subset_head = set()
##            subset_head.add(key)
##            #subset_head.add(graph.keys()[0])
##            #subset_head.update(key)
##            print "subset_head", subset_head
##        
##            #smaller_graph = dict(graph)
##            smaller_graph.pop(key)
##            print "smaller_graph", smaller_graph
##        
##            #for i in range(len(smaller_graph)):
##
##            #for i in range(size_requested):
##                #print "inside second loop"
##            nodes_to_add = create_subset(smaller_graph, size_requested - 1)
##            print "nodes_to_add", subset_head
##            for node in nodes_to_add:
##                subset_head.update(node)
##            print "subset_head", subset_head
##            
##                #full_subset = list(subset_head) #subset_head.copy()
##                #full_subset.extend(nodes_to_add)
##                #full_subset_as_list = set(full_subset)
##            returned_list_of_sets.append(subset_head)
##            
##            #full_subset = subset_head.copy()
##            #full_subset.extend(nodes_to_add)
##            #full_subset_as_list = full_subset
##
##            #print "about to add", full_subset, "to", returned_list_of_sets
##            #print "returned_set", returned_set
##            #returned_list_of_sets.append(full_subset_as_list)
##            #print "did it happen?", returned_list_of_sets
##    
##    return returned_list_of_sets


def create_list_of_edges(graph):

    list_of_edges = list()
    
    for node_id in graph.keys():
        for other_node_id in graph[node_id]:
            if (node_id < other_node_id):
                edge = tuple([node_id, other_node_id])
            else:
                edge = tuple([other_node_id, node_id])
            if (edge not in list_of_edges):
                list_of_edges.append(edge)

    return list_of_edges
        

def mystery(graph):

    num_nodes = len(graph)
    list_of_edges = create_list_of_edges(graph)
    all_possible_returns = list()
    #print "LIST_OF_EDGES", list_of_edges

    for i in range(1, num_nodes + 1):
    #for i in range(5, 6):
        
        list_of_sets = create_subset2(graph, i)
        #print "list_of_sets", list_of_sets
        
        for my_set in list_of_sets:
            #print "my_set", my_set
            flag = True

            # for each edge in ALL ORIGINAL EDGES
            for edge in list_of_edges:
                #print "EDGE", edge, edge[0], edge[1]
                # if this edge is not in the new list_of_sets
                if edge[0] not in my_set and edge[1] not in my_set:
                    #"flag=false", edge[0], edge[1], my_set
                    flag = False

            if flag == True:
                #return my_set
                all_possible_returns.append(my_set)

    return all_possible_returns

graph = {1:set([]), 2:set([7]), 3:set([4]), 4:set([3]), 5:set([6]), 6:set([5]), 7:set([2])}        
#graph = {1:set([2, 3, 4, 5, 6, 7]), 2:set([1, 3, 7]), 3:set([1, 2, 4]), 4:set([1, 3, 5]), 5:set([1, 4, 6]), 6:set([1, 5, 7]), 7:set([1, 2, 6])}
#graph = {1:set([3, 4]), 2:set(), 3:set([1]), 4:set([1])}
#graph = {1:set[2], 2:set[1]}
#print "GRAPH", graph
#print create_subset2(graph, 3)
#print "LIST OF EDGES", create_list_of_edges(graph)
#print mystery(graph)

GRAPH1 = {1 : set([]), 2 : set([3, 7]), 3 : set([2, 4]), 4 : set([3, 5]),
              5 : set([4, 6]), 6 : set([5, 7]), 7 : set([2, 6])}
GRAPH2 = {1 : set([2, 3, 4, 5, 6, 7]), 2 : set([1]), 3 : set([1]),
              4 : set([1]), 5 : set([1]), 6 : set([1]), 7 : set([1])}
    

# Example graphs stored on Coursera (AWS) if using desktop Python
GRAPH3_URL = "https://d396qusza40orc.cloudfront.net/foccapstone/exam_code/graph3.txt"
GRAPH4_URL = "https://d396qusza40orc.cloudfront.net/foccapstone/exam_code/graph4.txt"
GRAPH5_URL = "https://d396qusza40orc.cloudfront.net/foccapstone2/code/graph5_fall2015.txt"

# Example graphs stored on Google (Storage) if using CodeSkulptor
#GRAPH3_URL = "http://storage.googleapis.com/codeskulptor-assets/foc_assets/graph3.txt"
#GRAPH4_URL = "http://storage.googleapis.com/codeskulptor-assets/foc_assets/graph4.txt"
#GRAPH5_URL = "http://storage.googleapis.com/codeskulptor-assets/foc_assets/graph5_fall2015.txt"

GRAPH3 = load_graph(GRAPH3_URL)
GRAPH4 = load_graph(GRAPH4_URL)
GRAPH5 = load_graph(GRAPH5_URL)

print graph
foo= mystery(graph)
print foo
print len(foo)

