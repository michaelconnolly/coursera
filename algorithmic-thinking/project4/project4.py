"""
Michael Connolly
Alorithmic Thinking, Part 2
Project 4
"""


##################################################


"""
Provide code and solution for Application 4
"""

DESKTOP = True

import math
import random
import urllib2

if DESKTOP:
    import matplotlib.pyplot as plt
    #import alg_project4_solution as student
else:
    import simpleplot
    import userXX_XXXXXXX as student
    

# URLs for data files
PAM50_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt"
HUMAN_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt"
FRUITFLY_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt"
CONSENSUS_PAX_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt"
WORD_LIST_URL = "http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt"



###############################################
# provided code

def read_scoring_matrix(filename):
    """
    Read a scoring matrix from the file named filename.  

    Argument:
    filename -- name of file containing a scoring matrix

    Returns:
    A dictionary of dictionaries mapping X and Y characters to scores
    """
    scoring_dict = {}
    #scoring_file = urllib2.urlopen(filename)
    scoring_file = file(filename)
    ykeys = scoring_file.readline()
    ykeychars = ykeys.split()
    for line in scoring_file.readlines():
        vals = line.split()
        xkey = vals.pop(0)
        scoring_dict[xkey] = {}
        for ykey, val in zip(ykeychars, vals):
            scoring_dict[xkey][ykey] = int(val)
    return scoring_dict




def read_protein(filename):
    """
    Read a protein sequence from the file named filename.

    Arguments:
    filename -- name of file containing a protein sequence

    Returns:
    A string representing the protein
    """
  
    #protein_file = urllib2.urlopen(filename)
    protein_file = file(filename)
    protein_seq = protein_file.read()
    protein_seq = protein_seq.rstrip()
    return protein_seq


def read_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    # load assets
    word_file = urllib2.urlopen(filename)
    
    # read in files as string
    words = word_file.read()
    
    # template lines and solution lines list of line string
    word_list = words.split('\n')
    print "Loaded a dictionary with", len(word_list), "words"
    return word_list


##################################################


def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """
    Takes as input a set of characters alphabet and three scores diag_score, off_diag_score, and dash_score. The
    function returns a dictionary of dictionaries whose entries are indexed by pairs of characters in alphabet
    plus '-'. The score for any entry indexed by one or more dashes is dash_score. The score for the remaining
    diagonal entries is diag_score. Finally, the score for the remaining off-diagonal entries is off_diag_score.
    One final note for build_scoring_matrix is that, although an alignment with two matching dashes is not allowed,
    the scoring matrix should still include an entry for two dashes (which will never be used).
    """

    full_alphabet = set(alphabet)
    full_alphabet.add("-")
    
    master_dict = dict()

    for master_char in full_alphabet:

        sub_dict = dict()

        for sub_char in full_alphabet:

            if (sub_char == "-" or master_char == "-"):
                score = dash_score
            elif (sub_char == master_char):
                score = diag_score
            else:
                score = off_diag_score

            sub_dict[sub_char] = score

        master_dict[master_char] = sub_dict
        
    return master_dict


