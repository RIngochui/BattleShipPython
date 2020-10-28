from random import randint

grid = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#x = randint(10, 35)
#y = randint(10, 35)
# first commit

x = 20
y = 20

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
end = 0


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


def loadShips(key):
    tempRow = randint(0, y - 1)
    tempCol = randint(0, x - ships[key])
    # print(tempRow, tempCol)
    while (hiddenBoard[tempRow][tempCol:tempCol + ships[key]] !=
           ["~"] * ships[key]):
        tempRow = randint(0, x - 1)
        tempCol = randint(0, y - ships[key])
    # print(tempRow, tempCol, "*")

    hiddenBoard[tempRow][tempCol:tempCol + ships[key]] = key * ships[key]
    hiddenBoard[tempRow][tempCol] = "["
    hiddenBoard[tempRow][tempCol + ships[key] - 1] = ">"
    if (key != "S"):
        hiddenBoard[tempRow][tempCol + ships[key] - 2] = "="


def updateData():
    return (0)


def checkMove():
    return (0)


def playBattleship():
    initGame()
    drawBoard()


playBattleship()
print(hiddenBoard)
