class PeopleCircle:
    def order(self, numMales, numFemales, K):
        order = 'M'*numMales
        total = numMales + numFemales
        pos = 0
        flipped = False
        for i in xrange(numFemales):
            pos += K - 1
            pos %= total
            total -= 1
        while numFemales > 0:
            print order, pos
            if not flipped or pos != 0:
                order = order[0:pos] + 'F' + order[pos:]
            elif flipped and pos == 0:
                order = order + 'F'
            pos -= K-1
            total += 1
            if pos % total != pos:
                pos %= total
                flipped = True
            numFemales -= 1
        return order

buh = PeopleCircle()
#print buh.order(5,3,2)
#print buh.order(5,5,3)
#print buh.order(25,25,1000)
print buh.order(7,3,10)
