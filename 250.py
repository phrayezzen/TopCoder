class Acronyms:
    def acronize(self, document):
        big_sent = ''
        for seq in document:
            big_sent += seq + " "
        sents = big_sent.split('  ')
        i = 0
        for j in range(len(sents)):
            first = True
            sent = sents[j].split()
            length = len(sent)
            while i < length:
                if first:
                    first = False
                    i += 1
                    continue
                if sent[i][0].isupper():
                    asent = sent[0:i] + self.makeac(sent[i:])
                    length -= len(sent)
                    length += len(asent)
                    sent = asent
                i += 1
            sents[j] = " ".join(sent)
        return "  ".join(sents)
                    
    def makeac(self, sent):
        if len(sent) == 1:
            return sent
        acro = ''
        letters = 'abcdefghijklmnopqrstuvwxyz'
        lower = False
        last = 0
        for i in range(len(sent)):
            if sent[i][0].islower() or sent[i][0].lower() not in letters:
                if lower or sent[i][-1].lower() not in letters:
                    if len(acro) > 1:
                        if sent[i-2][-1].lower() not in letters:
                            acro += sent[i-2][-1]
                        sent = [acro] + sent[last+1:]
                    return sent
                lower = True
                continue
            else:
                lower = False
                last = i
            for char in sent[i]:
                if char.isupper():
                    acro += char
                    last = i
        if len(acro) > 1:
            if sent[i][-1].lower() not in letters:
                acro += sent[i][-1]
            sent = [acro] + sent[i+1:]
        return sent
                


ex0 = ("I would like a Bacon, Lettuce, and Tomato", "sandwich. I don't", "like Pickles, Onions, and Tomatoes.")

buh = Acronyms()
print buh.acronize(ex0)
