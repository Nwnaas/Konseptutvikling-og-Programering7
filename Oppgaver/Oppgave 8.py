
poengsum = 0
n=0
while n < 1:
    print("Hvor mange land er det i europa")
    sp1 = input()
    try:
        if int(sp1) == 48:
            print("riktig +1p")
            poengsum = poengsum + 1
            n=1
        else:
            print("Feil +0p")
            print("Riktig svar er 48 land")
            n=1
    except:
        print("Skriv bare tall")
n=0
while n < 1:
    print("Når startet Akademiet VGS Oslo: ")
    sp1 = input()
    try:
        if int(sp1) == 2005:
            print("riktig +1p")
            poengsum = poengsum + 1
            n=1
        else:
            print("Feil +0p")
            print("Riktig svar er 2005")
            n=1
    except:
        print("Skriv bare tall")
n=0
while n < 1:
    print("Hvor gammel er kong Harald V: ")
    sp1 = input()
    try:
        if int(sp1) == 85:
            print("riktig +1p")
            poengsum = poengsum + 1
            n=1
        else:
            print("Feil +0p")
            print("Riktig svar er 85 år")
            n=1
    except:
        print("Skriv bare tall")

print ("Nå er quizen ferdig du fikk " + str(poengsum) + "/3 riktig")