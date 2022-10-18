txt = ""
for i in range(2,31):
    for j in range(1,21):
        txt += str(i) + " x " + str(j) + " = " + str(j*i) + "\n"

with open("tab_multi",'w') as fNom:
    fNom.write(txt)