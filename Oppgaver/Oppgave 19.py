tall = {6, -12, -4, 7, -2, 8, -3, 9, -11}

x = 100
for i in tall:
    if i < x:
        x = i
print("Det laveste tallet er:", x)

x = -100
for i in tall:
    if i > x:
        x = i
print("Det høyeste tallet er:", x)

