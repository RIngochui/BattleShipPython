from random import randint
from os import system
from time import sleep

grid = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

x = randint(10, 35) # set x and y to 10 for AI to win quicker
y = randint(10, 35)

x = 10
y = 10

ships = {
    "A": 10,
    "C": 8,
    "F": 6,
    "U": 5,
    "S": 3,
}

gameBoard = []
hiddenBoard = []
missleAway = 00
missleLeft = 50 
score = 000
move = ""

# for AI
alreadyHit = []
lastSym = "X"
lastCol = 0
lastRow = 0
foundShip = 0
shipEnd = 0
shipBegin = 0


def initGame():
    gameBoard[:] = [["~"] * x for i in range(y)]
    hiddenBoard[:] = [["~"] * x for i in range(y)]
    for ship in ships:
        loadShips(ship)


def drawBoard():
    print("    Python Battleship...")
    print("   ", grid[:x])
    count = 0
    for set in gameBoard:
        print(grid[count], "|", "".join(set), "|", grid[count])
        count += 1
    print("   ", grid[:x])
    print("Missiles Away:", missleAway, "Missiles Left:", missleLeft)
    print("Current Score:", score, "Last Move:", move)


def loadShips(key):
    tempCol = randint(0, x - ships[key])
    tempRow = randint(0, y - 1)
    while (hiddenBoard[tempRow][tempCol:tempCol + ships[key]] !=
           ["~"] * ships[key]):
        tempRow = randint(0, x - 1)
        tempCol = randint(0, y - ships[key])

    hiddenBoard[tempRow][tempCol:tempCol + ships[key]] = key * ships[key]
    hiddenBoard[tempRow][tempCol] = "["
    hiddenBoard[tempRow][tempCol + ships[key] - 1] = ">"
    if (key != "S"):
        hiddenBoard[tempRow][tempCol + ships[key] - 2] = "="


def updateData(coord):
    global lastSym
    global lastCol
    global lastRow
    global missleAway
    global missleLeft
    global move
    global score

    tempCoord = ""

    if (coord == -1):
        return (0)

    count = 0
    for index in str(coord):
        count += 1

    if (count % 2 != 0):
        tempCoord = "0" + str(coord)
    else:
        tempCoord = str(coord)

    halfSize = int(len(tempCoord) / 2)
    tempCol = int(tempCoord[halfSize:])
    tempRow = int(tempCoord[:halfSize])

    missleAway += 1
    missleLeft -= 1

    if (hiddenBoard[tempRow][tempCol] == "~"):
        gameBoard[tempRow][tempCol] = "X"
        hiddenBoard[tempRow][tempCol] = "X"
        move = "MISS on " + grid[tempRow] + grid[tempCol]
    elif (gameBoard[tempRow][tempCol] != hiddenBoard[tempRow][tempCol]):
        gameBoard[tempRow][tempCol] = hiddenBoard[tempRow][tempCol]
        move = "HIT on " + grid[tempRow] + grid[tempCol]
        score += 5
    else:
        move = "ALREADY HIT on " + grid[tempRow] + grid[tempCol]
        missleAway -= 1
        missleLeft += 1
    lastSym = hiddenBoard[tempRow][tempCol]
    lastCol = tempCol
    lastRow = tempRow


def checkMove():
    coordinate = input("Enter Target Coordinates--> ")
    tempCol = ""
    tempRow = ""

    if (len(coordinate) != 2 or coordinate[0] == "-"):
        return (-1)

    for index in range(len(grid)):
        if (coordinate[0] == grid[index]):
            tempCol = index
        if (coordinate[1] == grid[index]):
            tempRow = index

    if (0 <= tempRow < x and 0 <= tempCol < y):
        if (0 <= int(tempRow) < 10):
            return (int(str(tempCol) + "0" + str(tempRow)))
        else:
            return (int(str(tempCol) + str(tempRow)))
    else:
        return (-1)

def AI():
    global lastSym
    global lastCol
    global lastRow
    global foundShip
    global shipEnd
    global shipBegin
    global alreadyHit
    
    if(lastSym != "X"):
      foundShip = 1
      if(lastSym == "["):
        shipEnd = 1
      elif(lastSym == ">"):
        shipBegin = 1
      aiRow = lastRow

    if(shipEnd == 1 and shipBegin == 1 and foundShip == 1):
      foundShip = 0
      shipEnd = 0
      shipBegin = 0
    
    if(shipEnd == 0 and shipBegin == 0 and foundShip == 0):
      aiCol = randint(0, x - 1)
      aiRow = randint(0, y - 1)

    if(shipEnd == 1 or foundShip == 1):
      aiCol = lastCol + 1

    if(shipBegin == 1):
      aiCol = lastCol - 1

    coordinate = str(grid[aiRow]) + str(grid[aiCol])
    tempCol = ""
    tempRow = ""

    if (len(coordinate) != 2 or coordinate[0] == "-"):
        return (-1)

    for index in range(len(grid)):
        if (coordinate[0] == grid[index]):
            tempCol = index
        if (coordinate[1] == grid[index]):
            tempRow = index

    if (0 <= tempRow < x and 0 <= tempCol < y):
        if (0 <= int(tempRow) < 10):
            return (int(str(tempCol) + "0" + str(tempRow)))
        else:
            return (int(str(tempCol) + str(tempRow)))
    else:
        return (-1)


def playBattleship():
    global missleLeft
    global missleAway
    end = 0
    initGame()
    playerNum = input("How many players? (1 or 0): ")
    system('clear')

    if (playerNum == "1"):
        while (end == 0):
            drawBoard()
            updateData(checkMove())
            system('clear')
            if (score == 160):
                end = 1
                print("YOU WON, IN", missleAway, "MOVES")
            elif (missleLeft == 0):
                end = 1
                print("YOU LOSE, RAN OUT OF MISSLES")
        drawBoard()
    elif (playerNum == "0"):
        while (end == 0):
            drawBoard()
            sleep(0.2) #put at 0.1 seconds, AI thinks slowly
            updateData(AI())
            system('clear')
            if (score == 160):
                end = 1
                print("COMPUTER WON, IN", missleAway, "MOVES")
            elif (missleLeft == 0):
                end = 1
                print("COMPUTER LOSE, RAN OUT OF MISSLES")
        drawBoard()
    else:
        print("NOT A VALID OPTION!!!")
        playBattleship()


playBattleship()
