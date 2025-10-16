import random
def computer_guess(tic):
    available_moves = []
    for i in range(9):
        if isinstance(tic[i], int): 
            available_moves.append(i)
    print(available_moves)

tic = [
    [0, 1, 2],
    [3, "X", 5],
    [6, 7, 8]
]

computer_guess(tic)