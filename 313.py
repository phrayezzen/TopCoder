class PrefixFreeSets:
    def maxElements(self, words):
        num_prefix = dict((pref,[]) for pref in words)
        for i in words:
            words1 = list(words)
            words1.remove(i)
            for j in words1:
                if self.is_prefix(i,j):
                    num_prefix[i].append(j)
        count = 0
        dup = []
        
        for k in num_prefix.iterkeys():
            if k in num_prefix[k] and k not in dup:
                dup.append(k)
                for v in num_prefix[k]:
                    if v != k:
                        pref = False
                        break
                    pref = True
                if pref:
                    count += 1
                    print k, num_prefix[k], count
            if len(num_prefix[k]) < 1:
                count += 1
                print k, num_prefix[k], count
        return count
    
    def is_prefix(self, prefix, word):
        if len(word) < len(prefix):
            return False
        else:
            for i in xrange(len(prefix)):
                if word[i] != prefix[i]:
                    return False
        return True

buh = PrefixFreeSets()
print buh.maxElements(("vsvvdxggvhraktqqkkfl", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvsogvobw", "fynrfcnxfjmqswmbwmznfzvaeocdozyorbfvcrguygztojdldp", "xgejpsemtuhshxpziqviiqs", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvsogvobw", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvsogvobw", "hfolqqhfvrfzdgsuuniyakyrottbfgtouxbfcibesuoqekf", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvsog", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvsogvobw", "fynrfcnxfjmqswmbwmznfzvaeocdozyorbfvcrguygztojdldn", "eblhpwsvbgjskhfdsqmdsxxhupcydgroae", "eonijaazhtdnvwryvjdcndteoeqxncqhddqofzcus", "fynrfcnxfjmqswmbwmznfzvaeocdozyorbfvcrguygztojdldp", "hfolqqhfvrfzdgsuuniyakyrottbfgtouxbfcibesuoqekfsc", "hfolqqhfvrfzdgsuuniyakyrottbfgtouxbfcibesuoqekfsc", "fynrfcnxfjmqswmbwmznfzvaeocdozyorbfvcrguygztojdldp", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvsjvbxdr", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvsjvbxdr", "fynrfcnxfjmqswmbwmznfzvaeocdozyorbfvcrguygztojdldn", "hfolqqhfvrfzdgsuuniyakyrottbfgtouxbfcibesuoqekfscd", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvsjvbxd", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvsogvobw", "fynrfcnxfjmqswmbwmznfzvaeocdozyorbfvcrguygztojdldp", "hfolqqhfvrfzdgsuuni", "fynrfcnxfjmqswmbwmznfzvaeocdozyorbfvcrguygztojdldn", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvsjvbxdr", "fynrfcnxfjmqswmbwmznfzvaeocdozyorbfvcrguygztojdld", "hfolqqhfvrfzdgsuuniyakyrottbfgtouxbfcibesuoqekfscd", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvsjvbxd", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvsjvbxdr", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvsjvb", "axcm", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvsjvbxdr", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvs", "anlecahk", "hfolqqhfvrfzdgsuuniyakyrottbfgtouxbfcibesuoqekfscd", "eonijaazhtdnvwryvjdcndteoeqxncqhddqofzc", "eonijaazhtdnv", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvsjvbxdr", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvsjvbxdr", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvso", "anlecahkrizwtqobdnycxeocojpumjfqtmpavuanhwvsjvbxd", "hfolqqhfvrfzdgsuuniyakyrottbfgtouxbfcibesuoqekfscg", "eonijaazhtdnvcwamgwulzwwuoypkqxaxzuttvbvsot", "eonijaazhtdnvwryvjdcndteoeqxncqhddq", "hfolqqhfvrfzdgsuuniyakyrottbfgtouxbfcibes", "hfolqqhfvrfzdgsuuniyakyrottbfgtouxbfcibesuoqekfscd", "eonijaazhtdnvpwxyeaprmzuscqdqjvs", "eonijaazhtdn", "fynrfcnxfjmqswmbwmznfzvae"))

