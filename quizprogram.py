print("Hei, og velkommen til quiz! \n\n")
poeng = 0

svar1 = input("Hva heter Asias største øy? \n")

if svar1.lower() == "borneo":
    poeng += 1
    print("Riktig!")
else:
    print("Feil! Det riktige svaret var Borneo")

svar2 = input("I hvilket land ligger hovedkontoret til flyselskapet Ryanair? \n")

if svar2.lower() == "irland":
    poeng += 1
    print("Riktig!")
else:
    print("Feil! Det riktige svaret var Irland")

svar3 = input("I hvilken by ligger Chryslerbygningen? \n")

if svar3.lower() == "new york":
    poeng += 1
    print("Riktig!")
else:
    print("Feil! Det riktige svaret var New York")

print("Takk for din deltakelse, du fikk " + str(poeng) + " poeng!")