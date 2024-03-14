def total_euro(x,y):
    total=x*y
    return total

hours=int(input("Radni sati: "))
pricePerHour=float(input("Satnica: "))
total=hours*pricePerHour

print("Ukupno:", total, "Eura")
print("Ukupno:", total_euro(hours,pricePerHour), "Eura")



