from itertools import permutations as P
class LittleElephantAndSubset:
    def getNumber(self,N):
        print N
        if N == 1:
            return 1
        total = 0
        for i in xrange(N):
            notin = True
            for j in str(i):
                if j in str(N):
                    notin = False
                    break
            if notin:
                total += 1
        total += self.getNumber(N-1)
        return total

buh = LittleElephantAndSubset()
