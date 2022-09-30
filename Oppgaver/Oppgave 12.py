maneder = ["Januar", "Februar", "Mars", "April","Mai","Juni","Juli","August","September","Oktober","November","Desember"]
n=0
while n <1:
    tall = input("Skriv in et tall mellom 1-12: ")
    try:
        if int(tall) > 0 and int(tall) <= 12:
            nummer = int(tall) - 1
            print("den ", tall," måneden er ", maneder[int(nummer)])
            n=1
        else:
            print("Ikke riktig tall")
    except:
        print("skriv bare ett tall")
        

