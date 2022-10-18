def valArrondie(ch):
    f = float(ch)
    e = int(f + .5)
    return str(e)

fiSource = input("Nom du fichier à traiter:")
fiDest = input("Nom du fichier destinataire:")
fs = open(fiSource, 'r')
fd = open(fiDest, 'w')

while 1:
    ligne = fs.readline()
    if ligne == "" or ligne == "\n":
        break
    ligne = valArrondie(ligne)
    fd.write(ligne +"\n")

fd.close()
fs.close()