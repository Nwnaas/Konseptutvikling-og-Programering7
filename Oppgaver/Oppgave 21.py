tall = []

n = 0
while n < 5:
    m = 1
    while m < 2:
        try:
            tall.append(int(input("Skriv inn et tall: ")))
            m = 3
        except:
            print("feil")
    n +=1

sum = 0
"\n"
for x in tall:
    sum += x
print("Summen av alle tallene er: ",sum)
for x in tall:
    if x < 10:
        print(str(x), " er mindre enn 10")

if 5 in tall:
    print("Tallet 5 finnes i listen!")
else:
    print("Tallet 5 finnes ikke i listen")

