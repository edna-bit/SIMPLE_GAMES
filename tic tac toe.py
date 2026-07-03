board= ["-", "-", "-", #makes an array where characters will be
        "-", "-", "-",
        "-", "-", "-"]



winner = None #just to set the winner to None at the start of the game (make the variable)
player1 = "X" #whos turn it is
still_playing = True #to check if the game is still going on or not



def display_board(): #displays the board in a 3x3 format
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
 
    display_board()
    while still_playing:
        handle_turn(player1)
        check_if_game_over()  # if game is over stop the loop
        if still_playing:
            flip_player()
    # when game has ended 
    if winner== "X" or winner== "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")
 


def handle_turn(player1):
    position = input(f"Player {player1}, choose a position from 1-9: ")
   
    valid = False
    while not valid: 
         # while the position is not valid from 1-9, ask the player to choose again
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input(f"Player {player1}, choose a position from 1-9: ")
            
        position = int(position) - 1
        
        # check to see if the position is not empty ("-") and if it is not, ask the player to choose again
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")
            
    board[position] = player1

    display_board()


    
def check_if_game_over():
    check_for_win()
    check_for_tie()


def check_for_win():
    global winner, still_playing 
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    winner = row_winner or column_winner or diagonal_winner
    if winner:
        still_playing = False


def check_rows():
    global still_playing
    #if the row is all the same but not "-" then it will return the winner
    row_1 = board[0] == board[1] == board[2] != "-" 
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
     still_playing = False
     #returns the value of the game winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    #if the column is all the same but not "-" then it will return the winner
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        still_playing = False
        #returns the value of the game winner (X or O)
    if column_1:    
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    #if the diagonal is all the same but not "-" then it will return the winner
    if board[0] == board[4] == board[8] != "-":
        return board[0]
    if board[2] == board[4] == board[6] != "-":
        still_playing = False
        #returns the value of the game winner (X or O)
        if diagonal_1:
            return board[0]
        elif diagonal_2:
            return board[2]
    return


def check_for_tie():
    global still_playing
    if "-" not in board:
        still_playing = False
        return

def flip_player():
    global player1
    if player1 == "X": #this is to check if the player is X then it will be O's turn
        player1 = "O"
    elif player1 == "O": #this is to check if the player is O then it will be X's turn
        player1 = "X"    
    return
   

play_game()