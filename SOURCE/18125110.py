import sys
import time
import getopt
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]
numOfmoveBTK = 0
timeCountingBTK = 0
numOfmove = 0
timeCounting = 0

def outputBTK(x, y, n , A):
    global timeCountingBTK
    sys.stdout = open("18125110_Backtracking.txt", "w")
    print(x,end=' ')
    print( y, end=' ')
    print( n )
    print(numOfmoveBTK)
    print(timeCountingBTK*1000)
    for j in range(n):
        for i in range(n):
            print(A[i][j], end=' ')
        print()
    sys.stdout.close()
def checkCondition(x, y,n, A):
    if(x >= 0 and y >= 0 and x < n and y < n and A[x][y] == -1):
        return True
    return False
def KNtour(x, y, n):
    global timeCountingBTK
    start = time.time()
    riuX =  x - 1
    riuY = y  -1 
    A = [[-1 for x in range(n)] for y in range(n)] 
    A[riuX][riuY] = 0     
    if(not moveBTK(riuX,riuY, 1, n, A)):
        end = time.time()
        timeCountingBTK= end-start
        outputBTK(x, y, n, A)
    else:
        end = time.time()
        timeCountingBTK= end-start
        outputBTK(x, y ,n, A)
def moveBTK(_x, _y, numOfStep, n, A):
    global numOfmoveBTK
    if(numOfStep == n**2):
        return True
    for i in range(8):
        xNext = _x + move_x[i]
        yNext = _y + move_y[i]
        numOfmoveBTK = numOfmoveBTK + 1  
        if(checkCondition(xNext, yNext,n, A)):
            A[xNext][yNext] = numOfStep
            if(moveBTK(xNext, yNext,numOfStep+1, n , A)):
                return True
            else: 
                A[xNext][yNext] = -1
    return False


#---------------WarnsdorffsHeuristic----------------------#
def output(x, y, n):
    global timeCounting
    riuX = x - 1
    riuY = y - 1
    A = [[-1 for x in range(n)] for y in range(n)] 
    sys.stdout = open("18125110_WarnsdorffsHeuristic.txt", "w")
    start = time.time()
    tmp= move(riuX, riuY, n, A)
    end = time.time()
    timeCounting= end-start
    print(x,end=' ')
    print( y, end=' ')
    print( n )
    print(numOfmove)
    print(timeCounting*1000)
    for j in range(n):
        for i in range(n):
            print(A[i][j], end=' ')
        print()
    sys.stdout.close()

def getDegree(x, y, n, A):
    deg=0
    for i in range(8):
        xNext = x + move_x[i]
        yNext = y + move_y[i]
        if (checkCondition(xNext, yNext, n, A)):
            deg=deg+1
    return deg

def getAccessiblePos(x, y, n, S, A):
    minDegree=9
    iMin=0
    countNumOfS =0 
    for i in range(8):
        xNext = x + move_x[i]
        yNext = y + move_y[i]
        if(checkCondition(xNext, yNext,n, A)):
            S[countNumOfS][0] = xNext
            S[countNumOfS][1] = yNext
            degree = getDegree(xNext, yNext, n, A)
            if (degree < minDegree):
                minDegree = degree
                iMin = countNumOfS
            countNumOfS= countNumOfS+1
    if (countNumOfS == 0):
        S[0][0] = -1
        S[0][1] = -1
        return [S[0][0], S[0][1]]
    return [S[iMin][0], S[iMin][1]]

def move(_x, _y, n, A):
    global numOfmove
    gotoPos=[]
    gotoPos.append(_x)
    gotoPos.append(_y)
    S = [[-1 for i in range(2)]for j in range(8)] 
    A[_x][_y] = 1
    for i in  range(2,n**2+1):
        gotoPos = getAccessiblePos(gotoPos[0], gotoPos[1],n, S, A)
        if(gotoPos[0]==-1):
            return False
        A[gotoPos[0]][gotoPos[1]]=i
        numOfmove= numOfmove+1;
    return True

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:],"px:py:s:", ["px=", "py=","size="])
    x=0
    y=0
    s=0
    for opt, arg in opts:
        if opt =="-x":
            x = int (arg)   
        elif opt =="-y":
            y = int (arg)
        elif opt =="-s":
            s = int (arg)

    KNtour(x, y, s)  # ---Backtracking
    output(x, y, s)  # ---Warnsdorffs Heuristic

    
 
