a = float(input("Côté a du traiangle :"))
b = float(input("Côté b du triangle :"))
c= float(input("Côté c du triangle : "))

ab = a+b
bc = b+c
ac = a+c

if ab > c and bc >a and ac > b:
    print(True)
else:
    print(False)