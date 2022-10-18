fich1 = input("Entrez le nom du premier fichier:")
fich2 = input("Enrez le nom du second fichier:")

fi1 = open(fich1,'r')
fi2 = open(fich2, 'r')

c, f = 0, 0
while 1:
    c = c + 1
    car1 = fi1.read(1)
    car2 = fi2.read(1)
    if car1 == "" or car2 == "":
        break
    if car1 != car2:
        f=1
        break

fi1.close()
fi2.close()

print("Ces deux fichiers", end=' ')
if f==1:
    print("diffèrent à partir du caractère n", c)
else:
    print("sont identiques")
    