#datei oeffnen
datei = open("fuhrpark.txt", "r")

#inhalt aus datei lesen
inhalt = datei.read()
datei.close()

#inhalt zu liste umkonvertieren
alle_zeilen = inhalt.split()

#liste sortieren
alle_zeilen.sort()

#neue datei oeffnen
datei_sortiert = open("furhpark_sortiert.txt", "w")

#sortieren inhalt in datei schreiben
for i in alle_zeilen:
    datei_sortiert.write(i + "\n")

#datei schließen
datei_sortiert.close()

for i in alle_zeilen:
    print(i)