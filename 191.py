class VolumeGuess:
    def correctVolume(self, queries, numberOfBoxes, ithBox):
        small = {}
        for s in queries:
            [box1,box2,vol] = s.split(',')
            box1 = int(box1)
            box2 = int(box2)
            vol = int(vol)
            if vol not in small:
                small[vol] = [box1,box2]
            else:
                if box1 in small[vol]:
                    small[vol] = [box1]
                elif box2 in small[vol]:
                    small[vol] = [box2]
                else:
                    print 'wtf'

        for i in small.iterkeys():
            if small[i][0] == ithBox:
                return i

buh = VolumeGuess()
print buh.correctVolume(("1,2,10","1,3,10","2,3,20"),3,1)
print buh.correctVolume(("1,02,10","2,3,010","1,3,20"),3,2)
print buh.correctVolume(("1,2,31","1,3,9","1,4,31","2,4,32","3,4,9","3,2,9"),4,1)
print buh.correctVolume(("1,2,31","1,3,9","1,4,31","2,4,32","3,4,9","3,2,9"),4,3)
print buh.correctVolume(("3,2,80", "5,2,15", "1,2,193", "3,1,80", "5,1,15", "5,3,15", "3,4,3", "4,5,3", "2,4,3", "4,1,3"), 5, 3)
print buh.correctVolume(("3,2,80", "5,2,15", "1,2,193", "3,1,80", "5,1,15", "5,3,15", "3,4,3", "4,5,3", "2,4,3", "4,1,3"), 5, 4)
