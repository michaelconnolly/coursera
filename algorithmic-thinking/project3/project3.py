"""
Michael Connolly
Alorithmic Thinking, Part 2
Project 3
"""

import urllib2
import math
import alg_cluster
import random
import time
import matplotlib.pyplot as plt
#import alg_project3_solution
#import alg_project3_viz

            
def slow_closest_pair(cluster_list):
    """
    Takes a list of Cluster objects and returns a closest pair where the pair is represented
    by the tuple (dist, idx1, idx2) with idx1 < idx2 where dist is the distance between the
    closest pair cluster_list[idx1] and cluster_list[idx2]. This function should implement
    the brute-force closest pair method described in SlowClosestPair from Homework 3.       
    """
    smallest_distance = 'inf'
    smallest_cluster1_index = -1
    smallest_cluster2_index = -1
    cluster_list_length = len(cluster_list)

    for cluster1_index in range(0, cluster_list_length):
        for cluster2_index in range(0, cluster_list_length):
            if (cluster1_index != cluster2_index):
                distance = cluster_list[cluster1_index].distance(cluster_list[cluster2_index])
                if (distance < smallest_distance):
                    smallest_distance = distance
                    smallest_cluster1_index = cluster1_index
                    smallest_cluster2_index = cluster2_index

    #print "cluster_list:", cluster_list
    #print "smallest_distance:", smallest_distance, "smallest_cluster1_index:", smallest_cluster1_index, "smallest_cluster2_index:", smallest_cluster2_index

    return (smallest_distance, smallest_cluster1_index, smallest_cluster2_index)
    
    
def fast_closest_pair(cluster_list):
    """
    Takes a list of Cluster objects and returns a closest pair where the pair is represented
    by the tuple (dist, idx1, idx2) with idx1 < idx2 where dist is the distance between the
    closest pair cluster_list[idx1] and cluster_list[idx2]. This function should implement
    the divide-and-conquer closest pair method described FastClosestPair from Homework 3.
    """

    # Note to self: should the list be sorted before it gets inputed, or within this function?
    #cluster_list.sort(key = lambda cluster: cluster.horiz_center())

    cluster_list_length = len(cluster_list)
    
    # if we have 3 or less clusters, go the brute force method.
    if ((cluster_list_length) <= 3):
        #print "slow_closest_pair:", slow_closest_pair(cluster_list)
        return slow_closest_pair(cluster_list)

    # Otherwise, divide and conquer.
    else:
        
        # pick the index of the middle cluster
        middle = cluster_list_length / 2
    
        # create two new clusters, the left and right hand sides of the starting cluster.
        cluster_list_left = cluster_list[0:middle]
        cluster_list_right = cluster_list[middle+1:]
        
        # figure out the closest clusters on the left side.
        closest_pair_left = fast_closest_pair(cluster_list_left)

        # remap the indexes to the original cluster_list
        #print "old left:", closest_pair_left
        real_cluster1_left = cluster_list.index(cluster_list_left[closest_pair_left[1]])
        real_cluster2_left = cluster_list.index(cluster_list_left[closest_pair_left[2]])
        closest_pair_left = (closest_pair_left[0], real_cluster1_left, real_cluster2_left)
        #print "new left:", closest_pair_left
    
        # figure out the closest clusters on the right side.
        closest_pair_right = fast_closest_pair(cluster_list_right)
        #print "old right:", closest_pair_right
        real_cluster1_right = cluster_list.index(cluster_list_right[closest_pair_right[1]])
        real_cluster2_right = cluster_list.index(cluster_list_right[closest_pair_right[2]])
        closest_pair_right = (closest_pair_right[0], real_cluster1_right, real_cluster2_right)
        #print "new right:", closest_pair_right
        
        # pick a winner to see which side had the closest cluster pair.
        if (closest_pair_left[0] <= closest_pair_right[0]):
            closest_pair = closest_pair_left
        else:
            closest_pair = closest_pair_right

        # Lastly, make sure there isn't a closer pair that overlaps the midline
        # that we would have missed by splitting the list into halves.
        # So, find the closest pair that happen to be in the middle of the two dimensional space.
        midline = cluster_list[middle].horiz_center()
        #print "midline:", midline
        closest_middle_pair = closest_pair_strip(cluster_list, midline, closest_pair[0])
        #print "closest_middle_pair:", closest_middle_pair
        #print "closest_pair:", closest_pair

        # If there is a closer pair in the middle, pick that one instead.
        if (closest_middle_pair[0] <= closest_pair[0]):
            closest_pair = closest_middle_pair

        return closest_pair


