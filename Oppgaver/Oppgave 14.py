hovedstaden = {"norge" : "Oslo", "nederland" : "Amsterdam","spania" : "Madrid", "sverige" : "Stockholm"}
språk = {"norge" : "Norsk", "nederland" : "Nederlandsk", "spania" : "Spansk", "sverige" : "Svensk"}
innbyggere = {"norge" : 5391369, "nederland" : 17282163, "spania" : 46733038, "sverige" : 10340000}

n=0
while n <1:
    Land = input("Skriv inn et land")
    lav = Land.lower
    try: 
        print("Hovedstaden i ", Land, " er ", hovedstaden[str(lav)],  ",\nDe snakker ", språk[str(lav)], ",\nOg det bor", innbyggere[str(lav)], " i ", Land, "\n")
    except:
        print("Informasjon om ", Land, " er ikke tiljengelig")