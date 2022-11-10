
def encodage():
    print("Veuillez entrer les données (ou <Entrée> pour terminer) :")
    while 1:
        nom = input()
        if nom == "":
            return []
        prenom = input("Entrez votre prénom:")
        rueNum = input("Entrez votre rue:")
        cPost = input("Entrez votre code postal:")
        local = input("Entrez votre ville:")
        tel = input("Entrez votre numéro de tel:")
        print(nom, prenom, rueNum, cPost, local, tel )
        ver = input("Veuillez entrer si c'est correct, sinon <n>")
        if ver == "":
            break
    return [nom, prenom, rueNum, cPost, local, tel]

def enregistrer(liste):
    i = 0
    while i < len(liste):
        of.write(liste[i] + "#")
        i += 1
    of.write("\n")

nomF = input("Nom du fichier destinataire:")
of = open(nomF,'a')
while 1:
    tt = encodage()
    if tt == []:
        break
    enregistrer(tt)

of.close()
