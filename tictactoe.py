#Tic-Tac-Toe
import random 
def drawBoard(board):
    def inputPlayerLetter(X):
        letter = 'X'
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
# both X and O cannot win. they are in a draw
        board = {'O', 'X', 'X', 
                   'O', 'X', 'X', 
                   'O', 'O', 'X'};

# board shows X has won
board = {'X', 'O', 'X', 
         'X', 'O', 'O', 
         'X', 'X', 'O'};

# board shows O has won
board = {'O', 'X', 'O', 
         'O', 'X', 'X', 
         'O', 'O', 'X'};

# rest board where game is not finished
board = {'O', 'X', '', 
         '', '', '', 
         '', '', ''};

# Step 2: Write a move function that accepts the string with the game board
def move(board, mark, position):
    move = ''
    while move in '0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19'.split():
        move = input()
        return int(move)
    
    # Step 3. a player_move function that accepts a string with the game board.
    def getPlayerMove(board):
        move = ''
        while move not in '0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10'. split() or not 'isSpaceFree' (board, int(move)):
            print('What is your next move?, (0-10)')
            move = input()
            return int(move)
        
        # Step 4 computer move. for this case, The first element in the list is the player's letter; the second is the computer's letter.
        def inputPlayerLetter():
            letter = ''
            while not (letter == 'X' or letter == 'O'):
                print('Do you want to be X or O?')
                letter = input().upper()
                if letter == 'X':
                    return ['X', 'O']
                else:
                    return ['O', 'X']


    def getComputerMove(board, computerLetter):
            if computerLetter == 'X':
                playerLetter = 'O'
            else:
                playerLetter = 'X'
                move = 'chooseRandomMoveFromList', (board), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19,]
                if move != None:
                    return move
                
   # Step 5   function that creates a string with a game board and alternately calls the player_move and pc_move functions until someone wins or draws
print('Welcome to Tic-Tac-Toe!')
while True:
    theBoard = [' '] *10
    playerLetter, computerLetter = inputPlayerLetter.()
    turn = whoGoesFirst.()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True                   

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
                else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
                    
            else:
                move = getComputerMove(theBoard, computerLetter)
makeMove(theBoard, computerLetter, move)
if isWinner(theBoard, computerLetter):
 drawBoard(theBoard)
 print('The computer has beaten you! You loose.')
 gameIsPlaying = False
else:
       if isBoardFull(theBoard)
       drawBoard(theBoard)
       print('The game is a tie!')
break 

else:
turn = 'player'   
print('Do you want to play again? (yes or no)')
if not input().lower().startswith('y'):
    break