def closest_pair_strip(cluster_list_input, horiz_center, half_width):
    """
    Takes a list of Cluster objects and two floats horiz_center and half_width. horiz_center
    specifies the horizontal position of the center line for a vertical strip. half_width
    specifies the maximal distance of any point in the strip from the center line. This
    function should implement the helper function described in ClosestPairStrip from
    Homework 3 and return a tuple corresponding to the closest pair of clusters that lie in
    the specified strip.
    """

    # Let S be a list of the set
    # Sort the indices in S in nondecreasing order of the vertical coordinates of their assoiated points
    #print "1:", cluster_list
    cluster_list = list(cluster_list_input)
    #cluster_list.sort(key = lambda cluster:cluster.vert_center())
    #print "2:", cluster_list
    
    # k <- |S|
    # initialize (d, i, j) to infinity, -1, -1
    smallest_distance = float('inf')
    smallest_cluster1_index = -1
    smallest_cluster2_index = -1
    cluster_list_length = len(cluster_list)
    left_edge = horiz_center - half_width
    right_edge = horiz_center + half_width

    #print "left_edge:", left_edge, "right_edge:", right_edge

    # for u <- 0 to k - 2 do
    for cluster1_index in range(0, cluster_list_length -1):

        #print "cluster1:", cluster_list[cluster1_index]
        #print "cluster1.horiz_center:", cluster_list[cluster1_index].horiz_center()
        
        # We only care about this cluster if it's within the strip.
        if ((cluster_list[cluster1_index].horiz_center() >= left_edge) and
            (cluster_list[cluster1_index].horiz_center() <= right_edge)):
    
            #print "this cluster1 is in the strip:", cluster_list[cluster1_index]
            
            for cluster2_index in range(cluster1_index + 1, cluster_list_length):
            
                # We only care about this cluster if it's within the strip.
                if ((cluster_list[cluster2_index].horiz_center() >= left_edge) and
                    (cluster_list[cluster2_index].horiz_center() <= right_edge)):

                    #print "this cluster2 is in the strip:", cluster_list[cluster2_index]

                    #(d,i,j) <- min)
                    distance = cluster_list[cluster1_index].distance(cluster_list[cluster2_index])
                    #print "cluster1:", cluster_list[cluster1_index], "cluster2:", cluster_list[cluster2_index]
                    #print "old:", smallest_distance, "new:", distance
                    if (distance < smallest_distance):
                        #print "resetting!"
                        smallest_distance = distance
                        smallest_cluster1_index = cluster1_index
                        smallest_cluster2_index = cluster2_index

        #else:
        #    print "this cluster1 is NOT in the strip:", cluster_list[cluster1_index]
            
    return (smallest_distance, smallest_cluster1_index, smallest_cluster2_index)


##DATA_3108_URL = "unifiedCancerData_3108.csv"
##DATA_896_URL = "unifiedCancerData_896.csv"
##DATA_290_URL = "unifiedCancerData_290.csv"
##DATA_111_URL = "unifiedCancerData_111.csv"
##DATA_24_URL = "unifiedCancerData_24.csv"

DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"
DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"

