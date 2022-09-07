def s(sp) :
    n = 0
    while n <1:
        print(sp)
        sp1 = input()
        try:
            if int(sp1) == 48:
                print("riktig +1p")
                poengsum = poengsum + 1
                n = 1
            else:
                print("Feil +0p")
        except:
            print("Skriv bare tall")

s("Hvem er du")



poengsum = 0
print("Hvor mange land er det i europa")
sp1 = input()


try:
    if int(sp1) == 48:
        print("riktig +1p")
        poengsum = poengsum + 1
    else:
        print("Feil +0p")
except:
    print("Skriv bare tall")

print("Hvor mange land er det i europa")
sp1 = input()

if int(sp1) == 48:
    print("riktig +1p")
    poengsum = poengsum + 1
else:
    print("Feil +0p")

print("Når ble Akademiet VGS Oslo grunnlagt")
sp2 = input()
try:       
    if int(sp2) == 2005:
     print("riktig +1p")
     poengsum = poengsum + 1
    else:
        print("Feil +0p")
except:
    print("Skriv bare tall")
print("Når ble Akademiet VGS Oslo grunnlagt")
sp2 = input()
if int(sp2) == 2005:
     print("riktig +1p")
     poengsum = poengsum + 1
else:
    print("Feil +0p")




print("Hvor gammel er kong Harald V")
sp3 = input()
if int(sp3) == 85:
    print("riktig +1p")
    poengsum = poengsum + 1
else:
    print("Feil +0p")


print ("Nå er quizen ferdig du fikk " + str(poengsum) + "/3 riktig")