# Nhom09_BaiTap03
# Đậu Văn An - 21000659 - K66A2 Toán Tin
# Đặng Huy Hoàng - 21000680 - K66A2 Toán Tin
# Đỗ Mạnh Hùng - 21000682 - K66A2 Toán Tin

#Bai2a:
def findDirectionVector(tupleX, tupleY):
    x = (tupleY[0] - tupleX[0])
    y = tupleY[1] - tupleX[1]
    return (x, y)


def getOrthogonalVector(directionVector):
    return (-1 * directionVector[1], directionVector[0])
    
def findFreeCoefficient(tupleX, orthogonalVector):
    return tupleX[0] * orthogonalVector[0] + tupleX[1] * orthogonalVector[1]
    
def inputTuple():
    x = float(input("- Enter x coordinates: "))
    if x.is_integer():
        x = int(x)
        
    y = float(input("- Enter y coordinates: "))
    if y.is_integer():
        y = int(y)
        
    return (x, y)
    
def slove():
    print("coordinates of the first point: ")
    tupleA = inputTuple()
    print("coordinates of the second point: ")
    tupleB = inputTuple()
    
    directionVector = findDirectionVector(tupleA, tupleB)
    orthogonalVector = getOrthogonalVector(directionVector)
    freeCoefficient = findFreeCoefficient(tupleA, orthogonalVector)
    
    a = orthogonalVector[0]
    b = orthogonalVector[1]
    c = freeCoefficient
    
    return (a, b, c)

def init():
    print("result:", slove())
    
init()


#Bai2b:
def cross_product(tupleX, tupleY):
    cross_product = (
        tupleX[1] * tupleY[2] - tupleX[2] * tupleY[1],
        tupleX[2] * tupleY[0] - tupleX[0] * tupleY[2],
        tupleX[0] * tupleY[1] - tupleX[1] * tupleY[0]
    )
    return cross_product

def findDirectionVector(tupleX, tupleY):
    x = (tupleY[0] - tupleX[0])
    y = tupleY[1] - tupleX[1]
    z = tupleY[2] - tupleX[2]
    return (x, y, z)

def inputTuple():
    x = float(input("- Enter x coordinates: "))
    if x.is_integer():
        x = int(x)
        
    y = float(input("- Enter y coordinates: "))
    if y.is_integer():
        y = int(y)
        
    z = float(input("- Enter z coordinates: "))
    if z.is_integer():
        z = int(z)
        
    return (x, y, z)
    
def getOrthogonalVector(tupleX, tupleY):
    return cross_product(tupleX, tupleY)

def findFreeCoefficient(tupleX, orthogonalVector):
    return tupleX[0] * orthogonalVector[0] + tupleX[1] * orthogonalVector[1] + tupleX[2] * orthogonalVector[2]
    
def slove():
    print("coordinates of the first point: ")
    tupleA = inputTuple()
    print("coordinates of the second point: ")
    tupleB = inputTuple()
    print("coordinates of the third point: ")
    tupleC = inputTuple()
    
    firstDirectionVector = findDirectionVector(tupleA, tupleB)
    secondDirectionVector = findDirectionVector(tupleA, tupleC)
    orthogonalVector = getOrthogonalVector(firstDirectionVector, secondDirectionVector)
    freeCoefficient = findFreeCoefficient(tupleA, orthogonalVector)
    
    a = orthogonalVector[0]
    b = orthogonalVector[1]
    c = orthogonalVector[2]
    d = freeCoefficient
    
    return (a, b, c, d)
    
def init():
    print("result:", slove())
    
init()