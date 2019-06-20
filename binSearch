def binSearch (liste, key):
    l = 0 #Linek Seite der Liste
    r = len(liste) #Rechte Seite
    while l <= r:
        m = (l + r)//2 #Wert in der Mitte der liste
        if liste[m] == key:
            return m+1 #Gibt die Stelle aus an dem sich der Key befindet
        elif key < liste[m]: #wenn Key kleiner ist
            r = m - 1 #"teile" den Anfang der liste
        else: l = m + 1 #"teile" das Ende der Liste
    return "No Key!"

zahlenliste = [1,2,4,5,6,24,34]
print (binSearch(zahlenliste,4))
