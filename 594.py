class LittleElephantAndIntervalsDiv2:
    def getNumber(self, M, L, R):
        vals = [-1] * M
        for i in xrange(len(L)):
            for j in xrange(L[i], R[i]+1):
                vals[j-1] = i
        ex = len(set(vals))
        if -1 in vals:
            ex -= 1
        return 2**ex

buh = LittleElephantAndIntervalsDiv2()
print buh.getNumber(4,(1,2,3),(1,2,3))
print buh.getNumber(3,(1,1,2),(3,1,3))
print buh.getNumber(100,(47,),(74,))
print buh.getNumber(100,(10,20,50),(20,50,100))
print buh.getNumber(42,(5, 23, 4, 1, 15, 2, 22, 26, 13, 16),(30, 41, 17, 1, 21, 6, 28, 30, 15, 19))
