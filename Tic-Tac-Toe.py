#======================================================================
# File: TicTacToe           Creator: Tudor Mironovici   tcm26@njit.edu
#
# Purpose: Lets two users play tic-tac-toe using the numpad
#======================================================================
import random
import turtle

#------Global Variables------
s = turtle.Screen()
t = turtle.Turtle()
t.speed(1000)
gameWon = False
inputText = ""
inputs = []
player1Name = ""
player1Color = [0.0,0.0,0.0]
player1Mark = ''
player2Name = ""
player2Color = [0.0,0.0,0.0]
player2Mark = ''
colorInUse = ""
codeInUse = [2.0,2.0,2.0]
winner = ""
turn = 0
correction = 0
gridLayout = [['A','A','A'],
              ['A','A','A'],
              ['A','A','A']]
#----------------------------



#-------------------
# Sets up the grid.
#-------------------
def setGrid(t):
    t.pencolor(0.0,0.0,0.0)
    t.up()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.down()
    t.forward(300)
    t.backward(600)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.backward(600)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.backward(600)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.backward(600)
    t.right(90)
    t.up()
    t.forward(100)
    t.left(90)
    t.forward(300)
    t.left(90)

    
#--------------------------
# Gets the names and color
# of both players.
#--------------------------
def preferences():
    #------Variables------
    global t
    global inputText
    global inputs
    global player1Name
    global player1Color
    global player2Name
    global player2Color
    inputChoice = ''
    player2NameSame = True
    #---------------------

    # Switches from numpad mode to keyboard mode
    inputChoice = str(input("Do you have a numpad available to use? (y/n) ")).lower()
    while (inputChoice != 'y' and inputChoice != 'n'):
        inputChoice = str(input("Please enter 'y' or 'n' ")).lower()
    if (inputChoice == 'n'):
        inputText = "Q W E\nA S D\nZ X C"
        inputs = ['Z','X','C','A','S','D','Q','W','E']
    elif (inputChoice == 'y'):
        inputText = "7 8 9\n4 5 6\n1 2 3"
        inputs = ['1','2','3','4','5','6','7','8','9']
    print("You will be using the following keys to place your marks on the grid:\n"+inputText)
                
            
    player1Name = str(input("Player one, what's your name? "))
    colorName = str(input("(Available colors: 'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'. You can also type in 'custom' if you want to input your own RGB values)\nWhat color do you want to be represented by? "))
    player1Color = colorParse(t,colorName)

    player2Name = str(input("Player two, what's your name? "))
    while (player2NameSame):
        if (player1Name == player2Name):
            player2Name = str(input("Sorry, can't have the same name as player one. Please enter a different name: "))
        else:
            player2NameSame = False
    colorName = str(input("What color do you want to be represented by? "))
    player2Color = colorParse(t,colorName)
    
    
#---------------------------------
# Puts the user's "color" input
# in terms turtle can understand.
#---------------------------------
def colorParse(t,colorName):
    #----Variables----
    global colorInUse
    global codeInUse
    colorOK = False
    #-----------------
    
    while True:
        colorName = colorName.lower()
        if (colorName == colorInUse):
            colorName = str(input(player1Name+" is already using this color. Please enter a different color: ")).lower()
            
        elif (len(colorName) == 0):
            colorName = str(input("Please enter a color: ")).lower()
            
        elif (colorName == "red"):
            colorInUse = "red"
            return [1.0,0.0,0.0]
        
        elif (colorName == "orange"):
            colorInUse = "orange"
            return [1.0,0.5,0.0]
        
        elif (colorName == "yellow"):
            colorInUse = "yellow"
            return [1.0,1.0,0.0]
        
        elif (colorName == "green"):
            colorInUse = "green"
            return [0.0,1.0,0.0]
        
        elif (colorName == "blue"):
            colorInUse = "blue"
            return [0.0,0.0,1.0]
        
        elif (colorName == "indigo"):
            colorInUse = "indigo"
            return [.29,0.0,.51]
        
        elif (colorName == "violet"):
            colorInUse = "violet"
            return [.93,.51,.93]

        elif (colorName == "custom"):
            while (colorOK == False):
                try: 
                    r = float(input("R: "))/255.0
                    g = float(input("G: "))/255.0
                    b = float(input("B: "))/255.0
                    t.pencolor(r,g,b)
                    if (r == codeInUse[0] and g == codeInUse[1] and b == codeInUse[2]):
                        colorName = str(input(player1Name+" is already using this color. Please enter a different color: ")).lower()
                    else:
                        codeInUse = [r, g, b]
                        return [r, g, b]
                    colorOK = True
                except:
                    print("This color isn't a standard RGB color. Please enter numbers from 0 to 255 (inclusive)")
                
        
        else:
            colorName = str(input("That's not one of the available colors. Please check above to see which colors are available\nWhat color do you want to be represented by? ")).lower()


