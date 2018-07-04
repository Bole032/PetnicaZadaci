import sys
import random

# Datoteka u kojoj se nalazi spisak reci
Datoteka = open("static/Reci.in", "r")
Reci = Datoteka.readlines()

# Generisemo nasumicnu rec iz liste reci
Rec = Reci[random.randint(0, len(Reci)-1)].rstrip()
Kopija = Rec[:]

# Trazimo input od korisnika sve dok ne dodje do kraja igre
# (ukoliko igrac pogodi ili pogresi slova nekoliko puta)
Kraj = False

def prikazi(Promaseno):
    Fajl = open("static/" + str(Promaseno+1) + ".in")
    Glisa = Fajl.readlines()
    for Red in Glisa:
        print(Red.rstrip())

# Promenjive kojima kontrolisemo tok igre
Promaseno = 0
Pogodjen = [0] * len(Rec)
Promasene =  ""
print(Rec)

# Glavna petlja
while not Kraj:
    Slovo = input("Unesi neko slovo\n")   
    if Rec.find(Slovo) != -1:
        print(Rec.find(Slovo))
        for i in range(0, len(Rec)):
            if Rec[i] == Slovo:
                Pogodjen[i] = 1
    else:
        Promaseno+=1
        Promasene += Slovo
    prikazi(Promaseno)
    Prikaz = ""
    Br = 0
    for t in range(0, len(Rec)):
        if Pogodjen[t] == 1:
            Prikaz += Rec[t]
            Br += 1
        else:
            Prikaz += "_"
    print(Prikaz)
    print("Promasene: " + str(Promasene))
    if (Promaseno == 7):
        Kraj = True
        print("Nisi uspeo da pogodis rec, rec je bila " + Rec)
    if (Br == len(Rec)):
        print("Cestitamo, pogodio si rec!")
        Kraj = True
