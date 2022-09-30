tall = [1, 2, 3, 4,5]
tall2 = []

for x in tall:
    tall2.append(x**2)
    print("Kvadratet av", x, "er ", x**2)

tall = tall2
for i in tall:
    print(i)