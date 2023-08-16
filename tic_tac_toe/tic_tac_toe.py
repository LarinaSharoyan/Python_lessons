board = [
        [0, 0, 0], 
        [0, 0, 0],
        [0, 0, 0]
]
qst = input("""Would you prefer to play with:
        1. Computer
        2. Friend
        """)
if qst.lower() == 'computer':
    print("fddkhiod")
for i in range(5):
    x = input("Enter column and row: ")
    row = int(x[0])
    column = int(x[1])
    print(x[row][column])
    if x[row][column] != 0:
        print("that field is busy")
    else:
        x[row][column] = 1
    print(board)
