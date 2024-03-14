try:
    n=float(input('Unesite ocjenu: '))
except ValueError:
    print("Can't be empty number")
if n <0.0 or n >1.0:
        print("ERROR: OCJENA NIJE IZMEĐU INTERVALA")
 
if (n >= 0.9):
    print("A")
elif (n >= 0.8):
    print("B")
elif (n >= 0.7):
    print("C")
elif (n >= 0.6):
    print("D")
else:
    print("F")


