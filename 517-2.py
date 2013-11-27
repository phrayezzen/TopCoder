class CompositeSmash:
    def thePossible(self, N, target):
        if N < target or N % target:
            return "No"
        if N == target:
            return "Yes"
        for i in xrange(2,int(N**.5)+1):
            if N % i == 0:
                if self.thePossible(i, target) == "No" and self.thePossible(N/i, target) == "No":
                    return "No"
        return "Yes"
    
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
##print buh.thePossible(517, 47)
##print buh.thePossible(8, 4)
##print buh.thePossible(12, 6)
##print buh.thePossible(5, 8)
##print buh.thePossible(10000, 10000)
##print buh.thePossible(5858, 2)
##print buh.thePossible(81461, 2809)
##print buh.thePossible(65536, 256)
print buh.thePossible(12, 6)
