class RedAndGreen:
    def minPaints(self, row):
        mini = float('inf')
        for i in xrange(len(row)+1):
            val = 'R' * i + 'G' * (len(row) - i)
            diff = self.checkDiff(row, val)
            if diff < mini:
                mini = diff
        return mini

    def checkDiff(self, row, val):
        diff = 0
        for i in xrange(len(row)):
            if row[i] != val[i]:
                diff += 1
        return diff

buh = RedAndGreen()
print buh.minPaints("RGRGR")
print buh.minPaints("RRRGGGGG")
print buh.minPaints("GGGGRRR")
print buh.minPaints("RGRGRGRGRGRGRGRGR")
print buh.minPaints("RRRGGGRGGGRGGRRRGGRRRGR")
