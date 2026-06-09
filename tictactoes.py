board = [" "," "," "," "," "," "," "," "," "," "]
def drawboard():
    print(board[1], " |", board[2],"|", board[3])
    print("---+---+---")
    print(board[4], " |",  board[5], "|",  board[6])
    print("---+---+---")
    print(board[7], " |",  board[8], "|",  board[9])

def checkWin(mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    if board[1] == board[5] == board[6] == mark:
        return True
    if board[7] == board[5] == board[3] == mark:
        return True    
# drawboard()

def checkDraw(mark):
    if board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[5] != " " and board[6] != " " and board[7] != " " and board[8] != " " and board[9] != " ":
        return True

player = 1
count = 0


while True:
    drawboard()
    if player == 1:
        mark = "X"
    else:
        mark = "O"

    pos = int(input("Enter Pos (1-9)"))
    if(board[pos] == " "):
        board[pos] = mark
        count = count + 1 
        # Check if win or not 
        if(checkWin(mark)):
            drawboard()
            print("Player",player, "Won")
            break
        
        # if(checkDraw(mark) == False):
        #     drawboard()
        #     print("Game Draw")
        #     break

        if count == 9:
            print("Draw")
            break

        if player == 1:
            player = 2
        else:
            player = 1

        
    

    elif board[pos] != " ":
        print("Position not available")

