class MonochromaticBoard:
    def theMin(self, board):
        A = self.minHelper(board)
        invB = []
        for i in xrange(len(board[0])):
            s = ''
            for j in xrange(len(board)):
                s += board[j][i]
            invB.append(s)
        B = self.minHelper(invB)
        if A < B:
            return A
        return B

    def minHelper(self, board):
        mini = 0
        l = list([False] * len(board[0]))
        for i in board:
            if "W" not in i:
                mini += 1
            else:
                for j,k in enumerate(i):
                    if k == "B" and not l[j]:
                        mini += 1
                        l[j] = True
        return mini

buh = MonochromaticBoard()
print buh.theMin(("BBBBBBBB",
 "BBBBBBBB",
 "BBBBBBBB",
 "WBWBBBWB",
 "BBBBBBBB"))
print buh.theMin(("WBWBW",
 "BBBBB",
 "WBWBW",
 "WBWBW"))
