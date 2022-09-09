import random


#maskin skal velge
valg = ["stein", "saks", "papir"]

#hei = "Hei"
#print(hei.lower())


#bruker velger
l=0
w=0
n=1
while n < 2:
    maskinValg = random.choice(valg)
    #print(maskinValg)
    brukerValg = input("Velg enten Stein, Saks eller Papir, eller skriv ferdig vis du ikke vil spille mere: \n")
    bruker = (brukerValg.lower())
    if bruker == "stein" and maskinValg == "saks" or bruker == "saks" and maskinValg == "papir" or bruker == "papir" and maskinValg == "stein":
        print ("Du vant")
        w = w + 1
    elif maskinValg == "stein" and bruker == "saks" or maskinValg == "saks" and bruker == "papir" or maskinValg == "papir" and bruker == "stein":
        print("Du tapte")
        l = l + 1
    elif maskinValg == bruker:
        print("Det ble likt, Prøv igjen")
    elif bruker == "ferdig":
        print("du vant " , w , " ganger og du tapte " , l , "ganger")
        n = 2
    else:
        print("Skriv rikrig")




# sjekk hvem som vinner

#skriv ut hvem som vinner