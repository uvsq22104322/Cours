import random
import time
import matplotlib.pyplot as plt
# initialisation d’un tableau de taille 10 avec des valeurs aléatoires
# pour vérifier la validité des algos de tris
tab_test=[random.randint(0,20)for i in range(1000)]
print(tab_test)

def est_trié(tab_test): 
#renvoie vrai si le tableau est trié
    for i in range(0,len(tab_test)+1):
        if tab_test[i] <= tab_test[i+1]:
            return True
        else:
            return False


def recherche_pos(tab_test,elem,fin):
    for j in range(0,fin): 
    #cherche la position à laquelle on attribuera la valeur de tab[i], donc elem
        if elem < tab_test[j]:
            return j
    return fin  


def triinsertion(tab_test):
    for i in range(1,len(tab_test)): 
    #processe chaque éléments du tableau
        elem = tab_test[i] 
        #sauvegarde la valeur que l'on veut déplacer
        pos = recherche_pos(tab_test,elem,i) 
        #cherche de position ou déplacer cette valeure
        for j in range(i-1,pos-1,-1): 
        #boucle de décalage des termes
                tab_test[j+1] = tab_test[j]
                tab_test[pos] = elem
    return tab_test

def recherche_pos_dicho(tab,elem,fin):
    debut = 0
    while debut != fin:
        milieu = (debut + fin)//2
        if tab[milieu] < elem:
            debut = milieu + 1
        else:
            fin = milieu 
    return fin 


def triinsertion_dicho(tab_test):
    #identique a triinsertion, avec une recherche de pose différente
    for i in range(1,len(tab_test)):
        pos = i
        elem = tab_test[i]
        pos = recherche_pos_dicho(tab_test,elem,i-1)
        for j in range(i-1,pos-1,-1):
                tab_test[j+1] = tab_test[j]
                tab_test[pos] = elem
    return tab_test

def tripermutation(tab_test):
    for i in range (0,len(tab_test)):
        for j in range(len(tab_test)-1):
            if tab_test[j] > tab_test[j+1]:
                tab_test[j], tab_test[j+1] = tab_test[j+1], tab_test[j]
    return tab_test

def fusion(tab1,tab2):
#les deux tableaux étant triés, on ajoute les plus petits des deux les uns après les autres pour n'obtenir qu'un tableau
    res = []
    i,j = 0,0
    while i < len(tab1) and j < len(tab2): #condition d'arret
        if tab1[i] < tab2[j]:
            res.append(tab1[i])
            i += 1
        else:
            res.append(tab2[j])
            j += 1
    res.extend(tab1[i:]) #on ajoute un tableau des bornes i à la fin
    res.extend(tab2[j:])
    return res

def trifusion(tab): #recursif jusqu'au moment ou les tableau sont de tailles 1 
    if len(tab) >= 2: #ou >1 (reviens au même)
        milieu = len(tab)//2 #création d'une slice
        tab1 = trifusion(tab[:milieu])
        tab2 = trifusion(tab[milieu:])
        tab = fusion(tab1,tab2)
    return(tab)


def partition(pivot,tab): #sépare le tableau
    tab1= []
    tab2=[]
    for elem in tab:
        if elem < pivot:
            tab1.append(elem)
        else:
            tab2.append(elem)
    return tab1,tab2

def trirapide(tab):
    if len(tab) > 1:
        pivot = tab[0] #on peut choisir n'importe quel pivot à partir qu'il soit compris dans len(tab)
        (tab1,tab2) = partition(pivot,tab[1:]) #on veut faire partition sans inclure le pivot, donc on fait commencer le tab envoyé à la première valeure
        tab = trirapide(tab1) + [pivot] + trirapide(tab2)
    return tab

def duree(tab,algo) :
    debut = time.time()
    if algo == 1:
        triinsertion(tab)
    elif algo == 2:
        triinsertion_dicho(tab)
    elif algo == 3 :
        tripermutation(tab)
    elif algo == 4 :
        trifusion(tab)
    elif algo == 5 :
        trirapide(tab)
    return (time.time() - debut)

x = []
insertion = []
insertiondicho = []
permutation = []
fusionres = []
rapide = []

for i in range(100,1000,10) :
    tab = [random.randint(0,20) for j in range(i)]
    x.append(i)
    insertion.append(duree(tab,1))
    insertiondicho.append(duree(tab,2))
    permutation.append(duree(tab,3))
    fusionres.append(duree(tab,4))
    rapide.append(duree(tab,5))
fig = plt.figure()
ax = plt.axes()

plt.plot(x,insertion,"r-",label="insertion")
plt.plot(x,insertiondicho,"m-",label="insertion_dichotomie")
plt.plot(x,permutation,"k-",label="permutation")
plt.plot(x,fusionres,"b-",label="fusion")
plt.plot(x,rapide,"g-",label="rapide")

plt.legend(loc="upper left")
plt.xlabel("taille tableau")
plt.ylabel("temps d'éxecution")
plt.show()

print(triinsertion(tab_test.copy()))
print(tripermutation(tab_test.copy()))
print(trifusion(tab_test.copy()))
print(trirapide(tab_test.copy()))

print(duree(tab_test.copy(),2))  #pb = parfois la durée renvoyée est égale a 0 !