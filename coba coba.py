a = float(input("Masukkan nilai n: "))
if a > 0:
    positif_negatif= 'positif'
elif a < 0:
    positif_negatif= 'negatif'

if a % 2 == 0: 
    ganjil_genap = 'genap'

if a % 2 > 0:
    ganjil_genap = 'ganjil'
print ("Bilangan N adalah " + ganjil_genap + " " + positif_negatif)
print(f"Bilangan N adalah {ganjil_genap} {positif_negatif}")
print("Bilangan N adalah", ganjil_genap, positif_negatif)