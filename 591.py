class ThreeTeleports:
    def shortestDistance(self, xMe, yMe, xHome, yHome, teleports):
        tele = {}
        posMe = (xMe,yMe)
        posHome = (xHome,yHome)
        for i in teleports:
            points = i.split()
            tele[(int(points[0]),int(points[1]))] = (int(points[2]),int(points[3]))
            tele[(int(points[2]),int(points[3]))] = (int(points[0]),int(points[1]))

        shortest = dist(posMe,posHome)
        shorter = float('inf')
        point = posMe
        while shortest < shorter:
            shorter = 0
            for i in tele.iterkeys():
                if dist(point, i) + shorter <

    def shortHelper(start, dists):
        

    def dist(p,q):
