class ChangingSounds:
    def maxFinal(self, changeIntervals, beginLevel, maxLevel):
        ci = len(changeIntervals)+1
        ml = maxLevel
        vols = [[0*ci]] * ci
        vols[0][0] = beginLevel
        for i in xrange(1,ci):
            if vols[i-1][0] - changeIntervals[i-1] >= 0:
                vols[i][0] = vols[i-1][0] - changeIntervals[i-1]
            else:
                vols[i][0] = -1
            if vols[0][i-1] + changeIntervals[i-1] <= ml:
                vols[0][i] = vols[0][i-1] + changeIntervals[i-1]
            else:
                vols[0][i] = -1

        for i in xrange(1,ci):
            for j in xrange(1,ci):
                sub = vols[i-1][j]
                add = vols[i][j-1]
                c = changeIntervals[i+j-1]
                if (add == -1 and sub == -1) or (add == -1 and sub - c < 0) or (sub == -1 and add + c > ml):
                    vols[i][j] = -1
                elif add == -1:
                    vols[i][j] = sub - changeIntervals[i+j-1]
                elif sub == -1:
                    vols[i][j] = add + changeIntervals[i+j-1]
                else:
                    if add
                
        
        i = 0
        vol = [beginLevel]
        while i < len(changeIntervals):
            vol2 = []
            print vol
            for j in vol:
                if j + changeIntervals[i] <= maxLevel:
                    vol2.append(j + changeIntervals[i])
                if j - changeIntervals[i] >= 0:
                    vol2.append(j - changeIntervals[i])
            vol = vol2
            i += 1
        if not vol:
            return -1
        return max(vol)

buh = ChangingSounds()
print buh.maxFinal((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50), 300, 1000)

