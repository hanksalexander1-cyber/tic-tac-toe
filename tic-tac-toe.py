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
    tic = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    return tic

def print_board(tic):
    for i in tic:
        print(*i)
        print("-------")
        

def make_move():
    try:
        ask = int(input("enter 0-8 -> "))
    except ValueError:
        print("not a number please retry")

    if not 0 <= ask <= 8:
        print("please select between 0-8")
    return ask


def replace_number(tic, ask):
    """
    if tic[ask] == ask: It's taken
    """
    for i in range(3):
        for j in range(3):
            if tic[i][j] == ask:
                tic[i][j]  = "X"
                return True
    return False


def computer_guess(tic):
    list = []
    index = 0
    for i in range(9):
        low = tic[index]
        if low == int:
            list.append(low)
        index += 1
    computer_guess = random.randint(list)
    print(computer_guess)


def main():
    tic = initialize_board()
    while True:
        ask = make_move()
        replace_number(tic, ask)
        print_board(tic)
        computer_guess(tic)
if __name__ == "__main__":
    main()





#CHANGE TO A 1D LIST LATER





