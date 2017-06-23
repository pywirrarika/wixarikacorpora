Fmtx = open("spa-x-bible-dhhe.mtx", "r")
Fwf = open("spa-x-bible-dhhe.wordforms", "r")
Fo = open("bible.es", "w")


dicF = Fwf.read().split("\n")
dic = {}
i = 1
for d in dicF:
    try:
        (word, c) = d.split("\t")
    except:
        print(d)
    dic[i]=word
    i =i + 1
corpus = [[] for x in range(47504)]

for line in Fmtx:
    l = line.split()
    word = dic[int(l[0])]
    indx = int(l[1])
    corpus[indx].append(word)


i = 0
for line in corpus:
    if not line:
        pass
    else:
        print("[",i,"] ", end="", sep="")
        for word in line:
            print(word, end=" ")
        print("")
    i=i+1
