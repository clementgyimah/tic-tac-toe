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



##def winner():
##    if board[0]=='x' and board[1]=='x' and board[2]=='x':
##        print("Congratulation !!!  You are the winner")
##    if board[0]=='x' and board[3]=='x' and board[7]=='x':
##        print("Congratulation !!!  You are the winner")
##    if board[3]=='x' and board[6]=='x' and board[9]=='x':
##        print("Congratulation !!!  You are the winner")
##    if board[7]=='x' and board[8]=='x' and board[9]=='x':
##        print("Congratulation !!!  You are the winner")
##    if board[0]=='x' and board[4]=='x' and board[9]=='x':
##        print("Congratulation !!!  You are the winner")

indicator = ['x','o']

def main(): # This function runs the whole game itself
    while True:
        player1 = int(input("Player one, enter the position of your choice: "))

##        if board[player1] == indicator[0]:
##            print("error movement, this position has been taken already")
        if player1<1 or player1>9:
            print("This is an invalid stand")
        if 1<=player1<=9:
            board[player1-1] = indicator[0]
        show()
        player2 = int(input("Player two, enter the position of your choice: "))
##        if board[player2] == indicator[1]:
##            print("error movement, this position has been taken already")
        if player2<1 or player2>9:
            print("This is an invalid stand")
        if 1<=player2<=9:
            board[player2-1] = indicator[1]
        show()
main()
