def lin_search(l,n):
    laenge = len(l)
    for i in range (laenge):
        if l[i] == n:
            res = "Die Zahl " + str(n) + " befindet sich in der Liste an Platz " + str(i+1)
            return res
    res = "Die Suche liefert leider kein Ergebnis."
    return res

l = [4,3,6,2,9,1]
print (lin_search(l,1))
