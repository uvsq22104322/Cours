def triplerEspace(ch):
    i, nouv = 0, ""
    while i < len(ch):
        if ch[i] == " ":
            nouv = nouv + "   "
        else:
            nouv = nouv + ch[i]
        i += 1
    return nouv

nomF = input("Nom du fichier:")
fichier = open(nomF, 'r+')
lignes = fichier.readlines()

n=0
while n < len(lignes):
    lignes[n] = triplerEspace(lignes[n])
    n += 1

fichier.seek(0)
fichier.writelines(lignes)
fichier.close

"C:\Users\cyria\OneDrive\Bureau\inputExo5.txt"