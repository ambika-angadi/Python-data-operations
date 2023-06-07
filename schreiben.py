#neues auto: VOLVO! muss in den fuhrpark aufgenommen werden!

#datei oeffnen
datei = open("fuhrpark.txt", "a+")

#datei schreiben
inhalt = "Volvo\n"
datei.write(inhalt)

inhalt = "Tesla\n"
datei.write(inhalt)

#datei schließen
datei.close()