from random import randint
opponent = randint(1,9)

print("***** This is a game played by two players. \nThey are both given the chance to choose a stand in a Tic Tac Toe board, one at a time. \nA chosen stand cannot be chosen again by any of the players *****\n\n\n")
board = [1,2,3,
        4,5,6,
        7,8,9] # This is the board that controls the game

def show():   # This function displays the board of the Tic Tac Toe game
    print("\n",board[0],board[1],board[2])
    print(" -----")
    print("",board[3],board[4],board[5])
    print(" -----")
    print("",board[6],board[7],board[8],"\n")
show()



def Firstplayer():
    player1 = int(input("Player one, enter the position of your choice: "))
    if board[player1-1] != 'x':
        if player1<1 or player1>9:#This range has been affected because of the previous if condition
            print("This is an invalid stand, try again")
        if 1<=player1<=9:
            board[player1-1] = 'x'
    elif board[player1-1]== 'x':
        print("Error! This stand is already chosen")
    show()

def Secondplayer():
    player2 = int(input("Player two, enter the position of your choice: "))
    if  board[player2-1] != 'o':
        if player2<1 or player2>9:#This range has been affected because of the previous if condition
            print("This is an invalid stand, try again")
        if 1<=player2<=9:
            board[player2-1] = 'o'
    elif board[player2-1] == 'o':
        print("Error! This stand is already chosen")
    show()

def main(): # This function runs the whole game itself
    while True:
        Firstplayer()
        Secondplayer()

main()
    
