n = 0
while n < 1:
    hovedstad= input("Skriv inn en hovedstad i Skandinavia: ")
    if hovedstad == "Oslo":
        print("Oslo er hovedstaden i Norge")
        print("Oslo hadde 634 293 inbyggere i 2021")
        n += 1
    elif hovedstad == "Stockholm":
        print("Stockholm er hovedstaden i Sverige")
        print("Stockholm hadde 975 551 inbyggere i 2020")
        n += 1
    elif hovedstad == "København":
        print("København er hovedstaden i Danmark")
        print("København hadde 602 481 inbyggere i 2017")
        n += 1
    else:
        print(hovedstad + " er ikke en hovedstad i skandinavia")
        print("Husk stor bokstav")