#----------------------------------
# Chooses which player goes first.
#----------------------------------
def flipCoin():
    #------------Variables-------------
    global turn
    global correction
    global player1Mark
    global player2Mark
    tempInputOK = False
    chosenPlayer = random.randint(1,2)
    #----------------------------------
    
    if (chosenPlayer == 1):
        turn = 1
        tempInput = str(input(player1Name+", you get to go first! do you want to be 'X' or 'O'? ")).upper()
        while (tempInputOK == False):
            if (tempInput != 'X' and tempInput != 'O'):
                tempInput = str(input("Please enter 'X' or 'O' ")).upper()
            else:
                player1Mark = tempInput
                tempInputOK = True
        player1Mark = tempInput

        # Sets the other player's mark to be the opposite
        if (tempInput == 'X'):
            player2Mark = 'O'
        else:
            player2Mark = 'X'
        
    else:
        correction = 1
        tempInput = str(input(player2Name+", you get to go first! do you want to be 'X' or 'O'? ")).upper()
        while (tempInputOK == False):
            if (tempInput != 'X' and tempInput != 'O'):
                tempInput = str(input("Please enter 'X' or 'O' ")).upper()
            else:
                player1Mark = tempInput
                tempInputOK = True
        player2Mark = tempInput

        # Sets the other player's mark to be the opposite
        if (tempInput == 'X'):
            player1Mark = 'O'
        else:
            player1Mark = 'X'
    
    print("To choose a location for your marks, enter the key on your keyboard corresponding to the location on the grid.")


#--------------------------------
# Moves the turtle to the user's
# input location and draws the
# appropriate mark.
#--------------------------------
def placeMark(t,turn):
    #-----Variables-----
    locationNum = 0
    tempLocation = [0,0]
    #-------------------
    while True:
        try: 
            if (turn%2 == 1):
                locationNum = str(input(player1Name+", where would you want to place your "+player1Mark+"? ")).upper()
                tempLocation = parseLocation(player1Mark,locationNum)
                moveTo(t,tempLocation)
                if (player1Mark == 'X'):
                    X(t,player1Color)
                else:
                    O(t,player1Color)
            
            else:
                locationNum = str(input(player2Name+", where would you want to place your "+player2Mark+"? ")).upper()
                tempLocation = parseLocation(player2Mark,locationNum)
                moveTo(t,tempLocation)
                if (player2Mark == 'X'):
                    X(t,player2Color)
                else:
                    O(t,player2Color)

            backFrom(t,tempLocation)
            break
        except:
            # Usually happens if the position is typed before the input statement is done printing
            print("Woops, something went wrong. Please try again.")


#----------------------------------
# Puts the user's "location" input
# in terms turtle can understand.
#----------------------------------
def parseLocation(mark,locationNum):
    #-----Variables-----
    global gridLayout
    global inputs
    global inputText
    tempLocation = [0,0]
    #-------------------
    
    while True:
        if locationNum not in inputs:
            locationNum = str(input("Your available options are:\n"+inputText+"\n")).upper()
            continue
        elif (locationNum == inputs[0]):
            tempLocation = [2,0]
        elif (locationNum == inputs[1]):
            tempLocation = [2,1]
        elif (locationNum == inputs[2]):
            tempLocation = [2,2]
        elif (locationNum == inputs[3]):
            tempLocation = [1,0]
        elif (locationNum == inputs[4]):
            tempLocation = [1,1]
        elif (locationNum == inputs[5]):
            tempLocation = [1,2]
        elif (locationNum == inputs[6]):
            tempLocation = [0,0]
        elif (locationNum == inputs[7]):
            tempLocation = [0,1]
        else:
            tempLocation = [0,2]

        #----------------------------------
        # Checks if the position is taken.
        #----------------------------------
        if (gridLayout[tempLocation[0]][tempLocation[1]] != 'A'):
            locationNum = str(input("This spot is already taken up. Please chose an empty spot: ")).upper()
        else:
            gridLayout[tempLocation[0]][tempLocation[1]] = mark
            return tempLocation


