# Nhom09_BaiTap02
# Đậu Văn An - 21000659 - K66A2 Toán Tin
# Đặng Huy Hoàng - 21000680 - K66A2 Toán Tin
# Đỗ Mạnh Hùng - 21000682 - K66A2 Toán Tin

# Bai 1:

def charCodeToString(number):
    return chr(number + 97)

def coordinatesChessboard():
    coordinatesList = []
    for i in range(0, 8):
        row = []
        for j in range(0, 8):
            row.append(charCodeToString(j) + str(-i + 8))
        coordinatesList.append(row)
    return coordinatesList
    
coordinatesList = coordinatesChessboard()
    
def getWhiteSquare():
    print("White square: ")
    for i in range(0, 8):
        for j in range(0, 8, 2):
            colIndex = j + 1 if i % 2 != 0 else j
            print(coordinatesList[i][colIndex], end = " ")

getWhiteSquare()  
print("\n")
    
def printCoordinates():
    print("Coordinates on the chessboard: ")
    for i in range(0, 8):
        for j in range(0, 8):
            print(coordinatesList[i][j], end = " ")
        print()
printCoordinates()

# Bai 2:
import random

def getElementRandom(list):
    indexRandom = random.randint(0, len(list) - 1)
    return list[indexRandom]
    
list = [1,2,3,4,5,6,7,8,9]
print("Random element from list: ")
print(getElementRandom(list))

# Bai 3:

def filterElement(listA, listB):
    listC = []
    for value in listA:
        if value not in listB:
            listC.append(value)
    return listC       

listA = [2,3,5,2,4,64,3,64,13,413,26,1]
listB = [2,34,5,23,2,34,5,64,4,2,46,78,5]
print("Element in list A not in list B: ")
print(filterElement(listA, listB)) # 3, 3, 13, 413, 26, 1

# Bai 4:

def calculateQueenMoves(position):
    coordinatesList = []
    col = ord(position[0]) - ord('a')
    row = int(position[1]) - 1

    for i in range(0, 8):
        if i != row:
            coordinatesList.append(position[0] + str(i + 1))
        if i != col:
            coordinatesList.append(charCodeToString(i) + position[1])

    for i in range(1, 8):
        if row + i < 8 and col + i < 8:
            coordinatesList.append(charCodeToString(col + i) + str(row + i + 1))
        if row - i >= 0 and col - i >= 0:
            coordinatesList.append(charCodeToString(col - i) + str(row - i + 1))
        if row + i < 8 and col - i >= 0:
            coordinatesList.append(charCodeToString(col - i) + str(row + i + 1))
        if row - i >= 0 and col + i < 8:
            coordinatesList.append(charCodeToString(col + i) + str(row - i + 1))
    return coordinatesList

print("Queen Move: ")
print(calculateQueenMoves('a1'))

    