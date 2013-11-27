class LittleElephantAndString:
    def getNumber(self, A, B):
        print A,B
        if len(A) == 1:
            if A != B:
                return -1
            else:
                return 0
        turns = 0
        l = len(A)-1
        while A[-1] != B[-1]:
            A = A[-1] + A[0:l]
            turns += 1
            print A,B
        val = self.getNumber(A[0:l], B[0:l])
        if val == -1:
            return -1
        else:
            turns += val
            return turns

buh = LittleElephantAndString()
print buh.getNumber("ABC","CBA")
