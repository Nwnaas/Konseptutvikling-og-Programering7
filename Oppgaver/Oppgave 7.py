barn = 0
ungdom = 20
voksen = 40
gammel = 20

alder = input("Hvor gammel er du: ")
if int(alder) < 9:
    print("du er et barn, det koster " + str(barn) + " kroner")
elif int(alder) > 8 and int(alder) < 18:
    print("Du er en ungdom, det koster " + str(ungdom) + " kroner")
elif int(alder) > 17 and int(alder) < 66:
    print("Du er en voksen, det koster " + str(voksen) + " kroner")
elif int(alder) > 65:
    print("Du er gammel, det koster " + str(gammel) + " kroner")
else:
    print("Du har skrevet inn noe feil")