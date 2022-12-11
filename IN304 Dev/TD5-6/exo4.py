
#pas complet !

def tablrMulti(n):
    i, ch = 0, ""
    while i < 20:
        i += 1
        ch = ch + str(i*n) + " "
    return ch

nomF = input("Entrez un nom:")
fichier = open(nomF,'w')

table = 2
while table < 31:
    fichiers.write(tableMulti(table) + "\n")
    table = table + 1
fichiers.close 



