import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input("Enter row-1 or 2 or 3:"))
        col=int(input("Enter column-1 or 2 or 3:"))
        if(row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-'):
            break
        else:
            print("Invalid input!!Please enter again!!")
            continue
    board[row-1][col-1]=symbol
def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if(board[r][c]==symbol):
                count+=1
        if(count==3):
            print(numpy.matrix(board))
            print(symbol," won!!")
            return True
    return False
def check_cols(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if(board[r][c]==symbol):
                count+=1
        if(count==3):
            print(numpy.matrix(board))
            print(symbol," won!!")
            return True
    return False
def check_diagonals(symbol):
    diag1 = 0
    for r in range(3):
        for c in range(2,-1,-1):
            if(r+c==2 and board[r][c]==symbol):
                diag1+=1
    diag2 = 0
    for r in range(3):
        for c in range(3):
            if(r==c and board[r][c]==symbol):
                diag2+=1
    if(diag1==3 or diag2==3):
        print(numpy.matrix(board))
        print(symbol," won!!")
        return True
    return False
def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)
def play():
    for turn in range(9):
        if(turn%2==0):
            print('X turn!!')
            place(p1s)
            if(won(p1s)):
                return
        else:
            print('O turn!!')
            place(p2s)
            if (won(p2s)):
                return
    if(not(won(p1s)) and not(won(p2s))):
        print("Draw!!")
p1s='X'
p2s='O'
play()