from string import digits as D
class SerialNumbers:
    def sortSerials(self, serialNumbers):
        serialNumbers = list(serialNumbers)
        returnme = [serialNumbers.pop(0)]
        while serialNumbers:
            val = serialNumbers.pop(0)
            i = 0
            while i < len(returnme) and not self.sort(val,returnme[i]):
                i += 1
            returnme.insert(i, val)
        return returnme

    def sort(self, toadd, inlist):
        if len(toadd) != len(inlist):
            return len(toadd) < len(inlist)
        
        toaddsum = 0
        inlistsum = 0
        for i in xrange(len(toadd)):
            if toadd[i] in D:
                toaddsum += int(toadd[i])
            if inlist[i] in D:
                inlistsum += int(inlist[i])
        if inlistsum != toaddsum:
            return toaddsum < inlistsum

        for i in xrange(len(toadd)):
            if toadd[i] != inlist[i]:
                return toadd[i] < inlist[i]

        return True

buh = SerialNumbers()
print buh.sortSerials(("ABCD","145C","A","A910","Z321"))
