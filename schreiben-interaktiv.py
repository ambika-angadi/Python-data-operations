#datei oeffnen
datei = open("fuhrpark.txt", "a+")

#user input to add a new auto
eingabe = input("Which car do you want add?(separated with comma): ")
einzelne_autos = eingabe.split(",")

for i in einzelne_autos:
    datei.write(i + "\n")

#datei schließen
datei.close()