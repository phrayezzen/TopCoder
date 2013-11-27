class CuttingGrass:
    def theMin(self, init, grow, H):
        N = len(grow)
        init2 = [x for (y,x) in sorted(zip(grow, init))]
        grow2 = sorted(grow)
        maxH = 0
        for i in xrange(N):
            maxH += N - 1 - i
        if maxH > H:
            return -1

        days = 0
        while(True):
            if self.minHelper(list(init), list(grow), days, H):
                return days
            days += 1

    def minHelper(self, init, grow, days, H):
        for i in xrange(len(grow)):
            init[i] += grow[i] * days

        maxs = []
        init2 = list(init)
        for i in xrange(days):
            maxs.append(grow[init2.index(max(init))])
            init.remove(max(init))

        maxs.sort()
        asum = sum(init)
        for i in xrange(days):
            asum += maxs[i] * (days-1-i)
        print asum
        if asum <= H:
            return True
        return False

buh = CuttingGrass()
#print buh.theMin((5,8,0), (2,1,1), 16)
#print buh.theMin((5, 1, 6, 5, 8, 4, 7),(2, 1, 1, 1, 4, 3, 2),33)
print buh.theMin((1231, 1536, 1519, 1940, 1539, 1385, 1599, 1613, 1394, 1803,
 1763, 1706, 1863, 1452, 1818, 1914, 1386, 1954, 1496, 1722,
 1616, 1862, 1755, 1215, 1233, 1078, 1448, 1241, 1732, 1561,
 1633, 1307, 1844, 1911, 1371, 1338, 1989, 1789, 1656, 1413,
 1929, 1182, 1815, 1474, 1540, 1797, 1586, 1427, 1996, 1202),
(86, 55, 2, 86, 96, 71, 81, 53, 79, 22,
 23, 8, 69, 32, 35, 39, 30, 18, 92, 64,
 88, 1, 48, 81, 91, 75, 44, 77, 3, 33,
 9, 52, 56, 4, 19, 73, 52, 18, 8, 77,
 91, 59, 50, 62, 42, 87, 89, 24, 71, 67),
63601)