def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a common alphabet with the scoring matrix
    scoring_matrix. The function computes and returns the alignment matrix for seq_x and seq_y as described in
    the Homework. If global_flag is True, each entry of the alignment matrix is computed using the method described
    in Question 8 of the Homework. If global_flag is False, each entry is computed using the method described
    in Question 12 of the Homework.
    """
    
    x_length = len(seq_x)
    y_length = len(seq_y)

    alignment = [[None for dummy_idx1 in range(y_length+1)] for dummy_idx2 in range(x_length+1)]
    alignment[0][0] = 0

    for i_index in range(1, x_length+1):
        current_x_char = seq_x[i_index - 1]
        score = alignment[i_index - 1][0] + scoring_matrix[current_x_char]["-"]  
        alignment[i_index][0] = calculate_score(score, global_flag)

    for j_index in range(1, y_length+1):
        current_y_char = seq_y[j_index - 1]
        score = alignment[0][j_index - 1] + scoring_matrix["-"][current_y_char] 
        alignment[0][j_index] = calculate_score(score, global_flag)

    for i_index in range(1, x_length+1):
        for j_index in range(1, y_length+1):
            current_x_char = seq_x[i_index - 1]
            current_y_char = seq_y[j_index - 1]
            score = scoring_matrix[current_x_char][current_y_char]
            #score_no_y = scoring_matrix[current_x_char]["-"]
            #score_no_x = scoring_matrix["-"][current_y_char]
            
            new_value = max(max((alignment[i_index - 1][j_index - 1] + score),
                                      (alignment[i_index - 1][j_index] + scoring_matrix[current_x_char]["-"])),
                                      (alignment[i_index][j_index - 1] + scoring_matrix["-"][current_y_char]))

            alignment[i_index][j_index] = calculate_score(new_value, global_flag)

    return alignment


def calculate_score(score, global_flag):
    """
    Figure out if we should baseline to zero in the !global_flag case.
    """

    if ((not global_flag) and (score < 0)):
        return 0

    return score
    

def compute_global_alignment(x_sequence, y_sequence, scoring_matrix, alignment_matrix):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a common alphabet with the scoring matrix
    scoring_matrix. This function computes a global alignment of seq_x and seq_y using the global alignment
    matrix alignment_matrix.  The function returns a tuple of the form (score, align_x, align_y) where score is
    the score of the global alignment align_x and align_y. Note that align_x and align_y should have the same
    length and may include the padding character '-'. 
    """

    x_optimal = ""
    y_optimal = ""
    x_length = len(x_sequence)
    y_length = len(y_sequence)

    # max_score is always the bottom-right cell in the alignment_matrix.
    max_score = alignment_matrix[x_length][y_length]

    while (x_length > 0 and y_length > 0):

        current_score = alignment_matrix[x_length][y_length]

        if (current_score == alignment_matrix[x_length-1][y_length-1] + scoring_matrix[x_sequence[x_length-1]][y_sequence[y_length-1]]):

            x_optimal = x_sequence[x_length-1] + x_optimal
            y_optimal = y_sequence[y_length-1] + y_optimal
            x_length = x_length - 1
            y_length = y_length - 1

        else:

            score_no_y = scoring_matrix[x_sequence[x_length-1]]["-"]
            
            if (current_score == (alignment_matrix[x_length-1][y_length] + score_no_y)):
                x_optimal = x_sequence[x_length-1] + x_optimal
                y_optimal = "-" + y_optimal # + "-"
                x_length = x_length -1

            else:
                x_optimal = "-" + x_optimal # + "-"
                y_optimal = y_sequence[y_length-1] + y_optimal
                y_length = y_length-1

    while (x_length > 0):

        x_optimal = x_sequence[x_length-1] + x_optimal
        y_optimal = "-" + y_optimal
        x_length = x_length - 1

    while (y_length > 0):

        x_optimal = "-" + x_optimal
        y_optimal = y_sequence[y_length-1] + y_optimal
        y_length = y_length - 1
            
    return (max_score, x_optimal, y_optimal)


