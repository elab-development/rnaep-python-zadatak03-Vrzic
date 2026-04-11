import random
import math

# 1. Lista proizvoda
proizvodi = [
    "lopta",
    "torba",
    "ranac",
    "suncobran",
    "kacket",
    "krema",
    "peskir",
    "lezaljka"
]

# 2. Rečnik sa cenama
cene = {
    "lopta": 359.99,
    "torba": 899.99,
    "ranac": 1034.99,
    "suncobran": 1403.99,
    "kacket": 567.99,
    "krema": 499.99,
    "peskir": 799.99,
    "lezaljka": 1099.99
}

# 3. Prikaz proizvoda i cena
print("Proizvodi i njihove cene:")
for proizvod, cena in cene.items():
    print(f"- {proizvod} - {cena:.2f} €")

# 4. Unos budžeta i prikaz proizvoda koje korisnik može da priušti
budzet = float(input("\nUnesite vaš budžet: "))

print("\nProizvodi koje možete da priuštite:")
for proizvod, cena in cene.items():
    if cena <= budzet:
        print(f"- {proizvod} - {cena:.2f} €")

# 5. Funkcija za najskuplji proizvod
def najskuplji_proizvod(recnik):
    return max(recnik, key=recnik.get)

najskuplji = najskuplji_proizvod(cene)
print(f"\nNajskuplji proizvod je: {najskuplji} - {cene[najskuplji]:.2f} €")

# 6. Nasumičan proizvod
slucajan_proizvod = random.choice(proizvodi)
print(f"\nKorisniku je privukao pažnju proizvod: {slucajan_proizvod}")

# 7. Prosečna cena
prosecna_cena = sum(cene.values()) / len(cene)
prosecna_cena = round(prosecna_cena, 2)
print(f"\nProsečna cena svih proizvoda je: {prosecna_cena:.2f} €")

# 8. Broj prodatih komada i ukupan prihod
prodate_kolicine = [10, 3, 5, 2, 3, 7, 4, 1]

ukupan_prihod = 0
for i in range(len(proizvodi)):
    ukupan_prihod += cene[proizvodi[i]] * prodate_kolicine[i]

print(f"\nUkupan prihod je: {ukupan_prihod:.2f} €")

# 9. Dodavanje novog proizvoda
novi_proizvod = "kupaci"
nova_cena = 789.99
nova_kolicina = 2

proizvodi.append(novi_proizvod)
cene[novi_proizvod] = nova_cena
prodate_kolicine.append(nova_kolicina)

print("\nAžurirana lista proizvoda:")
for proizvod in proizvodi:
    print(f"- {proizvod}")

# 10. Sortiranje po ceni
sortirani_proizvodi = sorted(cene.items(), key=lambda x: x[1])

print("\nProizvodi sortirani po ceni:")
for proizvod, cena in sortirani_proizvodi:
    print(f"- {proizvod} - {cena:.2f} €")