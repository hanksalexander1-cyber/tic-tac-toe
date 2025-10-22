import random


def initialize_board():
    """
    initializes the board
    """
    
    tic = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    return tic

def print_board(tic):
    """
    prints the board
    """
    print(f"{tic[0]} | {tic[1]} | {tic[2]} ")
    print("----------")
    print(f"{tic[3]} | {tic[4]} | {tic[5]} ")
    print("----------")
    print(f"{tic[6]} | {tic[7]} | {tic[8]} ")
        

def make_move(tic):
    """
    has the user enter where they want to go and checks if it is possible
    """
    while True:
        try:
            ask = int(input("Enter a position (0-8): "))
            if ask < 0 and ask > 8:
                print("Please choose a number between 0 and 8.")
                continue
            if str(tic[ask]) in ["X","O"]:
                print("spot is taken, try again")
                continue
            return ask
        except ValueError:
            print("Invalid input, Please enter a number.")


def replace_number(tic, ask):
    """
    replaces the tic index that is equal to ask with an X
    """
    for i in range(9):
        if tic[i] == ask:
            tic[i] = "X"
            return True
    return False

def check_draw(tic):
    """
    checks if the board is full
    """
    tic == initialize_board
    return all(isinstance(spot, str) for spot in tic)

def computer_move(tic):
    """
    gives the computer a list of possible moves from the non selected intergers
    """
    available_moves = [i for i in range(9) if isinstance(tic[i], int)]
    computer_guess = random.choice(available_moves)
    tic[computer_guess] = "O"
    print(f"computer selected {computer_guess}")
    return available_moves


def check_winner(tic):
    """
    checks weather the user or the computer won
    """
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
        ]
    
    for combo in win_combos:
        a, b, c = combo
        if tic[a] == tic[b] == tic[c]:
            return tic[a]
    return None

def retry():
    """
    asks if the user wants to retry and if so restards the code over again
    """
    retrying = input("if you want to play again enter either yes or no: ->").strip().lower()
    while retrying != "no" and retrying != "yes":
        print("you did not enter yes or no")
        retrying = input("if you want to play again enter either yes or no: ->").strip().lower()
    if retrying == "yes":
        play_game()
        

    

def play_game():
    """
    main code that ties everything together
    """
    tic = initialize_board()
    while True:
        print_board(tic)
        ask = make_move(tic)
        replace_number(tic, ask)
        winner = check_winner(tic)
        if winner == "X":
            print_board(tic)
            print("player won the game")
            break
        if check_draw(tic):
            print_board(tic)
            print("draw")
            break
        computer_move(tic)
        winner = check_winner(tic)
        if winner == "O":
            print_board(tic)
            print("computer won the game")
            break
        if check_draw(tic):
            print_board(tic)
            print("draw")
            break
    retry()

if __name__ == "__main__":
    play_game()





