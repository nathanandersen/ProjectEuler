# Problem 102
import numpy

#real	0m0.321s
#user	0m0.263s
#sys	0m0.045s

def vectorDif(p1,p2):
    return (p1[0]-p2[0],p1[1]-p2[1],0)

def crossProduct(vec1,vec2):
    return numpy.cross(vec1,vec2)

def dotProduct(vec1,vec2):
    return numpy.inner(vec1,vec2)

def sameSideOfLine(p1,p2,lineA,lineB):
    cp1 = crossProduct(vectorDif(lineB,lineA),vectorDif(p1,lineA))
    cp2 = crossProduct(vectorDif(lineB,lineA),vectorDif(p2,lineA))
    return (dotProduct(cp1,cp2) >= 0)


def triangle_contains_origin(pt1,pt2,pt3):
    # pt1 = (x,y) as a tuple
    o = (0,0)
    return (sameSideOfLine(o,pt1,pt2,pt3) and
            sameSideOfLine(o,pt2,pt1,pt3) and
            sameSideOfLine(o,pt3,pt1,pt2))

total = 0
for line in open("p102_triangles.txt"):
    (x1,y1,x2,y2,x3,y3) = eval( "(" + line + ")")
    if triangle_contains_origin((x1,y1),(x2,y2),(x3,y3)):
        total += 1

print(total)