#----------------------------------------
# Moves the turtle to the grid position.
#----------------------------------------
def moveTo(t,tempLocation):
    # Moves between colums 
    if (tempLocation[1] == 0):
        t.backward(200)
    elif (tempLocation[1] == 2):
        t.forward(200)
        
    # Moves between rows
    if (tempLocation[0] == 0):
        t.left(90)
        t.forward(200)
        t.right(90)
    elif (tempLocation[0] == 2):
        t.right(90)
        t.forward(200)
        t.left(90)


#--------------------------------------
# Moves the turtle back to the origin. 
#--------------------------------------
def backFrom(t,tempLocation):
    # Moves between columns
    if (tempLocation[1] == 0):
        t.forward(200)
    elif (tempLocation[1] == 2):
        t.backward(200)

    # Moves between rows
    if (tempLocation[0] == 0):
        t.right(90)
        t.forward(200)
        t.left(90)
    elif (tempLocation[0] == 2):
        t.left(90)
        t.forward(200)
        t.right(90)


#-------------------------
# Handles drawing an 'X'.
#-------------------------
def X(t,color):
    t.down()
    t.pencolor(color[0],color[1],color[2])
    t.right(45)
    t.forward(80)
    t.backward(160)
    t.forward(80)
    t.left(90)
    t.forward(80)
    t.backward(160)
    t.forward(80)
    t.right(45)
    t.up()


#-------------------------
# Handles drawing an 'O'.
#-------------------------
def O(t,color):
    t.right(90)
    t.forward(65)
    t.left(90)
    t.down()
    t.pencolor(color[0],color[1],color[2])
    t.circle(65)
    t.up()
    t.left(90)
    t.forward(65)
    t.right(90)


#-----------------------------
# Goes through all the 
# possible winning positions.
#-----------------------------
def checkIfWon():
    #----Variables----
    global gridLayout
    global winner
    #-----------------
    
    for row in range(len(gridLayout)):
        if (gridLayout[row][0] == 'X' or gridLayout[row][0] == 'O') and ((gridLayout[row][0] == gridLayout[row][1]) and (gridLayout[row][1] == gridLayout[row][2])):
            
            if (gridLayout[row][0] == player1Mark):
                winner = player1Name
            else:
                winner = player2Name
            return True
        
    for column in range(len(gridLayout[0])):
        if (gridLayout[0][column] == 'X' or gridLayout[0][column] == 'O') and (gridLayout[0][column] == gridLayout[1][column]) and (gridLayout[1][column] == gridLayout[2][column]):
            if (gridLayout[0][column] == player1Mark):
                winner = player1Name
            else:
                winner = player2Name
            return True

    # Also checks for the cross win statement 
    if (gridLayout[1][1] == 'X' or gridLayout[1][1] == 'O') and (((gridLayout[0][0] == gridLayout[1][1]) and (gridLayout[1][1] == gridLayout[2][2])) or ((gridLayout[0][2] == gridLayout[1][1]) and (gridLayout[1][1] == gridLayout[2][0]))):
        if (gridLayout[1][1] == player1Mark):
            winner = player1Name
        else:
            winner = player2Name
        return True
    
    return False


    
#-----------------------------
# Takes all the methods above
# and puts them to work.
#-----------------------------

#-----Variables-----
continueGame = True
cont = ""
#-------------------

preferences()

while (continueGame == True):
    setGrid(t)
    flipCoin()

    while (gameWon == False):
        if (turn+correction < 10):
            placeMark(t, turn)
            gameWon = checkIfWon()
            if (gameWon):
                print("Congradulations "+winner+", you won!")
                break
            turn += 1
        elif (turn+correction == 10):
            print("Nice draw, you two.")
            break
    

    cont = str(input("Would you like to play another game? (y/n) ")).lower()
    while True:
        if (cont != 'y' and cont != 'n'):
            cont = str(input("Please enter either 'y' or 'n' ")).lower()
        else: 
            break
        
    if (cont == 'y'):
        t.clear()
        #------Reset Variables------
        gameWon = False
        winner = ""
        turn = 0
        correction = 0
        gridLayout = [['A','A','A'],
                      ['A','A','A'],
                      ['A','A','A']]
        #---------------------------
    else:
        break