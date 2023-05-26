import sys

try:
    from polyglot.text import Text
    from polyglot.downloader import downloader

    #downloader.download("LANG:fr")
    downloader.download()

    def cw(word1, l):
        word1 = list(word1)
        wordlist = [list(i) for i in l]
        result = []
        for word2 in wordlist:
            i = 0
            while word1[:i] == word2[:i] and i <= len(word1):
                i += 1

            result.append(i / max(len(word1), len(word2)) * 100)
        if max(result) >= 66:
            return "".join(wordlist[result.index(max(result))])
        else:
            return None


    def search(word, iter, l):
        z = l.copy()
        for i in range(len(l)):
            try:
                if z[i][iter] != word[iter]:
                    del l[l.index(z[i])]
            except:
                del l[l.index(z[i])]
        return l


    def result(word):
        l = []
        if word[0].lower()  in "abcdefghijklmopqrstuvwyxz":
            fic = open("result\\" + word[0].lower() + ".txt", "r")
        else:
            return word
        for i in fic:
            s = i.split(" ")[0]
            l.append(s)
        l1 = l.copy()
        for i in range(int(len(word) * 0.75)):
            l = search(word, i + 1, l)
        if len(l) == 0:
            return word
        else:
            s = cw(word, l)
            if s is None:
                return word
            else:
                index = l1.index(s)
                if index >= len(l1) - 7:
                    return l1[len(l1) - 1]
                else:
                    return l1[index + 7]


    def readtxt(name):
        fr = open("t\\" + name, "r" ,encoding='utf8')
        fw = open("txtsp7\\resultof" + name, "w", encoding="utf8")

        for i in fr:
            if i == ".\n" or i=="\n":
                continue
            else:
                try:
                    text = Text(i.rstrip("\n")).pos_tags
                    r = ""
                    print(text)
                    for j in text:
                        if j[1] != "NOUN":
                            r += j[0] + " "
                        else:
                            r += result(j[0]) + " "
                    r += "\n"
                    fw.write(r)
                except Exception:
                    print(Exception)
                continue


    def resultv2(name):
        fr = open("txt\\" + name, "r" ,encoding='utf8')
        fw = open("t\\" + name, "w" ,encoding='utf8')
        r = ""
        for i in fr:
            s = i.rstrip("\n")
            for j in s:
                if not j in ".?!":
                    r+=j
                else:
                    r+=".\n"
                    fw.write(r)
                    r=""


    name = input("name of the fic + extension")
    # resultv2(name)
    readtxt(name)
    input("press enter")
except Exception:
    e = sys.exc_info()[1]
    print(e)

    input("press enter")