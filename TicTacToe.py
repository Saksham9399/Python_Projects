board = ['' for x in range(10)]

def insertLetter(letter, position):#letter can be X or O
    board[position] = letter

def spaceIsFree(position):
    return board[position] == ' '

def printBoard(board):
    print(' ' + board[1] +' | '+ board[2] + ' | '+ board[3])
    print('------------')
    print(' ' + board[4] +' | '+ board[5] + ' | '+ board[6])
    print('------------')
    print(' ' + board[7] +' | '+ board[8] + ' | '+ board[9])

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def isWinner(b,l):
    return((b[1]==l and b[2]==l and b[3]==l) or
    (b[4]==l and b[5]==l and b[6]==l) or
    (b[7]==l and b[8]==l and b[9]==l) or
    (b[1]==l and b[4]==l and b[7]==l) or
    (b[2]==l and b[5]==l and b[8]==l) or
    (b[3]==l and b[6]==l and b[9]==l) or
    (b[1]==l and b[5]==l and b[9]==l) or
    (b[3]==l and b[5]==l and b[7]==l))

def playerMove():
    run = True
    while run:
        move = input("Please enter a position to enter 'X' in between (1-9)")
        try:
            move = int(move)
            if move in range(1,10):
                if spaceIsFree(move):
                    run = False
                    insertLetter('X',move)
                else:
                    print('Sorry, this space is already occupied')
            else:
                print('Please enter a position between (1-9)')
        except:
            print("Please type a number")

def computerMove():
    possibleMoves =[x for x, letter in enumerate(board) if letter ==' ' and x != 0]
    move = 0

    for let in['0','X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(boardcopy,let):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen)> 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return 5

    edgesOpen =[]
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen)>0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(L):
    import random
    length= len(L)
    r= random.randrange(0,length)
    return L[r]

def main():
    print("Welcome to the game")
    printBoard(board)

    while not isBoardFull(board):
        if not isWinner(board,'O'):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, the computer won")
            break

        if not isWinner(board,'X'):
            move = computerMove()
            #if move == 0:
            #    print(" ")
            #else:
            insertLetter('O',move)
            print("Computer placed 'O' at position", move,":")
            printBoard(board)
        else:
            print("You Win")
            break

    if isBoardFull(board):
        print(" Game Tied")

while True:
    x= input("Do u want to play the game? ( Y / N )\n")
    if x.upper() == 'Y':
        board = [' ' for x in range(10)]
        print("-----------------------")
        main()
    else:
        print("Error!.........")
        break
