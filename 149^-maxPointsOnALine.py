'''
149. Max Points on a Line
Total Accepted: 51811 Total Submissions: 374055 Difficulty: Hard

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.




this is not better, but pretty interesting one:

def maxPoints(self, points):
    if len(points) <= 2: return len(points)
    d = collections.defaultdict(int) # (x,y) : count
    result = 0
    for i in range(len(points)):
        d.clear()
        overlap = 0
        curmax = 0
        for j in range(i+1, len(points)):
            dx = points[j].x - points[i].x
            dy = points[j].y - points[i].y
            if dx == 0 and dy == 0:
                overlap += 1
                continue
            gcd = self.getGcd(dx, dy)
            dx //= gcd
            dy //= gcd
            d[(dx,dy)] += 1
            curmax = max(curmax, d[(dx,dy)])
        result = max(result, curmax+overlap+1)
    return result

def getGcd(self, a, b):
    if b == 0: return a
    return self.getGcd(b, a%b)

    '''
    # Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points)<3:
            return len(points)

        globalmax=0

        for i in range(len(points)-1):
            slopes={}
            overlap=1

            for j in range(i+1,len(points)):
                if points[j].x==points[i].x and points[j].y==points[i].y:
                    overlap+=1
                    continue
                slope=float('inf') if points[j].x==points[i].x else \
                    (float(points[j].y)-points[i].y)/(float(points[j].x)-points[i].x)
                
                slopes[slope]=slopes[slope]+1 if slope in slopes else 1

            iMax=max(slopes.values())+overlap if slopes else overlap

            if globalmax< iMax:
                globalmax=iMax
        return globalmax

if __name__=="__main__":
    solution=Solution()
    pp0=Point(0,8)
    pp1=Point(13,2)
    pp2=Point(24,4)
    pp3=Point(42,8)
    pp4=Point(18,16)

    p0=Point(0,8)
    p1=Point(1,2)
    p11=Point(1,2)
    p2=Point(2,4)
    p3=Point(4,8)
    p4=Point(8,16)



    print solution.maxPoints([pp0, pp1,pp2,pp3,pp4, p0, p1,p11,p2,p3,p4])
    print solution.maxPoints([Point(1,1), Point(1,1), Point(1,1)])




