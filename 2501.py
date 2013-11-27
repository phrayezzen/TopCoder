class LittleElephantAndDouble:
    def getAnswer(self, A):
        sieve = [False, False] + [False, True] * (max(A) / 2)
        for i in xrange(len(sieve)):
            if sieve[i]:
                for j in xrange(len(sieve)/i):
                    if i*j <= i:
                        continue
                    sieve[i*j] = False
        sieve[2] = True
        primes = []
        for i in xrange(len(sieve)):
            if sieve[i]:
                primes.append(i)

        factors = []
        for i in A:
            for j in primes:
                if i % j == 0 and j != 2:
                    factors.append(j)

        for i in A:
            for j in factors:
                if i % j != 0:
                    return "NO"
        return "YES"

buh = LittleElephantAndDouble()
buh.getAnswer([4, 8, 2, 1, 16])