#print buh.maxElements(("jkeaqqoltlqssfpglhjgjdfuwuihuafmxi", "yinzxqercrwvymsudtzzrompqxzeulkdbnmjwspivquu", "nskapm", "yinzxqercrwvymsudtzzrompqxzeulkdbnmjwspivquuuejmbx", "ihogvogbitpjasiramjyiiimz", "leykhdxenpdwophpyjynkjjyytbkbahxdisiwfpptib", "zdbfbfosblupxqtiao", "zcguthmlaiwdeoijfkxlouqbselygtsfnlyvwsxkqlxctzm", "anndvehbegjqxbmhgzfazmyggvjoyyvrthadrmys", "suitsuinbzshsczwrgceqcppamortutbinw", "ptqchiizuciti", "hbkqvcpapfvagnwemhpczdjkrdpdwcbrgawdqemwspy", "jgxqelkmfgpjljvsdsthrxexusremiclheniitve", "leykhdxenpdwophpyjynkjjyytbkbahx", "zihhvrbyjcpprmqlbygiozfdxsaawraocukswvedurs", "ytgekfwcaskj", "suitsuinbzshsczwrgceqcppamortutbinwcuyicvwceaivb", "yinzxqercrwvymsudtzzrompqxzeulkdbnmjwspivquu", "hbkqvcpapfvagnwemhpczdjkrdpdwcbrgawdqemwspyspcb", "knsms", "pyaugqmgakwbabbsjd", "dqpwsjfmpalhyrijjqzdxsjzuyllxwptbgqjvhgtuu", "hbkqvcpapfvagnwemhpczdjkrdpdwcbrgawdqemwspyspcba", "eiegvkvxscdawtp", "hbkqvcpapfvagnwemhpczdjkrdpdwcbrgawdqem", "vyesnjhjajdiexpegiahjqwdxhhjfonsyyni", "isgpvqbzcdcbpacznbjtbiomudfnoxlnusgxgttbvedluq", "kqtflacxztrombtzalfnlqh", "suitsuinbzshsczwrgceqcppamortutbinwcuyic", "myfriynjw", "zvq", "qscbkf", "chwtidcezqulrrwbrrjywvczgbq", "bba", "rbttfdwrqycblntntuyzcuiqpz", "ptqchiizucititxfu", "yinzxqercrwvymsudtzzrompqxzeulkdbnmjwspivquu", "lvhklkiprqcvqygdabkl", "yinzxqercrwvymsudtzzrompqxzeulkdbnmjwspivquudwx", "wfeapnizvgsppotjwyelfgeoqudtduditkknxdevcso", "cvmenxcmdvbmlmxicwsailyzcghjfucry", "mwvjyogrboovclcnyrmfcaoa"))
#print buh.maxElements(("coyazentbwuyckqykjflzbywsozhsmnmcycjbbttfndoovxmk", "juozqkgmnslamsxcwiugjsnuzoxmjhgdgkaofcznvnyqtfpeq", "yevegfal", "coyazentbwuyckqykjflzbywskdanbdztc", "lgsqrfrlgmmppdkx", "yevegfalauogxjtkbudqhtcmlmynrrcestkwxxf", "yevegfalcxhmbpisfamdtykcygyzwmppitqlitdmbvfgtabgh", "iqwxqqeurmqptolrvoawcyabihpjfaceptbyag", "yevegfalauogxjtkbudqhtcmlmynrrcestkwxxfq", "cnntlgcemjkyicbwtpwnppxacgkyibpmvzckfbtzfucqvffw", "cnntlgcemjkyicbwtpwnppxacgkyibpmvzckfbtzf", "iqwxqqeurmqptolrvoawcyabihpjfaceptbyagmjge", "cnntlgcemjkyicbwtrzrlzltptikheccfuxxoickbsv", "qlgtbrbvwcuavkixsbhdlnutnjgsomm", "wlyrxztlykscwcrpywvpbnlkapnzxxpncevl", "cnntlgcemjkyicbwtrzrlzltptikheccfuxxoickb", "coyazentbwuyckqykjflzbywsozhsmnmcyc", "coyazentbwuyckqykjflzbywsrodiuzlldicusbhnpocream", "lmcgepiiuxlibgmaygocogfevxmdxkrfulhcfxdjmhh", "qsqedmzmdyk", "coyazentbwuyckqykjflzbywsozhsmnmcycmfselhhi", "fwzbocsqronzavprrbjv", "cnntlgcemjkyicbwtrzrlzltptikheccfuxxoickbzlgs", "coyazentbwuyckqykjflzbyws", "coyazentbwuyckqykjflzbywsozhsmnmcycmfselhhinni", "yrunwmhudwzzjhhrwzvjfkcwhp", "obspdwitkhjkolmzpyjvspmffxjuebwfveagblyl", "coyazentbwuyckqykjflzbywsrodiuzlldicusbhnpoc", "alyvikuszferppil", "dlyct", "bwtruteocoweionjpbclbwmsyzd", "dlyctfffglrwchehqgmp", "coyazentbwuyckqykjflzbywsrodiuzlldicusbhnpoccrq", "cnntlgcemjkyicbwtpwnppxacgkyibpmvzckfbtzf", "utwdshuooxxbphurepej", "cnntlgcemjkyicbwt"))
