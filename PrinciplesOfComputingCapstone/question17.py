
def take_a_turn(board):

    x = 5


def pick_a_number(board):
    #print board
    if len(board) < 2:
        print "ERROR!"
        return

    if len(board) == 2:
        if board[0] > board[1]:
            return (board[0], board[1])
        else:
            return (board[1], board[0])

    # let's do some game theory here.
    # let's see what happens if i always pick the first one.

    #pick_left = board[0]

    # from the left
    player1_score_left = board[0]
    rest_after_pick_left = board[1:]
    go_after_pick_left = pick_a_number(rest_after_pick_left)
    #print "left", player1_score_left, rest_after_pick_left, go_after_pick_left
    player1_score_left = player1_score_left + go_after_pick_left[1]
    player2_score_left = go_after_pick_left[0]

    # from the right
    player1_score_right = board[len(board)-1]
    rest_after_pick_right = board[0:-1]
    #print "player1_score_right"
    go_after_pick_right = pick_a_number(rest_after_pick_right)
    #print "right", player1_score_right, rest_after_pick_right, go_after_pick_right
    player1_score_right = player1_score_right + go_after_pick_right[1]
    player2_score_right = go_after_pick_right[0]

    if player1_score_left >= player1_score_right:
        return (player1_score_left, player2_score_left)
    else:
        return (player1_score_right, player2_score_right)

    return (player1_score, player2_score)


#print pick_a_number([3, 5, 2, 1])
print pick_a_number([12, 9, 7, 3, 4, 7, 4, 3, 16, 4, 8, 12, 1, 2, 7, 11, 6, 3, 9, 7, 1])
#my_list = [5, 6, 7]
#print my_list[len(my_list)-1]

