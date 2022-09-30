favorittmat = ["Taco", "Pizza", "Kebab"]
for i in favorittmat:
    print(i)
favorittmat.pop(1)
print("Det er ", len(favorittmat), "matretter i listen") 
for i in favorittmat:
    print(i.upper())