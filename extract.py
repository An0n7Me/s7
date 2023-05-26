def result(fic):
    f = open("dico\\"+fic, "r")
    for i in range(59):
        (f.readline())
    p = ""
    l = []
    while p!=['-------------------------', 'FIN', 'DU', 'FICHIER', '--------------------------------']:
        p = (f.readline()).split()
        try:
            if p[2][:3]=="Nom":
                l.append(p)
        except:
            pass
    result = open("result\\"+fic,"w")
    for i in l:
        s = " ".join(i)+"\n"
        result.write(s)

    print("Done :", fic)

a = "abcdefghijklmopqrstuvwxyz"
for i in a:
    result(i+".txt")