def compute_local_alignment(x_sequence, y_sequence, scoring_matrix, alignment_matrix):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a common alphabet with the scoring matrix scoring_matrix. This
    function computes a local alignment of seq_x and seq_y using the local alignment matrix alignment_matrix. The function returns a
    tuple of the form (score, align_x, align_y) where score is the score of the optimal local alignment align_x and align_y. Note that
    align_x and align_y should have the same length and may include the padding character '-'. 
    """

    x_optimal = ""
    y_optimal = ""
    x_length = len(x_sequence)
    y_length = len(y_sequence)
    max_score = 0

    # We don't have to initialize max_score_row or max_score_col, because the lowest
    # score in the alignment_matrix will always be 0.

    # for local alignment, we start not at the bottom-right cell, but the maximal value.
    for i_index in range(0, x_length+1):
        for j_index in range(0, y_length+1):
            if (alignment_matrix[i_index][j_index] >= max_score):
                max_score = alignment_matrix[i_index][j_index]
                max_score_row = i_index
                max_score_col = j_index

    # start our iteration through the table and the max cell we found.
    x_length = max_score_row
    y_length = max_score_col

    current_score = alignment_matrix[x_length][y_length]

    while (x_length > 0 and y_length > 0 and current_score != 0):

        if (current_score == alignment_matrix[x_length-1][y_length-1] + scoring_matrix[x_sequence[x_length-1]][y_sequence[y_length-1]]):

            x_optimal = x_sequence[x_length-1] + x_optimal
            y_optimal = y_sequence[y_length-1] + y_optimal
            x_length = x_length - 1
            y_length = y_length - 1

        else:

            score_no_y = scoring_matrix[x_sequence[x_length-1]]["-"]
            
            if (current_score == (alignment_matrix[x_length-1][y_length] + score_no_y)):
                x_optimal = x_sequence[x_length-1] + x_optimal
                y_optimal = "-" + y_optimal # + "-"
                x_length = x_length -1

            else:
                x_optimal = "-" + x_optimal # + "-"
                y_optimal = y_sequence[y_length-1] + y_optimal
                y_length = y_length-1

        current_score = alignment_matrix[x_length][y_length]
    
    return (max_score, x_optimal, y_optimal)


##########################################################################

def calculate_percent_similar(seq_x, seq_y):

    length_x = len(seq_x)
    length_y = len(seq_y)
    total_matches = float(0)

    if (length_x != length_y):
        print "error! lengths not the same in calculate_percent_similar!"
        return

    for index in range(0, length_x):
        x_char = seq_x[index]
        y_char = seq_y[index]
        if (x_char == y_char):
            total_matches = total_matches + 1

    percent_similar = total_matches / length_x

    return percent_similar
        



def question1():

    human_protein = read_protein("alg_HumanEyelessProtein.txt")
    fruitfly_protein = read_protein("alg_FruitflyEyelessProtein.txt")
    scoring_matrix = read_scoring_matrix("alg_PAM50.txt")
    alignment_matrix = compute_alignment_matrix(human_protein, fruitfly_protein, scoring_matrix, False)

    local_alignment = compute_local_alignment(human_protein, fruitfly_protein, scoring_matrix, alignment_matrix)

    print local_alignment
    
    return


def question2():

    human_protein = read_protein("alg_HumanEyelessProtein.txt")
    fruitfly_protein = read_protein("alg_FruitflyEyelessProtein.txt")
    scoring_matrix = read_scoring_matrix("alg_PAM50.txt")
    alignment_matrix = compute_alignment_matrix(human_protein, fruitfly_protein, scoring_matrix, False)

    local_alignment = compute_local_alignment(human_protein, fruitfly_protein, scoring_matrix, alignment_matrix)
    #print local_alignment
    human_optimal = local_alignment[1]
    fruitfly_optimal = local_alignment[2]
    human_optimal = human_optimal.replace("-", "")
    fruitfly_optimal = fruitfly_optimal.replace("-", "")
    #print human_optimal
    #print fruitfly_optimal

    consensus_pax = read_protein("alg_ConsensusPAXDomain.txt")
    #print consensus_pax

    human_alignment_matrix = compute_alignment_matrix(human_optimal, consensus_pax, scoring_matrix, True)
    human_global_alignment = compute_global_alignment(human_optimal, consensus_pax, scoring_matrix, human_alignment_matrix)
    #print human_global_alignment
    human_similar = calculate_percent_similar(human_global_alignment[1], human_global_alignment[2])
    print human_similar

    fruitfly_alignment_matrix = compute_alignment_matrix(fruitfly_optimal, consensus_pax, scoring_matrix, True)
    fruitfly_global_alignment = compute_global_alignment(fruitfly_optimal, consensus_pax, scoring_matrix, fruitfly_alignment_matrix)
    #print fruitfly_global_alignment
    fruitfly_similar = calculate_percent_similar(fruitfly_global_alignment[1], fruitfly_global_alignment[2])
    print fruitfly_similar

    return

def create_random_protein(alphabet, size_of_protein):

    alphabet_length = len(alphabet)
    output_string = ""

    for index in range(0, size_of_protein):
        new_char = alphabet[random.randrange(0, alphabet_length)]
        output_string = output_string + new_char

    return output_string
    

def question3():

    alphabet = "ACBEDGFIHKMLNQPSRTWVYXZ"

    human_protein = read_protein("alg_HumanEyelessProtein.txt")
    fruitfly_protein = read_protein("alg_FruitflyEyelessProtein.txt")
    scoring_matrix = read_scoring_matrix("alg_PAM50.txt")
    alignment_matrix = compute_alignment_matrix(human_protein, fruitfly_protein, scoring_matrix, False)

    local_alignment = compute_local_alignment(human_protein, fruitfly_protein, scoring_matrix, alignment_matrix)
    #print local_alignment
    human_optimal = local_alignment[1]
    fruitfly_optimal = local_alignment[2]
    
    similarity = calculate_percent_similar(human_optimal, fruitfly_optimal)
    print similarity

    #print len(human_protein)
    #print len(fruitfly_protein)

    random_1 = create_random_protein(alphabet, len(human_protein))
    random_2 = create_random_protein(alphabet, len(fruitfly_protein))

    random_alignment_matrix = compute_alignment_matrix(random_1, random_2, scoring_matrix, False)

    random_local_alignment = compute_local_alignment(random_1, random_2, scoring_matrix, random_alignment_matrix)
    #print local_alignment
    #human_optimal = local_alignment[1]
    #fruitfly_optimal = local_alignment[2]
    
    similarity = calculate_percent_similar(random_local_alignment[1], random_local_alignment[2])
    print similarity
    

    #print random_1
    #print random_2

def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):

    scoring_distribution = dict()
    
    for index in range(0, num_trials):

        rand_y_list = list(seq_y)
        #print seq_y
        #print "rand_y_list", rand_y_list
        random.shuffle(rand_y_list)
        rand_y = ""
        for char in rand_y_list:
            rand_y = rand_y + char
        #rand_y = str(rand_y_list)
        #print "rand_y", rand_y
        
        alignment_matrix = compute_alignment_matrix(seq_x, rand_y, scoring_matrix, False)
        local_alignment = compute_local_alignment(seq_x, rand_y, scoring_matrix, alignment_matrix)
        score = local_alignment[0]
        
        #scoring_distribution[index] = local_alignment[0]
        if (scoring_distribution.get(score) == None):
            scoring_distribution[score] = 1
        else:
            scoring_distribution[score] = scoring_distribution[score] + 1
            

    return scoring_distribution


def create_normal_distribution(distribution):

    normal_distribution = dict()


    key_sum = 0
    for key in distribution.keys():
        key_sum = key_sum + int(key)
    
    for key in distribution.keys():
        
        new_key = float(float(key) / float(key_sum))
        #print "key", int(key), "new_key", new_key
        normal_distribution[new_key] = distribution[key]

    return normal_distribution


def question4():
    """
    Write a function generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials) that takes as input two sequences
    seq_x and seq_y, a scoring matrix scoring_matrix, and a number of trials num_trials. This function should return a
    dictionary scoring_distribution that represents an un-normalized distribution generated by performing the following
    process num_trials times: • Generate a random permutation rand_y of the sequence seq_y using random.shuffle().
    Compute the maximum value score for the local alignment of seq_x and rand_y using the score matrix scoring_matrix.
    Increment the entry score in the dictionary scoring_distribution by one.

    Use the function generate_null_distribution to create a distribution with 1000 trials using the protein sequences
    HumanEyelessProtein and FruitflyEyelessProtein (using the PAM50 scoring matrix). Important: Use HumanEyelessProtein
    as the first parameter seq_x (which stays fixed) and FruitflyEyelessProtein as the second parameter seq_y (which is
    randomly shuffled) when calling generate_null_distribution. Switching the order of these two parameters will lead to
    a slightly different answers for question 5 that may lie outside the accepted ranges for correct answers.
    """

    human_protein = read_protein("alg_HumanEyelessProtein.txt")
    fruitfly_protein = read_protein("alg_FruitflyEyelessProtein.txt")
    scoring_matrix = read_scoring_matrix("alg_PAM50.txt")
    
    distribution = generate_null_distribution(human_protein, fruitfly_protein, scoring_matrix, 1000)
    print distribution

    # Let's save this out!
    #file = open("newfile.txt", "w")
    #file.write(distribution)
    #file.write("and another line\n")
    #file.close()

    normal_distribution = create_normal_distribution(distribution)
    #print normal_distribution

    dummy_list_keys = list(normal_distribution.keys())
    dummy_list_keys.sort()
    #print dummy_list_keys
    dummy_list_values = list([])
    for key in dummy_list_keys:
        dummy_list_values.append(normal_distribution[key])
    #print dummy_list_values

    import numpy as np
    import matplotlib.pyplot as plt
 
    n_groups = len(dummy_list_keys)
 
    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8
 
    rects1 = plt.bar(index, dummy_list_values, bar_width,
                 alpha=opacity,
                 color='b',
                 label='foo')
 
    #rects2 = plt.bar(index + bar_width, means_guido, bar_width,
    #             alpha=opacity,
    #             color='g',
    #             label='Guido')
 
    plt.xlabel('normalized local_alignment score')
    plt.ylabel('occurence')
    plt.title('normalized distribution of local_alignments')
    #plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))

    #plt.xticks(index + bar_width, normal_distribution.keys())
    #ax.set_xticklabels(dummy_list_keys, rotation=90 )

    plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off')

    plt.tight_layout()
    plt.show()


def test_edit_score(seq_x, seq_y):

    #seq_x = "kitten"
    #seq_y = "mitten" ## "kitteng" ## "sitting"
    #build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    scoring_matrix = build_scoring_matrix("abcdefghijklmnopqrstuvwxyz", 2, 1, 0)
    alignment_matrix = compute_alignment_matrix(seq_x, seq_y, scoring_matrix, True)
    #print scoring_matrix
    #print alignment_matrix
    global_alignment = compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
    #print global_alignment

    local_alignment = compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
    #print local_alignment

    calculated = len(seq_x) + len(seq_y) - global_alignment[0]
    print "seq_x", seq_x, "seq_y", seq_y, "optimal_x", global_alignment[1], "optimal_y", global_alignment[2], "length:", len(seq_x) + len(seq_y), "score:", global_alignment[0], "calculated:", calculated


def question7():

    test_edit_score("kitten", "kitten")
    test_edit_score("kitten", "mitten")
    test_edit_score("kitten", "kkitten")
    test_edit_score("kitten", "kittenk")
    test_edit_score("kitten", "sitting")


def check_spelling(checked_word, dist, word_list):
    """
    iterates through word_list and returns the set of all words that are within edit distance dist of the string checked_word.
    """
    
    matched_list = list([])
    scoring_matrix = build_scoring_matrix("abcdefghijklmnopqrstuvwxyz", 2, 1, 0)
    
    for word in word_list:

        alignment_matrix = compute_alignment_matrix(checked_word, word, scoring_matrix, True)
        global_alignment = compute_global_alignment(checked_word, word, scoring_matrix, alignment_matrix)
        score = len(checked_word) + len(word) - global_alignment[0]

        if (score <= dist):
            matched_list.append(word)

    return matched_list


def question8():

    word_list = read_words(WORD_LIST_URL)
    print len(word_list)
    print word_list[0]

    matched_list = check_spelling("humble", 1, word_list)
    print matched_list

    matched_list = check_spelling("firefly", 2, word_list)
    print matched_list


question8()