def load_data():
    """
    Load cancer risk data from .csv file
    """
    #data_file = urllib2.urlopen(DATA_111_URL)
    data_file = file(DATA_24_URL)
    data = data_file.read()
    data_lines = data.split('\n')
    print "Loaded", len(data_lines), "data points"
    data_tokens = [line.split(',') for line in data_lines]

    # return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])] for tokens in data_tokens]
    list_of_lists = [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])] for tokens in data_tokens]

    list_of_clusters = []
    for cluster_list in list_of_lists:
        cluster = alg_cluster.Cluster(cluster_list[0], cluster_list[1], cluster_list[2], cluster_list[3], cluster_list[4])
        list_of_clusters.append(cluster)

    return list_of_clusters


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Takes a list of Cluster objects and applies hierarchical clustering as described in the
    pseudo-code HierarchicalClustering from Homework 3 to this list of clusters. This clustering
    process should proceed until num_clusters clusters remain. The function then returns this
    list of clusters.
    """

    # n == |P|
    # cluster_list_length = len(cluster_list)

    # initialize n clusters C = {C1..Cn} such that Ci = {pi}
    # final_list = list(cluster_list)
    final_list = cluster_list
    final_list.sort(key=lambda cluster:cluster.horiz_center())
    
    # while |C| > k do
    while (len(final_list) > num_clusters):
        
        # (Ci, Cj) = argmin(.....)
        closest_cluster = fast_closest_pair(final_list)
        #print "calculated closest:", closest_cluster
        
        # C <- C U {Ci U C}
        cluster_target1 = final_list[closest_cluster[1]]
        #print "target1", cluster_target1
        cluster_target2 = final_list[closest_cluster[2]]
        #print "target2", cluster_target2
        cluster_target1.merge_clusters(cluster_target2)
    
        # C <- C \ {Ci, Cj}
        final_list.remove(cluster_target2)
        final_list.sort(key=lambda cluster:cluster.horiz_center())
        
    # return C
    

    return final_list


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Takes a list of Cluster objects and applies k-means clustering as described in the pseudo-code
    KMeansClustering from Homework 3 to this list of clusters. This function should compute an initial
    list of clusters (line 2 in the pseudo-code) with the property that each cluster consists of a
    single county chosen from the set of the num_cluster counties with the largest populations. The function
    should then compute num_iterations of k-means clustering and return this resulting list of clusters.
    """

    
    #list_count = len(cluster_list)
    clusters_to_merge = list(cluster_list)

    # Initialize the initial k clusters by picking the clusters with
    # highest population list.
    current_master_clusters = list(cluster_list)
    current_master_clusters.sort(key = lambda cluster:cluster.total_population())
    current_master_clusters.reverse()
    current_master_clusters = current_master_clusters[:num_clusters]
    
    # Iterate num_iteration times ...
    for dummy_iteration_count in range(0, num_iterations):

        #print "starting iteration #", iteration_count
        #print clusters_to_merge
        #print set_of_county_tuples(clusters_to_merge)

        # initialize k empty sets C1 .. Ck
        new_clusters = list([])
        for dummy_idx in range(0, num_clusters):
            #new_clusters.append(Cluster(set(current_master_clusters[idx_dummy].fips_codes()), 0, 0, 0, 0))
            new_clusters.append(alg_cluster.Cluster(set(), 0, 0, 0, 0))

        #for cluster_index in range(0, list_count):
        for cluster_to_merge_index in range(0, len(clusters_to_merge)):

            #print "starting merge #", cluster_to_merge_index
        
            # find the closest cluster in current_clusters
            closest_current_cluster_index = -1
            closest_distance = float('inf')
            for current_master_cluster_index in range(0, len(current_master_clusters)):
                distance = clusters_to_merge[cluster_to_merge_index].distance(current_master_clusters[current_master_cluster_index])
                if (distance < closest_distance):
                    closest_distance = distance
                    closest_current_cluster_index = current_master_cluster_index                         

            # merge this cluster with the closest_cluster
            #print "merge destination:" , new_clusters[closest_current_cluster_index]
            #print "merge source:", clusters_to_merge[cluster_to_merge_index]
            #if (new_clusters[closest_current_cluster_index].total_population() == 0):
            #    new_clusters[closest_current_cluster_index] = clusters_to_merge[cluster_to_merge_index]
            #else:
            new_clusters[closest_current_cluster_index].merge_clusters(clusters_to_merge[cluster_to_merge_index])
            #print "merge result:", new_clusters[closest_current_cluster_index]


        #for f_index in range(0, num_clusters):
        current_master_clusters = new_clusters
        clusters_to_merge = list(cluster_list)

    return current_master_clusters


def set_of_county_tuples(cluster_list):
    """
    Input: A list of Cluster objects
    Output: Set of sorted tuple of counties corresponds to counties in each cluster
    """
    set_of_clusters = set([])
    for cluster in cluster_list:
        counties_in_cluster = cluster.fips_codes()
        
        # convert to immutable representation before adding to set
        county_tuple = tuple(sorted(list(counties_in_cluster)))
        set_of_clusters.add(county_tuple)
    return set_of_clusters


def gen_random_clusters(num_clusters):

    cluster_list = list([])

    for cluster_index in range(0, num_clusters):

        horiz = random.uniform(-1, 1)
        vert = random.uniform(-1, 1)
        cluster = alg_cluster.Cluster(set(), horiz, vert, 0, 0)
        cluster_list.append(cluster)

    return cluster_list
    

def question_one():

    clusters = dict()
    times_slow = dict()
    times_fast = dict()

    for num_clusters in range(2, 201):
        
        cluster_list = gen_random_clusters(num_clusters)
        clusters[num_clusters] = cluster_list

        time_start = time.time()
        foo = slow_closest_pair(cluster_list)
        time_end = time.time() 
        time_total = time_end - time_start
        times_slow[num_clusters] = time_total

        time_start = time.time()
        foo = fast_closest_pair(cluster_list)
        time_end = time.time()
        time_total = time_end - time_start
        times_fast[num_clusters] = time_total
        
    print times_slow
    print times_fast

    plt.plot(times_slow.keys(), times_slow.values(), '-b', label="slow_closest_pair")
    plt.plot(times_fast.keys(), times_fast.values(), '-r', label="fast_closest_pair")
    #plt.plot(list_index, resilience_upa, '-g', label="upa m=3")
    #plt.plot(list_index, resilient_line, '-y', label="resilient_line")

    plt.xlabel('number of clusters')
    plt.ylabel('runtime')
    plt.title("time trials of two algorithims for finding the closest pair")
    plt.legend(loc='upper right')
    plt.show()


