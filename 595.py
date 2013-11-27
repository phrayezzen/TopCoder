class ThreeTeleports:
    def shortestDistance(self, xMe, yMe, xHome, yHome, teleports):
        tele = {}
        posMe = (xMe,yMe)
        posHome = (xHome,yHome)
        for i in teleports:
            points = i.split()
            tele[(int(points[0]),int(points[1]))] = (int(points[2]),int(points[3]))
            tele[(int(points[2]),int(points[3]))] = (int(points[0]),int(points[1]))
        tele[posMe] = posMe
        tele[posHome] = posHome
        return self.shortHelper(posMe, posHome, tele)

    def shortHelper(self, start, end, tele):
        if start == end:
            return 0
        minDist = float('inf')
        keys = tele.keys()
        for i in keys:
            temp = tele[i]
            del tele[i]
            if i == start:
                continue
            distI = self.dist(start, i) + self.shortHelper(temp, end, tele)
            if distI < minDist:
                minDist = distI
        return minDist
                

    def dist(self, p, q):
        x = abs(p[0]-q[0])
        y = abs(p[1]-q[1])
        return x + y
        
