#datei oeffnen
datei = open("fuhrpark.txt", "r")

#complete datei inhalt in a variable lesen
inhalt = datei.read()
#einzelne zeilen in liste schreiben
print(inhalt)
inhalt = inhalt.split()


for chars in inhalt:
    print(chars)

i = 1
for line in inhalt:
    print(i, line)
    i += 1

#ueber liste iterieren und inhalt zeilenweise ausgeben starting from 0
laenge = len(inhalt)
for i in range(laenge):
    print(i, inhalt[i])

#ueber liste iterieren und inhalt zeilenweise ausgeben starting from 1
laenge = len(inhalt)
for i in range(laenge):
    print(i+1, inhalt[i])

#datei schließen
datei.close()