import random
izabrani_brojevi = []
Brojevi = [1, 2, 3, 4, 5, 6, 7, 8]
random_izabir = random.choice(Brojevi)
print(f"Vas random izabrani broj je: {random_izabir}")

izabrani_brojevi.append(random_izabir)

Brojevi.remove(random_izabir)

done = True
while done == True:
    a = input("Da li zelite ponovo izbrati random broj bez vec izbranog (da/ne)? ")
    if a == "da":
       random_izabir = random.choice(Brojevi)
       print(f"Vas random izabrani broj je: {random_izabir}")
       izabrani_brojevi.append(random_izabir)
       Brojevi.remove(random_izabir)
    else:
        print(f"Vasi izabrani brojevi od 1-8 su: {izabrani_brojevi}")
        done  = False