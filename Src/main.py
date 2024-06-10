from asmuo import Asmuo
from darbuotojas import Darbuotojas
from lankytojas import Lankytojas
from knyga import Knyga
from paskolintos_knygos import PaskolintosKnygos
from esancios_bibliotekoje import EsanciosBibliotekoje
from datetime import datetime, timedelta

# Asmenys
asmuo1 = Asmuo("Jonas", "Jonaitis", "123456789", "+37060000000", "jonas@gmail.com")
asmuo2 = Asmuo("Petras", "Petraitis", "987654321", "+37060000001", "petras@gmail.com")
asmuo3 = Asmuo("Ona", "Onaitė", "123123123", "+37060000002", "ona@gmail.com")
asmuo4 = Asmuo("Ieva", "Ievaitė", "321321321", "+37060000003", "ieva@gmail.com")

# Darbuotojas
darbuotojas = Darbuotojas("Ieva", "Ievaitė", "321321321", "+37060000003", "ieva@gmail.com", "Bibliotekos darbuotojas", 1000)

# Knygos
knyga1 = Knyga(1, "Pavadinimas1", "Autorius1", "Vieta1", "Kategorija1")
knyga2 = Knyga(2, "Pavadinimas2", "Autorius2", "Vieta2", "Kategorija2")
knyga3 = Knyga(3, "Pavadinimas3", "Autorius3", "Vieta3", "Kategorija3")
knyga4 = Knyga(4, "Pavadinimas4", "Autorius4", "Vieta4", "Kategorija4")

knygu_sarasas = [knyga1, knyga2, knyga3, knyga4]

# Lankytojai
registruoti_lankytojai = [
    Lankytojas(asmuo2, []),
    Lankytojas(asmuo3, [
        PaskolintosKnygos(knyga1, datetime.now() - timedelta(days=15)),  # Vėluoja grąžinti
        PaskolintosKnygos(knyga2, datetime.now() - timedelta(days=5)),
        PaskolintosKnygos(knyga3, datetime.now() - timedelta(days=2)),
        PaskolintosKnygos(knyga4, datetime.now() - timedelta(days=1)),
        PaskolintosKnygos(knyga1, datetime.now() - timedelta(days=1))
    ])
]

# Tikrinimas
print("Sveiki atvykę į biblioteką!")
asmens_kodas = input("Įveskite savo asmens kodą: ")

# Ar darbuotojas
if asmens_kodas == darbuotojas.asmens_kodas:
    print(
        f"Jūs esate darbuotojas: {darbuotojas.vardas} {darbuotojas.pavarde}, {darbuotojas.darbuotojo_pareigos}, Atlyginimas: {darbuotojas.darbuotojo_atlyginimas}€")

# Ar registruotas lankytojas
else:
    # Ar jau nėra tokio asmens kodo
    existent_lankytojas = None
    for lankytojas in registruoti_lankytojai:
        if asmens_kodas == lankytojas.lankytojo_id.asmens_kodas:
            existent_lankytojas = lankytojas
            break

    if existent_lankytojas:
        print(
            f"Jūs esate registruotas lankytojas: {existent_lankytojas.lankytojo_id.vardas} {existent_lankytojas.lankytojo_id.pavarde}")
        print("Jūs turite šias paimtas knygas:")
        for paskolinta_knyga in existent_lankytojas.knygu_sarasas:
            print(f"- {paskolinta_knyga.knyga.pavadinimas}")
        if len(existent_lankytojas.knygu_sarasas) < 5:
            print("Galimi pasirinkimai:")
            galimos_knygos = [knyga for knyga in knygu_sarasas if
                              knyga not in [p.knyga for p in existent_lankytojas.knygu_sarasas]]
            for knyga in galimos_knygos:
                print(f"- {knyga.pavadinimas}")
            if galimos_knygos:
                knyga_pavadinimas = input("Įveskite norimos knygos pavadinimą iš sąrašo: ")
                for knyga in galimos_knygos:
                    if knyga.pavadinimas == knyga_pavadinimas:
                        existent_lankytojas.knygu_sarasas.append(PaskolintosKnygos(knyga, datetime.now()))
                        print(f"Knyga \"{knyga_pavadinimas}\" sėkmingai pridėta prie jūsų paimtų knygų sąrašo.")
                        break
                else:
                    print("Tokios knygos nėra bibliotekoje arba ji jau yra jūsų paimtoje knygų sąraše.")
            else:
                print("Nėra galimų pasirinkimų.")
        else:
            print("Jūs jau pasiekėte maksimalų knygų skaičių.")
    else:
        # Naujo lankytojo registravimas
        print("Jūs esate neregistruotas lankytojas.")
        vardas = input("Įveskite savo vardą: ")
        pavarde = input("Įveskite savo pavardę: ")
        telefonas = input("Įveskite savo telefono numerį: ")
        el_pastas = input("Įveskite savo elektroninio pašto adresą: ")

        naujas_lankytojas = Asmuo(vardas, pavarde, asmens_kodas, telefonas, el_pastas)

        print(f"Sveikiname, {vardas}! Jūs tapote registruotu lankytoju.")
        print("Galimi pasirinkimai:")
        for knyga in knygu_sarasas:
            print(f"- {knyga.pavadinimas}")
        knyga_pavadinimas = input("Įveskite norimos knygos pavadinimą iš sąrašo: ")

        # Ar knyga yra bibliotekoje
        for knyga in knygu_sarasas:
            if knyga_pavadinimas == knyga.pavadinimas:
                registruoti_lankytojai.append(Lankytojas(naujas_lankytojas, [PaskolintosKnygos(knyga, datetime.now())]))
                print(f"Knyga \"{knyga_pavadinimas}\" sėkmingai pridėta prie jūsų paimtų knygų sąrašo.")
                break
        else:
            print("Tokios knygos nėra bibliotekoje.")