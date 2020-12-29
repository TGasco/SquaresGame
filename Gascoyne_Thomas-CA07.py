#Student ID: 201419827      Gascoyne_Thomas-CA07.py
#December 2019
#Program to play an interactive game of 'squares' against a CPU opponent


#Global vars and importing necessary modules
from random import randint
from time import sleep
End = False
Play = True

def main():
    global Play
    global End
    while Play == True: #Handles replays of game until user specifies otherwise
        Difficulty = int(input("Select your difficulty:\n"
                               "\t1: Easy\n"
                               "\t2: Medium\n"
                               "\t3: Hard\n"
                               ))
        GameBoard = MatrixInit()
        PrintBoard(GameBoard)
        Count = 1
        while End == False: #Handles loop needed for the turns
            print("\nTurn",str(Count) +":\n")
            Player1Turn(GameBoard)
            if End == False:
                CPUTurn(GameBoard, Difficulty)
            else:
                pass
            Count += 1
            
        PlayAgain()
        
    return


#Function initialises 2d-array (7x7 to account for the numbering of rows/cols
#and extra space to allow the square detection algorithm to work)
def MatrixInit():
    Count = 1
    Board = [[0] * 7 for i in range(7)]
    for i in range(5):
        Board[0][Count] = Count
        Board[Count][0] = Count
        Count += 1

    return Board


#Handles the User's (player 1's) turn
def Player1Turn(GameBoard):
    Player = "Player 1"
    print("\nIts your turn...")
    sleep(0.5)
    P1Col = int(input("\nEnter a column (Numbered 1-5): "))
    P1Row = int(input("Enter a row (Numbered 1-5): "))
    
    while GameBoard[P1Row][P1Col] != 0:
        print("Square is occupied - try again")
        P1Col = int(input("\nEnter a column (Numbered 1-5): "))
        P1Row = int(input("Enter a row (Numbered 1-5): "))
    GameBoard[P1Row][P1Col] = 1
    PrintBoard(GameBoard)       
    Row = P1Row
    Col = P1Col
    FullBoard(GameBoard)
    Square(GameBoard, Row, Col, Player)
    
    return GameBoard


#Handles the CPU (Player 2) turn
def CPUTurn(GameBoard, Difficulty):
    global End
    if End == False:
        FullBoard(GameBoard)
        Player = "CPU"
        print("\nPlayer 2 is thinking...\n")
        sleep(1)
        for i in range(Difficulty):
            if End == False:
                P2Col = randint(1,5)
                P2Row = randint(1,5)
                while GameBoard[P2Row][P2Col] == 2:
                    P2Col = randint(1,5)
                    P2Row = randint(1,5)
                GameBoard[P2Row][P2Col] = 2
                print("CPU chose co-ordinates (",P2Col,",",P2Row,")\n")

                Row = P2Row
                Col = P2Col
                
                Square(GameBoard, Row, Col, Player)
                FullBoard(GameBoard)
            else:
                pass
        PrintBoard(GameBoard)
    else:
        pass
    
    return GameBoard


#Checks adjacent tiles from most recent move to see if a square is formed
def Square(GameBoard, Row, Col, Player):
    global End
    if Player == "Player 1":
        x = 1
    else:
        x = 2
        
    if (GameBoard[Row+1][Col] == x and
    GameBoard[Row][Col+1] == x and
    GameBoard[Row+1][Col+1] == x
        ):
        print(Player,"Wins!")
        End = True
        
    elif (GameBoard[Row-1][Col] == x and
    GameBoard[Row][Col-1] == x and
    GameBoard[Row-1][Col-1] == x
        ):
        print(Player,"Wins!")
        End = True
        
    elif (GameBoard[Row-1][Col] == x and
    GameBoard[Row-1][Col+1] == x and
    GameBoard[Row][Col+1] == x
        ):
        print(Player,"Wins!")
        End = True

    elif (GameBoard[Row+1][Col] == x and
    GameBoard[Row+1][Col-1] == x and
    GameBoard[Row][Col-1] == x
        ):
        print(Player,"Wins!")
        End = True

    else:
        pass
    
    return End


#Asks user whether they would like to play 'Squares' again
def PlayAgain():
    Error = True
    while Error == True:
        
        Again = input("Would you like to play again? Y/N: ")
        if Again.upper() == "N":
            global Play
            Play = False
            Error = False
        elif Again.upper() == "Y":
            global End
            End = False
            Error = False
        else:
            print("Invalid input - please enter Y or N")
            Error = True
            
    return


#Function checks whether the board is full (no 0's left) to end game
def FullBoard(GameBoard):
    global End
    Full = True
    Row = 1
    for i in range(5):
        Col = 1
        for j in range(5):
            if GameBoard[Row][Col] == 0:
                Full = False
            else:
                pass
            Col += 1
        Row += 1
    if Full == True:
        print("CPU wins!")
        End = True
    else:
        pass
    return
        
                
#Function to visualise the Game Board 
def PrintBoard(GameBoard):
    print()
    for row in range(len(GameBoard)-1):
        for column in range(len(GameBoard[row])-1):
            print(GameBoard[row][column],end="   ")
        print("\n")
    return



main()
exit()
