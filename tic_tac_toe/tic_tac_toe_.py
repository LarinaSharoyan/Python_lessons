def play_with():
    qst = input("""Would you prefer to play with:
            1. Computer
            2. Friend
    Your answer: """)
    return qst.lower()

def check_tie(b):
    for i in b:
        for j in i:
            if j == 0:
                return False
    return True

def x(board):
    while True:
        x = input("Enter row and column (e.g. 01, 22): ")
        if len(x) == 2 and int(x[0]) <= 2 and int(x[1]) <= 2:
            row = int(x[0])
            column = int(x[1])
            if board[row][column] != 0:
                print("That field is busy, please choose another one.")
            else:
                board[row][column] = 1
                break
        else:
            print("You should type here only two numbers: row and column(e.g. 01, 22).")
    return board

def o_friend(board):
    while True:
        o = input("Enter row and column (e.g. 01, 22): ")
        if len(o) == 2 and int(o[0]) <= 2 and int(o[1]) <= 2:
            rowo = int(o[0])
            columno = int(o[1])
            if board[rowo][columno] != 0:
                print("That field is busy, please choose another one.")
            else:
                board[rowo][columno] = 2
                break
        else:
            print("You should type here only two numbers: row and column(e.g. 01, 22).")
    return board

def check_corners(b):
    c1 = b[0][0] == b[1][1] == b[2][2] == 1
    c2 = b[0][2] == b[1][1] == b[2][0] == 1
    return c1 or c2

def check_comb(b, number):
    if check_corners(b):
        return True
    else:
        for i in range(len(b)):
            if b[i] == [number, number, number]:
                return True
            lst = []
            for j in range(len(b[i])):
                lst.append(b[j][i])
            if lst == [number, number, number]:
                return True
    return False

def print_board(board):
    for i in board:
        line = ""
        for j in i:
            if j == 0:
                line += "_ "
            elif j == 1:
                line += "X "
            else:
                line += "O "
        print(line)

def o_computer(board):
    import random
    directions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                directions.append(f"{i}{j}")
    random.shuffle(directions)
    r = int(directions[0][0])
    c = int(directions[0][1])
    board[r][c] = 2
    return board

def computer():
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print_board(board)
    while True:
        board = x(board)
        print_board(board)
        if check_comb(board, 1):
            return "Winner: X"
        elif check_tie(board):
            return "It's a tie"
        board = o_computer(board)
        print_board(board)
        if check_comb(board, 2):
            return "Winner: O"
        elif check_tie(board):
            return "It's a tie"

def friend():
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print_board(board)
    while True:
        board = x(board)
        print_board(board)
        if check_comb(board, 1):
            return "Winner: X"
        elif check_tie(board):
            return "It's a tie"
        board = o_friend(board)
        print_board(board)
        if check_comb(board, 2):
            return "Winner: O"
        elif check_tie(board):
            return "It's a tie"

def main():
    mode = play_with()
    if mode == "computer":
        print(computer())
    elif mode == 'friend':
        print(friend())
    else:
        print("No such mode for this game")

        

main()
