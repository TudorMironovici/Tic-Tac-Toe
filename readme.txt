********************************************************************************************************************
                                                    Tic-Tac-Toe
********************************************************************************************************************

This is a Python program (written with Python 3.7.3) that lets two users play a game of Tic-Tac-Toe using command 
line inputs, with some neat features. The visuals are all drawn using the Turtle graphics module.


Inputs:
The program allows the players to use either a standard numpad layout, or the first block of keys if they have a 
numpad, making the inputs either be:

7 8 9		Q W E
4 5 6	 or	A S D
1 2 3		Z X C

The program asks this as the first thing when it starts, and can only be changed when the program is restarted.


Player Info:
The program will ask for both players' names, and then the color they want their marks (the 'X' or 'O') to be. There
are 7 peselected colors (red, orange, yellow, green, blue, indigo, and violet) the users can choose from, but they 
can also type in their own custom RGB color code.The program prevents the two users from having the same names and 
colors, as it would cause confusion during the game. Names and colors can only be changed when the program is 
restarted.


Gameplay:
The program randomly chooses who goes first, and lets that user choose their mark. Then, that first player gets to
place their mark on the Tic-Tac-Toe grid first. The game goes on, alternating players like a normal game of Tic-Tac-
Toe does, until someone gets 3 of their marks in a row. After a game is finished, the users are asked if they want
to play again. If the users choose 'y', the grid is cleared, and the program starts again by randomly choosing who
goes frist. If the users choose 'n', the program closes.