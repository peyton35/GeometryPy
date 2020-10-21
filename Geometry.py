import math

def perimeter(perimType, x1, y1, x2, y2, x3, y3, x4 = 0, y4 = 0):

    if perimType == "Triangle":
        pointA = math.sqrt(( (x2-x1)**2 + (y2-y1)**2 ))
        pointB = math.sqrt(( (x3-x1)**2 + (y3-y1)**2 ))
        pointC = math.sqrt(( (x3-x2)**2 + (y3-y2)**2 ))
        pointD = 0

    elif perimType == "Rectangle":
        pointA = math.sqrt(( (x2-x1)**2 + (y2-y1)**2 ))
        pointB = math.sqrt(( (x4-x1)**2 + (y4-y1)**2 ))
        pointC = math.sqrt(( (x3-x2)**2 + (y3-y2)**2 ))
        pointD = math.sqrt(( (x4-x3)**2 + (y4-y3)**2 ))
    else:
        return print("Invalid perimeter type. Please use either Triangle or Rectangle.")
    
   
   

    total = pointA + pointB + pointC + pointD

    return total

def distanceFormula(x1, y1, x2, y2):

    total = math.sqrt(( (x2-x1)**2 + (y2-y1)**2 ))

    return total

def midpointFormula(x1, y1, x2, y2):

    totalx = ( ( (x1+x2) / 2) )
    totaly = ( ( (y2+y1) / 2) )

    return totalx, totaly

def missingEndpoint(x1, y1, x2, y2):

    x = (2 * x2) - x1
    y = (2 * y2) - y1


    return x, y



