lst= []

while True:
    x = input("Enter a number:")
    if (x == 'done'): 
        break
    try:
        x = int(x)
    except:
        print("You've entered the letter")
        continue
    
    lst.append(x)

print ("Korisnik je unio: %d brojeva." %len(lst))

print ("Minimalna vrijednost: %d" %min(lst))
print ("Maksimalna vrijednost: %d" %max(lst))

print ("Srednja vrijednost: %.2f" %(sum(lst)/len(lst)))

print(lst)

lst.sort()

print(lst)