class CompositeSmash:
    def thePossible(self, N, target):
        sieve = self.Esieve(N)
        factorsN = set()
        factorsT = set()
        for i,j in enumerate(sieve):
            if not j:
                continue
            if N % i == 0:
                factorsN.add(i)
            if target % i == 0:
                factorsT.add(i)
        print factorsT, factorsN
        if factorsT.issubset(factorsN):
            return "Yes"
        return "No"
    
    def Esieve(self, limit):
        sieve = [False, False, True] + [True, False] * (limit / 2)
        l = len(sieve)
        for i in xrange(l):
            if sieve[i]:
                for j in xrange(l/i):
                    if i*j > i:
                        sieve[i*j] = False
        return list(sieve)


buh = CompositeSmash()
print buh.thePossible(517, 47)
