# tall = input("Skriv inn et valgfrit tall: ")
# n = 0
# while n < int(tall) + 1:
#     print(n)
#     n = n + 1


# i = 0 
# while i < 1:
#     skriv = input("Skriv noe: ")
#     if skriv == "slutt":
#         print("Nå avsluttes programmet")
#         i = 1
#     else:
#         print("Hei")


tall = int(input("Skriv inn et tall over 10: "))
n = 0

while n < tall + 1:
    try:
        if tall > 9:
            print(n)
            n += 1
    except:
        print("Skriv et høyere tall")