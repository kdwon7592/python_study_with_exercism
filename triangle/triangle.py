def isTriangle(sides):
    if 0 in sides:
        return False
        
    if (sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[2] + sides[0] >= sides[1]):
        return True
    else:
        return False

def equilateral(sides):
    if isTriangle(sides):
        if sides[0] == sides[1] == sides[2]:
            return True
        else:
            return False
    else:
        return False

def isosceles(sides):
    if isTriangle(sides):
        if (sides[0] == sides[1]) or (sides[1] == sides[2]) or (sides[2] == sides[0]):
            return True
        else:
            return False
    else:
        return False
    
def scalene(sides):
    if isTriangle(sides):
        if not equilateral(sides) and not isosceles(sides):
            return True
        else:
            return False
    else:
        return False
        