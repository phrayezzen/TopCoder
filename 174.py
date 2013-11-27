class BirthdayOdds:
    def minPeople(self, minOdds, daysInYear):
        percent = 1
        d = daysInYear
        while (1 - percent) < (minOdds / 100.):
            percent *= float(d) / daysInYear
            d -= 1
        return daysInYear - d

buh = BirthdayOdds()
print buh.minPeople(75,5)
