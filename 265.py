from string import ascii_uppercase as U
from string import ascii_lowercase as L
class FontSize:
    def getPixelWidth(self, sentence, uppercase, lowercase):
        l = 0
        letters = 0
        for i in sentence:
            if i in U:
                l += uppercase[U.index(i)]
            elif i in L:
                l += lowercase[L.index(i)]
            else:
                l += 3
            letters += 1
        l += letters-1
        print letters, len(sentence)
        return l
buh = FontSize()
print buh.getPixelWidth("ThE qUiCk BrOwN fOx JuMpEd OvEr ThE lAzY dOg",
(36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11),
(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26))
print buh.getPixelWidth("two  spaces",
(9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9),
(3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3))