def load_data_table(data_url):
    """
    Import a table of county-based cancer risk data
    from a csv format file
    """
    data_file = urllib2.urlopen(data_url)
    data = data_file.read()
    data_lines = data.split('\n')
    print "Loaded", len(data_lines), "data points"
    data_tokens = [line.split(',') for line in data_lines]
    return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])] 
            for tokens in data_tokens]


def question_two():
    """
    Use alg_project3_viz to create an image of the 15 clusters generated by applying hierarchical
    clustering to the 3108 county cancer risk data set. You may submit an image with the 3108
    counties colored by clusters or an enhanced visualization with the original counties colored
    by cluster and linked to the center of their corresponding clusters by lines. You can generate
    such an enhanced plot using our alg_clusters_matplotlib code by modifying the last parameter
    of plot_clusters to be True. Note that plotting only the resulting cluster centers is not acceptable.
    """


def compute_distortion(cluster_list, data_table):
    """
    Write a function compute_distortion(cluster_list) that takes a list of clusters and uses cluster_error
    to compute its distortion. Now, use compute_distortion to compute the distortions of the two clusterings
    in questions 5 and 6. Enter the values for the distortions (with at least four significant digits) for
    these two clusterings in the box below. Clearly indicate the clusterings to which each value corresponds.
    """

    error = 0
    for cluster in cluster_list:
        error += cluster.cluster_error(data_table)

    return error


def question_ten():
    """
    Load a data table, compute a list of clusters and 
    plot a list of clusters

    Set DESKTOP = True/False to use either matplotlib or simplegui
    """
    #data_table = load_data_table(DATA_3108_URL)
    data_table = load_data_table(DATA_896_URL)
    #data_table = load_data_table(DATA_290_URL)
    #data_table = load_data_table(DATA_111_URL)

    hierarchical_distortion_list = dict([])
    for num_clusters in range(6, 21):
        print "hierarchical: num_cluster=", num_clusters

        singleton_list = []
        for line in data_table:
            singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
        
        cluster_list = hierarchical_clustering(singleton_list, num_clusters)
        distortion = compute_distortion(cluster_list, data_table)
        print distortion
        hierarchical_distortion_list[num_clusters] = distortion

    kmeans_distortion_list = dict([])
    for num_clusters in range(6, 21):
        print "kmeans: num_cluster=", num_clusters

        singleton_list = []
        for line in data_table:
            singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
        
        cluster_list = kmeans_clustering(singleton_list, num_clusters, 5)
        distortion = compute_distortion(cluster_list, data_table)
        print distortion
        kmeans_distortion_list[num_clusters] = distortion
        

    print "About to display ...."

    #cluster_list = alg_project3_solution.hierarchical_clustering(singleton_list, 16)
    #cluster_list = alg_project3_solution.hierarchical_clustering(singleton_list, 9)

    #print "Displaying", len(cluster_list), "hierarchical clusters"

    #cluster_list = alg_project3_solution.kmeans_clustering(singleton_list, 9, 5)	
    #print "Displaying", len(cluster_list), "k-means clusters"


    # compute the distortion
    if (False):
        distortion = compute_distortion(cluster_list, data_table)
        print distortion

    plt.plot(hierarchical_distortion_list.keys(), hierarchical_distortion_list.values(), '-b', label="hierarchical")
    plt.plot(kmeans_distortion_list.keys(), kmeans_distortion_list.values(), '-r', label="kmeans")
    #plt.plot(times_fast.keys(), times_fast.values(), '-r', label="fast_closest_pair")
    #plt.plot(list_index, resilience_upa, '-g', label="upa m=3")
    #plt.plot(list_index, resilient_line, '-y', label="resilient_line")

    plt.xlabel('number of clusters')
    plt.ylabel('distortion')
    plt.title("distortion levels of clustering techniques using 896 dataset")
    plt.legend(loc='upper right')
    plt.show()
        



###
###As one important coding note, you will need to sort a list of clusters by the horizontal
###(as well as vertical) positions of the cluster centers. This operation can be done in a
###single line of Python using the sort method for lists by providing a key argument of the form:
###cluster_list.sort(key = lambda cluster: cluster.horiz_center())
###"""

def test_suite():
    """
    These are the tests that i manually run, since they at one point failed in OwlTest.
    """
    
  
    if (False):

        cluster_list_test = load_data()
        #cluster_list_test = cluster_list_test[0:3]
        clustered_list = kmeans_clustering(cluster_list_test, 5, 3)
        print "START list:", set_of_county_tuples(cluster_list_test)
        print "FINAL clustered:" , set_of_county_tuples(clustered_list)

        #print len(cluster_list_test)
        #print len(clustered_list)
        #print type(cluster_list_test)
        #print type(clustered_list)
        #print type(cluster_list_test[0])
        #print type(clustered_list[0])
        #print cluster_list_test[0]
        #print clustered_list[0]
        #print clustered_list[-1]
    
#test_suite()
question_ten()


