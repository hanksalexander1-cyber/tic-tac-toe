import random


def garbage():
    if 0 > ask > 8:
        while True:
            ask = int(input("enter 0-8 -> "))
            if 8 >= ask >= 0:
                break 
        turns += 1
        while turns < 9:
            turns = 0
            tic = initialize_board()
            print_board(tic)
            pass

#board = [0,1,2,3,4,5,6,7,8]

def initialize_board():
    
    tic = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    return tic

def print_board(tic):
    print(f"{tic[0]} | {tic[1]} | {tic[2]} ")
    print(f"{tic[3]} | {tic[4]} | {tic[5]} ")
    print(f"{tic[6]} | {tic[7]} | {tic[8]} ")
        

def make_move(tic):
    while True:
        try:
            ask = int(input("Enter a position (0-8): "))
            if ask < 0 and ask > 8:
                print("Please choose a number between 0 and 8.")
                continue
            if str(tic[ask]) in ["X","O"]:
                print("Spot already taken. Try again.")
                continue
            return ask
        except ValueError:
            print("Invalid input. Please enter a number.")


def replace_number(tic, ask):
    """
    if tic[ask] == ask: It's taken
    """
    for i in range(9):
        if tic[i] == ask:
            tic[i] = "X"
            return True
    return False

def check_draw(tic):
    player_win = check_winner
    computer_win = check_winner
    tic == initialize_board
    if tic[0, -1] in ["X", "O"] and player_win == False and computer_win == False:
        print("board is full")
        end = 1
        while end != 1:
            break

def computer_move(tic):
    available_moves = [i for i in range(9) if isinstance(tic[i], int)]
    computer_guess = random.choice(available_moves)
    tic[computer_guess] = "O"
    print(f"computer selected {computer_guess}")
    return available_moves

def check_winner(tic):
    tic = initialize_board()
    player_win = False
    computer_win = False
    #player win statements
    if tic[0] == tic[1] == tic[2]:
        player_win = tic[0]
    elif tic[3] == tic[4] == tic[5]:
        player_win = tic[3]
    elif tic[6] == tic[7] == tic[8]:
        player_win = tic[6]
    # Columns
    elif tic[0] == tic[3] == tic[6]:
        player_win = tic[0]
    elif tic[1] == tic[4] == tic[7]:
        player_win = tic[1]
    elif tic[2] == tic[5] == tic[8]:
        player_win = tic[2]
    # Diagonals
    elif tic[0] == tic[4] == tic[8]:
        player_win = tic[0]
    elif tic[2] == tic[4] == tic[6]:
        player_win = tic[2]
        
    
    #computer win statements
    if tic[0] == "O" and tic[1] == "O" and tic[2] == "O" or tic[3] == "O" and tic[4] == "O" and tic[5] == "O" or tic[6] == "O" and tic[7] == "O" and tic[8] == "O":
        computer_win = True
    if tic[0] == "O" and tic[3] == "O" and tic[6] == "O" or tic[1] == "O" and tic[4] == "O" and tic[7] == "O" or tic[2] == "O" and tic[5] == "O" and tic[8] == "O":
        computer_win = True
    if tic[0] == "O" and tic[4] == "O" and tic[8] == "O" or tic[2] == "O" and tic[4] == "O" and tic[6] == "O":
        computer_win = True
        print("computer won the game")
    return player_win and computer_win

def play_game():
    tic = initialize_board()
    while True:
        ask = make_move(tic)
        replace_number(tic, ask)
        print_board(tic)
        computer_move(tic)
        print_board(tic)
        check_winner(tic)
        player_win = check_winner(tic)
        computer_win = check_winner
        if player_win == True:
            print("player won the game")
            break
        if computer_win == True:
            print("computer won the game")
            break

if __name__ == "__main__":
    play_game()





#CHANGE TO A 1D LIST LATER





